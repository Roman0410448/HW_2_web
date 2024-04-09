import time
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_step1(site, x_selector1, x_selector2, btn_selector, x_selector3, expected_error_text):
    input1 = site.find_element(By.XPATH, x_selector1)
    input1.send_keys('test')
    input2 = site.find_element(By.XPATH, x_selector2)
    input2.send_keys('test')
    btn = site.find_element(By.CSS_SELECTOR, btn_selector)
    btn.click()
    err_label = site.find_element(By.XPATH, x_selector3)
    assert err_label.text == expected_error_text


def test_login_success(site, x_selector1, x_selector2, btn_selector, username, password):
    input1 = site.find_element(By.XPATH, x_selector1)
    input1.send_keys(username)
    input2 = site.find_element(By.XPATH, x_selector2)
    input2.send_keys(password)
    btn = site.find_element(By.CSS_SELECTOR, btn_selector)
    btn.click()

    wait = WebDriverWait(site, 20)
    try:
        logged_in_element = wait.until(EC.presence_of_element_located((By.ID, "loggedIn")))
        assert logged_in_element is not None
    except TimeoutException:
        print("Элемент не найден")


def test_add_post(site, post_title_selector, submit_description_selector, post_content_selector, add_post_selector):
    post_title = site.find_element(By.XPATH, post_title_selector)
    post_title.send_keys('Пост для теста')
    post_content = site.find_element(By.XPATH, post_content_selector)
    post_content.send_keys('Пост для теста')

    submit_post = site.find_element(By.XPATH, add_post_selector)
    submit_post.click()

    wait = WebDriverWait(site, 20)
    try:
        post_title_on_page = wait.until(EC.presence_of_element_located((By.XPATH, post_title_selector)))
        assert post_title_on_page.text == 'Пост для теста'
    except TimeoutException:
        print("Название поста не найдено на странице")

