from playwright.sync_api import Page


class Header:
    def __init__(self, page: Page):
        self.page = page

    def element(self, selector):
        return self.page.locator(selector)

    # селекторы
    _about_link_selector = ".mr-1"
    _contacts_link_selector = "a.sub-header-btn[href='/about/contacts/']"
    _payment_link_selector = "a.sub-header-btn[href='/about/payment/']"
    _deliver_link_selector = ".sub-deliver"
    _login_button_selector = ".authButton_buttonText__wGjvY"
    _logo_selector = ".navbar-brand"
    _phone_number_selector = "div[data-qa-locator='phoneNumber']"
    _telegram_selector = ".telegramm_ico"
    _max_selector = ".max_ico"
    _whatsapp_selector = ".whats_ico"

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

    def logo_locator(self):
        return self.element(self._logo_selector)

    def phone_number_locator(self):
        return self.element(self._phone_number_selector)

    def telegram_locator(self):
        return self.element(self._telegram_selector)

    def max_locator(self):
        return self.element(self._max_selector)

    def whatsapp_locator(self):
        return self.element(self._whatsapp_selector)

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
