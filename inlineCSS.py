from inlinestyler.utils import inline_css
import os
import sys

file = sys.argv[-1]
htmlFile = open(file, "r")
message_inline_css = inline_css(htmlFile.read())
htmlFile.close()

outputHtml = "inlined/inlined-" + os.path.basename(file)
outputFile = open(outputHtml, "w")
outputFile.write(message_inline_css)
outputFile.close()
