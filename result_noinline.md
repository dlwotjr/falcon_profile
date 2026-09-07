# Falcon Profiling Results: O0 vs O3 (without `-fno-inline`)

> 1000 iterations each | `-pg` only (inlining enabled) | Falcon-512 and Falcon-1024

## Total Runtime Summary (cumulative seconds, 1000 ops)

| Operation | O0 (s) | O3 (s) | Speedup |
|-----------|-------:|-------:|--------:|
| `falcon512_keygen` | 51.46 | 10.04 | **5.13×** |
| `falcon512_sign` | 16.03 | 2.74 | **5.85×** |
| `falcon512_verify` | 0.18 | 0.02 | **9.00×** |
| `falcon1024_keygen` | 150.66 | 28.90 | **5.21×** |
| `falcon1024_sign` | 35.50 | 6.47 | **5.49×** |
| `falcon1024_verify` | 0.37 | 0.05 | **7.40×** |

## Inlined Functions Summary (present in O0, absent in O3)

| Operation | O0 visible | O3 visible | Inlined by O3 |
|-----------|----------:|----------:|--------------:|
| `falcon512_keygen` | 204 | 93 | **115** |
| `falcon512_sign` | 154 | 85 | **70** |
| `falcon512_verify` | 57 | 37 | **20** |
| `falcon1024_keygen` | 205 | 93 | **116** |
| `falcon1024_sign` | 154 | 85 | **70** |
| `falcon1024_verify` | 57 | 37 | **20** |

**Functions inlined across all 6 variants (7):** `keccak_inc_finalize`, `keccak_inc_init`, `keccak_inc_squeeze`, `mq_add`, `mq_montymul`, `mq_rshift1`, `mq_sub`

---

## FALCON512 KEYGEN

Total: **51.46s** (O0) → **10.04s** (O3)  — **5.13× faster**

### O0 — Top functions

| % time | self (s) | calls | function |
|-------:|---------:|------:|----------|
| 30.74% | 15.820 | 295.0M | `PQCLEAN_FALCON512_CLEAN_fpr_add` |
| 12.45% | 6.410 | 979.6M | `modp_montymul` |
| 11.06% | 5.690 | 650.1M | `FPR` |
| 9.77% | 5.030 | 300.2M | `PQCLEAN_FALCON512_CLEAN_fpr_mul` |
| 5.09% | 2.620 | 686.1M | `modp_add` |
| 3.94% | 2.030 | 53.0M | `PQCLEAN_FALCON512_CLEAN_fpr_scaled` |
| 3.67% | 1.890 | 2.6M | `KeccakF1600_StatePermute` |
| 2.08% | 1.070 | 295.0M | `fpr_ulsh` |
| 2.07% | 1.060 | 11.0M | `mkgauss` |
| 1.98% | 1.020 | 18.1M | `zint_add_scaled_mul_small` |

### O3 — Top functions

| % time | self (s) | calls | function |
|-------:|---------:|------:|----------|
| 37.05% | 3.720 | 293.3M | `PQCLEAN_FALCON512_CLEAN_fpr_add` |
| 10.46% | 1.050 | 298.9M | `PQCLEAN_FALCON512_CLEAN_fpr_mul` |
| 7.87% | 0.790 | 172.8K | `zint_rebuild_CRT.constprop.3` |
| 5.08% | 0.510 | 2.5M | `KeccakF1600_StatePermute` |
| 4.98% | 0.500 | 20.8K | `poly_small_mkgauss` |
| 4.78% | 0.480 | 3.6M | `poly_big_to_fp` |
| 4.78% | 0.480 | 7.0K | `solve_NTRU_intermediate` |
| 3.88% | 0.390 | 996.2K | `modp_mkgm2` |
| 2.89% | 0.290 | 521.8K | `poly_sub_scaled` |
| 2.69% | 0.270 | 53.0M | `PQCLEAN_FALCON512_CLEAN_fpr_scaled` |

### Inlined by O3 (named functions only)

