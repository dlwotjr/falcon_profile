#!/bin/bash
set -e

OPERATIONS="falcon512_keygen falcon512_sign falcon512_verify falcon1024_keygen falcon1024_sign falcon1024_verify"

for OPT in O0 O3; do
    BIN="./falcon_profile_${OPT}"
    echo "=== Profiling with ${OPT} ==="
    for OP in $OPERATIONS; do
        echo "  Running ${OP} ..."
        ${BIN} ${OP}
        gprof ${BIN} gmon.out > "analysis_${OP}_${OPT}.txt"
        rm -f gmon.out
        echo "  -> analysis_${OP}_${OPT}.txt saved"
    done
done

echo ""
echo "Generating result.md ..."
python3 gen_result.py
echo "Done."
