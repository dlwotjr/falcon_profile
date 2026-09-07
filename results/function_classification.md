# Falcon Profiling: Function Classification by Cycle Cost (O0)

> Split at **100 ns/call** (≈300 cycles @ 3 GHz).
> **Group A** — high-frequency cheap leaf functions (< 100 ns/call).
> **Group B** — heavy per-call functions (≥ 100 ns/call).

---

## FALCON512 KEYGEN

### Group A — High-frequency, small cycle count per call (44 functions)

| function | calls | self (s) | ns/call | % time |
|----------|------:|---------:|--------:|-------:|
| `modp_montymul` | 979.6M | 6.410 | 6.5 | 12.45% |
| `modp_add` | 686.1M | 2.620 | 3.8 | 5.09% |
| `FPR` | 650.1M | 5.690 | 8.8 | 11.06% |
| `modp_sub` | 368.1M | 0.530 | 1.4 | 1.03% |
| `PQCLEAN_FALCON512_CLEAN_fpr_mul` | 300.2M | 5.030 | 16.8 | 9.77% |
| `PQCLEAN_FALCON512_CLEAN_fpr_add` | 295.0M | 15.820 | 53.6 | 30.74% |
| `fpr_ulsh` | 295.0M | 1.070 | 3.6 | 2.08% |
| `fpr_ursh` | 295.0M | 0.660 | 2.2 | 1.28% |
| `fpr_sub` | 117.8M | 0.100 | 0.8 | 0.20% |
| `PQCLEAN_FALCON512_CLEAN_fpr_scaled` | 53.0M | 2.030 | 38.3 | 3.94% |
| `fpr_of` | 53.0M | 0.010 | 0.2 | 0.03% |
| `zint_mod_small_unsigned` | 50.0M | 0.930 | 18.6 | 1.80% |
| `keccak_inc_squeeze` | 44.0M | 0.860 | 19.6 | 1.67% |
| `get_rng_u64` | 44.0M | 0.120 | 2.7 | 0.22% |
| `shake256_inc_squeeze` | 44.0M | 0.040 | 0.9 | 0.08% |
| `modp_set` | 30.1M | 0.010 | 0.3 | 0.03% |
| `zint_mod_small_signed` | 28.3M | 0.100 | 3.5 | 0.20% |
| `zint_add_mul_small` | 21.7M | 0.430 | 19.8 | 0.84% |
| `zint_norm_zero` | 21.1M | 0.330 | 15.6 | 0.64% |
| `zint_sub` | 21.1M | 0.120 | 5.7 | 0.23% |
| `mq_montymul` | 18.3M | 0.160 | 8.7 | 0.31% |
| `zint_add_scaled_mul_small` | 18.1M | 1.020 | 56.3 | 1.98% |
| `mkgauss` | 11.0M | 1.060 | 96.5 | 2.07% |
| `fpr_neg` | 7.9M | 0.060 | 7.6 | 0.11% |
| `mq_add` | 7.2M | 0.040 | 5.6 | 0.08% |
| `mq_sub` | 7.2M | 0.010 | 1.4 | 0.02% |
| `fpr_sqr` | 7.1M | 0.010 | 1.4 | 0.02% |
| `modp_R` | 6.8M | 0.010 | 1.5 | 0.02% |
| `fpr_sqr` | 6.5M | 0.010 | 1.5 | 0.01% |
| `fpr_lt` | 6.5M | 0.060 | 9.3 | 0.11% |
| `fpr_rint` | 4.3M | 0.060 | 14.1 | 0.12% |
| `fpr_ulsh` | 4.3M | 0.020 | 4.7 | 0.04% |
| `fpr_ursh` | 4.3M | 0.010 | 2.3 | 0.02% |
| `zint_sub_scaled` | 3.7M | 0.040 | 11.0 | 0.08% |
| `modp_ninv31` | 2.8M | 0.020 | 7.1 | 0.04% |
| `modp_norm` | 2.1M | 0.010 | 4.9 | 0.01% |
| `zint_mul_small` | 1.5M | 0.120 | 79.9 | 0.23% |
| `modp_mkgm2` | 999.1K | 0.070 | 70.1 | 0.14% |
| `modp_Rx` | 964.5K | 0.010 | 10.4 | 0.03% |
| `PQCLEAN_FALCON512_CLEAN_poly_mul_fft` | 577.7K | 0.020 | 34.6 | 0.04% |
| `mq_div_12289` | 529.8K | 0.040 | 75.5 | 0.08% |
| `poly_sub_scaled` | 519.7K | 0.040 | 77.0 | 0.08% |
| `zint_negate` | 447.5K | 0.040 | 89.4 | 0.08% |
| `PQCLEAN_FALCON512_CLEAN_poly_mul_autoadj_fft` | 299.6K | 0.020 | 66.7 | 0.04% |

