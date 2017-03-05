TOP_DIR=../
OUTDIR=$(TOP_DIR)build/

draft: main.tex
	pdflatex -shell-escape -draftmode -file-line-error -interaction=nonstopmode -output-directory=$(OUTDIR) main.tex
	#bibtex -terse main.aux
	biber --debug --nolog --input-directory=$(OUTDIR) --output-directory=$(OUTDIR) main.bcf
	# makeindex main
	pdflatex -shell-escape -draftmode -file-line-error -interaction=nonstopmode -output-directory=$(OUTDIR) main.tex

latex: draft
	pdflatex -shell-escape -file-line-error -synctex=1 -interaction=nonstopmode -output-directory=$(OUTDIR) main.tex

