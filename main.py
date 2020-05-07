from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.select import Select

from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException


from time import sleep
import logging
logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)

def main():
    url = 'http://www.cmc.gov.co:8080/CmcFrontEnd/consulta/index.cmc'
    options = webdriver.FirefoxOptions()
    options.add_argument('--incognito')

    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference("browser.privatebrowsing.autostart", True)

    driver = webdriver.Firefox( executable_path='./geckodriver.exe', options = options, firefox_profile = firefox_profile)
    driver.get(url)
    delay = 10
    try:
        elem = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.ID, "titulo"))
        ).click()
        logger.info('Ya abrió la página')
        # Quiero que vuelva a ejecutar el try except, para no tener que anidarlos
    except TimeoutException:
        print('La página ha demorado demasiado en cargar')
        driver.quit()

    # elem.click()
    sleep(5)
    dropdown = Select(driver.find_element_by_xpath('//select[@id="mineral"]'))
    try:
        dropdown.select_by_index(1000)
    except NoSuchElementException:
        # NoSuchElementException : :: when selenium dont found the value with these index
        logger.info('NoSuchElementException: No lo encontró')


    driver.close()



if __name__ == '__main__':
    main()
