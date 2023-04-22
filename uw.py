import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
# manages imports


STEPS = [
    '//*[@id="input-area"]/div/div/div[3]/div/button',
    '//*[@id="input-area"]/div/div/div[3]/div/button',
    '//*[@id="wrapper-car-choice-table-column2-render-area"]/div/div/img',
    '//*[@id="input-area"]/div/div/div[4]/div/button'
]
# XPATH click steps


WAIT_TIME = 5
# maximum element load wait time


DELAY = 1
# guarunteed delay between clicks


MAIN_PAGE = "https://mpo.pch.com/path/OBMarTV23CtlReg?tid=bf204b1e-a30d-4160-9a46-1bbce69671b1"
# main (starting) page to load each time


def init():
    """
    Creates driver and opens site.
    
    :return: driver
    :rtype: webdriver
    """

    driver = uc.Chrome(use_subprocess=True)
    driver.get(MAIN_PAGE)
    
    input("Login, then click enter to continue...")
    
    return driver
    
    
def main():
    """
    Run commands.
    """
    
    driver = init()
    
    while True:
        try:
            driver.get(MAIN_PAGE)
            # loads page
        
            for xpath in STEPS:
                element = WebDriverWait(driver, WAIT_TIME).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                )
                driver.find_element(by=By.XPATH, value=xpath).click()
                # clicks each element in order
                
                sleep(DELAY)
                
        except Exception as e:
            print(e)
    
 
if __name__ == "__main__":
    main()
