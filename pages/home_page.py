import time

from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage


class HomePage(BasePage):

    title = ""

    def click_brands(self, selector):
        """
        Click brands
        """
        # self.wait_for_element(selector)
        time.sleep(3)
        self.driver.find_element_by_css_selector(selector).click()
        self.wait_for_ajax()

    def verify_navigation(self, selector):
        titles_list = []
        self.driver.find_element_by_css_selector(selector).click()
        page_title = self.driver.title
        titles_list.append(page_title)
        return titles_list

    def verify_navigation_bar(self, list1, list2):
        """
              Verify that nav bar items redirect to correct page
        """
        for x in list1:
            for y in list2:
                self.driver.find_element_by_css_selector(x).click()
                print(self.driver.title)
                y = self.driver.title

    def verify_nav_bar(self, selectors_list):
        """
       Verify that nav bar items are redirected to correct page
       """
        page_title_list = []
        for x in selectors_list:
            self.driver.find_element_by_css_selector(x).click()
            page_title_list.append(self.driver.title)
        print(page_title_list)
        return page_title_list

    def verify_item_in_cart(self, page_selector, item_selector, to_cart, to_checkout):
        """
              Verify that selected item is in the cart
        """

        self.driver.find_element_by_css_selector(page_selector).click()
        self.wait_for_element(item_selector)
        self.driver.find_element_by_css_selector(item_selector).click()
        # self.wait_for_element(to_cart)
        time.sleep(5)
        element_list = self.driver.find_elements_by_css_selector(to_cart)
        print(len(element_list))
        element_one = element_list[1]

        # # first = self.driver.find_elements_by_css_selector(to_cart)
        action = ActionChains(self.driver)
        action.move_to_element(element_one).click().perform()
        # self.wait_for_element(to_checkout)
        # self.driver.find_element_by_css_selector(to_checkout).click()
