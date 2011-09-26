#!/usr/bin/python
import sys
import re

cssfile = open('../css/style.css', 'r')
inputhtml = open('../resume.html', 'r')
outputhtml = open('../jobmine.html', 'w+')

for line in inputhtml:
    if re.match('(.*)style.css(.*)', line):
        outputhtml.write('<style type="text/css">\n')
        for sline in cssfile:
            outputhtml.write('\t' + sline)
        outputhtml.write('</style>\n')
    else:        
        outputhtml.write(line)
