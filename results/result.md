# Falcon Profiling Results: O0 vs O3

> 1000 iterations each | `-fno-inline -pg` | Falcon-512 and Falcon-1024

## Total Runtime Summary (cumulative seconds, 1000 ops)

| Operation | O0 (s) | O3 (s) | Speedup |
|-----------|-------:|-------:|--------:|
| `falcon512_keygen` | 51.95 | 11.74 | **4.43×** |
| `falcon512_sign` | 15.93 | 3.24 | **4.92×** |
| `falcon512_verify` | 0.19 | 0.05 | **3.80×** |
| `falcon1024_keygen` | 143.26 | 34.31 | **4.18×** |
| `falcon1024_sign` | 34.23 | 6.81 | **5.03×** |
| `falcon1024_verify` | 0.59 | 0.08 | **7.37×** |

---

## FALCON512 KEYGEN

Total: **51.95s** (O0) → **11.74s** (O3)  — **4.43× faster**

### O0 — Top functions

| % time | self (s) | calls | function |
|-------:|---------:|------:|----------|
| 30.78% | 15.990 | 301.7M | `PQCLEAN_FALCON512_CLEAN_fpr_add` |
| 11.90% | 6.180 | 980.6M | `modp_montymul` |
| 11.01% | 5.720 | 662.7M | `FPR` |
| 10.61% | 5.510 | 305.8M | `PQCLEAN_FALCON512_CLEAN_fpr_mul` |
| 4.89% | 2.540 | 686.8M | `modp_add` |
| 3.75% | 1.950 | 2.7M | `KeccakF1600_StatePermute` |
| 3.45% | 1.790 | 53.3M | `PQCLEAN_FALCON512_CLEAN_fpr_scaled` |
| 2.54% | 1.320 | 11.5M | `mkgauss` |
| 2.25% | 1.170 | 50.0M | `zint_mod_small_unsigned` |
| 2.06% | 1.070 | 301.7M | `fpr_ulsh` |

### O3 — Top functions

| % time | self (s) | calls | function |
|-------:|---------:|------:|----------|
| 27.68% | 3.250 | 294.8M | `PQCLEAN_FALCON512_CLEAN_fpr_add` |
| 18.48% | 2.170 | 968.1M | `modp_montymul` |
| 11.93% | 1.400 | 300.1M | `PQCLEAN_FALCON512_CLEAN_fpr_mul` |
| 4.77% | 0.560 | 2.6M | `KeccakF1600_StatePermute` |
| 4.00% | 0.470 | 10.9M | `mkgauss` |
| 3.15% | 0.370 | 53.0M | `PQCLEAN_FALCON512_CLEAN_fpr_scaled` |
| 3.07% | 0.360 | 649.8M | `FPR` |
| 2.81% | 0.330 | 686.0M | `modp_add` |
| 1.96% | 0.230 | 366.5M | `modp_sub` |
| 1.87% | 0.220 | 18.1M | `zint_add_scaled_mul_small` |

---

## FALCON512 SIGN

Total: **15.93s** (O0) → **3.24s** (O3)  — **4.92× faster**

### O0 — Top functions

| % time | self (s) | calls | function |
|-------:|---------:|------:|----------|
| 50.85% | 8.100 | 148.6M | `PQCLEAN_FALCON512_CLEAN_fpr_add` |
| 15.94% | 2.540 | 297.5M | `FPR` |
| 14.69% | 2.340 | 134.0M | `PQCLEAN_FALCON512_CLEAN_fpr_mul` |
| 2.70% | 0.430 | 148.6M | `fpr_ulsh` |
| 2.32% | 0.370 | 12.0M | `PQCLEAN_FALCON512_CLEAN_fpr_scaled` |
| 2.07% | 0.330 | 152.2M | `fpr_ursh` |
| 1.69% | 0.270 | 2.3M | `PQCLEAN_FALCON512_CLEAN_fpr_div` |
| 1.32% | 0.210 | 1.8M | `PQCLEAN_FALCON512_CLEAN_fpr_expm_p63` |
| 1.19% | 0.190 | 39.1K | `PQCLEAN_FALCON512_CLEAN_prng_refill` |
| 0.94% | 0.150 | 21.0M | `mq_montymul` |

### O3 — Top functions

| % time | self (s) | calls | function |
|-------:|---------:|------:|----------|
| 50.93% | 1.650 | 148.7M | `PQCLEAN_FALCON512_CLEAN_fpr_add` |
| 16.05% | 0.520 | 134.1M | `PQCLEAN_FALCON512_CLEAN_fpr_mul` |
| 5.56% | 0.180 | 297.7M | `FPR` |
| 4.32% | 0.140 | 2.3M | `PQCLEAN_FALCON512_CLEAN_fpr_div` |
| 4.01% | 0.130 | 152.3M | `fpr_ursh` |
| 3.40% | 0.110 | 152.3M | `fpr_trunc` |
| 2.78% | 0.090 | 12.0M | `PQCLEAN_FALCON512_CLEAN_fpr_scaled` |
| 1.54% | 0.050 | 1.8M | `PQCLEAN_FALCON512_CLEAN_fpr_expm_p63` |
| 1.23% | 0.040 | 20.0M | `mq_montymul` |
| 1.23% | 0.040 | 39.2K | `PQCLEAN_FALCON512_CLEAN_prng_refill` |