- `FPR`
- `align_fpr`
- `align_u32`
- `fpr_half`
- `fpr_inv`
- `fpr_lt`
- `fpr_neg`
- `fpr_of`
- `fpr_rint`
- `fpr_sqr`
- `fpr_sub`
- `fpr_trunc`
- `fpr_ulsh`
- `fpr_ursh`
- `get_rng_u64`
- `keccak_inc_finalize`
- `keccak_inc_init`
- `keccak_inc_squeeze`
- `mkgauss`
- `modp_NTT2_ext`
- `modp_R`
- `modp_Rx`
- `modp_add`
- `modp_div`
- `modp_iNTT2_ext`
- `modp_montymul`
- `modp_ninv31`
- `modp_norm`
- `modp_poly_rec_res`
- `modp_set`
- `modp_sub`
- `mq_add`
- `mq_conv_small`
- `mq_div_12289`
- `mq_montymul`
- `mq_montysqr`
- `mq_rshift1`
- `mq_sub`
- `poly_big_to_small`
- `poly_small_sqnorm`
- `poly_small_to_fp`
- `randombytes_linux_randombytes_getrandom`
- `solve_NTRU`
- `solve_NTRU_binary_depth0`
- `solve_NTRU_deepest`
- `zint_add_mul_small`
- `zint_add_scaled_mul_small`
- `zint_bezout`
- `zint_co_reduce`
- `zint_finish_mod`
- `zint_mod_small_signed`
- `zint_mod_small_unsigned`
- `zint_mul_small`
- `zint_negate`
- `zint_norm_zero`
- `zint_one_to_plain`
- `zint_rebuild_CRT`
- `zint_sub`
- `zint_sub_scaled`

---

## FALCON512 SIGN

Total: **16.03s** (O0) → **2.74s** (O3)  — **5.85× faster**

### O0 — Top functions

| % time | self (s) | calls | function |
|-------:|---------:|------:|----------|
| 52.59% | 8.430 | 148.4M | `PQCLEAN_FALCON512_CLEAN_fpr_add` |
| 16.59% | 2.660 | 297.0M | `FPR` |
| 13.97% | 2.240 | 133.8M | `PQCLEAN_FALCON512_CLEAN_fpr_mul` |
| 2.56% | 0.410 | 152.0M | `fpr_ursh` |
| 2.37% | 0.380 | 148.4M | `fpr_ulsh` |
| 2.12% | 0.340 | 12.0M | `PQCLEAN_FALCON512_CLEAN_fpr_scaled` |
| 1.68% | 0.270 | 2.3M | `PQCLEAN_FALCON512_CLEAN_fpr_div` |
| 1.25% | 0.200 | 39.1K | `PQCLEAN_FALCON512_CLEAN_prng_refill` |
| 0.94% | 0.150 | 1.8M | `PQCLEAN_FALCON512_CLEAN_gaussian0_sampler` |
| 0.81% | 0.130 | 1.8M | `PQCLEAN_FALCON512_CLEAN_fpr_expm_p63` |

### O3 — Top functions

| % time | self (s) | calls | function |
|-------:|---------:|------:|----------|
| 65.33% | 1.790 | 148.4M | `PQCLEAN_FALCON512_CLEAN_fpr_add` |
| 17.88% | 0.490 | 133.8M | `PQCLEAN_FALCON512_CLEAN_fpr_mul` |
| 6.57% | 0.180 | 2.3M | `PQCLEAN_FALCON512_CLEAN_fpr_div` |
| 2.19% | 0.060 | 12.0M | `PQCLEAN_FALCON512_CLEAN_fpr_scaled` |
| 1.46% | 0.040 | 512.0K | `PQCLEAN_FALCON512_CLEAN_fpr_sqrt` |
| 1.09% | 0.030 | 1.0K | `PQCLEAN_FALCON512_CLEAN_hash_to_point_ct` |
| 0.73% | 0.020 | 1.0M | `PQCLEAN_FALCON512_CLEAN_sampler` |
| 0.73% | 0.020 | 39.1K | `PQCLEAN_FALCON512_CLEAN_prng_refill` |
| 0.73% | 0.020 | 9.0K | `PQCLEAN_FALCON512_CLEAN_FFT` |
| 0.73% | 0.020 | 1.0K | `PQCLEAN_FALCON512_CLEAN_complete_private` |

