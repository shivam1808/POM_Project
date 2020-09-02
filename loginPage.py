from locator import Locator

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_id = Locator.username_textbox_id
        self.password_textbox_id = Locator.password_textbox_id
        self.login_button_id = Locator.login_button_id
        self.invalidUsername_message_id = 'spanMessage'

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.login_button_id).click()

    def check_invalid(self):
        msg = self.driver.find_element_by_id(self.invalidUsername_message_id).text
        return msg