---

## FALCON512 VERIFY

Total: **0.19s** (O0) → **0.05s** (O3)  — **3.80× faster**

### O0 — Top functions

| % time | self (s) | calls | function |
|-------:|---------:|------:|----------|
| 42.11% | 0.080 | 8.5M | `mq_montymul` |
| 15.79% | 0.030 | 7.4M | `mq_sub` |
| 15.79% | 0.030 | 927.0K | `FPR` |
| 10.53% | 0.020 | 6.9M | `mq_add` |
| 5.26% | 0.010 | 683.6K | `modp_add` |
| 5.26% | 0.010 | 432.9K | `PQCLEAN_FALCON512_CLEAN_fpr_add` |
| 5.26% | 0.010 | 1.0K | `mq_iNTT` |
| 0.00% | 0.000 | 975.9K | `modp_montymul` |
| 0.00% | 0.000 | 758.7K | `keccak_inc_squeeze` |
| 0.00% | 0.000 | 758.7K | `shake256_inc_squeeze` |

### O3 — Top functions

| % time | self (s) | calls | function |
|-------:|---------:|------:|----------|
| 40.00% | 0.020 | 6.9M | `mq_add` |
| 40.00% | 0.020 | 1.0K | `PQCLEAN_FALCON512_CLEAN_hash_to_point_ct` |
| 20.00% | 0.010 | 8.0M | `mq_montymul` |
| 0.00% | 0.000 | 7.4M | `mq_sub` |
| 0.00% | 0.000 | 963.3K | `modp_montymul` |
| 0.00% | 0.000 | 877.8K | `FPR` |
| 0.00% | 0.000 | 743.3K | `keccak_inc_finalize` |
| 0.00% | 0.000 | 742.3K | `shake256_inc_squeeze` |
| 0.00% | 0.000 | 682.5K | `modp_add` |
| 0.00% | 0.000 | 513.5K | `mq_montymul.constprop.0` |

---

## FALCON1024 KEYGEN

Total: **143.26s** (O0) → **34.31s** (O3)  — **4.18× faster**

### O0 — Top functions

| % time | self (s) | calls | function |
|-------:|---------:|------:|----------|
| 32.73% | 46.890 | 875.3M | `PQCLEAN_FALCON1024_CLEAN_fpr_add` |
| 12.24% | 17.540 | 2.80B | `modp_montymul` |
| 11.49% | 16.460 | 1.84B | `FPR` |
| 10.04% | 14.380 | 835.4M | `PQCLEAN_FALCON1024_CLEAN_fpr_mul` |
| 5.65% | 8.090 | 2.17B | `modp_add` |
| 3.49% | 5.000 | 124.6M | `PQCLEAN_FALCON1024_CLEAN_fpr_scaled` |
| 3.36% | 4.820 | 74.9M | `zint_add_scaled_mul_small` |
| 2.75% | 3.940 | 112.4M | `zint_mod_small_unsigned` |
| 2.03% | 2.910 | 4.2M | `KeccakF1600_StatePermute` |
| 1.79% | 2.560 | 875.3M | `fpr_ulsh` |

### O3 — Top functions

| % time | self (s) | calls | function |
|-------:|---------:|------:|----------|
| 29.12% | 9.990 | 908.5M | `PQCLEAN_FALCON1024_CLEAN_fpr_add` |
| 20.23% | 6.940 | 2.81B | `modp_montymul` |
| 11.75% | 4.030 | 862.8M | `PQCLEAN_FALCON1024_CLEAN_fpr_mul` |
| 3.67% | 1.260 | 1.90B | `FPR` |
| 3.12% | 1.070 | 75.2M | `zint_add_scaled_mul_small` |
| 2.97% | 1.020 | 2.20B | `modp_add` |
| 2.74% | 0.940 | 4.5M | `KeccakF1600_StatePermute` |
| 2.27% | 0.780 | 126.3M | `PQCLEAN_FALCON1024_CLEAN_fpr_scaled` |
| 2.07% | 0.710 | 38.1M | `mkgauss` |
| 1.81% | 0.620 | 908.5M | `fpr_trunc` |

---

## FALCON1024 SIGN

Total: **34.23s** (O0) → **6.81s** (O3)  — **5.03× faster**

### O0 — Top functions

| % time | self (s) | calls | function |
|-------:|---------:|------:|----------|
| 50.22% | 17.190 | 330.0M | `PQCLEAN_FALCON1024_CLEAN_fpr_add` |
| 17.79% | 6.090 | 653.4M | `FPR` |
| 13.99% | 4.790 | 293.3M | `PQCLEAN_FALCON1024_CLEAN_fpr_mul` |
| 2.66% | 0.910 | 330.0M | `fpr_ulsh` |
| 2.54% | 0.870 | 23.9M | `PQCLEAN_FALCON1024_CLEAN_fpr_scaled` |
| 1.87% | 0.640 | 337.0M | `fpr_ursh` |
| 1.72% | 0.590 | 5.1M | `PQCLEAN_FALCON1024_CLEAN_fpr_div` |
| 1.26% | 0.430 | 76.6K | `PQCLEAN_FALCON1024_CLEAN_prng_refill` |
| 1.17% | 0.400 | 3.5M | `PQCLEAN_FALCON1024_CLEAN_fpr_expm_p63` |
| 0.91% | 0.310 | 1.0M | `PQCLEAN_FALCON1024_CLEAN_fpr_sqrt` |

