# Falcon Profiling Results: O0 vs O3

> 1000 iterations each | `-pg` instrumentation | Falcon-512 and Falcon-1024

## Total Runtime Summary (cumulative seconds, 1000 ops)

| Operation | O0 (s) | O3 (s) | Speedup |
|-----------|-------:|-------:|--------:|
| `falcon512_keygen` | 52.37 | 12.37 | **4.23×** |
| `falcon512_sign` | 16.78 | 3.24 | **5.18×** |
| `falcon512_verify` | 0.17 | 0.03 | **5.67×** |
| `falcon1024_keygen` | 154.45 | 34.26 | **4.51×** |
| `falcon1024_sign` | 36.09 | 7.57 | **4.77×** |
| `falcon1024_verify` | 0.35 | 0.15 | **2.33×** |

---

## FALCON512 KEYGEN

Total: **52.37s** (O0) → **12.37s** (O3)  — **4.23× faster**

### O0 — Top functions

| % time | self (s) | calls | function |
|-------:|---------:|------:|----------|
| 30.13% | 15.780 | 301.5M | `PQCLEAN_FALCON512_CLEAN_fpr_add` |
| 12.99% | 6.800 | 982.1M | `modp_montymul` |
| 11.44% | 5.990 | 662.4M | `FPR` |
| 10.12% | 5.300 | 305.7M | `PQCLEAN_FALCON512_CLEAN_fpr_mul` |
| 4.63% | 2.420 | 688.0M | `modp_add` |
| 3.95% | 2.070 | 53.3M | `PQCLEAN_FALCON512_CLEAN_fpr_scaled` |
| 3.93% | 2.060 | 2.7M | `KeccakF1600_StatePermute` |
| 2.30% | 1.210 | 50.1M | `zint_mod_small_unsigned` |
| 2.25% | 1.180 | 11.4M | `mkgauss` |
| 2.02% | 1.060 | 18.2M | `zint_add_scaled_mul_small` |

### O3 — Top functions

| % time | self (s) | calls | function |
|-------:|---------:|------:|----------|
| 27.08% | 3.350 | 302.6M | `PQCLEAN_FALCON512_CLEAN_fpr_add` |
| 16.98% | 2.100 | 967.8M | `modp_montymul` |
| 12.93% | 1.600 | 306.4M | `PQCLEAN_FALCON512_CLEAN_fpr_mul` |
| 4.85% | 0.600 | 2.7M | `KeccakF1600_StatePermute` |
| 3.23% | 0.400 | 664.3M | `FPR` |
| 2.99% | 0.370 | 11.4M | `mkgauss` |
| 2.91% | 0.360 | 53.3M | `PQCLEAN_FALCON512_CLEAN_fpr_scaled` |
| 2.75% | 0.340 | 36.2M | `zint_rebuild_CRT.constprop.2` |
| 2.43% | 0.300 | 49.5M | `zint_mod_small_unsigned` |
| 2.43% | 0.300 | 18.1M | `zint_add_scaled_mul_small` |

---

## FALCON512 SIGN

Total: **16.78s** (O0) → **3.24s** (O3)  — **5.18× faster**

### O0 — Top functions

| % time | self (s) | calls | function |
|-------:|---------:|------:|----------|
| 48.33% | 8.110 | 148.4M | `PQCLEAN_FALCON512_CLEAN_fpr_add` |
| 17.82% | 2.990 | 297.1M | `FPR` |
| 13.86% | 2.330 | 133.8M | `PQCLEAN_FALCON512_CLEAN_fpr_mul` |
| 3.25% | 0.550 | 148.4M | `fpr_ulsh` |
| 3.16% | 0.530 | 12.0M | `PQCLEAN_FALCON512_CLEAN_fpr_scaled` |
| 2.29% | 0.390 | 152.0M | `fpr_ursh` |
| 1.34% | 0.230 | 2.3M | `PQCLEAN_FALCON512_CLEAN_fpr_div` |
| 1.19% | 0.200 | 21.0M | `mq_montymul` |
| 1.19% | 0.200 | 512.0K | `PQCLEAN_FALCON512_CLEAN_fpr_sqrt` |
| 1.19% | 0.200 | 39.2K | `PQCLEAN_FALCON512_CLEAN_prng_refill` |

### O3 — Top functions

| % time | self (s) | calls | function |
|-------:|---------:|------:|----------|
| 49.07% | 1.590 | 148.4M | `PQCLEAN_FALCON512_CLEAN_fpr_add` |
| 19.44% | 0.630 | 133.8M | `PQCLEAN_FALCON512_CLEAN_fpr_mul` |
| 7.10% | 0.230 | 297.0M | `FPR` |
| 4.63% | 0.150 | 2.3M | `PQCLEAN_FALCON512_CLEAN_fpr_div` |
| 3.40% | 0.110 | 152.0M | `fpr_trunc` |
| 2.16% | 0.070 | 152.0M | `fpr_ursh` |
| 2.16% | 0.070 | 1.8M | `PQCLEAN_FALCON512_CLEAN_fpr_expm_p63` |
| 1.23% | 0.040 | 20.0M | `mq_montymul` |
| 1.23% | 0.040 | 12.0M | `PQCLEAN_FALCON512_CLEAN_fpr_scaled` |
| 1.23% | 0.040 | 511.0K | `PQCLEAN_FALCON512_CLEAN_poly_LDL_fft` |

