#!/usr/bin/env python3
"""Read gprof flat profiles and write an O0/O3 inlining comparison report."""

import re
import os

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESULTS_DIR = os.path.join(REPO_ROOT, "results")

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
    in_table = False
    with open(path) as f:
        for line in f:
            if re.match(r"\s+%\s+cumulative", line):
                in_table = True
                continue
            if not in_table:
                continue
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
    if entries:
        total = max(e[1] for e in entries)
    else:
        total = 0.0
    return total, entries[:TOP_N]


def parse_flat_profile_all(path):
    """Return set of function names visible in the flat profile."""
    funcs = set()
    in_table = False
    with open(path) as f:
        for line in f:
            if re.match(r"\s+%\s+cumulative", line):
                in_table = True
                continue
            if not in_table:
                continue
            if line.strip() == "":
                continue
            parts = line.strip().split()
            if len(parts) >= 2 and re.match(r'^[\d.]', parts[0]):
                funcs.add(parts[-1])
    return funcs


def fmt_calls(n):
    if n >= 1e9:
        return f"{n/1e9:.2f}B"
    if n >= 1e6:
        return f"{n/1e6:.1f}M"
    if n >= 1e3:
        return f"{n/1e3:.1f}K"
    return str(int(n))


lines = []
lines.append("# Falcon Profiling Results: O0 vs O3 (Inlining Enabled)")
lines.append("")
lines.append("> 1000 iterations each | `-pg` only (inlining enabled) | Falcon-512 and Falcon-1024")
lines.append("")

# Summary speedup table
lines.append("## Total Runtime Summary (cumulative seconds, 1000 ops)")
lines.append("")
lines.append("| Operation | O0 (s) | O3 (s) | Speedup |")
lines.append("|-----------|-------:|-------:|--------:|")

speedups = {}
for op in OPERATIONS:
    p0 = os.path.join(RESULTS_DIR, f"analysis_{op}_O0.txt")
    p3 = os.path.join(RESULTS_DIR, f"analysis_{op}_O3.txt")
    if not os.path.exists(p0) or not os.path.exists(p3):
        continue
    t0, _ = parse_flat_profile(p0)
    t3, _ = parse_flat_profile(p3)
    sp = t0 / t3 if t3 > 0 else 0
    speedups[op] = sp
    lines.append(f"| `{op}` | {t0:.2f} | {t3:.2f} | **{sp:.2f}×** |")

lines.append("")

# Inlined functions summary table
lines.append("## Inlined Functions Summary (present in O0, absent in O3)")
lines.append("")
lines.append("| Operation | O0 visible | O3 visible | Inlined by O3 |")
lines.append("|-----------|----------:|----------:|--------------:|")

all_inlined = {}
for op in OPERATIONS:
    p0 = os.path.join(RESULTS_DIR, f"analysis_{op}_O0.txt")
    p3 = os.path.join(RESULTS_DIR, f"analysis_{op}_O3.txt")
    if not os.path.exists(p0) or not os.path.exists(p3):
        continue
    f0 = parse_flat_profile_all(p0)
    f3 = parse_flat_profile_all(p3)
    inlined = f0 - f3
    all_inlined[op] = inlined
    lines.append(f"| `{op}` | {len(f0)} | {len(f3)} | **{len(inlined)}** |")

lines.append("")

# Functions inlined in all variants
if all_inlined:
    common = set.intersection(*all_inlined.values())
    lines.append(f"**Functions inlined across all 6 variants ({len(common)}):** "
                 + ", ".join(f"`{f}`" for f in sorted(common)))
    lines.append("")

# Per-operation detail
for op in OPERATIONS:
    p0 = f"analysis_{op}_O0.txt"
    p3 = f"analysis_{op}_O3.txt"
    if not os.path.exists(p0) or not os.path.exists(p3):
        continue

    t0, top0 = parse_flat_profile(p0)
    t3, top3 = parse_flat_profile(p3)
    inlined = sorted(f for f in all_inlined.get(op, set())
                     if not f.startswith('['))  # exclude anonymous [N] nodes

    lines.append("---")
    lines.append("")
    lines.append(f"## {op.replace('_', ' ').upper()}")
    lines.append("")
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

    if inlined:
        lines.append("")
        lines.append("### Inlined by O3 (named functions only)")
        lines.append("")
        for f in inlined:
            lines.append(f"- `{f}`")

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
lines.append("| `-O3` | Aggressive inlining enabled. Small leaf functions (`fpr_*`, `modp_*`, `mq_*`, `zint_*`) are inlined into callers and disappear from the profile. |")
lines.append("| `-pg` | Inserts `mcount` hooks at every function entry for call counting and adds timer sampling for time attribution. Inlined functions no longer have entry hooks and are invisible. |")
lines.append("")
lines.append("### Key observations")
lines.append("")
lines.append("- **At O3, the compiler inlines 20–116 functions per operation.** The profile loses leaf-function detail but better reflects optimized execution.")
lines.append("- **keygen** loses nearly half its visible functions (204→93 for Falcon-512). All `fpr_*`, `modp_*`, `zint_*` helpers vanish — inlined into `poly_*` / `solve_NTRU*` callers.")
lines.append("- **sign** loses `do_sign_dyn` and `ffSampling_fft_dyntree` — the core recursive FFT sampler is fully absorbed. `BerExp` and `smallints_to_fpr` also disappear.")
lines.append("- **verify** is the lightest operation; even so, all `mq_add/sub/montymul/rshift1` helpers are inlined into `mq_NTT` / `mq_iNTT`.")
lines.append("- **Universally inlined** (all 6 variants): `keccak_inc_finalize`, `keccak_inc_init`, `keccak_inc_squeeze`, `mq_add`, `mq_montymul`, `mq_rshift1`, `mq_sub`.")

out_path = os.path.join(RESULTS_DIR, "inlining_report.md")
with open(out_path, "w") as f:
    f.write("\n".join(lines) + "\n")

print(f"Written: {out_path}")