### Group B — Heavy per-call functions (27 functions)

| function | calls | self (s) | ns/call | % time |
|----------|------:|---------:|--------:|-------:|
| `KeccakF1600_StatePermute` | 2.6M | 1.890 | 730.8 | 3.67% |
| `modp_NTT2_ext` | 2.0M | 0.730 | 371.3 | 1.42% |
| `modp_R2` | 3.8M | 0.600 | 157.2 | 1.17% |
| `zint_finish_mod` | 895.0K | 0.420 | 469.3 | 0.82% |
| `modp_iNTT2_ext` | 1.8M | 0.350 | 197.1 | 0.68% |
| `PQCLEAN_FALCON512_CLEAN_fpr_div` | 1.9M | 0.260 | 137.5 | 0.51% |
| `PQCLEAN_FALCON512_CLEAN_iFFT` | 302.6K | 0.220 | 726.9 | 0.43% |
| `zint_bezout` | 1.0K | 0.180 | 176,991.2 | 0.35% |
| `PQCLEAN_FALCON512_CLEAN_FFT` | 607.5K | 0.160 | 263.4 | 0.31% |
| `zint_co_reduce_mod` | 447.5K | 0.130 | 290.5 | 0.25% |
| `poly_big_to_fp` | 593.8K | 0.120 | 202.1 | 0.23% |
| `modp_div` | 999.1K | 0.100 | 100.1 | 0.19% |
| `zint_rebuild_CRT` | 175.6K | 0.090 | 512.4 | 0.17% |
| `zint_co_reduce` | 223.7K | 0.080 | 357.6 | 0.16% |
| `poly_sub_scaled_ntt` | 56.1K | 0.050 | 892.0 | 0.10% |
| `make_fg_step` | 44.2K | 0.030 | 678.0 | 0.06% |
| `solve_NTRU_intermediate` | 7.0K | 0.030 | 4,276.6 | 0.06% |
| `poly_small_sqnorm` | 21.4K | 0.020 | 933.6 | 0.04% |
| `mq_NTT` | 2.1K | 0.020 | 9,514.7 | 0.04% |
| `PQCLEAN_FALCON512_CLEAN_keygen` | 1.0K | 0.020 | 20,000.0 | 0.04% |
| `poly_small_mkgauss` | 21.4K | 0.010 | 466.8 | 0.02% |
| `PQCLEAN_FALCON512_CLEAN_poly_mulconst` | 10.8K | 0.010 | 928.2 | 0.02% |
| `poly_small_to_fp` | 10.8K | 0.010 | 928.2 | 0.02% |
| `PQCLEAN_FALCON512_CLEAN_trim_i8_encode` | 3.0K | 0.010 | 3,333.3 | 0.02% |
| `mq_iNTT` | 1.0K | 0.010 | 9,832.8 | 0.02% |
| `solve_NTRU` | 1.0K | 0.010 | 9,832.8 | 0.02% |
| `solve_NTRU_binary_depth0` | 1.0K | 0.010 | 9,990.0 | 0.02% |

---

## FALCON512 SIGN

### Group A — High-frequency, small cycle count per call (32 functions)

