import urllib2
from bs4 import BeautifulSoup
import os
#Deschidere pagina mea
url = "index.html"
potato = BeautifulSoup(open(url),'lxml')

#deschidere pagina elefant
link='http://www.elefant.ro/list?filtercampanie=12168'
page = urllib2.urlopen(link)
soup = BeautifulSoup(page, 'lxml')

#gasirea imaginii din elefant
divdata = soup.findAll('div',{'class':'thumbnail'})
for div in divdata:
	sursa = div.img['data-original']
	break

#gasirea textului in elefant
divtext = soup.findAll('div',{'class': 'col-sm-12 elf-brand'} )
for div in divtext:
	author = div.text.strip()
	print(author)
	break
	
divtext = soup.findAll('div',{'class': 'col-sm-12 elf-title'})
for div in divtext:
	title = div.text.strip()
	print(title)
	break

#Gasirea clasei cu numele elefant si modificarea continutului(src imagine)
imgs = potato.findAll(class_= 'elefant_carte')
for element in imgs:
	element['src'] = sursa 	

#Gasirea clasei cu numele emag si modificarea continutului(text)
for element in potato.find(class_="elefant_carte_text"):
	text = element.string.strip()
	if text:
		element.string.replace_with(author + os.linesep +title)  

#gasirea discountului pe elefant(text)
spandata = soup.findAll(class_='elf-badge pull-right')
for span in spandata:
	discount = span.text.strip()
	print(discount)
	break

#modificarea discountului in site 
for element in potato.findAll(class_="elefant_carte_disc"):
	text = element.string.strip()
	if text:
		element.string.replace_with(discount)

#BOX-5

#deschidere pagina elefant
link='http://www.elefant.ro/list/ceasuri/brand-axcent-of-scandinavia,belmond,henry-london,just-watch,karen-millen,mark-maddox,momentus,orla-kiely,paris-hilton,pierre-cardin,rodania-classics?sortsales=desc&filterDiscount=Reducere+50%25-70%25'
page = urllib2.urlopen(link)
soup = BeautifulSoup(page, 'lxml')

#gasirea imaginii din elefant
divdata = soup.findAll('div',{'class':'thumbnail'})
for div in divdata:
	sursa = div.img['data-original']
	break

#gasirea textului in elefant
divtext = soup.findAll('div',{'class': 'col-sm-12 elf-brand'} )
for div in divtext:
	author = div.text.strip()
	print(author)
	break
divtext = soup.findAll('div',{'class': 'col-sm-12 elf-title'})
for div in divtext:
	title = div.text.strip()
	print(title)
	break

#Gasirea clasei cu numele elefant si modificarea continutului(src imagine)
imgs = potato.findAll(class_= 'elefant_ceas')
for element in imgs:
	element['src'] = sursa 	

#Gasirea clasei cu numele emag si modificarea continutului(text)
for element in potato.find(class_="elefant_ceas_text"):
	text = element.string.strip()
	if text:
		element.string.replace_with(title[0:30])  

#gasirea discountului pe elefant(text)
spandata = soup.findAll(class_='elf-badge pull-right')
for span in spandata:
	discount = span.text.strip()
	print(discount)
	break

#modificarea discountului in site 
for element in potato.findAll(class_="elefant_ceas_disc"):
	text = element.string.strip()
	if text:
		element.string.replace_with(discount)


#BOX 6

#deschidere pagina elefant
link='http://www.elefant.ro/list/cosmetice-si-parfumuri/parfumuri?filtersex=Femei~~~Unisex'
page = urllib2.urlopen(link)
soup = BeautifulSoup(page, 'lxml')

#gasirea imaginii din elefant
divdata = soup.findAll('div',{'class':'thumbnail'})
for div in divdata:
	sursa = div.img['data-original']
	break

#gasirea textului in elefant
divtext = soup.findAll('div',{'class': 'col-sm-12 elf-brand'} )
for div in divtext:
	author = div.text.strip()
	print(author)
	break
divtext = soup.findAll('div',{'class': 'col-sm-12 elf-title'})
for div in divtext:
	title = div.text.strip()
	print(title)
	break

#Gasirea clasei cu numele elefant si modificarea continutului(src imagine)
imgs = potato.findAll(class_= 'elefant_parfum')
for element in imgs:
	element['src'] = sursa 	

#Gasirea clasei cu numele emag si modificarea continutului(text)
for element in potato.find(class_="elefant_parfum_text"):
	text = element.string.strip()
	if text:
		element.string.replace_with(title[0:30])  

#gasirea discountului pe elefant(text)
spandata = soup.findAll(class_='elf-badge pull-right')
for span in spandata:
	discount = span.text.strip()
	print(discount)
	break

#modificarea discountului in site 
for element in potato.findAll(class_="elefant_parfum_disc"):
	text = element.string.strip()
	if text:
		element.string.replace_with(discount)

#salvarea paginii html modificate
html = potato.prettify("utf-8")
with open("index.html", "wb") as file:
    file.write(html)
print("Done!")