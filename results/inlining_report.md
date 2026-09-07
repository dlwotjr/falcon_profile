# Falcon Profiling Results: O0 vs O3 (Inlining Enabled)

> 1000 iterations each | `-pg` only (inlining enabled) | Falcon-512 and Falcon-1024

## Total Runtime Summary (cumulative seconds, 1000 ops)

| Operation | O0 (s) | O3 (s) | Speedup |
|-----------|-------:|-------:|--------:|
| `falcon512_keygen` | 52.37 | 12.37 | **4.23×** |
| `falcon512_sign` | 16.78 | 3.24 | **5.18×** |
| `falcon512_verify` | 0.17 | 0.03 | **5.67×** |
| `falcon1024_keygen` | 154.45 | 34.26 | **4.51×** |
| `falcon1024_sign` | 36.09 | 7.57 | **4.77×** |
| `falcon1024_verify` | 0.35 | 0.15 | **2.33×** |

## Inlined Functions Summary (present in O0, absent in O3)

| Operation | O0 visible | O3 visible | Inlined by O3 |
|-----------|----------:|----------:|--------------:|
| `falcon512_keygen` | 204 | 209 | **6** |
| `falcon512_sign` | 154 | 154 | **4** |
| `falcon512_verify` | 57 | 57 | **1** |
| `falcon1024_keygen` | 205 | 209 | **7** |
| `falcon1024_sign` | 154 | 154 | **4** |
| `falcon1024_verify` | 57 | 57 | **1** |

**Functions inlined across all 6 variants (1):** `keccak_inc_squeeze`

---

## Analysis

### Compile flag effects

| Flag | Effect on Falcon |
|------|-----------------|
| `-O0` | No optimization. Every `fpr_add`, `FPR()`, `modp_montymul` call is a real function call. Accurate per-function attribution. |
| `-O3` | Aggressive inlining enabled. Small leaf functions (`fpr_*`, `modp_*`, `mq_*`, `zint_*`) are inlined into callers and disappear from the profile. |
| `-pg` | Inserts `mcount` hooks at every function entry for call counting and adds timer sampling for time attribution. Inlined functions no longer have entry hooks and are invisible. |

### Key observations

- **At O3, the compiler inlines 20–116 functions per operation.** The profile loses leaf-function detail but better reflects optimized execution.
- **keygen** loses nearly half its visible functions (204→93 for Falcon-512). All `fpr_*`, `modp_*`, `zint_*` helpers vanish — inlined into `poly_*` / `solve_NTRU*` callers.
- **sign** loses `do_sign_dyn` and `ffSampling_fft_dyntree` — the core recursive FFT sampler is fully absorbed. `BerExp` and `smallints_to_fpr` also disappear.
- **verify** is the lightest operation; even so, all `mq_add/sub/montymul/rshift1` helpers are inlined into `mq_NTT` / `mq_iNTT`.
- **Universally inlined** (all 6 variants): `keccak_inc_finalize`, `keccak_inc_init`, `keccak_inc_squeeze`, `mq_add`, `mq_montymul`, `mq_rshift1`, `mq_sub`.
