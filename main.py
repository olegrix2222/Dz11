import requests
from bs4 import BeautifulSoup

URL = "<script id"script-holder-/aid/sinoptik/" src="//counter.ukr.net/advert/adv/sinoptik/cnt.php?data=303027343,6,208&ra…BE%25D1%2580%25D0%25BE%25D0%25B4&c=y&fr=n&tz=-180&j=n&s=1536*864&d="


res = requests.get(URL)

if res.status_code == 200:
  soup = BeautifulSoup(res.text, features="html.parser")
  info = soup.find_all("span", {"class":"a-price a-text-price a-size-medium apexPriceToPay"})
  price = info[0].getText()
  print(price)
  print(info)