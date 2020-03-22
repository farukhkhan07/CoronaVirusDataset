# __author__ = "Farrukh Khan"
# __maintainer__ = "Farrukh Khan"
# __email__ = "farukhcs15@gmail.com"
# __about__ = "Image Scrapper for ML Datasets"

import requests 
import bs4 as bs  #BeautifulSoup
import urllib.request


# Input Website
url = str(input('URL: '))

print(url)

opener = urllib.request.build_opener()

opener.add_headers = [{'User-Agent' : 'Mozilla'}]
urllib.request.install_opener(opener)

raw = requests.get(url).text
soup = bs.BeautifulSoup(raw, 'html.parser')

imgs = soup.find_all('img')
links = []

for img in imgs:
  link = img.get('src')
  if 'https://' not in link:
    link = url + link
  links.append(link)


  print("Imges Detected:" + str(len(links)))


  for i in range(len(links)):
    filename = 'img{}.png'.format(i)
    urllib.request.urlretrieve(links[i], filename)
    print('Done!')
