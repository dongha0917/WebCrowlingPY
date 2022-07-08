import requests;
from bs4 import BeautifulSoup;
import math;
search = input("구글에 무엇을 검색하시겠습니까?")
grade = int(input("구글검색어 몇위까지 검색하시겠습니까?"))
to_page = grade // 10 + 1
count = 0;
f = open('google.txt', 'w');
for i in range(to_page):
  if (count == grade):
    break;
  re = requests.get("https://www.google.com/search?q=" + search + "&start=" + str(i + 1));
  soup = BeautifulSoup(re.content, 'html.parser');
  for j in range(9):
    if (count == grade):
      break;
    f.write(soup.select('h3')[j].text + ' ')
    f.write(soup.select('a:has(h3)')[j]['href'][7:] + '\n')
    count += 1;
print('성공!')
f.close()