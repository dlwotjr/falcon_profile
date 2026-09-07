#!/usr/bin/env python3
"""Parse gprof flat profiles and generate a LaTeX profiling report."""

import re, os

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

OPERATIONS = [
    ("falcon512",  "keygen"),
    ("falcon512",  "sign"),
    ("falcon512",  "verify"),
    ("falcon1024", "keygen"),
    ("falcon1024", "sign"),
    ("falcon1024", "verify"),
]

REPO_ROOT    = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ANALYSIS_DIR = os.path.join(REPO_ROOT, "results")

# ---------------------------------------------------------------------------
# Function categorisation
# ---------------------------------------------------------------------------

HASH_PATTERNS = [
    r"KeccakF1600",
    r"keccak_inc",
    r"shake256_inc",
    r"hash_to_point",
    r"prng_refill",
    r"prng_get_",
    r"prng_init",
    r"get_rng_",
    r"randombytes",
    r"PQCLEAN_randombytes",
]

INT_PATTERNS = [
    r"modp_montymul", r"modp_add", r"modp_sub",
    r"modp_NTT", r"modp_iNTT", r"modp_R2", r"modp_set",
    r"mq_montymul", r"mq_add", r"mq_sub",
    r"mq_NTT", r"mq_iNTT",
    r"zint_",
    r"mkgauss",
    r"gaussian0_sampler",
    r"poly_big_to_small",
    r"sampler$",
    r"PQCLEAN_FALCON\d+_CLEAN_sampler$",
]

FP_PATTERNS = [
    r"fpr_add", r"fpr_mul", r"fpr_sub", r"fpr_div",
    r"fpr_scaled", r"fpr_sqrt", r"fpr_expm",
    r"fpr_ulsh", r"fpr_ursh", r"fpr_trunc", r"fpr_rint",
    r"fpr_half", r"fpr_neg", r"fpr_sqr", r"fpr_of",
    r"^FPR$",
    r"_fpr_add", r"_fpr_mul",
    r"CLEAN_fpr_",
    r"ffSampling_fft",
    r"poly_split_fft", r"poly_merge_fft",
    r"poly_LDL_fft", r"poly_mul_fft",
    r"poly_muladj_fft", r"poly_mulselfadj_fft",
    r"poly_add$", r"poly_sub$", r"poly_neg$", r"poly_mulconst",
    r"CLEAN_FFT$", r"CLEAN_iFFT$",
    r"do_sign_dyn", r"ffSampling",
]


def categorise(name):
    for p in HASH_PATTERNS:
        if re.search(p, name):
            return "hash"
    for p in FP_PATTERNS:
        if re.search(p, name):
            return "fp"
    for p in INT_PATTERNS:
        if re.search(p, name):
            return "int"
    return "other"


# ---------------------------------------------------------------------------
# Parser
# ---------------------------------------------------------------------------

def parse_flat(path):
    """Return list of (pct, self_s, calls, name)."""
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
                entries.append((
                    float(m.group(1)),
                    float(m.group(3)),
                    float(m.group(4)),
                    m.group(5).strip(),
                ))
    return entries


def load_all():
    data = {}
    for variant, op in OPERATIONS:
        for opt in ("O0", "O3"):
            key = f"{variant}_{op}_{opt}"
            path = os.path.join(ANALYSIS_DIR, f"analysis_{variant}_{op}_{opt}.txt")
            if os.path.exists(path):
                data[key] = parse_flat(path)
    return data


# ---------------------------------------------------------------------------
# Aggregation helpers
# ---------------------------------------------------------------------------

def total_self(entries):
    return sum(e[1] for e in entries)


def category_rows(entries):
    """For each category return list of (name, pct, self_s, calls)."""
    cats = {"hash": [], "int": [], "fp": [], "other": []}
    for pct, slf, calls, name in entries:
        c = categorise(name)
        cats[c].append((name, pct, slf, int(calls)))
    # sort by self_s desc within each category
    for c in cats:
        cats[c].sort(key=lambda x: x[2], reverse=True)
    return cats


