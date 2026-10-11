import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options



@pytest.fixture(scope="module")
def driver():
    servicio = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=servicio)
    
    yield driver
 
    driver.quit()



def test_01_login(driver):
    driver.get("https://www.saucedemo.com/")
    
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    assert "/inventory.html" in driver.current_url , "ERROR: logueo incorrecto /inventory.html"

def test_02_verificar_titulo(driver):

    page_title = driver.title
    
    assert page_title == "Swag Labs" , f"ERROR: titulo incorrecto', obtenido '{page_title}'"

def test_03_verificar_titulo_de_inventario(driver):

    section_tittle = driver.find_element(By.CLASS_NAME, "title").text
    
    assert section_tittle == 'Products' , f'ERROR: Titulo de la seccion debe ser "products", Obtenido {section_tittle}'

def test_04_verificar_productos_existentes (driver):

    inventory_item = driver.find_elements(By.CLASS_NAME, 'inventory_item')

    assert len(inventory_item) > 0 , f'ERROR: No se encontraron productos visibles en el inventario'

