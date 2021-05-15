# Auto Almost Everything
# Youtube Channel https://www.youtube.com/c/AutoAlmostEverything
# Please read README.md carefully before use

import random, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Proxy
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from Modules import update, notification, wordlist

app = 'PreSearch'
wl = wordlist.get()

# Browser config
chromedriver_path = '.\\chromedriver.exe'  # <-- Change to your Chrome WebDriver path, replace "\" with "\\".
opts = Options()
opts.binary_location = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'  # <-- Change to your Chromium browser path, replace "\" with "\\".
isNetBox = True
if opts.binary_location.split('\\')[-1].split('.')[0].lower() != "netboxbrowser":
    isNetBox = False
opts.add_experimental_option('excludeSwitches', ['enable-automation'])
opts.add_experimental_option('useAutomationExtension', False)
opts.add_experimental_option('prefs', {'download_restrictions': 3})
# opts.headless = True  # <-- Remove comment this line if you want to hide browser.
cap = DesiredCapabilities.CHROME.copy()
cap['platform'] = 'WINDOWS'
cap['version'] = '10'
proxy = 'YourProxy'  # <-- To use proxy, replace 'YourProxy' by proxy string, ex: 18.222.190.66:81
if proxy != '' and proxy != 'YourProxy':
    proxies = Proxy({
        'httpProxy': proxy,
        'ftpProxy': proxy,
        'sslProxy': proxy,
        'proxyType': 'MANUAL',
    })
    proxies.add_to_capabilities(cap)
    opts.add_argument('--ignore-ssl-errors=yes')
    opts.add_argument('--ignore-certificate-errors')

if isNetBox:
    netbox_login_path = 'https://account.netbox.global/'
    netbox_cookies = [
        {
            'name': 'token',
            # Replace by your token -->
            'value': 'YourToken',
            # <-- Replace by your token
            'domain': '.netbox.global',
            'path': '/',
        },
    ]
    netbox_wallet_path = 'chrome://wallet'
    # Replace by your wallet code -->
    netbox_wallet_code = 'YourWalletCode'
    # <-- Replace by your wallet code


# Search 30 times
def PreSearch():
    search_path = 'https://engine.presearch.org'
    # Account config
    presearch_cookies = [
        {
            # Replace by your remember name -->
            'name': 'remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d',
            # <-- Replace by your remember name
            # Replace by your remember token -->
            'value': 'YourRememberToken',
            # <-- Replace by your remember token
            'domain': '.presearch.org',
            'path': '/',
        },
        {
            'name': 'token',
            # Replace by your token -->
            'value': 'YourToken',
            # <-- Replace by your token
            'domain': '.presearch.org',
            'path': '/',
        },
    ]

    presearch_max_count = 30
    while True:
        browser = webdriver.Chrome(desired_capabilities=cap, options=opts, executable_path=chromedriver_path)
        browser.set_page_load_timeout(60)
        try:
            if isNetBox:
                browser.get(netbox_login_path)
                time.sleep(1)
                for cookie in netbox_cookies:
                    browser.add_cookie(cookie)
                browser.get(netbox_login_path)
                time.sleep(1)
                browser.get(netbox_wallet_path)
                time.sleep(1)
                try:
                    browser.find_element_by_xpath("//textarea[@id='restore__mnemonic']").send_keys(netbox_wallet_code)
                    browser.find_element_by_xpath("//button[@id='restore__control']").click()
                    time.sleep(30)
                except:
                    pass

            browser.get(search_path)
            time.sleep(1)
            for cookie in presearch_cookies:
                browser.add_cookie(cookie)
            browser.get(search_path)
            time.sleep(1)
            count = 0
            while True:
                browser.get(search_path)
                time.sleep(random.randint(3, 12))
                q = wordlist.gen(wl)
                try:
                    browser.find_element_by_xpath("//input[@placeholder='Search']").send_keys(q, Keys.ENTER)
                    time.sleep(3)
                    if 'Oops, something went wrong with your search' not in browser.page_source and 'The request could not be satisfied' not in browser.title:
                        currentPage = 1
                        for i in range(random.randint(1, 7)):
                            try:
                                if (random.randint(1, 10)) <= 2:
                                    currentUrl = str(browser.current_url)
                                    if '&page=' in currentUrl:
                                        browser.get(currentUrl.replace('&page=' + str(currentPage),
                                                                       '&page=' + str(currentPage + 1)))
                                    else:
                                        browser.get(browser.current_url + "&page=" + str(currentPage + 1))
                                    currentPage += 1
                                else:
                                    results = browser.find_elements_by_xpath(
                                        "//h3[@class='font-semibold text-lg text-primary-600 transition duration-150 hover:underline hover:opacity-70 dark:hover:opacity-60 dark:text-blue-200 dark:font-normal']")
                                    results[random.randint(0, len(results) - 1)].click()
                                    time.sleep(random.randint(3, 12))
                                    browser.back()
                                    time.sleep(random.randint(3, 12))
                            except:
                                pass
                        count += 1
                except:
                    pass
                if count > presearch_max_count * random.randint(6, 14) * 10 / 100:
                    notification.notify(app, 'Searched 30 times!')
                    break
                time.sleep(random.randint(20, 40))
        except Exception as ex:
            print('%s has exception:\n%s!' % (app, ex))
            notification.notify(app, '%s has exception:\n%s!' % (app, ex))
        finally:
            browser.quit()
        time.sleep(random.randint(1200, 2400))


if update.check():
    notification.notify(app, 'New version is released. Please download it! Thank you.')
else:
    PreSearch()
