from inlinestyler.utils import inline_css
import os, sys


htmlFile = open(sys.argv[-1], "r")
message_inline_css = inline_css(htmlFile.read())
htmlFile.close()

outputHtml = "inlined-" + sys.argv[-1]
outputFile = open(outputHtml, "w")
outputFile.write(message_inline_css)
outputFile.close()
