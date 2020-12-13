VERSIONCMD = git describe --dirty --tags --always 2> /dev/null
VERSION := $(shell $(VERSIONCMD) || cat VERSION)

PREFIX ?= /usr/local
BINPREFIX ?= $(PREFIX)/bin
MANPREFIX ?= $(PREFIX)/share/man

MANPAGE = tb.1

all: tb $(MANPAGE)

tb: tb.in
	sed "s/@VERSION/$(VERSION)/" tb.in > tb
	chmod +x tb

$(MANPAGE): man/$(MANPAGE).pod
	pod2man -n=tb -c=tb -r=$(VERSION) $< $(MANPAGE)

install:
	mkdir -p $(DESTDIR)$(BINPREFIX)
	cp -p tb $(DESTDIR)$(BINPREFIX)
	mkdir -p $(DESTDIR)$(MANPREFIX)/man1
	cp -p $(MANPAGE) $(DESTDIR)$(MANPREFIX)/man1

uninstall:
	rm -f $(DESTDIR)$(BINPREFIX)/tb
	rm -f $(DESTDIR)$(MANPREFIX)/man1/tb.1

clean:
	rm -f tb $(MANPAGE)

.PHONY: all install uninstall clean
