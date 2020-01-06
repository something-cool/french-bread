from bs4 import BeautifulSoup
from url_list import urls
import re

import requests


def append_page_number_to_url(url_dict, page_number=None):
  page_number = page_number or 6

  for link in url_dict:
    for i in range(1, page_number):
      new_url = link + link.join(str(i))
      url_dict[link][1].append(new_url)
  return url_dict

def get_reviews(url_dict):
  
  for url in url_dict:
    markup = requests.get(url).text
    soup = BeautifulSoup(markup, 'html.parser')
    review = soup.find_all(class_='trunc')
    for words in review:
      url_dict[url][0].append(words.text)
  return url_dict


if __name__ == "__main__":
  shows = {
  'https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page': ([], []),
  'https://www.crunchyroll.com/my-hero-academia': ([], [])
}
  append_page_number_to_url(shows)
  reviews = get_reviews(shows)
  print(reviews)
 