### Inlined by O3 (named functions only)

- `BerExp`
- `FPR`
- `do_sign_dyn`
- `ffSampling_fft_dyntree`
- `fpr_floor`
- `fpr_half`
- `fpr_inv`
- `fpr_irsh`
- `fpr_neg`
- `fpr_of`
- `fpr_rint`
- `fpr_sqr`
- `fpr_sub`
- `fpr_trunc`
- `fpr_ulsh`
- `fpr_ursh`
- `keccak_inc_finalize`
- `keccak_inc_init`
- `keccak_inc_squeeze`
- `mq_add`
- `mq_conv_small`
- `mq_div_12289`
- `mq_montymul`
- `mq_montysqr`
- `mq_poly_montymul_ntt`
- `mq_poly_tomonty`
- `mq_rshift1`
- `mq_sub`
- `prng_get_u64`
- `prng_get_u8`
- `randombytes_linux_randombytes_getrandom`
- `smallints_to_fpr`

---

## FALCON512 VERIFY

Total: **0.18s** (O0) → **0.02s** (O3)  — **9.00× faster**

### O0 — Top functions

| % time | self (s) | calls | function |
|-------:|---------:|------:|----------|
| 33.33% | 0.060 | 8.4M | `mq_montymul` |
| 27.78% | 0.050 | 1.0K | `PQCLEAN_FALCON512_CLEAN_hash_to_point_ct` |
| 16.67% | 0.030 | 6.9M | `mq_add` |
| 11.11% | 0.020 | 2.0K | `mq_NTT` |
| 5.56% | 0.010 | 7.4M | `mq_sub` |
| 5.56% | 0.010 | 11.0K | `KeccakF1600_StatePermute` |
| 0.00% | 0.000 | 717.0K | `keccak_inc_squeeze` |
| 0.00% | 0.000 | 717.0K | `shake256_inc_squeeze` |
| 0.00% | 0.000 | 9.0K | `mq_rshift1` |
| 0.00% | 0.000 | 2.0K | `keccak_inc_absorb` |

### O3 — Top functions

| % time | self (s) | calls | function |
|-------:|---------:|------:|----------|
| 50.00% | 0.010 | 1.0K | `PQCLEAN_FALCON512_CLEAN_hash_to_point_ct` |
| 50.00% | 0.010 | 1.0K | `mq_iNTT` |
| 0.00% | 0.000 | 717.0K | `shake256_inc_squeeze` |
| 0.00% | 0.000 | 11.0K | `KeccakF1600_StatePermute` |
| 0.00% | 0.000 | 2.0K | `keccak_inc_absorb` |
| 0.00% | 0.000 | 2.0K | `mq_NTT` |
| 0.00% | 0.000 | 2.0K | `shake256_inc_absorb` |
| 0.00% | 0.000 | 1.0K | `PQCLEAN_FALCON512_CLEAN_comp_decode` |
| 0.00% | 0.000 | 1.0K | `PQCLEAN_FALCON512_CLEAN_crypto_sign_verify` |
| 0.00% | 0.000 | 1.0K | `PQCLEAN_FALCON512_CLEAN_is_short` |

### Inlined by O3 (named functions only)

- `keccak_inc_finalize`
- `keccak_inc_init`
- `keccak_inc_squeeze`
- `mq_add`
- `mq_montymul`
- `mq_poly_montymul_ntt`
- `mq_poly_sub`
- `mq_poly_tomonty`
- `mq_rshift1`
- `mq_sub`

---

## FALCON1024 KEYGEN

