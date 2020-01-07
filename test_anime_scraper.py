from anime_scraper import append_page_number_to_url
import pytest
@pytest.fixture
def my_list():
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


def test_append_page_number(my_list):
  append_page_number_to_url(my_list)
  expected_my_hero = ['https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page1', 'https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page2', 'https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page3', 'https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page4', 'https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page5']
  
  expected_one_piece = ['https://www.crunchyroll.com/one-piece/reviews/helpful/page1', 'https://www.crunchyroll.com/one-piece/reviews/helpful/page2', 'https://www.crunchyroll.com/one-piece/reviews/helpful/page3', 'https://www.crunchyroll.com/one-piece/reviews/helpful/page4', 'https://www.crunchyroll.com/one-piece/reviews/helpful/page5']

  assert my_list['https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page']['url_list'] == expected_my_hero
  assert my_list['https://www.crunchyroll.com/one-piece/reviews/helpful/page']['url_list'] == expected_one_piece

def test_append_page_number_with_page(my_list):
  append_page_number_to_url(my_list, 3)
  
  expected_my_hero = ['https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page1', 'https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page2']
  expected_one_piece = ['https://www.crunchyroll.com/one-piece/reviews/helpful/page1', 'https://www.crunchyroll.com/one-piece/reviews/helpful/page2']
  assert my_list['https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page']['url_list'] == expected_my_hero
  assert my_list['https://www.crunchyroll.com/one-piece/reviews/helpful/page']['url_list'] == expected_one_piece