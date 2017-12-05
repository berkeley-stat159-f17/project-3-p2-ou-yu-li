# Minimal makefile for Sphinx documentation
#

IPYNB_FILES=$(wildcard demographics-p*.ipynb)

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = python -msphinx
SPHINXPROJ    = p3
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: github

github: html
	ghp-import $(BUILDDIR)/html/
	git push -u origin gh-pages
	@echo
	@echo "Published to Github"


.PHONY : env
env: environment.yml
	conda env create -f environment.yml

.PHONY: all
all: $(IPYNB_FILES)
	jupyter nbconvert --ExecutePreprocessor.timeout=-1 --inplace --execute demographics-p1.ipynb
	jupyter nbconvert --ExecutePreprocessor.timeout=-1 --inplace --execute demographics-p2.ipynb
	jupyter nbconvert --ExecutePreprocessor.timeout=-1 --inplace --execute demographics-p3.ipynb
	jupyter nbconvert --ExecutePreprocessor.timeout=-1 --inplace --execute demographics-p4.ipynb
	jupyter nbconvert --ExecutePreprocessor.timeout=-1 --inplace --execute demographics-p5.ipynb
	jupyter nbconvert --ExecutePreprocessor.timeout=-1 --inplace --execute main.ipynb