| function | calls | self (s) | ns/call | % time |
|----------|------:|---------:|--------:|-------:|
| `FPR` | 297.0M | 2.660 | 9.0 | 16.59% |
| `fpr_ursh` | 152.0M | 0.410 | 2.7 | 2.56% |
| `PQCLEAN_FALCON512_CLEAN_fpr_add` | 148.4M | 8.430 | 56.8 | 52.59% |
| `fpr_ulsh` | 148.4M | 0.380 | 2.6 | 2.37% |
| `PQCLEAN_FALCON512_CLEAN_fpr_mul` | 133.8M | 2.240 | 16.7 | 13.97% |
| `fpr_sub` | 70.4M | 0.020 | 0.3 | 0.12% |
| `mq_montymul` | 21.0M | 0.110 | 5.2 | 0.69% |
| `fpr_half` | 16.4M | 0.030 | 1.8 | 0.19% |
| `fpr_neg` | 14.1M | 0.010 | 0.7 | 0.06% |
| `PQCLEAN_FALCON512_CLEAN_fpr_scaled` | 12.0M | 0.340 | 28.4 | 2.12% |
| `fpr_of` | 12.0M | 0.020 | 1.7 | 0.12% |
| `mq_add` | 9.2M | 0.030 | 3.3 | 0.19% |
| `mq_sub` | 9.2M | 0.020 | 2.2 | 0.12% |
| `fpr_sub` | 6.4M | 0.010 | 1.6 | 0.06% |
| `mq_montysqr` | 5.6M | 0.030 | 5.3 | 0.16% |
| `fpr_trunc` | 3.6M | 0.060 | 16.9 | 0.37% |
| `PQCLEAN_FALCON512_CLEAN_poly_split_fft` | 2.0M | 0.050 | 24.5 | 0.31% |
| `PQCLEAN_FALCON512_CLEAN_gaussian0_sampler` | 1.8M | 0.150 | 84.4 | 0.94% |
| `PQCLEAN_FALCON512_CLEAN_fpr_expm_p63` | 1.8M | 0.130 | 73.1 | 0.81% |
| `prng_get_u64` | 1.8M | 0.020 | 11.2 | 0.12% |
| `BerExp` | 1.8M | 0.010 | 5.6 | 0.06% |
| `fpr_trunc` | 1.8M | 0.010 | 5.6 | 0.03% |
| `PQCLEAN_FALCON512_CLEAN_sampler` | 1.0M | 0.060 | 58.6 | 0.37% |
| `fpr_rint` | 1.0M | 0.020 | 19.5 | 0.12% |
| `fpr_ulsh` | 1.0M | 0.010 | 9.8 | 0.06% |
| `fpr_floor` | 1.0M | 0.010 | 9.8 | 0.03% |
| `PQCLEAN_FALCON512_CLEAN_poly_merge_fft` | 1.0M | 0.010 | 9.8 | 0.06% |
| `keccak_inc_squeeze` | 718.0K | 0.010 | 13.9 | 0.06% |
| `PQCLEAN_FALCON512_CLEAN_poly_mul_fft` | 517.0K | 0.020 | 38.7 | 0.12% |
| `mq_div_12289` | 512.0K | 0.010 | 19.5 | 0.03% |
| `PQCLEAN_FALCON512_CLEAN_poly_LDL_fft` | 511.0K | 0.040 | 78.3 | 0.25% |
| `PQCLEAN_FALCON512_CLEAN_poly_sub` | 511.0K | 0.010 | 19.6 | 0.06% |

### Group B — Heavy per-call functions (11 functions)

| function | calls | self (s) | ns/call | % time |
|----------|------:|---------:|--------:|-------:|
| `PQCLEAN_FALCON512_CLEAN_fpr_div` | 2.3M | 0.270 | 117.2 | 1.68% |
| `PQCLEAN_FALCON512_CLEAN_prng_refill` | 39.1K | 0.200 | 5,110.5 | 1.25% |
| `PQCLEAN_FALCON512_CLEAN_fpr_sqrt` | 512.0K | 0.090 | 175.8 | 0.56% |
| `PQCLEAN_FALCON512_CLEAN_hash_to_point_ct` | 1.0K | 0.040 | 40,000.0 | 0.25% |
| `ffSampling_fft_dyntree` | 1.0K | 0.020 | 20,000.0 | 0.12% |
| `PQCLEAN_FALCON512_CLEAN_FFT` | 9.0K | 0.010 | 1,111.1 | 0.06% |
| `PQCLEAN_FALCON512_CLEAN_trim_i8_decode` | 3.0K | 0.010 | 3,333.3 | 0.06% |
| `mq_NTT` | 3.0K | 0.010 | 3,333.3 | 0.06% |
| `PQCLEAN_FALCON512_CLEAN_iFFT` | 2.0K | 0.010 | 5,000.0 | 0.06% |
| `PQCLEAN_FALCON512_CLEAN_poly_muladj_fft` | 2.0K | 0.010 | 5,000.0 | 0.06% |
| `PQCLEAN_FALCON512_CLEAN_comp_encode` | 1.0K | 0.010 | 10,000.0 | 0.06% |

