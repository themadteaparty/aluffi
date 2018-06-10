all: main.pdf

main.pdf: *.tex
	pdflatex main.tex
