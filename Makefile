CC      = gcc
CFLAGS  = -std=c99 -Wall -Wextra -Wpedantic -Wvla -Wconversion \
          -I. -Icommon -Ifalcon-512/clean -Ifalcon-1024/clean

FALCON512_SRC = \
    falcon-512/clean/codec.c \
    falcon-512/clean/common.c \
    falcon-512/clean/fft.c \
    falcon-512/clean/fpr.c \
    falcon-512/clean/keygen.c \
    falcon-512/clean/pqclean.c \
    falcon-512/clean/rng.c \
    falcon-512/clean/sign.c \
    falcon-512/clean/vrfy.c

FALCON1024_SRC = \
    falcon-1024/clean/codec.c \
    falcon-1024/clean/common.c \
    falcon-1024/clean/fft.c \
    falcon-1024/clean/fpr.c \
    falcon-1024/clean/keygen.c \
    falcon-1024/clean/pqclean.c \
    falcon-1024/clean/rng.c \
    falcon-1024/clean/sign.c \
    falcon-1024/clean/vrfy.c

COMMON_SRC = \
    common/fips202.c \
    common/randombytes.c

TEST_TARGET  = falcon_test
TEST_SRCS    = main.c $(FALCON512_SRC) $(COMMON_SRC)
TEST_CFLAGS  = $(CFLAGS) -O2

PROF_SRCS    = main_profile.c $(FALCON512_SRC) $(FALCON1024_SRC) $(COMMON_SRC)
PROF_O0      = falcon_profile_O0
PROF_O3      = falcon_profile_O3
PROF_O0_FLAGS = $(CFLAGS) -O0 -pg
PROF_O3_FLAGS = $(CFLAGS) -O3 -pg

OPERATIONS = falcon512_keygen falcon512_sign falcon512_verify \
             falcon1024_keygen falcon1024_sign falcon1024_verify

.PHONY: all run profile_o0 profile_o3 result graph clean distclean

all: $(TEST_TARGET)

$(TEST_TARGET): $(TEST_SRCS)
	$(CC) $(TEST_CFLAGS) -o $@ $^

$(PROF_O0): $(PROF_SRCS)
	$(CC) $(PROF_O0_FLAGS) -o $@ $^

$(PROF_O3): $(PROF_SRCS)
	$(CC) $(PROF_O3_FLAGS) -o $@ $^

# Run one operation with a given binary, save analysis to named file
define run_op
	./$(1) $(2)
	gprof $(1) gmon.out > analysis_$(2)_$(3).txt
	$(RM) gmon.out
endef

profile_o0: $(PROF_O0)
	@echo "=== Profiling with O0 ==="
	$(foreach op,$(OPERATIONS),$(call run_op,$(PROF_O0),$(op),O0))

profile_o3: $(PROF_O3)
	@echo "=== Profiling with O3 ==="
	$(foreach op,$(OPERATIONS),$(call run_op,$(PROF_O3),$(op),O3))

result: profile_o0 profile_o3
	python3 gen_result.py

graph: venv
	for op in $(OPERATIONS); do \
	    venv/bin/gprof2dot -f prof analysis_$${op}_O0.txt -o output_$${op}_O0.dot; \
	    venv/bin/gprof2dot -f prof analysis_$${op}_O3.txt -o output_$${op}_O3.dot; \
	    dot -Tpng output_$${op}_O0.dot -o output_$${op}_O0.png; \
	    dot -Tpng output_$${op}_O3.dot -o output_$${op}_O3.png; \
	    echo "PNG: output_$${op}_O0.png  output_$${op}_O3.png"; \
	done

venv:
	python3 -m venv venv
	venv/bin/pip install -q gprof2dot

run: $(TEST_TARGET)
	./$(TEST_TARGET)

clean:
	$(RM) $(TEST_TARGET) $(PROF_O0) $(PROF_O3)
	$(RM) gmon.out output_*.dot output_*.png
	$(RM) -r venv

distclean: clean
	$(RM) analysis_*.txt result.md
