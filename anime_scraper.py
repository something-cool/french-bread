from bs4 import BeautifulSoup
from url_dict import shows, shows_testing
import pprint
pp = pprint.PrettyPrinter()

import requests

def append_page_number_to_url(url_dict, page_number=None):
  page_number = page_number or 6

  for link in url_dict:
    for i in range(1, page_number):
      new_url = link + link.join(str(i))
      url_dict[link]['url_list'].append(new_url)
  return url_dict

def get_reviews(show_dict):
  
  for key in show_dict:
    for url in show_dict[key]['url_list']:
      markup = requests.get(url).text
      soup = BeautifulSoup(markup, 'html.parser')
      reviews = soup.find_all('div', {'class':'trunc'}, {'class': 'more'})
      for review in reviews:
        show_dict[key]['reviews'].append(review.text)

  return show_dict

def get_ratings(show_dict):
  for key in show_dict:
    for url in show_dict[key]['url_list']:
      markup = requests.get(url).text
      soup = BeautifulSoup(markup, 'html.parser')
      ratings = soup.find_all(class_='rating-widget-static-large')
      for rating in ratings:
        show_dict[key]['ratings'].append(rating['content'])
  return show_dict

def save_to_dictionary():
  pages = append_page_number_to_url(shows_testing, 3)
  reviews = get_reviews(pages)
  ratings = get_ratings(reviews)
  print(ratings)
  return ratings

if __name__ == "__main__":
  save_to_dictionary()


  # shows = {
  # 'https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page': ([], []),
  # 'https://www.crunchyroll.com/my-hero-academia': ([], [])
  # }
  # append_page_number_to_url(shows)
  # reviews = get_reviews(shows)
  # print(reviews)
 
