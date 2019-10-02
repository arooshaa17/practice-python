import unittest

from selenium import webdriver
from constants import BASE_URL, HOME_PAGE_TITLE, EXPECTED_PAGE_TITLE_LIST, ADD_TO_CART, SELECT_PARFUM, \
    EXPECTED_ITEM_VALUE, MOVE_TO_CART, \
    PAGE_SELECTORS_LIST, SELECT_PARFUM_ITEM
from pages.home_page import HomePage


class NavigationTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='C:\Program Files\geckodriver\geckodriver')
        self.driver.get(BASE_URL)
        self.home_page = HomePage(self.driver)

    def test_valid_home_page(self):
        self.assertTrue('Not on the Home page', self.home_page.is_browser_on_page(HOME_PAGE_TITLE))
        actual_page_title_list = self.home_page.verify_nav_bar(PAGE_SELECTORS_LIST)
        self.assertEqual(actual_page_title_list, EXPECTED_PAGE_TITLE_LIST)

    def test_items_in_cart(self):
        actual_item_value = self.home_page.verify_item_in_cart(SELECT_PARFUM, SELECT_PARFUM_ITEM, ADD_TO_CART, MOVE_TO_CART)
        self.assertEqual(actual_item_value, EXPECTED_ITEM_VALUE)

    def tearDown(self):
        self.driver.close()