Total: **150.66s** (O0) → **28.90s** (O3)  — **5.21× faster**

### O0 — Top functions

| % time | self (s) | calls | function |
|-------:|---------:|------:|----------|
| 31.96% | 48.150 | 895.3M | `PQCLEAN_FALCON1024_CLEAN_fpr_add` |
| 12.50% | 18.830 | 2.83B | `modp_montymul` |
| 11.34% | 17.080 | 1.88B | `FPR` |
| 10.16% | 15.300 | 852.2M | `PQCLEAN_FALCON1024_CLEAN_fpr_mul` |
| 5.42% | 8.170 | 2.20B | `modp_add` |
| 3.37% | 5.070 | 75.2M | `zint_add_scaled_mul_small` |
| 3.01% | 4.530 | 125.8M | `PQCLEAN_FALCON1024_CLEAN_fpr_scaled` |
| 2.98% | 4.500 | 113.3M | `zint_mod_small_unsigned` |
| 2.01% | 3.030 | 4.3M | `KeccakF1600_StatePermute` |
| 1.79% | 2.700 | 895.3M | `fpr_ulsh` |

### O3 — Top functions

| % time | self (s) | calls | function |
|-------:|---------:|------:|----------|
| 37.72% | 10.900 | 874.7M | `PQCLEAN_FALCON1024_CLEAN_fpr_add` |
| 11.14% | 3.220 | 835.4M | `PQCLEAN_FALCON1024_CLEAN_fpr_mul` |
| 10.73% | 3.100 | 202.6K | `zint_rebuild_CRT.constprop.3` |
| 6.57% | 1.900 | 8.2K | `solve_NTRU_intermediate` |
| 4.05% | 1.170 | 6.9M | `poly_big_to_fp` |
| 3.81% | 1.100 | 1.1M | `poly_sub_scaled` |
| 3.29% | 0.950 | 34.7K | `poly_small_mkgauss` |
| 3.11% | 0.900 | 947.8K | `zint_co_reduce_mod` |
| 2.98% | 0.860 | 4.2M | `KeccakF1600_StatePermute` |
| 2.84% | 0.820 | 47.4K | `make_fg_step.constprop.0` |

### Inlined by O3 (named functions only)

- `FPR`
- `align_fpr`
- `align_u32`
- `fpr_inv`
- `fpr_lt`
- `fpr_neg`
- `fpr_of`
- `fpr_rint`
- `fpr_sqr`
- `fpr_sub`
- `fpr_trunc`
- `fpr_ulsh`
- `fpr_ursh`
- `get_rng_u64`
- `keccak_inc_finalize`
- `keccak_inc_init`
- `keccak_inc_squeeze`
- `mkgauss`
- `modp_NTT2_ext`
- `modp_R`
- `modp_Rx`
- `modp_add`
- `modp_div`
- `modp_iNTT2_ext`
- `modp_montymul`
- `modp_ninv31`
- `modp_norm`
- `modp_poly_rec_res`
- `modp_set`
- `modp_sub`
- `mq_add`
- `mq_conv_small`
- `mq_div_12289`
- `mq_montymul`
- `mq_montysqr`
- `mq_rshift1`
- `mq_sub`
- `poly_big_to_small`
- `poly_small_sqnorm`
- `poly_small_to_fp`
- `randombytes_linux_randombytes_getrandom`
- `shake128_inc_init`
- `shake256_inc_ctx_clone`
- `solve_NTRU`
- `solve_NTRU_binary_depth0`
- `solve_NTRU_deepest`
- `zint_add_mul_small`
- `zint_add_scaled_mul_small`
- `zint_bezout`
- `zint_co_reduce`
- `zint_finish_mod`
- `zint_mod_small_signed`
- `zint_mod_small_unsigned`
- `zint_mul_small`
- `zint_negate`
- `zint_norm_zero`
- `zint_one_to_plain`
- `zint_rebuild_CRT`
- `zint_sub`
- `zint_sub_scaled`

---

