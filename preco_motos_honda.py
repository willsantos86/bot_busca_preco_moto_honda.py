from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import os


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1300,1000', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    return driver

driver = iniciar_driver()


# Navegar até o site
driver.get("https://www.honda.com.br/motos/modelos")


# Carregar todos os elementos da tela movendo até o final da pagina e depois ao topo.
sleep(10)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
sleep(2)

# Encontrar os títulos
titulos = driver.find_elements(By.XPATH, "//div[@class='single-product-container']//h3")

# Encontrar os preços
precos = driver.find_elements(By.XPATH,"//span[@class='price']")

 # Encontrar os links
links = driver.find_elements(By.XPATH, "//h3[@class='title']//a")

# Guardar isso em um arquivo .csv
for titulo, preco, link in zip(titulos, precos, links):
    with open('precos.csv', 'a', encoding='utf-8', newline='') as arquivo:
        link_processado = link.get_attribute('href')
        arquivo.write(f'{titulo.text};{preco.text};{link_processado}{os.linesep}')
