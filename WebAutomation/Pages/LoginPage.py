from Config.config import Data
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    """The locators we have to use for this class and its functions"""
    signin_nav = (By.XPATH,'//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
    email_reg = (By.XPATH,'//*[@id="email_create"]')
    reg_button = (By.CSS_SELECTOR, '#SubmitCreate')
    gender_reg = (By.CSS_SELECTOR, '#id_gender1')
    firstName_reg = (By.XPATH, '//*[@id="customer_firstname"]')
    lastName_reg = (By.XPATH, '//*[@id="customer_lastname"]')
    pass_reg = (By.XPATH, '//*[@id="passwd"]')
    date_reg = (By.XPATH, '//*[@id="days"]')
    month_reg = (By.XPATH, '//*[@id="months"]')
    year_reg = (By.XPATH, '//*[@id="years"]')
    checkbox1_reg = (By.XPATH, '//*[@id="newsletter"]')
    checkbox2_reg = (By.XPATH, '//*[@id="optin"]')
    company_reg = (By.XPATH, '//*[@id="company"]')
    address_reg = (By.XPATH, '//*[@id="address1"]')
    addressLine2_reg = (By.XPATH, '//*[@id="address2"]')
    city_reg = (By.XPATH, '//*[@id="city"]')
    state_reg = (By.XPATH, '//*[@id="id_state"]')
    zip_reg = (By.XPATH, '//*[@id="postcode"]')
    country_reg = (By.XPATH, '//*[@id="id_country"]')
    additional_reg = (By.XPATH, '//*[@id="other"]')
    mobile_reg = (By.XPATH, '//*[@id="phone_mobile"]')
    reference_address = (By.XPATH, '//*[@id="alias"]')
    register_account = (By.CSS_SELECTOR, '#submitAccount')

    email_log = (By.XPATH,'//*[@id="email"]')
    pass_log = (By.XPATH,'//*[@id="passwd"]')
    log_button = (By.CSS_SELECTOR,'#SubmitLogin > span')
    sign_out = (By.CSS_SELECTOR,'#header > div.nav > div > div > nav > div:nth-child(2) > a')

    """initializing the web driver and get into the web page"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Data.base_url)

    """This method helps to register account with proper details
        this method covers all the required field"""
    def register(self, email,fn, ln, pass_word, date,month,
                 year, company,address, address2, city,
                 state, zip, country,info, mobile, reference_add):

        self.do_click(self.signin_nav)
        self.do_send_keys(self.email_reg, email)
        self.do_click(self.reg_button)
        self.do_click(self.gender_reg)
        self.do_send_keys(self.firstName_reg, fn)
        self.do_send_keys(self.lastName_reg, ln)
        self.do_send_keys(self.pass_reg, pass_word)
        self.do_select(self.date_reg, date)
        self.do_select(self.month_reg, month)
        self.do_select(self.year_reg, year)
        self.do_click(self.checkbox1_reg)
        self.do_click(self.checkbox2_reg)
        self.do_send_keys(self.country_reg, company)
        self.do_send_keys(self.address_reg, address)
        self.do_send_keys(self.addressLine2_reg, address2)
        self.do_send_keys(self.city_reg, city)
        self.do_send_keys(self.state_reg, state)
        self.do_send_keys(self.zip_reg, zip)
        self.do_send_keys(self.country_reg, country)
        self.do_send_keys(self.additional_reg, info)
        self.do_send_keys(self.mobile_reg, mobile)
        self.do_send_keys(self.reference_address, reference_add)
        self.do_click(self.register_account)

    """Login with email and password"""
    def log_in(self, email, password):
        self.do_click(self.signin_nav)
        self.do_send_keys(self.email_log, email)
        self.do_send_keys(self.pass_log, password)
        self.do_click(self.log_button)

    """Logout from the account"""
    def logout(self):
        self.do_click(self.sign_out)















