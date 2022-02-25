import pytest

from Config.config import Data
from Pages.CheckOutPage import CheckOutPage
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_Login(BaseTest):
    def test_register1(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.register(Data.userEmail1, Data.firstName1, Data.lastName1,
                                 Data.password1, Data.date1,Data.month1, Data.year1,
                                 Data.companyName1, Data.address1,Data.addressLine2_1,
                                 Data.city1, Data.state1, Data.zipCode1, Data.country1,
                                 Data.info1,Data.mobile1, Data.add_ref1)

        self.login_page.logout()

    def test_register2(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.register(Data.userEmail2, Data.firstName2, Data.lastName2,
                                 Data.password2, Data.date2,Data.month2, Data.year2,
                                 Data.companyName2, Data.address2,Data.addressLine2_2,
                                 Data.city2, Data.state2, Data.zipCode2, Data.country2,
                                 Data.info2,Data.mobile2, Data.add_ref2)

        self.login_page.logout()

    def test_Purchase_user1(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.log_in(Data.userEmail1, Data.password1)
        self.check_page = CheckOutPage(self.driver)
        self.check_page.add_dress_to_cart()
        self.check_page.add_shirts_to_cart()
        self.check_page.checkOut()
        self.login_page.logout()

    def test_Purchase_user2(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.log_in(Data.userEmail2, Data.password2)
        self.check_page = CheckOutPage(self.driver)
        self.check_page.add_dress_to_cart()
        self.check_page.add_shirts_to_cart()
        self.check_page.checkOut()
        self.login_page.logout()


