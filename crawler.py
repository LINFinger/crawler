import json
import time

import requests
from seleniumwire import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from model import request_info
from model.request_info import RequestInfo

if __name__ == '__main__':
    try:
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--disable-gpu")
        options = {
            'verify_ssl': False  # Verify SSL certificates but beware of errors with self-signed certificates
        }
        driver = webdriver.Chrome(options=chrome_options, executable_path='service/chromedriver.exe',
                                  seleniumwire_options=options)
        driver.get('https://www.marinetraffic.com/en/ais/details/ports/1253?name=SHANGHAI&country=China')
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[1]')))
        driver.find_element_by_xpath('//*[@id="qc-cmp2-ui"]/div[2]/div/button[1]').click()
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="portDetailsHeader"]/div/div[1]/div/div[2]/h1')))
        name_div = driver.find_element_by_xpath('//*[@id="portDetailsHeader"]/div/div[1]/div/div[2]/h1')
        print(name_div.text)
        js = "var q=document.documentElement.scrollTop=100000"
        driver.execute_script(js)

        request = driver.wait_for_request('recent_arrivals$')
        driver.close()
        print(
            request.url,
            request.response.status_code,
            request.response.headers['Content-Type'],
            request.headers,
        )
        headers = request.headers
        req = RequestInfo().headers_only(request.headers)
        res = requests.get('https://www.marinetraffic.com/en/ports/1253/statistics/recent_arrivals', headers=req.headers)
        print(res.text)
    except Exception as e:
        print(e)
