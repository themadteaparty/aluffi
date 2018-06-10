all: main.pdf

main.pdf: *.tex authors.gen.tex
	pdflatex main.tex

authors.gen.tex: AUTHORS mkauthors.py
	./mkauthors.py