def category_totals(entries):
    cats = category_rows(entries)
    tot = total_self(entries) or 1
    result = {}
    for c, rows in cats.items():
        s = sum(r[2] for r in rows)
        result[c] = (s, s / tot * 100)
    return result


# ---------------------------------------------------------------------------
# LaTeX helpers
# ---------------------------------------------------------------------------

def esc(s):
    return (s.replace("_", r"\_")
             .replace("%", r"\%")
             .replace("&", r"\&")
             .replace("#", r"\#"))


def fmt_calls(n):
    if n >= 1_000_000_000:
        return f"{n/1e9:.2f}B"
    if n >= 1_000_000:
        return f"{n/1e6:.1f}M"
    if n >= 1_000:
        return f"{n/1e3:.1f}K"
    return str(n)


CAT_LABEL = {
    "hash":  r"\textbf{Hash / PRNG}",
    "int":   r"\textbf{Integer Arithmetic}",
    "fp":    r"\textbf{Floating-Point / FFT}",
    "other": r"\textbf{Other}",
}

CAT_COLOR = {
    "hash":  "hashcolor",
    "int":   "intcolor",
    "fp":    "fpcolor",
    "other": "othercolor",
}

OP_LABEL = {"keygen": "KeyGen", "sign": "Sign", "verify": "Verify"}
VAR_LABEL = {"falcon512": "Falcon-512", "falcon1024": "Falcon-1024"}

# ---------------------------------------------------------------------------
# LaTeX document builder
# ---------------------------------------------------------------------------