### O3 — Top functions

| % time | self (s) | calls | function |
|-------:|---------:|------:|----------|
| 49.05% | 3.340 | 329.9M | `PQCLEAN_FALCON1024_CLEAN_fpr_add` |
| 21.88% | 1.490 | 293.3M | `PQCLEAN_FALCON1024_CLEAN_fpr_mul` |
| 6.17% | 0.420 | 653.2M | `FPR` |
| 4.55% | 0.310 | 5.1M | `PQCLEAN_FALCON1024_CLEAN_fpr_div` |
| 3.08% | 0.210 | 336.9M | `fpr_ursh` |
| 1.76% | 0.120 | 336.9M | `fpr_trunc` |
| 1.62% | 0.110 | 23.9M | `PQCLEAN_FALCON1024_CLEAN_fpr_scaled` |
| 1.62% | 0.110 | 3.5M | `PQCLEAN_FALCON1024_CLEAN_fpr_expm_p63` |
| 1.03% | 0.070 | 42.0M | `mq_montymul` |
| 1.03% | 0.070 | 1.0M | `PQCLEAN_FALCON1024_CLEAN_fpr_sqrt` |

---

## FALCON1024 VERIFY

Total: **0.59s** (O0) → **0.08s** (O3)  — **7.37× faster**

### O0 — Top functions

| % time | self (s) | calls | function |
|-------:|---------:|------:|----------|
| 23.73% | 0.140 | 18.5M | `mq_montymul` |
| 18.64% | 0.110 | 2.2M | `PQCLEAN_FALCON1024_CLEAN_fpr_add` |
| 11.86% | 0.070 | 1.0K | `PQCLEAN_FALCON1024_CLEAN_hash_to_point_ct` |
| 8.47% | 0.050 | 15.4M | `mq_add` |
| 5.08% | 0.030 | 4.3M | `FPR` |
| 5.08% | 0.030 | 3.9M | `modp_montymul` |
| 3.39% | 0.020 | 3.1M | `modp_add` |
| 3.39% | 0.020 | 2.0K | `mq_NTT` |
| 3.39% | 0.020 | 1.0K | `PQCLEAN_FALCON1024_CLEAN_comp_decode` |
| 1.69% | 0.010 | 16.4M | `mq_sub` |

### O3 — Top functions

| % time | self (s) | calls | function |
|-------:|---------:|------:|----------|
| 25.00% | 0.020 | 15.4M | `mq_add` |
| 12.50% | 0.010 | 17.5M | `mq_montymul` |
| 12.50% | 0.010 | 1.2M | `PQCLEAN_FALCON1024_CLEAN_fpr_mul` |
| 12.50% | 0.010 | 25.3K | `KeccakF1600_StatePermute` |
| 12.50% | 0.010 | 2.0K | `mq_NTT` |
| 12.50% | 0.010 | 1.0K | `mq_iNTT` |
| 12.50% | 0.010 | 1.0K | `PQCLEAN_FALCON1024_CLEAN_hash_to_point_ct` |
| 0.00% | 0.000 | 16.4M | `mq_sub` |
| 0.00% | 0.000 | 3.9M | `modp_montymul` |
| 0.00% | 0.000 | 3.1M | `modp_add` |

---

## Analysis

### Compile flag effects

| Flag | Effect on Falcon |
|------|-----------------|
| `-O0` | No optimization. Every `fpr_add`, `FPR()`, `modp_montymul` call is a real function call. Accurate per-function attribution. |
| `-O3` | Aggressive optimization. Loop unrolling, vectorization, CSE. Hot leaf functions may be partially inlined even with `-fno-inline` (macros/static inlines). |
| `-fno-inline` | Prevents function inlining so gprof can still count calls. Without this, small functions vanish from the profile at `-O3`. |
| `-pg` | Inserts `mcount` hooks at every function entry for call counting and adds timer sampling for time attribution. |

### Key observations

- **keygen** is the heaviest operation — dominated by `fpr_add` / `modp_montymul` (lattice basis generation via NTT+FFT).
- **sign** is ~3× faster than keygen but still FFT-heavy (`fpr_add` ~48%). Rejection sampling (`prng_refill`, `mkgauss`) visible.
- **verify** is 70–300× faster than keygen. Uses integer NTT only (`mq_montymul`, `mq_NTT`) — no floating-point FFT.
- **Falcon-1024 costs ~2–3× more** than Falcon-512 in all operations (N doubles, FFT is O(N log N)).
- **O3 speedup** is largest for keygen/sign (arithmetic-heavy), smaller for verify (already fast, memory-bound).
