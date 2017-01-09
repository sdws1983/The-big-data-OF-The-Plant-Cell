'''Python2.7'''

from bs4 import BeautifulSoup
import urllib2
import re

def get_html(url):
	send_headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36',
		'Accept':'*/*',
		'Connection':'keep-alive',
		'Host':'www.plantcell.org'
	}

	req = urllib2.Request(url,headers = send_headers)
	response = urllib2.urlopen(req)
	html = response.read().decode('utf-8')

	return html

def analyse(html):
	soup = BeautifulSoup(html,'lxml')
	for i in soup.find_all('p'):
		#print (i.string)
		try:
			if i['id'] == "p-5":
				#print (str(i))
				#print (str(str(i).find(">") + 1))
				#print (str(i).find("<", str(i).find(">") + 1))
				content = str(i)[(str(i).find(">") + 1):(str(i).find("</p>", str(i).find(">") + 1))]
				content = re.sub(r'<.*?>', '', str(content))
				content = re.sub(r'\n', ' ', str(content))
				content = re.sub(r' +', ' ', str(content))
				#print (content)
		except:
			pass
	
	count = 1
	address_list = []
	author_list = []
	for each in soup.find_all('li'):
		try:
			if 'last' in each['class'] and u'name' in str(each):
				author = each.find_all('a')[0].string
				author_list.append(author)

			elif 'aff' in each['class']:
				address = str(each.find_all('address')[0])
				address = address[(address.find('</sup>') + len('</sup>')):(address.find('\n'))]
				address = (str(count) + "\t" + address + "\n")
				address_list.append(address)
				count += 1
		except:
			pass
	
	return  content, ''.join(author_list), ''.join(address_list)

def main(vol,page):
	url = "http://www.plantcell.org/content/28/" + str(vol) + "/" + str(page) + ".abstract"

	html = get_html(url)
	content, author, address = analyse(html)
	f1 = open((str(vol) + '-content.csv'), 'a')
	f2 = open((str(vol) + '-author.csv'), 'a')
	f3 = open((str(vol) + '-address.csv'), 'a')
	f1.write(content + "\n")
	f2.write(author + "\n")
	f3.write(address + "\n")

if __name__ == "__main__":
	main(11, 2715)



