import time

from pages.base_page import BasePage


class HomePage(BasePage):

    title = ""

    def click_brands(self, selector):
        """
        Click brands
        """
        self.wait_for_element(selector)
        self.driver.find_element_by_css_selector(selector).click()
        self.wait_for_ajax()

    def verify_nav_bar(self, selectors_list):
        """
       Verify that nav bar items are redirected to correct page
       """
        page_title_list = []
        for x in selectors_list:
            self.driver.find_element_by_css_selector(x).click()
            page_title_list.append(self.driver.title)
        return page_title_list

    def verify_item_in_cart(self, perfume_page_selector, item_selector, add_to_cart, to_checkout):
        """
        Verify that selected item is in the cart
        """
        self.driver.find_element_by_css_selector(perfume_page_selector).click()
        self.wait_for_element(item_selector)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element_by_css_selector(item_selector))
        self.wait_for_element(add_to_cart)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element_by_css_selector(add_to_cart))
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element_by_css_selector(to_checkout))
        cart_item_value = self.driver.find_element_by_css_selector(item_selector).get_attribute("href")
        return cart_item_value
