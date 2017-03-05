OUTDIR = build/
CODEDIR = src/
DIAGRAM_FILES := $(wildcard ../assets/diagram/*.dia)

.PHONY: pdf clean move diagram split

pdf:
	$(MAKE) -C $(CODEDIR) latex

move:
	rm -f pdf/skripsi.pdf && \
	cp -a $(OUTDIR)/main.pdf pdf/skripsi.pdf && \
	rm -rf $(OUTDIR)/main.pdf

clean:
	cd $(OUTDIR) && \
	rm -f *.lof *.lot *.lol *.toc *.aux *.idx *.log *.out *.gz *.bbl *.blg *.ilg *.ind *.dvi *.bcf *.run.xml && \
	rm -rf _minted-main/
	rm -rf $(OUTDIR)components/*
	rm -rf $(CODEDIR)_minted-main/

diagram:
	# Exporting DIA diagram to tex and png
	for x in $(DIAGRAM_FILES); \
		do \
			file=$${x##*/}; \
			tex=$${x%/*}/export/$${file%.dia}.tex; \
			png=$${x%/*}/export/$${file%.dia}.png; \
			dia --export=$$tex $$x ; \
			dia --export=$$png $$x ; \
		done

split:
	# Splitting PDF per chapter
	./split.py
