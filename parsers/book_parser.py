import re
from locators.books_locators import BookLocators


class BookParser:
    Ratings = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self,parent):
        self.parent = parent


    def __repr__(self):
        return f'<Book {self.name} ,£{self.price},{self.rating}>'

    @property
    def name(self):
        locator = BookLocators.NAME_LOCATORS
        item_link = self.parent.select_one(locator)
        item_name = item_link.attrs['title']
        return item_name


    @property
    def link(self):
        locator = BookLocators.LINK_LOCATORS
        item_link = self.parent.slelct_one(locator).attrs['title']
        return item_link

    @property
    def price(self):
        locator = BookLocators.PRICE_LOCATORS
        item_price = self.parent.select_one(locator).string
        matcher = re.match('£([0-9]+.[0-9]+)', item_price)
        return (matcher.group(1))

    @property
    def rating(self):
        locator = BookLocators.RATING_LOCATORS
        star_rating_tag = self.parent.select_one(locator)
        classes = star_rating_tag.attrs['class']
        rating_classes = [r for r in classes if r != 'star-rating']
        rating_number = BookParser.Ratings.get(rating_classes[0])
        return rating_number
