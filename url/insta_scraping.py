import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\\Users\\yuki\\Documents\\chromedriver.exe')
try:
    driver.get('https://www.instagram.com/?hl=ja')
    time.sleep(5)
    loginForms = driver.find_elements_by_tag_name("input")
    loginForms[0].send_keys("lavi7965")
    loginForms[1].send_keys("syokotan4")
    time.sleep(1)
    btns = driver.find_elements_by_tag_name("button")
    btns[1].click()
    time.sleep(10)
    print("log 1")
    elm = driver.find_elements_by_class_name("q9xVd")
    elm[0].click()
    time.sleep(5)
    print("logged in!")
    elm = driver.find_elements_by_class_name("mt3GC")
    btns = elm[0].find_elements_by_tag_name("button")
    btns[1].click()
    inpts = driver.find_elements_by_tag_name("input")
    time.sleep(3)
    print("searching 池袋!")
    inpts[2].send_keys("池袋")
    time.sleep(10)
    elm = driver.find_elements_by_class_name("yPP5B")
    driver.get("https://www.instagram.com/explore/tags/%E6%B1%A0%E8%A2%8B%E3%82%B0%E3%83%AB%E3%83%A1/")
    time.sleep(100)
    elm = driver.find_elements_by_class_name("_9AhH0")
    elm[5].click()
    time.sleep(5)
    elm = driver.find_elements_by_tag_name("svg")
    for i, el in enumerate(elm):
        if el.get_attribute("aria-label") == 'いいね！':
            if el.get_attribute("height") == '24':
                el.click()
    # prt.click()
    # elm = driver.find_elements_by_class_name("JvDyy")
    # elm[0].click()
    time.sleep(50)
finally:
    driver.quit()
# loginBtn = driver.find_elements_by_class_name("loginbtn")
# loginBtn[0].click() yPP5B
# time.sleep(5)
# driver.get('https://inte-www.kinto-jp.com/kinto_one/lineup/toyota/')
# elem = driver.find_elements_by_class_name("p-one_lineup__carlist")
# children = elem[0].find_elements_by_tag_name("li")
# for i in range(0, len(children)):
#     children[i].click()
#     time.sleep(5)
#     btn = driver.find_elements_by_class_name("PrimaryButton")
#     btn[0].click()
#     time.sleep(5)
#     btn2 = driver.find_elements_by_class_name("PrimaryButton")
#     btn2[0].click()
#     time.sleep(5)
#     btn3 = driver.find_elements_by_class_name("PrimaryButton")
#     btn3[0].click()
#     time.sleep(5)
#     btn4 = driver.find_elements_by_class_name("PrimaryButton")
#     btn4[0].click()
#     time.sleep(5)
#     dealer_elems = driver.find_elements_by_class_name("entryListWrapper__list")
#     dealer_elem = dealer_elems[0].find_elements_by_tag_name("li")
#     dealer_elem[0].click()
#     time.sleep(5)
#     btn5 = driver.find_elements_by_id("nextStepButton")
#     btn5[0].click()
#     time.sleep(5)
#     checkBoxes = driver.find_elements_by_class_name("formContent__checkBox__input__title")
#     for j in range(0, len(checkBoxes)):
#         checkBoxes[j].click()
#
#     driver.get('https://inte-www.kinto-jp.com/kinto_one/lineup/toyota/')
#     elem = driver.find_elements_by_class_name("p-one_lineup__carlist")
#     children = elem[0].find_elements_by_tag_name("li")
# time.sleep(100)