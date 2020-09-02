from locator import Locator

class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.welcome_link_id = Locator.welcome_link_id
        self.logout_link_linkText = Locator.logout_link_linkText

    def click_welcome(self):
        self.driver.find_element_by_id(self.welcome_link_id).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_link_linkText).click()