---

## FALCON512 VERIFY

### Group A — High-frequency, small cycle count per call (3 functions)

| function | calls | self (s) | ns/call | % time |
|----------|------:|---------:|--------:|-------:|
| `mq_montymul` | 8.4M | 0.060 | 7.1 | 33.33% |
| `mq_sub` | 7.4M | 0.010 | 1.3 | 5.56% |
| `mq_add` | 6.9M | 0.030 | 4.3 | 16.67% |

### Group B — Heavy per-call functions (3 functions)

| function | calls | self (s) | ns/call | % time |
|----------|------:|---------:|--------:|-------:|
| `PQCLEAN_FALCON512_CLEAN_hash_to_point_ct` | 1.0K | 0.050 | 50,000.0 | 27.78% |
| `mq_NTT` | 2.0K | 0.020 | 10,000.0 | 11.11% |
| `KeccakF1600_StatePermute` | 11.0K | 0.010 | 909.1 | 5.56% |

---

## FALCON1024 KEYGEN

### Group A — High-frequency, small cycle count per call (45 functions)

| function | calls | self (s) | ns/call | % time |
|----------|------:|---------:|--------:|-------:|
| `modp_montymul` | 2.83B | 18.830 | 6.7 | 12.50% |
| `modp_add` | 2.20B | 8.170 | 3.7 | 5.42% |
| `FPR` | 1.88B | 17.080 | 9.1 | 11.34% |
| `modp_sub` | 897.5M | 1.350 | 1.5 | 0.90% |
| `PQCLEAN_FALCON1024_CLEAN_fpr_add` | 895.3M | 48.150 | 53.8 | 31.96% |
| `fpr_ulsh` | 895.3M | 2.700 | 3.0 | 1.79% |
| `fpr_ursh` | 895.3M | 2.100 | 2.3 | 1.39% |
| `PQCLEAN_FALCON1024_CLEAN_fpr_mul` | 852.2M | 15.300 | 18.0 | 10.16% |
| `fpr_sub` | 375.2M | 0.170 | 0.5 | 0.11% |
| `PQCLEAN_FALCON1024_CLEAN_fpr_scaled` | 125.8M | 4.530 | 36.0 | 3.01% |
| `fpr_of` | 125.8M | 0.060 | 0.5 | 0.04% |
| `zint_mod_small_unsigned` | 113.3M | 4.500 | 39.7 | 2.98% |
| `zint_add_scaled_mul_small` | 75.2M | 5.070 | 67.4 | 3.37% |
| `keccak_inc_squeeze` | 73.7M | 1.420 | 19.3 | 0.94% |
| `get_rng_u64` | 73.7M | 0.170 | 2.3 | 0.11% |
| `shake256_inc_squeeze` | 73.7M | 0.110 | 1.5 | 0.07% |
| `zint_mod_small_signed` | 63.7M | 0.210 | 3.3 | 0.14% |
| `modp_set` | 63.0M | 0.040 | 0.6 | 0.03% |
| `zint_add_mul_small` | 49.6M | 1.370 | 27.6 | 0.91% |
| `zint_norm_zero` | 47.8M | 0.650 | 13.6 | 0.43% |
| `zint_sub` | 47.8M | 0.350 | 7.3 | 0.23% |
| `mq_montymul` | 43.0M | 0.450 | 10.5 | 0.30% |
| `mkgauss` | 36.9M | 2.310 | 62.7 | 1.53% |
| `fpr_neg` | 23.6M | 0.060 | 2.5 | 0.04% |
| `fpr_sqr` | 21.7M | 0.010 | 0.5 | 0.01% |
| `fpr_sqr` | 20.7M | 0.030 | 1.5 | 0.02% |
| `mq_add` | 18.1M | 0.020 | 1.1 | 0.01% |
| `mq_sub` | 18.1M | 0.020 | 1.1 | 0.01% |
| `fpr_lt` | 14.2M | 0.040 | 2.8 | 0.03% |
| `mq_montysqr` | 13.1M | 0.010 | 0.8 | 0.01% |
| `modp_R` | 13.0M | 0.060 | 4.6 | 0.04% |
| `fpr_rint` | 9.1M | 0.120 | 13.1 | 0.08% |
| `fpr_ulsh` | 9.1M | 0.030 | 3.3 | 0.02% |
| `fpr_ursh` | 9.1M | 0.030 | 3.3 | 0.02% |
| `zint_sub_scaled` | 7.3M | 0.150 | 20.5 | 0.10% |
| `modp_ninv31` | 5.6M | 0.070 | 12.5 | 0.05% |
| `modp_norm` | 4.1M | 0.010 | 2.4 | 0.01% |
| `zint_one_to_plain` | 3.1M | 0.010 | 3.2 | 0.01% |
| `zint_mul_small` | 3.1M | 0.290 | 94.3 | 0.19% |
| `modp_mkgm2` | 1.9M | 0.180 | 96.6 | 0.12% |
| `modp_div` | 1.9M | 0.160 | 85.9 | 0.11% |
| `modp_Rx` | 1.8M | 0.010 | 5.5 | 0.01% |
| `mq_div_12289` | 1.2M | 0.050 | 42.1 | 0.03% |
| `PQCLEAN_FALCON1024_CLEAN_poly_mul_fft` | 1.2M | 0.020 | 17.1 | 0.01% |
| `PQCLEAN_FALCON1024_CLEAN_poly_mul_autoadj_fft` | 601.3K | 0.020 | 33.3 | 0.01% |

