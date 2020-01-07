from bs4 import BeautifulSoup
from url_dict import shows, shows_testing
import pprint
pp = pprint.PrettyPrinter()

import requests

def append_page_number_to_url(url_dict, page_number=None):
  '''
  In a seperate file we have a dictionary with keys
  in this format: https://www.crunchyroll.com/one-piece/reviews/helpful/page
  This function appends a number at the end of the link for every
  number in a given range. The links are then appended to a list
  associated with the appropriate key.
  This allows us to grab as many links as we need while only having to 
  manually grab them once.
  '''
  page_number = page_number or 6

  for link in url_dict:
    for i in range(1, page_number):
      new_url = link + link.join(str(i))
      url_dict[link]['url_list'].append(new_url)
  return url_dict

def get_reviews(anime_dict):
  '''
  This function takes in a formatted dictionary
  It iterates through the url lists generated in the
  previous function and uses beautiful soup to scrape
  the review data. Class names were found by inspecting 
  the crunchy roll site using chrome's dev tools.
  The reviews are appended to a list in the dictionary
  and we return the modified dictionary.
  '''
  
  for key in anime_dict:
    for url in anime_dict[key]['url_list']:
      markup = requests.get(url).text
      soup = BeautifulSoup(markup, 'html.parser')
      reviews = soup.find_all('div', {'class':'trunc'}, {'class': 'more'})
      for review in reviews:
        anime_dict[key]['reviews'].append(review.text)

  return anime_dict

def get_ratings(anime_dict):
  '''
  This function takes in a formatted dictionary
  Similar to the above function, it iterates
  over the url list but instead grabs the ratings,
  which should be a string number between 1 and 5
  '''
  for key in anime_dict:
    for url in anime_dict[key]['url_list']:
      markup = requests.get(url).text
      soup = BeautifulSoup(markup, 'html.parser')
      ratings = soup.find_all(class_='rating-widget-static-large')
      for rating in ratings:
        anime_dict[key]['ratings'].append(rating['content'])
  return anime_dict

def save_to_dictionary():
  '''
  This function calls all the helper functions and returns
  a full dictionary with all lists filled out.
  It's then saved to a csv file. Ideally you just run
  this function one time to get all the data you need at once.
  '''
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
 
