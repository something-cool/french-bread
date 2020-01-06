# Requirements and User Stories

## Requirements

[Requirements](https://codefellows.github.io/common_curriculum/projects/SoftwareReqs)

### Vision

Device an accurate way to forecast the popularity of future anime series using sentiment analisys. We will do this by training our models on reviews of existing anime as found on crunchyroll.com, a website for viewing anime and manga comics. Using this data we will prioritize lists of popular anime themes so to guide development of new anime series pilots.

### Scope (In/Out)

Project scope is composed of two related yet distinct components:

* Successfully scrape reviews of popular anime series on crunchyroll.com

* Using that data, construct forecasting models utilizing machine learning that will lead to fresh, novel anime series not obvious using traditional means.

Out of scope will be [TODO]

### MVP

Successfully scrape reviews using python3, python modules Beautiful Soup, jupyter, numpy, against top 20 anime series on crunchyroll.com/videos/anime. They are 'My Hero Academia', 'One Piece', 'Black Clover', 'Dr. STONE', and 'BORUTO'. This constitutes 100 unique reviews per show for a total of 2000 reviews.

Build a sentiment analysis model using scraped user reviews from these shows to see if our model accurately reflects each show's popularity.

Data will be graphed using machine learning libaries in jupyter notebooks.

### Functional Requirements

* Able to scrape user reviews
* Use user reviews to build sentiment analysis model in a jupyter notebook 
* Also required are pandas, numpy, tensorflow, and matplotlib / sklearn libraries for linear and polynomial regressions.

### Non-Functional Requirements

* Computer hardware performant enough to build these models

## User Stories

### Initial User Stories

* [Example](https://codefellows.github.io/common_curriculum/projects/UserStories)
  * Title
  * User Story sentence
  * Feature Tasks
  * Acceptance Tests

* Visualize data for anime shows
  * As a user, I want a visualization of data about shows that gives insight about what makes them popular.
    * Clean data
    * Build ML models

* Scrape show reviews
  * As a user, I want to have access to reviews for each show on chrunchyroll.com
    * Scrape reviews

* Determine favorite shows on website
  * As a user, I want to see a breakdown of the top 10 shows
  * As a user, I want to see a breakdown of the 10 least favorite shows

* Determine common elements for each show
  * As a user, I want to see common elements, if any, for shows that fall within the same sentiment level

* Determine sentiment for each show
  * As a DS, I want to determine user sentiment for each show
    * Build ml model
    * Clean data

