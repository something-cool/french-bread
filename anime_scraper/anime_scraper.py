from bs4 import BeautifulSoup
from url_dict import shows, shows_testing
import json
import csv
import requests
import re
import time


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
    page_number = page_number or int(input('How many pages of data would you like?'))
    print('generating URLs...')
    for link in url_dict:
        for i in range(1, page_number):
            new_url = link + str(i)
            url_dict[link]['url_list'].append(new_url)
    print('success')
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
    print('gathering reviews...grab a beer, this may take a moment')
    for key in anime_dict:
        for url in anime_dict[key]['url_list']:
            time.sleep(0.15)
            markup = requests.get(url).text
            soup = BeautifulSoup(markup, 'html.parser')
            reviews = soup.find_all('div', {'class': 'more'})
            for review in reviews:
                anime_dict[key]['reviews'].append(review.text.replace(
                    "\t", "").replace("\r", "").replace('\n', '').strip())
    print('success')
    return anime_dict


def get_ratings(anime_dict):
    '''
    This function takes in a formatted dictionary
    Similar to the above function, it iterates
    over the url list but instead grabs the ratings,
    which should be a string number between 1 and 5
    '''
    print('gathering ratings...')
    for key in anime_dict:
        for url in anime_dict[key]['url_list']:
            time.sleep(0.2)
            markup = requests.get(url).text
            soup = BeautifulSoup(markup, 'html.parser')
            ratings = soup.find_all(class_='rating-widget-static-large')
            for rating in ratings:
                anime_dict[key]['ratings'].append(rating['content']) #Content is an attribute of the ratings class on crunchy roll

    print('success')            
    return anime_dict

def get_tags(anime_dict):
  print('gathering tags...')
  for key in anime_dict:
      for url in anime_dict[key]['url_list']:
          time.sleep(0.1)
          markup = requests.get(url).text
          soup = BeautifulSoup(markup, 'html.parser')
          tags = soup.find_all(href= re.compile('genre'))
          for tag in tags:
            anime_dict[key]['tags'].append(tag.text)
          break
          
  print('success')              
  return anime_dict  

def save_to_csv(anime_dict):

    '''
    This function takes in a formatted dictionary
    and writes a new csv file from its data.
    The data we need is nested so we have to iterate 
    a couple levels deep to populate the rows
    I use the enumerate method to be able to
    append reviews and ratings to the same row in one pass
    The initial row is for the column headers
    '''
    csv_file = input('All data retrieved. Enter a file name for your csv:') +'.csv'
    # csv_file = 'even_more_anime_reviews.csv'
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['show_title', 'review', 'rating', 'tags'])
            for key in anime_dict:
                for _ in anime_dict[key]:
                    reviews = anime_dict[key]['reviews']
                    for i, review in enumerate(reviews):
                        show_titles = key.replace(
                            'https://www.crunchyroll.com/', "").replace('/reviews/helpful/page', "")
                        rating = anime_dict[key]['ratings'][i]
                        tags = anime_dict[key]['tags']
                        writer.writerow([show_titles, review, rating, tags])
                    break
        print(f'successfully created {csv_file}')
    except IOError:
        print('I/O error')


def order_66(anime_dict):
    '''
    This function calls all the helper functions to produce
    the filled out csv
    '''
    pages = append_page_number_to_url(anime_dict)
    reviews = get_reviews(pages)
    ratings = get_ratings(reviews)
    tags = get_tags(ratings)
    save_to_csv(tags)


if __name__ == "__main__":
    order_66(shows_testing)