## FALCON1024 SIGN

Total: **35.50s** (O0) → **6.47s** (O3)  — **5.49× faster**

### O0 — Top functions

| % time | self (s) | calls | function |
|-------:|---------:|------:|----------|
| 51.55% | 18.300 | 329.5M | `PQCLEAN_FALCON1024_CLEAN_fpr_add` |
| 15.86% | 5.630 | 292.8M | `PQCLEAN_FALCON1024_CLEAN_fpr_mul` |
| 15.72% | 5.580 | 652.2M | `FPR` |
| 2.68% | 0.950 | 329.5M | `fpr_ulsh` |
| 2.25% | 0.800 | 336.5M | `fpr_ursh` |
| 1.94% | 0.690 | 23.8M | `PQCLEAN_FALCON1024_CLEAN_fpr_scaled` |
| 1.46% | 0.520 | 5.1M | `PQCLEAN_FALCON1024_CLEAN_fpr_div` |
| 1.24% | 0.440 | 76.6K | `PQCLEAN_FALCON1024_CLEAN_prng_refill` |
| 1.10% | 0.390 | 44.0M | `mq_montymul` |
| 0.96% | 0.340 | 3.5M | `PQCLEAN_FALCON1024_CLEAN_fpr_expm_p63` |

### O3 — Top functions

| % time | self (s) | calls | function |
|-------:|---------:|------:|----------|
| 61.82% | 4.000 | 329.5M | `PQCLEAN_FALCON1024_CLEAN_fpr_add` |
| 17.93% | 1.160 | 292.8M | `PQCLEAN_FALCON1024_CLEAN_fpr_mul` |
| 4.48% | 0.290 | 5.1M | `PQCLEAN_FALCON1024_CLEAN_fpr_div` |
| 3.55% | 0.230 | 23.8M | `PQCLEAN_FALCON1024_CLEAN_fpr_scaled` |
| 2.16% | 0.140 | 3.5M | `PQCLEAN_FALCON1024_CLEAN_fpr_expm_p63` |
| 2.16% | 0.140 | 9.0K | `PQCLEAN_FALCON1024_CLEAN_FFT` |
| 1.39% | 0.090 | 1.0M | `PQCLEAN_FALCON1024_CLEAN_fpr_sqrt` |
| 1.08% | 0.070 | 3.5M | `PQCLEAN_FALCON1024_CLEAN_gaussian0_sampler` |
| 0.93% | 0.060 | 1.0K | `PQCLEAN_FALCON1024_CLEAN_complete_private` |
| 0.62% | 0.040 | 4.1M | `PQCLEAN_FALCON1024_CLEAN_poly_split_fft` |

### Inlined by O3 (named functions only)

- `BerExp`
- `FPR`
- `do_sign_dyn`
- `ffSampling_fft_dyntree`
- `fpr_floor`
- `fpr_half`
- `fpr_inv`
- `fpr_irsh`
- `fpr_neg`
- `fpr_of`
- `fpr_rint`
- `fpr_sqr`
- `fpr_sub`
- `fpr_trunc`
- `fpr_ulsh`
- `fpr_ursh`
- `keccak_inc_finalize`
- `keccak_inc_init`
- `keccak_inc_squeeze`
- `mq_add`
- `mq_conv_small`
- `mq_div_12289`
- `mq_montymul`
- `mq_montysqr`
- `mq_poly_montymul_ntt`
- `mq_poly_tomonty`
- `mq_rshift1`
- `mq_sub`
- `prng_get_u64`
- `prng_get_u8`
- `randombytes_linux_randombytes_getrandom`
- `smallints_to_fpr`

---

## FALCON1024 VERIFY

Total: **0.37s** (O0) → **0.05s** (O3)  — **7.40× faster**

### O0 — Top functions

