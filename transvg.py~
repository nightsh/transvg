#!/usr/bin/python
import sys
import pprint
import elementtree.ElementTree as ET
import re

pp = pprint.PrettyPrinter()

fname=sys.argv[1]       # Read file name from stdin
f = open(fname, 'r')    # Opens file (sorry, no error checking yet, if it doesn't exist => crash)
xmlsig = '<?xml'        # Some XML-specific identification string (signature)
svgsig = '<svg'         # SVG-specific identification string (signature)


if xmlsig in f.readline():
    print f.name + " is an xml file"
    if svgsig in f.read():
        print f.name + " is a svg file"
    else:
        print "Not a valid SVG file, aborted"
        quit()
else:
    print "Not a valid xml file, aborted"
    quit()



def parseElem(element):
    children = []
    for child in element:
        #print child.text
        #if child.tag in "text":
        if "tspan" in child.tag:
            print child.text
        #    children.append(child)
        #print child.tag
        #print child.text
        parseElem(child)
    return children

svg = ET.parse(fname)
tree = svg.getroot()

parseElem(tree)