---

## FALCON512 VERIFY

Total: **0.17s** (O0) → **0.03s** (O3)  — **5.67× faster**

### O0 — Top functions

| % time | self (s) | calls | function |
|-------:|---------:|------:|----------|
| 64.71% | 0.110 | 8.4M | `mq_montymul` |
| 11.76% | 0.020 | 6.9M | `mq_add` |
| 11.76% | 0.020 | 1.0K | `PQCLEAN_FALCON512_CLEAN_hash_to_point_ct` |
| 5.88% | 0.010 | 11.0K | `KeccakF1600_StatePermute` |
| 5.88% | 0.010 | 2.0K | `mq_NTT` |
| 0.00% | 0.000 | 7.4M | `mq_sub` |
| 0.00% | 0.000 | 717.0K | `keccak_inc_squeeze` |
| 0.00% | 0.000 | 717.0K | `shake256_inc_squeeze` |
| 0.00% | 0.000 | 9.0K | `mq_rshift1` |
| 0.00% | 0.000 | 2.0K | `keccak_inc_absorb` |

### O3 — Top functions

| % time | self (s) | calls | function |
|-------:|---------:|------:|----------|
| 33.33% | 0.010 | 512.0K | `mq_montymul.constprop.0` |
| 33.33% | 0.010 | 1.0K | `PQCLEAN_FALCON512_CLEAN_hash_to_point_ct` |
| 33.33% | 0.010 | 1.0K | `mq_iNTT` |
| 0.00% | 0.000 | 7.9M | `mq_montymul` |
| 0.00% | 0.000 | 7.4M | `mq_sub` |
| 0.00% | 0.000 | 6.9M | `mq_add` |
| 0.00% | 0.000 | 718.0K | `keccak_inc_finalize` |
| 0.00% | 0.000 | 717.0K | `shake256_inc_squeeze` |
| 0.00% | 0.000 | 11.0K | `KeccakF1600_StatePermute` |
| 0.00% | 0.000 | 9.0K | `mq_rshift1` |

---

## FALCON1024 KEYGEN

Total: **154.45s** (O0) → **34.26s** (O3)  — **4.51× faster**

### O0 — Top functions

| % time | self (s) | calls | function |
|-------:|---------:|------:|----------|
| 32.35% | 49.960 | 904.3M | `PQCLEAN_FALCON1024_CLEAN_fpr_add` |
| 12.18% | 18.810 | 2.84B | `modp_montymul` |
| 10.96% | 16.930 | 1.90B | `FPR` |
| 10.62% | 16.410 | 859.8M | `PQCLEAN_FALCON1024_CLEAN_fpr_mul` |
| 5.57% | 8.610 | 2.21B | `modp_add` |
| 3.31% | 5.110 | 75.3M | `zint_add_scaled_mul_small` |
| 3.18% | 4.910 | 126.4M | `PQCLEAN_FALCON1024_CLEAN_fpr_scaled` |
| 2.81% | 4.340 | 113.6M | `zint_mod_small_unsigned` |
| 2.18% | 3.360 | 904.3M | `fpr_ulsh` |
| 1.96% | 3.020 | 4.3M | `KeccakF1600_StatePermute` |

### O3 — Top functions

| % time | self (s) | calls | function |
|-------:|---------:|------:|----------|
| 28.49% | 9.760 | 865.4M | `PQCLEAN_FALCON1024_CLEAN_fpr_add` |
| 18.51% | 6.340 | 2.80B | `modp_montymul` |
| 12.03% | 4.120 | 828.2M | `PQCLEAN_FALCON1024_CLEAN_fpr_mul` |
| 4.38% | 1.500 | 75.2M | `zint_add_scaled_mul_small` |
| 3.94% | 1.350 | 1.82B | `FPR` |
| 3.30% | 1.130 | 2.19B | `modp_add` |
| 2.92% | 1.000 | 124.7M | `PQCLEAN_FALCON1024_CLEAN_fpr_scaled` |
| 2.60% | 0.890 | 4.1M | `KeccakF1600_StatePermute` |
| 2.36% | 0.810 | 112.2M | `zint_mod_small_unsigned` |
| 2.01% | 0.690 | 865.4M | `fpr_trunc` |

---

## FALCON1024 SIGN

Total: **36.09s** (O0) → **7.57s** (O3)  — **4.77× faster**

### O0 — Top functions