| % time | self (s) | calls | function |
|-------:|---------:|------:|----------|
| 35.14% | 0.130 | 18.4M | `mq_montymul` |
| 16.22% | 0.060 | 15.4M | `mq_add` |
| 13.51% | 0.050 | 20.0K | `KeccakF1600_StatePermute` |
| 13.51% | 0.050 | 1.0K | `PQCLEAN_FALCON1024_CLEAN_hash_to_point_ct` |
| 8.11% | 0.030 | 16.4M | `mq_sub` |
| 8.11% | 0.030 | 1.0K | `mq_iNTT` |
| 2.70% | 0.010 | 10.0K | `mq_rshift1` |
| 2.70% | 0.010 | 2.0K | `mq_NTT` |
| 0.00% | 0.000 | 1.3M | `keccak_inc_squeeze` |
| 0.00% | 0.000 | 1.3M | `shake256_inc_squeeze` |

### O3 — Top functions

| % time | self (s) | calls | function |
|-------:|---------:|------:|----------|
| 60.00% | 0.030 | 1.0K | `PQCLEAN_FALCON1024_CLEAN_hash_to_point_ct` |
| 20.00% | 0.010 | 2.0K | `mq_NTT` |
| 20.00% | 0.010 | 1.0K | `PQCLEAN_FALCON1024_CLEAN_comp_decode` |
| 0.00% | 0.000 | 1.3M | `shake256_inc_squeeze` |
| 0.00% | 0.000 | 20.0K | `KeccakF1600_StatePermute` |
| 0.00% | 0.000 | 2.0K | `keccak_inc_absorb` |
| 0.00% | 0.000 | 2.0K | `shake256_inc_absorb` |
| 0.00% | 0.000 | 1.0K | `PQCLEAN_FALCON1024_CLEAN_crypto_sign_verify` |
| 0.00% | 0.000 | 1.0K | `PQCLEAN_FALCON1024_CLEAN_is_short` |
| 0.00% | 0.000 | 1.0K | `PQCLEAN_FALCON1024_CLEAN_modq_decode` |

### Inlined by O3 (named functions only)

- `keccak_inc_finalize`
- `keccak_inc_init`
- `keccak_inc_squeeze`
- `mq_add`
- `mq_montymul`
- `mq_poly_montymul_ntt`
- `mq_poly_sub`
- `mq_poly_tomonty`
- `mq_rshift1`
- `mq_sub`

---

## Analysis

### Compile flag effects

| Flag | Effect on Falcon |
|------|-----------------|
| `-O0` | No optimization. Every `fpr_add`, `FPR()`, `modp_montymul` call is a real function call. Accurate per-function attribution. |
| `-O3` | Aggressive inlining enabled. Small leaf functions (`fpr_*`, `modp_*`, `mq_*`, `zint_*`) are inlined into callers and disappear from the profile. |
| `-pg` | Inserts `mcount` hooks at every function entry for call counting and adds timer sampling for time attribution. Inlined functions no longer have entry hooks and are invisible. |

### Key observations

- **Without `-fno-inline`, O3 inlines 20–116 functions per operation** — far more than the 1–7 seen with `-fno-inline`. The profile loses detail but reflects true execution.
- **keygen** loses nearly half its visible functions (204→93 for Falcon-512). All `fpr_*`, `modp_*`, `zint_*` helpers vanish — inlined into `poly_*` / `solve_NTRU*` callers.
- **sign** loses `do_sign_dyn` and `ffSampling_fft_dyntree` — the core recursive FFT sampler is fully absorbed. `BerExp` and `smallints_to_fpr` also disappear.
- **verify** is the lightest operation; even so, all `mq_add/sub/montymul/rshift1` helpers are inlined into `mq_NTT` / `mq_iNTT`.
- **Universally inlined** (all 6 variants): `keccak_inc_finalize`, `keccak_inc_init`, `keccak_inc_squeeze`, `mq_add`, `mq_montymul`, `mq_rshift1`, `mq_sub`.
- **Speedups are unchanged** from the `-fno-inline` run — the `-fno-inline` flag only affects profiling visibility, not the optimized binary's inlining decisions.
