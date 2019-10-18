# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
SOURCERSTDIR  = "$(SOURCEDIR)/rst"
BUILDDIR      = build
SPHINXAPIDOC  ?= sphinx-apidoc
SPHINXAPIOPTS ?= --force --separate --private --module-first
PROJECTDIR    = ../

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	rm -f $(SOURCERSTDIR)/*
	@$(SPHINXAPIDOC) $(SPHINXAPIOPTS) --output-dir "$(SOURCERSTDIR)" "$(PROJECTDIR)"
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
