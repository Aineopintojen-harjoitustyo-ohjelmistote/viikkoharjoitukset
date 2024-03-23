#!/bin/sh
for f in *.md; do
	markdown $f | \
		html2ps -t -C hb -f html2ps.conf | \
		gs -o ../${f%.*}.pdf -sDEVICE=pdfwrite -
done
