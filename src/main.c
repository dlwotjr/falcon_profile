#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <stddef.h>

#include "falcon-512/clean/api.h"
#include "common/randombytes.h"

#define NTESTS  1000
#define MLEN    32

static int run_test(int iter) {
    uint8_t pk[PQCLEAN_FALCON512_CLEAN_CRYPTO_PUBLICKEYBYTES];
    uint8_t sk[PQCLEAN_FALCON512_CLEAN_CRYPTO_SECRETKEYBYTES];
    uint8_t sig[PQCLEAN_FALCON512_CLEAN_CRYPTO_BYTES];
    uint8_t msg[MLEN];
    size_t siglen;

    /* keygen */
    if (PQCLEAN_FALCON512_CLEAN_crypto_sign_keypair(pk, sk) != 0) {
        fprintf(stderr, "[%d] keygen failed\n", iter);
        return -1;
    }

    /* random message */
    randombytes(msg, MLEN);

    /* sign */
    if (PQCLEAN_FALCON512_CLEAN_crypto_sign_signature(sig, &siglen, msg, MLEN, sk) != 0) {
        fprintf(stderr, "[%d] sign failed\n", iter);
        return -1;
    }

    /* verify */
    if (PQCLEAN_FALCON512_CLEAN_crypto_sign_verify(sig, siglen, msg, MLEN, pk) != 0) {
        fprintf(stderr, "[%d] verify failed\n", iter);
        return -1;
    }

    /* negative test: tampered message must NOT verify */
    msg[0] ^= 0xFF;
    if (PQCLEAN_FALCON512_CLEAN_crypto_sign_verify(sig, siglen, msg, MLEN, pk) == 0) {
        fprintf(stderr, "[%d] verify accepted tampered message\n", iter);
        return -1;
    }

    return 0;
}

int main(void) {
    printf("Falcon-512 test: %d iterations\n", NTESTS);

    int failures = 0;
    for (int i = 0; i < NTESTS; i++) {
        if (run_test(i) != 0) {
            failures++;
        }
        if ((i + 1) % 100 == 0) {
            printf("  %d / %d done\n", i + 1, NTESTS);
        }
    }

    if (failures == 0) {
        printf("All %d tests PASSED\n", NTESTS);
        return 0;
    } else {
        printf("%d / %d tests FAILED\n", failures, NTESTS);
        return 1;
    }
}
