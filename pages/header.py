from playwright.sync_api import Page


class Header:
    def __init__(self, page: Page):
        self.page = page

    def element(self, selector):
        return self.page.locator(selector)

    # селекторы
    _about_link_selector = ".mr-1"
    _contacts_link_selector = "a[href='/about/contacts/']"
    _payment_link_selector = "a[href='/about/payment/']"
    _deliver_link_selector = ".sub-deliver"
    _login_button_selector = ".authButton_buttonText__wGjvY"

    # локаторы
    def about_link_locator(self):
        return self.element(self._about_link_selector)

    def contacts_link_locator(self):
        return self.element(self._contacts_link_selector)

    def payment_link_locator(self):
        return self.element(self._payment_link_selector)

    def deliver_link_locator(self):
        return self.element(self._deliver_link_selector)

    def login_button_locator(self):
        return self.element(self._login_button_selector)

    # методы
    def click_about(self):
        self.about_link_locator().click()

    def click_contacts(self):
        self.contacts_link_locator().click()

    def click_payment(self):
        self.payment_link_locator().click()

    def click_deliver(self):
        self.deliver_link_locator().click()

    def click_login(self):
        self.login_button_locator().click()
