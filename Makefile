# Makefile for the TeX bit of the project. We'll probably also
# need stuff for the actual programming part...

.SUFFIXES: tex pdf
.PHONY: clean

# If/when we add figures, we will want to update the list of
# dependencies.

DebrayWu-AstronomicalImplicationsofMachineLearning.pdf: DebrayWu-AstronomicalImplicationsofMachineLearning.tex macros.tex
	pdflatex -halt-on-error DebrayWu-AstronomicalImplicationsofMachineLearning
	@pdflatex -halt-on-error DebrayWu-AstronomicalImplicationsofMachineLearning > /dev/null

clean:
	rm -f *.aux *.out *.log
