from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import time


def menuSelector(menu_ordered, menuList):
    print(menu_ordered)
    for menu in menuList:
        if menu_ordered == menu.text.strip():
            return menu
    print('해당 메뉴가 없습니다')
    return


def order(adrs1, store, detail_address, menu_ordered, quantity):
    # adrs1 = "고려대학교 안암캠퍼스"
    # store = '멕시카나'
    # menu_ordered = '불닭치킨'
    # quantity = 2
    # detail_address = '공학관'

    driver = webdriver.Chrome(
        './chromedriver.exe')
    waiting = WebDriverWait(driver, 10)

    driver.get('https://www.yogiyo.co.kr/')

    waiting.until(EC.invisibility_of_element_located(
        (By.XPATH, "//*[@id=\"spinner\"]")))

    # 주소입력- adrs1
    element0 = waiting.until(
        EC.visibility_of_element_located((By.NAME, "address_input")))
    time.sleep(2)
    element0.clear()
    element0.send_keys(adrs1)

    # 주소 검색
    driver.find_element_by_xpath(
        "//*[@id=\"button_search_address\"]/button[2]").click()

    # 검색 버튼 클릭(음식점,메뉴 검색)
    element1 = waiting.until(EC.visibility_of_element_located((
        By.XPATH, "//*[@id=\"category\"]/ul/li[1]/a"
    )))
    element1.click()

    # 음식점, 메뉴 이름 입력 -store
    searchInput = waiting.until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="category"]/ul/li[15]/form/div/input')))
    searchInput.clear()
    searchInput.send_keys(store)
    # 음식점, 메뉴 이름 검색
    searchBtn = waiting.until(
        EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="category_search_button"]'))
    )
    searchBtn.click()

    # 첫번째 음식점 클릭
    restaurant = waiting.until(
        EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="content"]/div/div[5]/div/div/div[1]/div'))
    )
    restaurant.click()

    # 메뉴 가져오기
    menuPhoto = waiting.until(
        EC.visibility_of_element_located(
            (By.XPATH,
             '//*[@id="menu"]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[2]')
        )
    )

    menuList = driver.find_elements_by_class_name('menu-name')

    # 메뉴선택
    menu_selected = menuSelector(menu_ordered, menuList)
    menu_selected.click()

    # 수량선택
    plus = waiting.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, 'plus')
        )
    )
    for i in range(quantity-1):
        plus.click()

    # 주문하기 버튼 클릭
    orderBtn = waiting.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, 'btn-order')
        )
    )
    orderBtn.click()

    # 상세주소 입력
    detailAdr = waiting.until(
        EC.visibility_of_element_located(
            (By.XPATH,
             '//*[@id="content"]/div/form[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/input')
        )
    )
    detailAdr.clear()
    detailAdr.send_keys(detail_address)

    time.sleep(100000)
