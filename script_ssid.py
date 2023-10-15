from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.select import Select
from time import sleep

login = "xxxxxx" #login de adm
password = "xxxxxx" #senha de adm

# Selecionar opções na lista - TASK PENDENTE

# Abrir navegador e acessar a página de login do modem
driver = webdriver.Chrome()
driver.get('http://192.168.0.1/')
sleep(5)

# Preencher dados de login e clicar em "Entrar"
campo_login = driver.find_element(By.XPATH,"//input[@id='Frm_Username']")
campo_login.send_keys(login)

campo_senha = driver.find_element(By.XPATH,"//input[@id='Frm_Password']")
campo_senha.send_keys(password)

botao_login = driver.find_element(By.XPATH,"//button[@id='LoginId']")
botao_login.click()
sleep(10)

# Acesso às configurações avançadas
config_adv = driver.find_element(By.XPATH,"//a[@id='Qstate']")
config_adv.click()
sleep(5)

# Abre as opções de Wi-Fi
botao_menu = driver.find_element(By.XPATH,"//label[@class='main-menu-button']")
botao_menu.click()
sleep(5)

wifi_config = driver.find_element(By.XPATH,"//label[@for='menu-wlan']")
wifi_config.click()
sleep(3)

wifi_mainNet = driver.find_element(By.XPATH,"//a[@id='wlanSSID']")
wifi_mainNet.click()
sleep(5)

# Oculta o SSID da rede, salva e, após 10 segundos, reverte a alteração
oculta_SSID = driver.find_element(By.XPATH,"//input[@id='ESSIDHideEnable0:0']")
oculta_SSID.click()

salva_SSID = driver.find_element(By.XPATH,"//input[@id='Btn_apply_WLANSSIDConf:0']")
salva_SSID.click()
sleep(10)

exibe_SSID = driver.find_element(By.XPATH,"//input[@id='ESSIDHideEnable1:0']")
exibe_SSID.click()

salva_SSID.click()
sleep(60)
