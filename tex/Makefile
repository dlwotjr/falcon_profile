TEX = falcon_profiling

all: $(TEX).pdf

$(TEX).pdf: $(TEX).tex
	pdflatex -interaction=nonstopmode $(TEX).tex
	pdflatex -interaction=nonstopmode $(TEX).tex

clean:
	$(RM) $(TEX).aux $(TEX).log $(TEX).out $(TEX).toc
