# Auto Almost Everything
# Youtube Channel https://www.youtube.com/channel/UC4cNnZIrjAC8Q4mcnhKqPEQ
# Please read README.md carefully before use

import threading, random, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from Modules import update, notification, wordlist

app = 'PreSearch'
wl = wordlist.get()

# Multi account config
accounts = [
    {  # Account 1 -->
        'cookies': [
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
        ],
        # 'proxy': 'YourProxy',  # <-- To use proxy, remove comment this line then replace 'YourProxy' by proxy string, such as 18.222.190.66:81.
    },  # <-- Account 1
    {  # Account 2 -->
        'cookies': [
            {
                'name': 'remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d',
                'value': 'YourRememberTokenHere',
                'domain': '.presearch.org',
                'path': '/',
            },
            {
                'name': 'token',
                'value': 'YourTokenHere',
                'domain': '.presearch.org',
                'path': '/',
            },
        ],
        # 'proxy': 'YourProxy',  # <-- To use proxy, remove comment this line then replace 'YourProxy' by proxy string, such as 18.222.190.66:81.
    },  # <-- Account 2
    {  # Account 3 -->
        'cookies': [
            {
                'name': 'remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d',
                'value': 'YourRememberTokenHere',
                'domain': '.presearch.org',
                'path': '/',
            },
            {
                'name': 'token',
                'value': 'YourTokenHere',
                'domain': '.presearch.org',
                'path': '/',
            },
        ],
        # 'proxy': 'YourProxy',  # <-- To use proxy, remove comment this line then replace 'YourProxy' by proxy string, such as 18.222.190.66:81.
    },  # <-- Account 3
]

sync = True


# Search 30 times
def PreSearch(account):
    # Browser config
    chromedriver_path = '.\\chromedriver.exe'  # <-- Change to your Chrome WebDriver path, replace "\" with "\\".
    opts = Options()
    opts.binary_location = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'  # <-- Change to your Chromium browser path, replace "\" with "\\".
    opts.add_experimental_option('excludeSwitches', ['enable-automation'])
    opts.add_experimental_option('useAutomationExtension', False)
    opts.add_experimental_option('prefs', {'download_restrictions': 3})
    # opts.headless = True  # <-- Comment this line if you want to show browser.
    if 'proxy' in account and account['proxy'] != 'YourProxy':
        opts.add_argument('--proxy-server=%s' % account['proxy'])

    search_path = 'https://engine.presearch.org'
    presearch_cookies = account['cookies']

    presearch_max_count = 30
    while True:
        global sync
        if sync:
            sync = False
            browser = webdriver.Chrome(options=opts, executable_path=chromedriver_path)
            browser.set_page_load_timeout(60)
            try:
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
            sync = True
            time.sleep(random.randint(1200, 2400))
        else:
            time.sleep(1)


if update.check():
    notification.notify(app, 'New version is released. Please download it! Thank you.')
else:
    try:
        threads = []
        for account in accounts:
            threads.append(threading.Thread(target=PreSearch, args=(account,)))
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
    except Exception as ex:
        print('%s has exception:\n%s!' % (app, ex))
        notification.notify(app, '%s has exception:\n%s!' % (app, ex))