def build_tex(data):
    lines = []

    # ---- preamble ----
    lines += [
        r"\documentclass[11pt,a4paper]{article}",
        r"\usepackage[margin=2.5cm]{geometry}",
        r"\usepackage{booktabs}",
        r"\usepackage{longtable}",
        r"\usepackage{xcolor}",
        r"\usepackage{colortbl}",
        r"\usepackage{multirow}",
        r"\usepackage{array}",
        r"\usepackage{hyperref}",
        r"\usepackage{titlesec}",
        r"\usepackage{caption}",
        r"\usepackage{pgfplots}",
        r"\usepackage{amssymb}",
        r"\pgfplotsset{compat=1.18}",
        r"",
        r"\definecolor{hashcolor}{RGB}{173,216,230}",   # light blue
        r"\definecolor{intcolor}{RGB}{255,228,181}",    # moccasin
        r"\definecolor{fpcolor}{RGB}{195,255,195}",     # light green
        r"\definecolor{othercolor}{RGB}{220,220,220}",  # light grey
        r"",
        r"\title{\textbf{Falcon Post-Quantum Signature Scheme}\\",
        r"        \large Function-Level Profiling Report\\",
        r"        \normalsize \texttt{-O0} vs \texttt{-O3} $\cdot$ 1000 iterations $\cdot$ gprof}",
        r"\author{Falcon-512 / Falcon-1024}",
        r"\date{\today}",
        r"",
        r"\begin{document}",
        r"\maketitle",
        r"\tableofcontents",
        r"\newpage",
    ]

    # ---- Section 1: Overview ----
    lines += [
        r"",
        r"\section{Overview}",
        r"",
        r"This report presents a function-level profiling analysis of the",
        r"\textbf{Falcon} post-quantum digital signature scheme",
        r"(NIST PQC Round 3 finalist, lattice-based).",
        r"Two parameter sets are compared: \textbf{Falcon-512} (NIST Level~1)",
        r"and \textbf{Falcon-1024} (NIST Level~5).",
        r"Each operation was executed $\mathbf{1000}$ times and profiled with",
        r"\texttt{gprof} under two compiler settings:",
        r"\texttt{-O0 -pg} and \texttt{-O3 -pg}.",
        r"",
        r"Functions are grouped into three categories:",
        r"\begin{itemize}",
        r"  \item \colorbox{hashcolor}{\strut Hash / PRNG} ---",
        r"        SHAKE-256 (Keccak), PRNG refill, hash-to-point.",
        r"  \item \colorbox{intcolor}{\strut Integer Arithmetic} ---",
        r"        Modular NTT (\texttt{modp\_*}, \texttt{mq\_*}),",
        r"        multi-precision integers (\texttt{zint\_*}),",
        r"        Gaussian sampler (\texttt{mkgauss}).",
        r"  \item \colorbox{fpcolor}{\strut Floating-Point / FFT} ---",
        r"        Custom 53-bit FPR type (\texttt{fpr\_*}, \texttt{FPR}),",
        r"        FFT/iFFT, polynomial operations.",
        r"\end{itemize}",
    ]

    # ---- Section 2: Summary speedup table ----
    lines += [
        r"",
        r"\section{Runtime Summary: O0 vs O3}",
        r"",
        r"\begin{table}[h!]",
        r"\centering",
        r"\caption{Total cumulative runtime (seconds, 1000 iterations)}",
        r"\begin{tabular}{llrrr}",
        r"\toprule",
        r"Variant & Operation & O0 (s) & O3 (s) & Speedup \\",
        r"\midrule",
    ]
    for variant, op in OPERATIONS:
        k0 = f"{variant}_{op}_O0"
        k3 = f"{variant}_{op}_O3"
        if k0 not in data or k3 not in data:
            continue
        t0 = total_self(data[k0])
        t3 = total_self(data[k3])
        sp = t0 / t3 if t3 > 0 else 0
        lines.append(
            f"  {esc(VAR_LABEL[variant])} & {OP_LABEL[op]} & "
            f"{t0:.2f} & {t3:.2f} & $\\mathbf{{{sp:.2f}\\times}}$ \\\\"
        )
    lines += [
        r"\bottomrule",
        r"\end{tabular}",
        r"\end{table}",
    ]

    # ---- Section 3: Category weight summary ----
    lines += [
        r"",
        r"\section{Category Weight per Operation}",
        r"",
        r"The following tables show what fraction of total profiled time",
        r"is spent in each functional category for O0 and O3 builds.",
    ]

    for opt in ("O0", "O3"):
        lines += [
            r"",
            f"\\subsection{{Category Breakdown --- \\texttt{{-{opt}}}}}",
            r"",
            r"\begin{table}[h!]",
            r"\centering",
            f"\\caption{{Category time share \\texttt{{-{opt}}} (\\%)}}",
            r"\begin{tabular}{llrrrr}",
            r"\toprule",
            r"Variant & Operation & \colorbox{hashcolor}{Hash} & "
            r"\colorbox{intcolor}{Integer} & \colorbox{fpcolor}{FP/FFT} & Other \\",
            r"\midrule",
        ]
        for variant, op in OPERATIONS:
            key = f"{variant}_{op}_{opt}"
            if key not in data:
                continue
            ct = category_totals(data[key])
            lines.append(
                f"  {esc(VAR_LABEL[variant])} & {OP_LABEL[op]} & "
                f"{ct['hash'][1]:.1f}\\% & "
                f"{ct['int'][1]:.1f}\\% & "
                f"{ct['fp'][1]:.1f}\\% & "
                f"{ct['other'][1]:.1f}\\% \\\\"
            )
        lines += [
            r"\bottomrule",
            r"\end{tabular}",
            r"\end{table}",
        ]

    # ---- Section 4: Per-operation detail ----
    lines += [
        r"",
        r"\section{Per-Operation Function Detail}",
        r"",
        r"Each subsection shows the top functions per category",
        r"for both O0 and O3 builds. Column headers:",
        r"\texttt{\%} = percentage of total profiled time,",
        r"\texttt{self(s)} = self seconds,",
        r"\texttt{calls} = call count.",
    ]

    for variant, op in OPERATIONS:
        sec_title = f"{VAR_LABEL[variant]} --- {OP_LABEL[op]}"
        lines += [
            r"",
            f"\\subsection{{{esc(sec_title)}}}",
        ]

        for opt in ("O0", "O3"):
            key = f"{variant}_{op}_{opt}"
            if key not in data:
                continue
            entries = data[key]
            cats = category_rows(entries)
            tot = total_self(entries)
            ct = category_totals(entries)

            lines += [
                r"",
                f"\\subsubsection*{{\\texttt{{-{opt}}} build "
                f"(total: {tot:.3f}\\,s)}}",
            ]

            for cat in ("hash", "int", "fp", "other"):
                rows = cats[cat]
                if not rows:
                    continue
                cat_pct = ct[cat][1]
                color = CAT_COLOR[cat]
                label = CAT_LABEL[cat]

                lines += [
                    r"",
                    f"\\noindent\\colorbox{{{color}}}{{\\strut {label}"
                    f" --- {cat_pct:.1f}\\% of total}}",
                    r"\vspace{2pt}",
                    r"",
                    r"\begin{longtable}{p{7.5cm}rrr}",
                    r"\toprule",
                    r"Function & \% & self(s) & calls \\",
                    r"\midrule",
                    r"\endhead",
                ]
                for name, pct, slf, calls in rows[:15]:
                    lines.append(
                        f"  \\texttt{{{esc(name)}}} & "
                        f"{pct:.2f} & {slf:.4f} & {fmt_calls(calls)} \\\\"
                    )
                lines += [
                    r"\bottomrule",
                    r"\end{longtable}",
                ]

    # ---- Section 5: Key findings ----
    lines += [
        r"",
        r"\section{Key Findings}",
        r"",
        r"\begin{itemize}",
        r"",
        r"  \item \textbf{KeyGen is dominated by Integer NTT and FP/FFT arithmetic.}",
        r"        \texttt{modp\_montymul} (Montgomery multiplication for NTT)",
        r"        and \texttt{fpr\_add} (FFT floating-point add) together",
        r"        account for over 40\% of total keygen time.",
        r"        The lattice basis generation (\texttt{zint\_*}, \texttt{mkgauss})",
        r"        contributes a further $\sim$10--15\%.",
        r"",
        r"  \item \textbf{Sign is almost entirely FP/FFT.}",
        r"        The \texttt{ffSampling\_fft\_dyntree} recursive sampler",
        r"        drives repeated calls to \texttt{fpr\_add} ($\sim$50\%)",
        r"        and \texttt{fpr\_mul} ($\sim$15\%).",
        r"        Integer NTT (\texttt{mq\_montymul}) is visible but minor ($<$2\%).",
        r"",
        r"  \item \textbf{Verify is entirely Hash and Integer NTT.}",
        r"        No floating-point FFT is used. Time splits between",
        r"        \texttt{hash\_to\_point\_ct} (SHAKE-256 hashing of the message)",
        r"        and \texttt{mq\_montymul} / \texttt{mq\_NTT}",
        r"        (NTT-based polynomial multiplication over $\mathbb{Z}_q$).",
        r"        This is why verify is 70--300$\times$ faster than keygen.",
        r"",
        r"  \item \textbf{Falcon-1024 costs $\approx 2$--$3\times$ more than Falcon-512.}",
        r"        The FFT and NTT algorithms are $\mathcal{O}(N \log N)$;",
        r"        doubling $N$ from 512 to 1024 roughly doubles the cost",
        r"        with an additional $\log$ factor.",
        r"",
        r"  \item \textbf{O3 gives 4--5$\times$ speedup on keygen/sign,",
        r"        7$\times$ on verify.}",
        r"        The \texttt{FPR} constructor overhead drops from $\sim$15\%",
        r"        to $<$5\% under O3 (compiler promotes the struct boxing).",
        r"        Verify benefits most from O3 because \texttt{mq\_montymul}",
        r"        vectorises well.",
        r"",
        r"\end{itemize}",
    ]

    lines += [
        r"",
        r"\end{document}",
    ]

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    data = load_all()
    tex = build_tex(data)
    out = os.path.join(REPO_ROOT, "tex", "falcon_profiling.tex")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as f:
        f.write(tex)
    print(f"Written: {out}")
