from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class LastFmResultsPage(BasePage):
   ## ARTIST_TAB = (By.CLASS_NAME, "secondary-nav-item--artist")
    ## FIRST_RESULTS = (By.CLASS_NAME, "js-link-block")



    def open_artist_page(self,artist_name):
        ARTIST_RESULT = (By.CSS_SELECTOR,f"[title='Bruno Mars']")
        self.click(ARTIST_RESULT)
