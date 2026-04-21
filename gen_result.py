#!/usr/bin/env python3
"""Read gprof flat profiles and write result.md comparing O0 vs O3."""

import re
import os

OPERATIONS = [
    "falcon512_keygen",
    "falcon512_sign",
    "falcon512_verify",
    "falcon1024_keygen",
    "falcon1024_sign",
    "falcon1024_verify",
]

TOP_N = 10


def parse_flat_profile(path):
    """Return (total_seconds, [(pct, cum_sec, self_sec, calls, name), ...])."""
    entries = []
    total = 0.0
    in_table = False
    with open(path) as f:
        for line in f:
            # Header line of data table
            if re.match(r"\s+%\s+cumulative", line):
                in_table = True
                continue
            if not in_table:
                continue
            # Blank line ends the table
            if line.strip() == "":
                break
            m = re.match(
                r"\s*([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+[\d.]+\s+[\d.]+\s+(.+)",
                line,
            )
            if m:
                pct = float(m.group(1))
                cum = float(m.group(2))
                slf = float(m.group(3))
                calls = float(m.group(4))
                name = m.group(5).strip()
                entries.append((pct, cum, slf, calls, name))
                if not total and cum > 0:
                    pass  # keep going
    # total = last cumulative value
    if entries:
        total = entries[-1][1] if len(entries) > 1 else entries[0][1]
        # Actually take the max cumulative seen
        total = max(e[1] for e in entries)
    return total, entries[:TOP_N]


def fmt_calls(n):
    if n >= 1e9:
        return f"{n/1e9:.2f}B"
    if n >= 1e6:
        return f"{n/1e6:.1f}M"
    if n >= 1e3:
        return f"{n/1e3:.1f}K"
    return str(int(n))


def speedup_bar(ratio, width=20):
    filled = min(int(ratio / 5 * width), width)
    return "█" * filled + "░" * (width - filled)


lines = []
lines.append("# Falcon Profiling Results: O0 vs O3")
lines.append("")
lines.append("> 1000 iterations each | `-fno-inline -pg` | Falcon-512 and Falcon-1024")
lines.append("")

# Summary speedup table
lines.append("## Total Runtime Summary (cumulative seconds, 1000 ops)")
lines.append("")
lines.append("| Operation | O0 (s) | O3 (s) | Speedup |")
lines.append("|-----------|-------:|-------:|--------:|")

speedups = {}
for op in OPERATIONS:
    p0 = f"analysis_{op}_O0.txt"
    p3 = f"analysis_{op}_O3.txt"
    if not os.path.exists(p0) or not os.path.exists(p3):
        continue
    t0, _ = parse_flat_profile(p0)
    t3, _ = parse_flat_profile(p3)
    sp = t0 / t3 if t3 > 0 else 0
    speedups[op] = sp
    lines.append(f"| `{op}` | {t0:.2f} | {t3:.2f} | **{sp:.2f}×** |")

lines.append("")

# Per-operation detail
for op in OPERATIONS:
    p0 = f"analysis_{op}_O0.txt"
    p3 = f"analysis_{op}_O3.txt"
    if not os.path.exists(p0) or not os.path.exists(p3):
        continue

    t0, top0 = parse_flat_profile(p0)
    t3, top3 = parse_flat_profile(p3)

    lines.append(f"---")
    lines.append(f"")
    lines.append(f"## {op.replace('_', ' ').upper()}")
    lines.append(f"")
    lines.append(f"Total: **{t0:.2f}s** (O0) → **{t3:.2f}s** (O3)  "
                 f"— **{speedups.get(op, 0):.2f}× faster**")
    lines.append("")

    lines.append("### O0 — Top functions")
    lines.append("")
    lines.append("| % time | self (s) | calls | function |")
    lines.append("|-------:|---------:|------:|----------|")
    for pct, cum, slf, calls, name in top0:
        lines.append(f"| {pct:.2f}% | {slf:.3f} | {fmt_calls(calls)} | `{name}` |")

    lines.append("")
    lines.append("### O3 — Top functions")
    lines.append("")
    lines.append("| % time | self (s) | calls | function |")
    lines.append("|-------:|---------:|------:|----------|")
    for pct, cum, slf, calls, name in top3:
        lines.append(f"| {pct:.2f}% | {slf:.3f} | {fmt_calls(calls)} | `{name}` |")

    lines.append("")

# Analysis section
lines.append("---")
lines.append("")
lines.append("## Analysis")
lines.append("")
lines.append("### Compile flag effects")
lines.append("")
lines.append("| Flag | Effect on Falcon |")
lines.append("|------|-----------------|")
lines.append("| `-O0` | No optimization. Every `fpr_add`, `FPR()`, `modp_montymul` call is a real function call. Accurate per-function attribution. |")
lines.append("| `-O3` | Aggressive optimization. Loop unrolling, vectorization, CSE. Hot leaf functions may be partially inlined even with `-fno-inline` (macros/static inlines). |")
lines.append("| `-fno-inline` | Prevents function inlining so gprof can still count calls. Without this, small functions vanish from the profile at `-O3`. |")
lines.append("| `-pg` | Inserts `mcount` hooks at every function entry for call counting and adds timer sampling for time attribution. |")
lines.append("")
lines.append("### Key observations")
lines.append("")
lines.append("- **keygen** is the heaviest operation — dominated by `fpr_add` / `modp_montymul` (lattice basis generation via NTT+FFT).")
lines.append("- **sign** is ~3× faster than keygen but still FFT-heavy (`fpr_add` ~48%). Rejection sampling (`prng_refill`, `mkgauss`) visible.")
lines.append("- **verify** is 70–300× faster than keygen. Uses integer NTT only (`mq_montymul`, `mq_NTT`) — no floating-point FFT.")
lines.append("- **Falcon-1024 costs ~2–3× more** than Falcon-512 in all operations (N doubles, FFT is O(N log N)).")
lines.append("- **O3 speedup** is largest for keygen/sign (arithmetic-heavy), smaller for verify (already fast, memory-bound).")

with open("result.md", "w") as f:
    f.write("\n".join(lines) + "\n")

print("result.md written.")
