import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from login import receber_dados


def login_alura():
    email = receber_dados.user_login
    pwd = receber_dados.pwd_login

    # Configurações do Chrome
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--lang=pt-BR")

    # Inicializando o navegador corretamente
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=chrome_options
    )

    # Acessa o site da Alura
    driver.get("https://cursos.alura.com.br/loginForm?logout")
    time.sleep(5)

    # Clicar e escrever e-mail
    driver.find_element(By.ID, "login-email").click()
    driver.find_element(By.ID, "login-email").send_keys(email)

    # Clicar e escrever senha
    driver.find_element(By.ID, "password").click()
    driver.find_element(By.ID, "password").send_keys(pwd)

    # Clicar no botão de entrar
    driver.find_element(By.XPATH, '//*[@id="form-default"]/button').click()
