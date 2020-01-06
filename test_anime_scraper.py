from anime_scraper import append_page_number_to_url

from url_list import sample_urls

def test_append_page_number():
  actual = append_page_number_to_url(sample_urls)
  expected = ['https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page1', 'https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page2', 'https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page3', 'https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page4', 'https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page5', 'https://www.crunchyroll.com/one-piece/reviews/helpful/page1', 'https://www.crunchyroll.com/one-piece/reviews/helpful/page2', 'https://www.crunchyroll.com/one-piece/reviews/helpful/page3', 'https://www.crunchyroll.com/one-piece/reviews/helpful/page4', 'https://www.crunchyroll.com/one-piece/reviews/helpful/page5']
  assert actual == expected

def test_append_page_number_with_page():
  actual = append_page_number_to_url(sample_urls, 3)
  expected = ['https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page1', 'https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page2', 'https://www.crunchyroll.com/one-piece/reviews/helpful/page1', 'https://www.crunchyroll.com/one-piece/reviews/helpful/page2']
  assert actual == expected