from Config.config import Data
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class CheckOutPage(BasePage):

    """Locators we have to use in this class"""

    """locators to add items from 'Casual Dress'"""
    dress = (By.CSS_SELECTOR, '#block_top_menu > ul > li:nth-child(2) > a')
    casual_dress = (By.CSS_SELECTOR, '#block_top_menu > ul > li:nth-child(2) > ul > li:nth-child(1) > a')
    dress_item = (By.CSS_SELECTOR, '#center_column > ul > li > div > div.left-block > div > a.product_img_link > img')
    add_to_cart_dress = (By.CSS_SELECTOR, '#center_column > ul > li > div > div.right-block > div.button-container > a.button.ajax_add_to_cart_button.btn.btn-default > span')
    cross_popup = (By.CSS_SELECTOR, "#layer_cart > div.clearfix > div.layer_cart_product.col-xs-12.col-md-6 > span")

    """locators to add items from 'T-shirts'"""
    tshirt = (By.XPATH, '//*[@id="block_top_menu"]/ul/li[3]/a')
    blue_filter = (By.CSS_SELECTOR,'#layered_id_attribute_group_14')
    tshirt_item = (By.CSS_SELECTOR, '#center_column > ul > li > div > div.left-block > div > a.product_img_link > img')
    check_blue = (By.CSS_SELECTOR, '#color_2')
    add_to_cart_shirt = (By.CSS_SELECTOR,'#add_to_cart > button')

    """Finally the locators we have to use for checkout and payment"""
    cart = (By.CSS_SELECTOR, '#header > div:nth-child(3) > div > div > div:nth-child(3) > div > a')
    checkout = (By.CSS_SELECTOR, '#button_order_cart > span')
    proceed1 =(By.CSS_SELECTOR,'#center_column > p.cart_navigation.clearfix > a.button.btn.btn-default.standard-checkout.button-medium > span')
    proceed2 = (By.CSS_SELECTOR,'#center_column > form > p > button > span')
    proceed3 = (By.XPATH,'//*[@id="cgv"]')
    proceed4 = (By.CSS_SELECTOR,'#form > p > button > span')
    pay_by_check =(By.CSS_SELECTOR,'#HOOK_PAYMENT > div:nth-child(2) > div > p > a')
    confirm = (By.CSS_SELECTOR,'#cart_navigation > button > span')

    """initializing the web driver and get into the web page"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Data.base_url)

    """This method helps to choose casual dresses into cart"""
    def add_dress_to_cart(self):
        self.do_hover(self.dress, self.casual_dress)
        self.do_hover(self.dress_item, self.add_to_cart_dress)
        self.do_clickable(self.cross_popup)

    """This method helps to choose T-shirts into cart"""
    def add_shirts_to_cart(self):
        self.do_click(self.tshirt)
        self.do_click(self.blue_filter)
        self.do_hover(self.tshirt_item, self.check_blue)
        self.do_click(self.add_to_cart_shirt)
        self.do_clickable(self.cross_popup)

    """checkout and payment"""
    def checkOut(self):
        self.do_hover(self.cart, self.checkout)
        self.do_click(self.proceed1)
        self.do_click(self.proceed2)
        self.do_click(self.proceed3)
        self.do_click(self.proceed4)
        self.do_click(self.pay_by_check)
        self.do_click(self.confirm)













