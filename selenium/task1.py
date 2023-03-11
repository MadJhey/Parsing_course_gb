# 1) Написать программу, которая собирает входящие письма из своего или тестового почтового ящика и сложить
# данные о письмах в базу данных (от кого, дата отправки, тема письма, текст письма полный)
# Логин тестового ящика: study.ai_172@mail.ru
# Пароль тестового ящика: NextPassword172
# 2) Написать программу, которая собирает «Хиты продаж» с сайта техники mvideo
# и складывает данные в БД. Магазины можно выбрать свои. Главный критерий выбора: динамически загружаемые товары

def main():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import time
    from pprint import pprint
    import json

    ser = Service()
    op = webdriver.ChromeOptions()
    op.add_argument('start-maximized')
    driver = webdriver.Chrome(service=ser, options=op)
    driver.get(
        'https://passport.yandex.ru/auth?retpath=https%3A%2F%2Fmail.yandex.ru')
    driver.implicitly_wait(20)
    login = driver.find_element(By.ID, 'passp-field-login')
    login.send_keys('')
    login.send_keys(Keys.ENTER)

    time.sleep(1)
    passw = driver.find_element(By.ID, 'passp-field-passwd')

    passw.send_keys('')
    passw.send_keys(Keys.ENTER)
    spam = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Спам, папка']"))
    )
    spam.click()
    pages = 0
    while True:
        try:
            more_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'js-message-load-more')]"))
            )
            more_button.click()
            pages += 1
        except:
            print(f'Finished to load {pages} pages')
            break
    driver.refresh()
    letters = driver.find_elements(By.CLASS_NAME, "ns-view-messages-item-wrap")
    letts = []
    for letter in letters:
        topic = letter.find_element(By.CLASS_NAME, "mail-MessageSnippet-Item_subject").text
        frm = letter.find_element(By.CLASS_NAME, "mail-MessageSnippet-FromText").text
        let = {}
        let['from'] = frm
        let['topic'] = topic
        letts.append(let)

    pprint(letts)

    with open(r"emails.txt", "w") as file:
        json.dump(letts, file)
    file.close()

    driver.close()



if __name__ == '__main__':
    main()