### Group B — Heavy per-call functions (28 functions)

| function | calls | self (s) | ns/call | % time |
|----------|------:|---------:|--------:|-------:|
| `KeccakF1600_StatePermute` | 4.3M | 3.030 | 698.5 | 2.01% |
| `zint_finish_mod` | 1.9M | 1.600 | 831.9 | 1.06% |
| `modp_NTT2_ext` | 3.7M | 1.570 | 430.0 | 1.04% |
| `modp_R2` | 7.5M | 1.470 | 196.6 | 0.98% |
| `zint_co_reduce_mod` | 961.6K | 0.890 | 925.5 | 0.59% |
| `modp_iNTT2_ext` | 3.5M | 0.760 | 216.9 | 0.50% |
| `PQCLEAN_FALCON1024_CLEAN_fpr_div` | 5.7M | 0.730 | 128.4 | 0.49% |
| `PQCLEAN_FALCON1024_CLEAN_FFT` | 1.2M | 0.700 | 580.4 | 0.46% |
| `PQCLEAN_FALCON1024_CLEAN_iFFT` | 604.3K | 0.690 | 1,141.7 | 0.46% |
| `zint_bezout` | 1.1K | 0.480 | 431,266.8 | 0.32% |
| `poly_big_to_fp` | 1.2M | 0.400 | 337.6 | 0.27% |
| `zint_co_reduce` | 480.8K | 0.350 | 727.9 | 0.23% |
| `poly_sub_scaled` | 1.1M | 0.220 | 198.6 | 0.15% |
| `zint_negate` | 961.6K | 0.220 | 228.8 | 0.15% |
| `zint_rebuild_CRT` | 206.8K | 0.190 | 918.7 | 0.13% |
| `make_fg_step` | 57.2K | 0.160 | 2,795.3 | 0.11% |
| `poly_small_mkgauss` | 36.0K | 0.130 | 3,614.5 | 0.09% |
| `solve_NTRU_intermediate` | 8.3K | 0.090 | 10,891.9 | 0.06% |
| `poly_sub_scaled_ntt` | 56.2K | 0.090 | 1,602.3 | 0.06% |
| `PQCLEAN_FALCON1024_CLEAN_keygen` | 1.0K | 0.070 | 70,000.0 | 0.05% |
| `poly_small_sqnorm` | 36.0K | 0.040 | 1,112.2 | 0.03% |
| `mq_NTT` | 2.4K | 0.040 | 16,542.6 | 0.03% |
| `PQCLEAN_FALCON1024_CLEAN_poly_mulconst` | 18.2K | 0.020 | 1,099.1 | 0.01% |
| `poly_small_to_fp` | 18.2K | 0.020 | 1,099.1 | 0.01% |
| `PQCLEAN_FALCON1024_CLEAN_compute_public` | 1.2K | 0.020 | 16,542.6 | 0.01% |
| `mq_iNTT` | 1.1K | 0.020 | 17,969.5 | 0.01% |
| `PQCLEAN_FALCON1024_CLEAN_poly_invnorm2_fft` | 18.4K | 0.010 | 544.5 | 0.01% |
| `PQCLEAN_FALCON1024_CLEAN_poly_add_muladj_fft` | 1.0K | 0.010 | 9,970.1 | 0.01% |

