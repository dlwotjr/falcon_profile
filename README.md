# Falcon Profiling

Function-level profiling of the **Falcon** post-quantum signature scheme
(Falcon-512 and Falcon-1024) using `gprof`.
Compares **-O0** and **-O3** build performance across 1000 iterations of
KeyGen, Sign, and Verify.

## Repository Layout

```
falcon_profiling/
├── README.md
├── .gitignore
│
├── src/
│   └── main_profile.c        # Profiling harness — dispatches to one
│                             #   of 6 operations via argv[1]
│
├── scripts/
│   ├── run_profile.sh        # Full pipeline: build → profile → generate
│   ├── gen_result.py         # Reads analysis files → results/result.md
│   └── gen_tex.py            # Reads analysis files → tex/falcon_profiling.tex
│
├── results/
│   ├── analysis_<variant>_<op>_<OPT>.txt   # raw gprof output (12 files)
│   └── result.md             # O0 vs O3 comparison summary (Markdown)
│
├── graphs/
│   └── output_<variant>_<op>_<OPT>.png     # call graph images (12 files)
│
└── tex/
    ├── Makefile              # compile .tex → .pdf
    ├── falcon_profiling.tex  # LaTeX report (auto-generated)
    └── falcon_profiling.pdf  # compiled PDF (23 pages)
```

## Dependencies

| Tool | Purpose | Install |
|------|---------|---------|
| `gcc` | C compiler | `sudo apt install gcc` |
| `gprof` | profiler | included in `binutils` |
| `graphviz` | call graph PNG | `sudo apt install graphviz` |
| `python3` | script runner | `sudo apt install python3` |
| `gprof2dot` | dot file generator | installed automatically into `venv/` |
| `pdflatex` | PDF compilation | `sudo apt install texlive-full` |

## Quick Start

### 1. Prerequisites — build the Falcon source

This repo expects the PQClean Falcon source at `../swcode/` (sibling directory).

```
workspace/
├── swcode/          # Falcon source (PQClean)
└── falcon_profiling/  # this repo
```

### 2. Run everything at once

From the `falcon_profiling/` root:

```bash
bash scripts/run_profile.sh
```

This will:
1. Build `falcon_profile_O0` and `falcon_profile_O3` in `../swcode/` if needed
2. Run all 6 operations × 2 builds = 12 gprof runs → `results/analysis_*.txt`
3. Generate `results/result.md`
4. Generate `graphs/output_*.png` call graph images (needs graphviz)
5. Generate `tex/falcon_profiling.tex`

### 3. Compile the PDF

```bash
make -C tex
```

Output: `tex/falcon_profiling.pdf`

---

## Step-by-step (Manual)

### Build the profiling binaries

```bash
# from ../swcode/
make falcon_profile_O0 falcon_profile_O3
```

Compiler flags:
| Binary | Flags |
|--------|-------|
| `falcon_profile_O0` | `-O0 -fno-inline -pg` |
| `falcon_profile_O3` | `-O3 -fno-inline -pg` |

`-pg` inserts gprof instrumentation hooks.
`-fno-inline` keeps functions visible even at `-O3`.

### Run a single operation

```bash
# from ../swcode/
./falcon_profile_O3 falcon512_sign
gprof ./falcon_profile_O3 gmon.out > analysis.txt
```

Available operations:
- `falcon512_keygen` / `falcon512_sign` / `falcon512_verify`
- `falcon1024_keygen` / `falcon1024_sign` / `falcon1024_verify`

### Regenerate Markdown summary

```bash
# from falcon_profiling/
python3 scripts/gen_result.py
# writes: results/result.md
```

### Regenerate call graph PNGs

```bash
# from falcon_profiling/
python3 -m venv venv && venv/bin/pip install -q gprof2dot
for f in results/analysis_*.txt; do
    op=$(basename "$f" .txt)
    venv/bin/gprof2dot -f prof "$f" | dot -Tpng -o "graphs/output_${op}.png"
done
```

### Regenerate LaTeX report

```bash
# from falcon_profiling/
python3 scripts/gen_tex.py
# writes: tex/falcon_profiling.tex
make -C tex
# writes: tex/falcon_profiling.pdf
```

---

## Profiling Results Summary

### Total runtime (1000 iterations)

| Operation | O0 (s) | O3 (s) | Speedup |
|-----------|-------:|-------:|--------:|
| falcon512 keygen  | 51.95 | 11.74 | **4.43×** |
| falcon512 sign    | 15.93 |  3.24 | **4.92×** |
| falcon512 verify  |  0.19 |  0.05 | **3.80×** |
| falcon1024 keygen | 143.26 | 34.31 | **4.18×** |
| falcon1024 sign   |  34.23 |  6.81 | **5.03×** |
| falcon1024 verify |   0.59 |  0.08 | **7.37×** |

### Function category breakdown (O3)

| Operation | Hash/PRNG | Integer NTT | FP/FFT |
|-----------|----------:|------------:|-------:|
| keygen    | ~4%       | ~35%        | ~55%   |
| sign      | ~2%       | ~2%         | ~95%   |
| verify    | ~35%      | ~60%        | ~5%    |

**Key observations:**
- **Sign** is almost entirely floating-point FFT (`fpr_add` ~49%, `fpr_mul` ~16%) driven by the `ffSampling_fft_dyntree` recursive lattice sampler.
- **Verify** uses no floating-point FFT at all — only integer NTT (`mq_montymul`, `mq_NTT`) and SHAKE-256 hashing, making it 70–300× faster than keygen.
- **Falcon-1024 costs ~2–3× more** than Falcon-512 (FFT is O(N log N), N doubles).
- Under **O3**, the `FPR` constructor overhead drops from ~15% → ~4% and `mq_montymul` vectorises well, giving 7× speedup on verify.

---

## Call Graph Trees

PNG call graphs are in `graphs/`. Each node shows `% total time` and self-seconds.
Hot nodes are red/orange.

| Operation | O0 | O3 |
|-----------|----|----|
| falcon512 keygen  | [O0](graphs/output_falcon512_keygen_O0.png)  | [O3](graphs/output_falcon512_keygen_O3.png)  |
| falcon512 sign    | [O0](graphs/output_falcon512_sign_O0.png)    | [O3](graphs/output_falcon512_sign_O3.png)    |
| falcon512 verify  | [O0](graphs/output_falcon512_verify_O0.png)  | [O3](graphs/output_falcon512_verify_O3.png)  |
| falcon1024 keygen | [O0](graphs/output_falcon1024_keygen_O0.png) | [O3](graphs/output_falcon1024_keygen_O3.png) |
| falcon1024 sign   | [O0](graphs/output_falcon1024_sign_O0.png)   | [O3](graphs/output_falcon1024_sign_O3.png)   |
| falcon1024 verify | [O0](graphs/output_falcon1024_verify_O0.png) | [O3](graphs/output_falcon1024_verify_O3.png) |

---

## LaTeX Report

`tex/falcon_profiling.pdf` is a 23-page report containing:
- Runtime summary table (O0 vs O3)
- Category weight tables (Hash / Integer / FP) per operation
- Per-function detail tables for all 12 operation × build combinations
- Key findings and analysis

Regenerate after new profiling runs:
```bash
python3 scripts/gen_tex.py && make -C tex
```
