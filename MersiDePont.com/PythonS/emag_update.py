import urllib2
from bs4 import BeautifulSoup

#Deschidere pagina mea
url = "index.html"
potato = BeautifulSoup(open(url),'lxml')

#deschidere pagina emag
link='https://www.emag.ro/label/telefoane-mobile/Lichidari-de-stoc%3A-Telefoane-mobile/c'
page = urllib2.urlopen(link)
soup = BeautifulSoup(page, 'lxml')

#gasirea imaginii din emag
divdata = soup.findAll('div',{'class':'thumbnail-wrapper'})
for div in divdata:
	sursa = div.img['src']
	break
#Gasirea clasei cu numele emag si modificarea continutului(src imagine)
imgs = potato.findAll(class_= 'emag_mobile')
for element in imgs:
	element['src'] = sursa 

#Gasirea clasei cu numele emag si modificarea continutului(text)
for element in potato.find(class_="emag_mobile_text"):
	text = element.string.strip()
	if text:
		element.replace_with(soup.h2.text.strip())  

#gasirea discountului pe emag(text)
spandata = soup.findAll(class_='font-size-base')
for span in spandata:
	discount = span.text.strip()
	break
#gasirea clasei in site si modificare(text)
for element in potato.findAll(class_="emag_mobile_disc"):
	text = element.string.strip()
	if text:
		element.string.replace_with(discount)

#deschidere pagina emag
link='https://www.emag.ro/label/televizoare/Lichidari-de-stoc%3A-Televizoare/c'
page = urllib2.urlopen(link)
soup = BeautifulSoup(page, 'lxml')

#gasirea imaginii din emag
divdata = soup.findAll('div',{'class':'thumbnail-wrapper'})
for div in divdata:
	sursa = div.img['src']
	break
#Gasirea clasei cu numele emag si modificarea continutului(src imagine)
imgs = potato.findAll(class_= 'emag_tv')
for element in imgs:
	element['src'] = sursa 

#Gasirea clasei cu numele emag si modificarea continutului(text)
for element in potato.find(class_="emag_tv_text"):
	text = element.string.strip()
	if text:
		element.replace_with(soup.h2.text.strip())  

#gasirea discountului pe emag(text)
spandata = soup.findAll(class_='font-size-base')
for span in spandata:
	discount = span.text.strip()
	break
#gasirea clasei in site si modificare(text)
for element in potato.findAll(class_="emag_tv_disc"):
	text = element.string.strip()
	if text:
		element.string.replace_with(discount)

#deschidere pagina emag
link='https://www.emag.ro/label/Lichidari-de-stoc:-Laptopuri-&-Gaming'
page = urllib2.urlopen(link)
soup = BeautifulSoup(page, 'lxml')

divdata = soup.findAll('div',{'class':'thumbnail-wrapper'})
for div in divdata:
	sursa = div.img['src']
	break

#Gasirea clasei cu numele emag si modificarea continutului(src imagine)
imgs = potato.findAll(class_= 'emag_laptop')
for element in imgs:
	element['src'] = sursa   

#Gasirea clasei cu numele emag si modificarea continutului(text)
for element in potato.find(class_='emag_laptop_text'):
	text = element.string.strip()
	if text:
		element.replace_with(soup.h2.text.strip())  

#gasirea discountului pe emag(text)
spandata = soup.findAll(class_='font-size-base')
for span in spandata:
	discount = span.text.strip()
	break
#gasirea clasei in site si modificare(text)
for element in potato.findAll(class_="emag_laptop_disc"):
	text = element.string.strip()
	if text:
		element.string.replace_with(discount)

#afisare html draguta
#print potato.prettify()

#salvarea paginii html modificate
html = potato.prettify("utf-8")
with open("index.html", "wb") as file:
    file.write(html)
print("Done!")
