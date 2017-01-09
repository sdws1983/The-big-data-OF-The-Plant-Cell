'''Python 2.7'''

from urllib2 import urlopen
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
import re

def convert_pdf_to_txt(fp):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    fp.close()
    device.close()
    textstr = retstr.getvalue()
    retstr.close()
    return textstr

def get_issues(iss):
	
	url='http://www.plantcell.org/content/28/' + str(iss) + '.toc.pdf'
	fp = StringIO(urlopen(url).read())
	text=convert_pdf_to_txt(fp)
	text = str(text).split("\n")
	all = []
	for i in text:
		#print (i)
		if re.findall('\D+', i):
			pass
		elif i != '' :
			all.append(i)
	print (all)

if __name__ == "__main__":
	for iss in range(1,12):
		#print (iss)
		get_issues(iss)

