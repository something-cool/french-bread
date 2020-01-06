from anime_scraper import append_page_number_to_url

from url_dict import shows_testing

def test_append_page_number():
  append_page_number_to_url(shows_testing)
  expected_my_hero = ['https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page1', 'https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page2', 'https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page3', 'https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page4', 'https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page5']
  
  expected_one_piece = ['https://www.crunchyroll.com/one-piece/reviews/helpful/page1', 'https://www.crunchyroll.com/one-piece/reviews/helpful/page2', 'https://www.crunchyroll.com/one-piece/reviews/helpful/page3', 'https://www.crunchyroll.com/one-piece/reviews/helpful/page4', 'https://www.crunchyroll.com/one-piece/reviews/helpful/page5']

  assert shows_testing['https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page'][1] == expected_my_hero
  assert shows_testing['https://www.crunchyroll.com/one-piece/reviews/helpful/page'][1] == expected_one_piece

# def test_append_page_number_with_page():
#   append_page_number_to_url(shows_testing, 3)
  
#   expected_my_hero = ['https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page1', 'https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page2']
#   expected_one_piece = ['https://www.crunchyroll.com/one-piece/reviews/helpful/page1', 'https://www.crunchyroll.com/one-piece/reviews/helpful/page2']
#   assert shows_testing['https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page'][1] == expected_my_hero
#   assert shows_testing['https://www.crunchyroll.com/one-piece/reviews/helpful/page'][1] == expected_one_piece