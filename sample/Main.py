import sys
import os
from DocReader import DocReader
from DocCreator import DocCreator


if (len(sys.argv) > 2):
    raise ValueError('Only one argument is allowed')
if (len(sys.argv) == 1):
    path = os.getcwd()
else:
    path = sys.argv[1]

docreader = DocReader(path)
uncreated_doc = docreader.read()
doccreator = DocCreator(uncreated_doc, path)

print(doccreator.create())
