from anime_scraper import append_page_number_to_url, get_ratings, get_reviews
import pytest


my_hero_list = ['https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page1','https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page2', 'https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page3','https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page4','https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page5','https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page6','https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page7','https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page8','https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page9', 'https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page10']

one_piece_list = ['https://www.crunchyroll.com/one-piece/reviews/helpful/page1','https://www.crunchyroll.com/one-piece/reviews/helpful/page2', 'https://www.crunchyroll.com/one-piece/reviews/helpful/page3','https://www.crunchyroll.com/one-piece/reviews/helpful/page4','https://www.crunchyroll.com/one-piece/reviews/helpful/page5','https://www.crunchyroll.com/one-piece/reviews/helpful/page6','https://www.crunchyroll.com/one-piece/reviews/helpful/page7','https://www.crunchyroll.com/one-piece/reviews/helpful/page8','https://www.crunchyroll.com/one-piece/reviews/helpful/page9', 'https://www.crunchyroll.com/one-piece/reviews/helpful/page10']

def test_append_page_number(anime_list):
  append_page_number_to_url(anime_list)

  assert anime_list['https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page']['url_list'] == my_hero_list
  assert anime_list['https://www.crunchyroll.com/one-piece/reviews/helpful/page']['url_list'] == one_piece_list

def test_append_page_number_with_page(anime_list):
  append_page_number_to_url(anime_list, 3)
  
  expected_my_hero = ['https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page1', 'https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page2']
  expected_one_piece = ['https://www.crunchyroll.com/one-piece/reviews/helpful/page1', 'https://www.crunchyroll.com/one-piece/reviews/helpful/page2']

  assert anime_list['https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page']['url_list'] == expected_my_hero
  assert anime_list['https://www.crunchyroll.com/one-piece/reviews/helpful/page']['url_list'] == expected_one_piece

def test_get_reviews(anime_list):
  append_page_number_to_url(anime_list, 2)
  get_reviews(anime_list)

  assert type(anime_list['https://www.crunchyroll.com/one-piece/reviews/helpful/page']['reviews'][0]) == str
  assert type(anime_list['https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page']['reviews'][0]) == str

def test_get_ratings(anime_list):
  append_page_number_to_url(anime_list, 2)
  get_ratings(anime_list)

  assert type(anime_list['https://www.crunchyroll.com/one-piece/reviews/helpful/page']['ratings'][0]) == str
  assert type(anime_list['https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page']['ratings'][0]) == str


@pytest.fixture
def anime_list():
  shows_testing = {
      'https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page': {
        'url_list' : [],
        'reviews' : [],
        'ratings' : [],
      },
      'https://www.crunchyroll.com/one-piece/reviews/helpful/page': {
        'url_list' : [],
        'reviews' : [],
        'ratings' : [],
      },

    }
  return shows_testing

