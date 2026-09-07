#!/bin/bash
# Run all 6 gprof profiling operations (O0 and O3) and save results.
# Usage: bash scripts/run_profile.sh   (from the repository root)
set -e

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
RESULTS="$REPO_ROOT/results"
GRAPHS="$REPO_ROOT/graphs"

OPERATIONS="falcon512_keygen falcon512_sign falcon512_verify
            falcon1024_keygen falcon1024_sign falcon1024_verify"

mkdir -p "$RESULTS" "$GRAPHS"

# ---- build profiling binaries ----
echo "[build] Building profiling binaries..."
make -C "$REPO_ROOT" falcon_profile_O0 falcon_profile_O3

# ---- run all 12 profiles ----
cd "$REPO_ROOT"
for OPT in O0 O3; do
    BIN="./falcon_profile_${OPT}"
    echo "=== Profiling with -${OPT} ==="
    for OP in $OPERATIONS; do
        echo "  ${OP} ..."
        ${BIN} ${OP}
        gprof ${BIN} gmon.out > "$RESULTS/analysis_${OP}_${OPT}.txt"
        rm -f gmon.out
    done
done
# ---- generate result.md ----
echo "[gen] result.md"
python3 "$REPO_ROOT/scripts/gen_result.py"

# ---- generate call graph PNGs (requires graphviz) ----
if command -v dot &>/dev/null; then
    echo "[gen] call graph PNGs"
    if [ ! -d "$REPO_ROOT/venv" ]; then
        python3 -m venv "$REPO_ROOT/venv"
        "$REPO_ROOT/venv/bin/pip" install -q gprof2dot
    fi
    for OPT in O0 O3; do
        for OP in $OPERATIONS; do
            "$REPO_ROOT/venv/bin/gprof2dot" -f prof \
                "$RESULTS/analysis_${OP}_${OPT}.txt" \
                | dot -Tpng -o "$GRAPHS/output_${OP}_${OPT}.png" 2>/dev/null || true
        done
    done
else
    echo "[skip] graphviz not found — install with: sudo apt install graphviz"
fi

# ---- generate LaTeX ----
echo "[gen] LaTeX report"
python3 "$REPO_ROOT/scripts/gen_tex.py"

echo ""
echo "All done."
echo "  results/           -> gprof analysis files + result.md"
echo "  graphs/            -> call graph PNGs"
echo "  tex/               -> LaTeX source + PDF"
