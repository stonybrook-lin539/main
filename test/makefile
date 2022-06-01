CSS = $(realpath ../includes/web-custom.css)
CMDS = ../includes/mycommands.mdown

# BUILDDIR := build
NAMES := full-style-and-feature-test
HTML := $(addsuffix .html, $(NAMES))
# HTML := $(addprefix $(BUILDDIR)/, $(HTML))

.PHONY: all
all: $(HTML)

# $(BUILDDIR):
# 	mkdir -p $@

%.html: %.mdown $(CSS)
	pandoc -s --standalone -f markdown-implicit_figures \
		--css $(CSS) -H $(CMDS) \
		$< -o $@

.PHONY: clean
clean:
	rm -rf $(HTML)