---

## FALCON1024 SIGN

### Group A — High-frequency, small cycle count per call (35 functions)

| function | calls | self (s) | ns/call | % time |
|----------|------:|---------:|--------:|-------:|
| `FPR` | 652.2M | 5.580 | 8.6 | 15.72% |
| `fpr_ursh` | 336.5M | 0.800 | 2.4 | 2.25% |
| `PQCLEAN_FALCON1024_CLEAN_fpr_add` | 329.5M | 18.300 | 55.5 | 51.55% |
| `fpr_ulsh` | 329.5M | 0.950 | 2.9 | 2.68% |
| `PQCLEAN_FALCON1024_CLEAN_fpr_mul` | 292.8M | 5.630 | 19.2 | 15.86% |
| `fpr_sub` | 157.4M | 0.100 | 0.6 | 0.30% |
| `mq_montymul` | 44.0M | 0.390 | 8.9 | 1.10% |
| `fpr_half` | 36.9M | 0.130 | 3.5 | 0.37% |
| `fpr_neg` | 30.7M | 0.040 | 1.3 | 0.10% |
| `PQCLEAN_FALCON1024_CLEAN_fpr_scaled` | 23.8M | 0.690 | 29.0 | 1.94% |
| `fpr_of` | 23.8M | 0.010 | 0.4 | 0.03% |
| `mq_add` | 20.5M | 0.090 | 4.4 | 0.25% |
| `mq_sub` | 20.5M | 0.010 | 0.5 | 0.03% |
| `fpr_sqr` | 14.3M | 0.030 | 2.1 | 0.07% |
| `fpr_sub` | 12.5M | 0.010 | 0.8 | 0.03% |
| `fpr_trunc` | 7.0M | 0.030 | 4.3 | 0.08% |
| `fpr_inv` | 5.1M | 0.010 | 2.0 | 0.01% |
| `PQCLEAN_FALCON1024_CLEAN_poly_split_fft` | 4.1M | 0.090 | 22.0 | 0.25% |
| `PQCLEAN_FALCON1024_CLEAN_fpr_expm_p63` | 3.5M | 0.340 | 97.1 | 0.96% |
| `PQCLEAN_FALCON1024_CLEAN_gaussian0_sampler` | 3.5M | 0.170 | 48.6 | 0.48% |
| `BerExp` | 3.5M | 0.030 | 8.6 | 0.08% |
| `prng_get_u64` | 3.5M | 0.020 | 5.7 | 0.06% |
| `fpr_trunc` | 3.5M | 0.010 | 2.9 | 0.03% |
| `mq_conv_small` | 3.1M | 0.010 | 3.3 | 0.03% |
| `fpr_rint` | 2.0M | 0.040 | 19.5 | 0.11% |
| `PQCLEAN_FALCON1024_CLEAN_sampler` | 2.0M | 0.020 | 9.8 | 0.06% |
| `fpr_floor` | 2.0M | 0.020 | 9.8 | 0.06% |
| `fpr_half` | 2.0M | 0.010 | 4.9 | 0.03% |
| `fpr_irsh` | 2.0M | 0.010 | 4.9 | 0.03% |
| `PQCLEAN_FALCON1024_CLEAN_poly_merge_fft` | 2.0M | 0.060 | 29.3 | 0.17% |
| `keccak_inc_squeeze` | 1.3M | 0.020 | 15.2 | 0.06% |
| `PQCLEAN_FALCON1024_CLEAN_poly_mul_fft` | 1.0M | 0.080 | 77.7 | 0.23% |
| `PQCLEAN_FALCON1024_CLEAN_poly_add` | 1.0M | 0.010 | 9.7 | 0.03% |
| `mq_div_12289` | 1.0M | 0.010 | 9.8 | 0.03% |
| `PQCLEAN_FALCON1024_CLEAN_poly_LDL_fft` | 1.0M | 0.030 | 29.3 | 0.08% |