| % time | self (s) | calls | function |
|-------:|---------:|------:|----------|
| 49.99% | 18.040 | 329.5M | `PQCLEAN_FALCON1024_CLEAN_fpr_add` |
| 17.54% | 6.330 | 652.2M | `FPR` |
| 15.36% | 5.540 | 292.8M | `PQCLEAN_FALCON1024_CLEAN_fpr_mul` |
| 2.59% | 0.940 | 329.5M | `fpr_ulsh` |
| 2.36% | 0.850 | 23.8M | `PQCLEAN_FALCON1024_CLEAN_fpr_scaled` |
| 2.26% | 0.810 | 336.5M | `fpr_ursh` |
| 1.62% | 0.580 | 5.1M | `PQCLEAN_FALCON1024_CLEAN_fpr_div` |
| 1.25% | 0.450 | 76.6K | `PQCLEAN_FALCON1024_CLEAN_prng_refill` |
| 1.03% | 0.370 | 3.5M | `PQCLEAN_FALCON1024_CLEAN_fpr_expm_p63` |
| 0.86% | 0.310 | 44.0M | `mq_montymul` |

### O3 — Top functions

| % time | self (s) | calls | function |
|-------:|---------:|------:|----------|
| 53.24% | 4.030 | 329.5M | `PQCLEAN_FALCON1024_CLEAN_fpr_add` |
| 17.04% | 1.290 | 292.8M | `PQCLEAN_FALCON1024_CLEAN_fpr_mul` |
| 5.55% | 0.420 | 5.1M | `PQCLEAN_FALCON1024_CLEAN_fpr_div` |
| 4.62% | 0.350 | 652.2M | `FPR` |
| 2.77% | 0.210 | 336.5M | `fpr_trunc` |
| 2.64% | 0.200 | 336.5M | `fpr_ursh` |
| 2.38% | 0.180 | 23.8M | `PQCLEAN_FALCON1024_CLEAN_fpr_scaled` |
| 1.72% | 0.130 | 3.5M | `PQCLEAN_FALCON1024_CLEAN_fpr_expm_p63` |
| 1.19% | 0.090 | 9.0K | `PQCLEAN_FALCON1024_CLEAN_FFT` |
| 1.06% | 0.080 | 42.0M | `mq_montymul` |

---

## FALCON1024 VERIFY

Total: **0.35s** (O0) → **0.15s** (O3)  — **2.33× faster**

### O0 — Top functions

| % time | self (s) | calls | function |
|-------:|---------:|------:|----------|
| 45.71% | 0.160 | 18.4M | `mq_montymul` |
| 14.29% | 0.050 | 15.4M | `mq_add` |
| 14.29% | 0.050 | 1.0K | `PQCLEAN_FALCON1024_CLEAN_hash_to_point_ct` |
| 8.57% | 0.030 | 2.0K | `mq_NTT` |
| 5.71% | 0.020 | 16.4M | `mq_sub` |
| 5.71% | 0.020 | 1.0K | `mq_iNTT` |
| 2.86% | 0.010 | 20.0K | `KeccakF1600_StatePermute` |
| 2.86% | 0.010 | 1.0K | `mq_poly_sub` |
| 0.00% | 0.000 | 1.3M | `keccak_inc_squeeze` |
| 0.00% | 0.000 | 1.3M | `shake256_inc_squeeze` |

### O3 — Top functions

| % time | self (s) | calls | function |
|-------:|---------:|------:|----------|
| 53.33% | 0.080 | 17.4M | `mq_montymul` |
| 20.00% | 0.030 | 1.0K | `PQCLEAN_FALCON1024_CLEAN_hash_to_point_ct` |
| 6.67% | 0.010 | 16.4M | `mq_sub` |
| 6.67% | 0.010 | 15.4M | `mq_add` |
| 6.67% | 0.010 | 1.0M | `mq_montymul.constprop.0` |
| 6.67% | 0.010 | 1.0K | `PQCLEAN_FALCON1024_CLEAN_is_short` |
| 0.00% | 0.000 | 1.3M | `keccak_inc_finalize` |
| 0.00% | 0.000 | 1.3M | `shake256_inc_squeeze` |
| 0.00% | 0.000 | 20.0K | `KeccakF1600_StatePermute` |
| 0.00% | 0.000 | 10.0K | `mq_rshift1` |

---

## Analysis

### Compile flag effects

| Flag | Effect on Falcon |
|------|-----------------|
| `-O0` | No optimization. Every `fpr_add`, `FPR()`, `modp_montymul` call is a real function call. Accurate per-function attribution. |
| `-O3` | Aggressive optimization. Loop unrolling, vectorization, CSE, and inlining can move work into callers. |
| `-pg` | Inserts `mcount` hooks at every function entry for call counting and adds timer sampling for time attribution. |

### Key observations

- **keygen** is the heaviest operation — dominated by `fpr_add` / `modp_montymul` (lattice basis generation via NTT+FFT).
- **sign** is ~3× faster than keygen but still FFT-heavy (`fpr_add` ~48%). Rejection sampling (`prng_refill`, `mkgauss`) visible.
- **verify** is 70–300× faster than keygen. Uses integer NTT only (`mq_montymul`, `mq_NTT`) — no floating-point FFT.
- **Falcon-1024 costs ~2–3× more** than Falcon-512 in all operations (N doubles, FFT is O(N log N)).
- **O3 speedup** is largest for keygen/sign (arithmetic-heavy), smaller for verify (already fast, memory-bound).
