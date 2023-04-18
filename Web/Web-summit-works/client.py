from selenium import webdriver
import time
import base64

url='http://127.0.0.1:5000/welcome'
flag = base64.b64encode(b'summitCTF{x$$_iS_b@D_4_bUs1NeSs}')
print(flag.decode())
while True:
    browser = webdriver.Firefox()
    try:
        browser.get(url)
        browser.add_cookie({'name': 'flag', 'value': flag.decode()})
        browser.get(url)
        time.sleep(6)
        browser.close()
    except Exception as e:
        print(e)
        browser.close()
        continue