### Group B — Heavy per-call functions (17 functions)

| function | calls | self (s) | ns/call | % time |
|----------|------:|---------:|--------:|-------:|
| `PQCLEAN_FALCON1024_CLEAN_fpr_div` | 5.1M | 0.520 | 101.6 | 1.46% |
| `PQCLEAN_FALCON1024_CLEAN_prng_refill` | 76.6K | 0.440 | 5,744.7 | 1.24% |
| `PQCLEAN_FALCON1024_CLEAN_fpr_sqrt` | 1.0M | 0.260 | 253.9 | 0.73% |
| `PQCLEAN_FALCON1024_CLEAN_FFT` | 9.0K | 0.220 | 24,444.4 | 0.62% |
| `mq_NTT` | 3.0K | 0.060 | 20,000.0 | 0.17% |
| `PQCLEAN_FALCON1024_CLEAN_hash_to_point_ct` | 1.0K | 0.060 | 60,000.0 | 0.17% |
| `PQCLEAN_FALCON1024_CLEAN_iFFT` | 2.0K | 0.040 | 20,000.0 | 0.11% |
| `KeccakF1600_StatePermute` | 21.0K | 0.020 | 952.4 | 0.06% |
| `PQCLEAN_FALCON1024_CLEAN_complete_private` | 1.0K | 0.020 | 20,000.0 | 0.06% |
| `mq_iNTT` | 1.0K | 0.020 | 20,000.0 | 0.06% |
| `smallints_to_fpr` | 8.0K | 0.010 | 1,250.0 | 0.03% |
| `PQCLEAN_FALCON1024_CLEAN_trim_i8_decode` | 3.0K | 0.010 | 3,333.3 | 0.03% |
| `PQCLEAN_FALCON1024_CLEAN_poly_muladj_fft` | 2.0K | 0.010 | 5,000.0 | 0.03% |
| `PQCLEAN_FALCON1024_CLEAN_comp_encode` | 1.0K | 0.010 | 10,000.0 | 0.03% |
| `PQCLEAN_FALCON1024_CLEAN_sign_dyn` | 1.0K | 0.010 | 10,000.0 | 0.03% |
| `ffSampling_fft_dyntree` | 1.0K | 0.010 | 10,000.0 | 0.03% |
| `mq_poly_montymul_ntt` | 1.0K | 0.010 | 10,000.0 | 0.03% |

---

## FALCON1024 VERIFY

### Group A — High-frequency, small cycle count per call (3 functions)

| function | calls | self (s) | ns/call | % time |
|----------|------:|---------:|--------:|-------:|
| `mq_montymul` | 18.4M | 0.130 | 7.1 | 35.14% |
| `mq_sub` | 16.4M | 0.030 | 1.8 | 8.11% |
| `mq_add` | 15.4M | 0.060 | 3.9 | 16.22% |

### Group B — Heavy per-call functions (5 functions)

| function | calls | self (s) | ns/call | % time |
|----------|------:|---------:|--------:|-------:|
| `KeccakF1600_StatePermute` | 20.0K | 0.050 | 2,500.0 | 13.51% |
| `PQCLEAN_FALCON1024_CLEAN_hash_to_point_ct` | 1.0K | 0.050 | 50,000.0 | 13.51% |
| `mq_iNTT` | 1.0K | 0.030 | 30,000.0 | 8.11% |
| `mq_rshift1` | 10.0K | 0.010 | 1,000.0 | 2.70% |
| `mq_NTT` | 2.0K | 0.010 | 5,000.0 | 2.70% |
