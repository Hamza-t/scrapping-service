# scraper.py
from facebook_scraper import get_posts


class Scraper():

    def scrapers(self, page_name: str):
        listposts = []
        for post in get_posts(page_name, pages=3):

            listposts.append(post)
        return listposts
