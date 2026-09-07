# Falcon Software and Profiling

A self-contained implementation and function-level performance study of the
**Falcon-512** and **Falcon-1024** post-quantum signature schemes. The project
builds the PQClean-derived C implementation, checks its signing flow, and uses
`gprof` to compare `-O0` and `-O3` behavior across key generation, signing, and
verification.

The source code and profiling artifacts were previously maintained in the
separate `falcon_swcode` and `falcon_profile` repositories. Their Git histories
are preserved in this repository.

## Highlights

- One-command build and functional smoke test
- Six profiling workloads: KeyGen, Sign, and Verify for Falcon-512/1024
- Direct `-O0` versus `-O3` comparison over 1,000 iterations
- Raw `gprof` output, call graphs, a Markdown analysis, and a PDF report
- Setup work excluded from Sign and Verify measurements with `moncontrol`

## Repository layout

```text
.
├── falcon-512/clean/        # Falcon-512 implementation
├── falcon-1024/clean/       # Falcon-1024 implementation
├── common/                  # Shared hashing and randomness utilities
├── src/
│   ├── main.c               # Functional smoke test
│   └── main_profile.c       # Profiling workload dispatcher
├── test/                    # PQClean test programs
├── scripts/                 # Profiling and report-generation tools
├── results/                 # Raw profiles and Markdown reports
├── graphs/                  # Generated call graphs
├── tex/                     # LaTeX source and compiled report
└── Makefile
```

## Requirements

The basic build requires GCC, GNU Make, `gprof` (binutils), and Python 3.
Generating call graphs additionally requires Graphviz; the pipeline creates a
local virtual environment for `gprof2dot`. Building the PDF requires a LaTeX
installation with `pdflatex`.

On Ubuntu/Debian:

```bash
sudo apt install build-essential binutils graphviz python3-venv
```

## Build and test

```bash
make
./falcon_test
```

The smoke test generates a Falcon-512 key pair, signs a message, and verifies
the signature.

## Run the profiling pipeline

```bash
bash scripts/run_profile.sh
```

The pipeline performs the following steps:

1. Builds `falcon_profile_O0` with `-O0 -pg` and `falcon_profile_O3` with
   `-O3 -pg`.
2. Runs KeyGen, Sign, and Verify for Falcon-512 and Falcon-1024, with 1,000
   iterations per workload.
3. Writes raw profiles to `results/analysis_*.txt`.
4. Regenerates `results/result.md`, call-graph PNGs, and the LaTeX report.

To build only the profiling executables or run one workload:

```bash
make falcon_profile_O0 falcon_profile_O3
./falcon_profile_O3 falcon512_sign
```

Accepted workload names are:

```text
falcon512_keygen   falcon512_sign   falcon512_verify
falcon1024_keygen  falcon1024_sign  falcon1024_verify
```

## Results

Measured cumulative runtime for 1,000 operations:

| Workload | O0 (s) | O3 (s) | Speedup |
|---|---:|---:|---:|
| Falcon-512 KeyGen | 52.37 | 12.37 | 4.23× |
| Falcon-512 Sign | 16.78 | 3.24 | 5.18× |
| Falcon-512 Verify | 0.17 | 0.03 | 5.67× |
| Falcon-1024 KeyGen | 154.45 | 34.26 | 4.51× |
| Falcon-1024 Sign | 36.09 | 7.57 | 4.77× |
| Falcon-1024 Verify | 0.35 | 0.15 | 2.33× |

Key observations:

- Key generation is the most expensive workload and combines NTT and FFT
  arithmetic.
- Signing is dominated by floating-point FFT operations used by the lattice
  sampler.
- Verification is substantially faster and primarily uses integer NTT and
  SHAKE-256 operations.
- Compiler inlining at `-O3` improves realistic performance but folds some
  leaf functions into their callers, reducing per-function visibility in
  `gprof`.

See the [detailed profiling report](results/result.md),
[function classification](results/function_classification.md), and
[inlining analysis](results/inlining_report.md). The generated PDF is available
at [`tex/falcon_profiling.pdf`](tex/falcon_profiling.pdf).

Profiling measurements depend on the CPU, compiler, system load, and sampling
resolution. The checked-in results should therefore be treated as one measured
environment, not universal Falcon performance figures.

## Regenerate individual reports

```bash
python3 scripts/gen_result.py
python3 scripts/gen_inlining_report.py
python3 scripts/gen_tex.py
make -C tex
```

## License and provenance

The Falcon implementations are derived from PQClean's clean implementations.
Their license notices are retained in `falcon-512/clean/LICENSE` and
`falcon-1024/clean/LICENSE`.
