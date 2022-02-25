import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Config.config import Data

"""params=['chrome', 'firefox]"""
@pytest.fixture(params=['chrome'],scope='class')
def init_driver(request):

    # request.param is helping us to overcome the redundancy of writing separate
    # code blocks for different browser

    web_driver = webdriver.Chrome(ChromeDriverManager().install())
    web_driver.maximize_window()

    request.cls.driver = web_driver
    # web_driver.implicitly_wait(10)
    yield
    web_driver.close()
