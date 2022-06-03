from seleniumwire import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from constant import pre_const


def get_real_headers():
    try:
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--disable-gpu")
        options = {
            'verify_ssl': False
        }
        driver = webdriver.Chrome(options=chrome_options,
                                  executable_path=pre_const.DRIVER_PATH,
                                  seleniumwire_options=options)
        driver.get(pre_const.INIT_URL)
    except Exception as e:
        raise e
    try:
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[1]')))
        driver.find_element_by_xpath('//*[@id="qc-cmp2-ui"]/div[2]/div/button[1]').click()
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="portDetailsHeader"]/div/div[1]/div/div[2]/h1')))
        name_div = driver.find_element_by_xpath('//*[@id="portDetailsHeader"]/div/div[1]/div/div[2]/h1')
        js = "var q=document.documentElement.scrollTop=100000"
        driver.execute_script(js)
        request = driver.wait_for_request('recent_arrivals$')
        return request.headers
    except Exception as e:
        raise e
    finally:
        driver.close()


if __name__ == '__main__':
    print(get_real_headers())
