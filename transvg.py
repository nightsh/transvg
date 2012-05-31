#!/usr/bin/python
import sys

fname=sys.argv[1]       # Read file name from stdin
f = open(fname, 'r+')   # Opens file (sorry, no error checking yet, if it doesn't exist => crash)
xmlsig = '<?xml'        # Some XML-specific identification string (signature)
svgsig = '<svg' # SVG-specific identification string (signature)

if xmlsig in f.readline():
    print f.name + " is an xml file"
    if svgsig in f.read():
        print f.name + " is a svg file"
    else:
        print "Not a SVG file, aborted"
        quit()
else:
    print "Not an xml file, aborted"
    quit()

