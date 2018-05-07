import urllib2
from bs4 import BeautifulSoup
import os
#Deschidere pagina mea
url = "index.html"
potato = BeautifulSoup(open(url),'lxml')

#BOX -7 

#deschidere pagina fashiondays
link='https://www.fashiondays.ro/s/ankle-boots-categ-mmse-w?origin=top&position=1'
page = urllib2.urlopen(link)
soup = BeautifulSoup(page, 'lxml')

#gasirea imaginii din fashiondays
spandata1 = soup.findAll('span',{'class':'campaign-photo'})
for span in spandata1:
	sursa = span.img['data-original']
	print(sursa)
	break
#gasirea textului in fashiondays
spantext = soup.findAll(class_="product-description" )
for span in spantext:
	author = span.text.strip()
	print(author)
	break

#Gasirea clasei cu numele fashiondays si modificarea continutului(src imagine)
imgs = potato.findAll(class_= 'fashion_femei')
for element in imgs:
	element['src'] = sursa 	


#Gasirea clasei cu numele emag si modificarea continutului(text)
for element in potato.find(class_="fashion_femei_text"):
	text = element.string.strip()
	if text:
		element.string.replace_with(author[0:30])  

#gasirea discountului pe elefant(text)
spandata = soup.findAll(class_='discount')
for span in spandata:
	discount = span.text.strip()
	print(discount)
	break

#modificarea discountului in site 
for element in potato.findAll(class_="fashion_femei_disc"):
	text = element.string.strip()
	if text:
		element.string.replace_with(discount)

#BOX-8

#deschidere pagina fashiondays
link='https://www.fashiondays.ro/s/shirts-categ-mmse-m'
page = urllib2.urlopen(link)
soup = BeautifulSoup(page, 'lxml')

#gasirea imaginii din fashiondays
spandata1 = soup.findAll('span',{'class':'campaign-photo'})
for span in spandata1:
	sursa = span.img['data-original']
	print(sursa)
	break
#gasirea textului in fashiondays
spantext = soup.findAll(class_="product-description" )
for span in spantext:
	author = span.text.strip()
	print(author)
	break

#Gasirea clasei cu numele fashiondays si modificarea continutului(src imagine)
imgs = potato.findAll(class_= 'fashion_barbati')
for element in imgs:
	element['src'] = sursa 	


#Gasirea clasei cu numele emag si modificarea continutului(text)
for element in potato.find(class_="fashion_barbati_text"):
	text = element.string.strip()
	if text:
		element.string.replace_with(author)  

#gasirea discountului pe elefant(text)
spandata = soup.findAll(class_='discount')
for span in spandata:
	discount = span.text.strip()
	print(discount)
	break

#modificarea discountului in site 
for element in potato.findAll(class_="fashion_barbati_disc"):
	text = element.string.strip()
	if text:
		element.string.replace_with(discount)

#BOX - 9

#deschidere pagina fashiondays
link='https://www.fashiondays.ro/g/femei-/pentru_casa?s=highest_price'
page = urllib2.urlopen(link)
soup = BeautifulSoup(page, 'lxml')

#gasirea imaginii din fashiondays
spandata1 = soup.findAll('span',{'class':'campaign-photo'})
for span in spandata1:
	sursa = span.img['data-original']
	print(sursa)
	break

#gasirea textului in fashiondays
spantext = soup.findAll(class_="product-description" )
for span in spantext:
	author = span.text.strip()
	print(author)
	break

#Gasirea clasei cu numele fashiondays si modificarea continutului(src imagine)
imgs = potato.findAll(class_= 'fashion_femeihaine')
for element in imgs:
	element['src'] = sursa 	


#Gasirea clasei cu numele emag si modificarea continutului(text)
for element in potato.find(class_="fashion_femeihaine_text"):
	text = element.string.strip()
	if text:
		element.string.replace_with(author)  

#gasirea discountului pe elefant(text)
spandata = soup.findAll(class_='discount')
for span in spandata:
	discount = span.text.strip()
	print(discount)
	break

#modificarea discountului in site 
for element in potato.findAll(class_="fashion_femeihaine_disc"):
	text = element.string.strip()
	if text:
		element.string.replace_with(discount)

#salvarea paginii html modificate
html = potato.prettify("utf-8")
with open("index.html", "wb") as file:
    file.write(html)
print("Done!")