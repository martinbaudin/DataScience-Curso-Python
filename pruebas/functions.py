from bs4 import BeautifulSoup
import urllib.request as urlReq

response = urlReq.urlopen('https://www.app.soyhenry.com/course-detail/25d0332d-1e89-481f-9d09-01aad5b2c50a/lecture/7c176c1e-e3de-42e6-ac78-303036f07962?lectureUrl=https://capsulasv2.soyhenry.com/scorm/475c2d53-dd21-4a80-9c28-86df6262861b/scormcontent/iframe.html&idModLecture=bc4617b1-92ac-4514-a91e-5ae701c9de72')
html = response.read()

soup = BeautifulSoup(html, 'html.parser')
text = soup.get_text()

print(text.find('Henry'))