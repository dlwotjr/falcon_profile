#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <stddef.h>

#include "falcon-512/clean/api.h"
#include "falcon-1024/clean/api.h"
#include "common/randombytes.h"

#define NTESTS 1000
#define MLEN   32

/* -------- Falcon-512 -------- */

static void run_falcon512_keygen(void) {
    uint8_t pk[PQCLEAN_FALCON512_CLEAN_CRYPTO_PUBLICKEYBYTES];
    uint8_t sk[PQCLEAN_FALCON512_CLEAN_CRYPTO_SECRETKEYBYTES];
    for (int i = 0; i < NTESTS; i++) {
        PQCLEAN_FALCON512_CLEAN_crypto_sign_keypair(pk, sk);
    }
}

static void run_falcon512_sign(void) {
    uint8_t pk[PQCLEAN_FALCON512_CLEAN_CRYPTO_PUBLICKEYBYTES];
    uint8_t sk[PQCLEAN_FALCON512_CLEAN_CRYPTO_SECRETKEYBYTES];
    uint8_t sig[PQCLEAN_FALCON512_CLEAN_CRYPTO_BYTES];
    uint8_t msg[MLEN];
    size_t  siglen;

    PQCLEAN_FALCON512_CLEAN_crypto_sign_keypair(pk, sk);
    randombytes(msg, MLEN);
    for (int i = 0; i < NTESTS; i++) {
        PQCLEAN_FALCON512_CLEAN_crypto_sign_signature(sig, &siglen, msg, MLEN, sk);
    }
}

static void run_falcon512_verify(void) {
    uint8_t pk[PQCLEAN_FALCON512_CLEAN_CRYPTO_PUBLICKEYBYTES];
    uint8_t sk[PQCLEAN_FALCON512_CLEAN_CRYPTO_SECRETKEYBYTES];
    uint8_t sig[PQCLEAN_FALCON512_CLEAN_CRYPTO_BYTES];
    uint8_t msg[MLEN];
    size_t  siglen;

    PQCLEAN_FALCON512_CLEAN_crypto_sign_keypair(pk, sk);
    randombytes(msg, MLEN);
    PQCLEAN_FALCON512_CLEAN_crypto_sign_signature(sig, &siglen, msg, MLEN, sk);
    for (int i = 0; i < NTESTS; i++) {
        PQCLEAN_FALCON512_CLEAN_crypto_sign_verify(sig, siglen, msg, MLEN, pk);
    }
}

/* -------- Falcon-1024 -------- */

static void run_falcon1024_keygen(void) {
    uint8_t pk[PQCLEAN_FALCON1024_CLEAN_CRYPTO_PUBLICKEYBYTES];
    uint8_t sk[PQCLEAN_FALCON1024_CLEAN_CRYPTO_SECRETKEYBYTES];
    for (int i = 0; i < NTESTS; i++) {
        PQCLEAN_FALCON1024_CLEAN_crypto_sign_keypair(pk, sk);
    }
}

static void run_falcon1024_sign(void) {
    uint8_t pk[PQCLEAN_FALCON1024_CLEAN_CRYPTO_PUBLICKEYBYTES];
    uint8_t sk[PQCLEAN_FALCON1024_CLEAN_CRYPTO_SECRETKEYBYTES];
    uint8_t sig[PQCLEAN_FALCON1024_CLEAN_CRYPTO_BYTES];
    uint8_t msg[MLEN];
    size_t  siglen;

    PQCLEAN_FALCON1024_CLEAN_crypto_sign_keypair(pk, sk);
    randombytes(msg, MLEN);
    for (int i = 0; i < NTESTS; i++) {
        PQCLEAN_FALCON1024_CLEAN_crypto_sign_signature(sig, &siglen, msg, MLEN, sk);
    }
}

static void run_falcon1024_verify(void) {
    uint8_t pk[PQCLEAN_FALCON1024_CLEAN_CRYPTO_PUBLICKEYBYTES];
    uint8_t sk[PQCLEAN_FALCON1024_CLEAN_CRYPTO_SECRETKEYBYTES];
    uint8_t sig[PQCLEAN_FALCON1024_CLEAN_CRYPTO_BYTES];
    uint8_t msg[MLEN];
    size_t  siglen;

    PQCLEAN_FALCON1024_CLEAN_crypto_sign_keypair(pk, sk);
    randombytes(msg, MLEN);
    PQCLEAN_FALCON1024_CLEAN_crypto_sign_signature(sig, &siglen, msg, MLEN, sk);
    for (int i = 0; i < NTESTS; i++) {
        PQCLEAN_FALCON1024_CLEAN_crypto_sign_verify(sig, siglen, msg, MLEN, pk);
    }
}

/* -------- dispatch -------- */

typedef struct { const char *name; void (*fn)(void); } op_t;

static const op_t ops[] = {
    { "falcon512_keygen",   run_falcon512_keygen   },
    { "falcon512_sign",     run_falcon512_sign     },
    { "falcon512_verify",   run_falcon512_verify   },
    { "falcon1024_keygen",  run_falcon1024_keygen  },
    { "falcon1024_sign",    run_falcon1024_sign    },
    { "falcon1024_verify",  run_falcon1024_verify  },
};
#define NOPS (int)(sizeof(ops) / sizeof(ops[0]))

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <operation>\nOperations:\n", argv[0]);
        for (int i = 0; i < NOPS; i++) {
            fprintf(stderr, "  %s\n", ops[i].name);
        }
        return 1;
    }
    for (int i = 0; i < NOPS; i++) {
        if (strcmp(argv[1], ops[i].name) == 0) {
            printf("Running %s x%d ...\n", ops[i].name, NTESTS);
            ops[i].fn();
            printf("Done.\n");
            return 0;
        }
    }
    fprintf(stderr, "Unknown operation: %s\n", argv[1]);
    return 1;
}
