import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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


def test_05_verificar_interfaz_burger_menu ( driver ):     
    menu_button = driver.find_element(By.ID, 'react-burger-menu-btn')
    
    assert menu_button.is_displayed(), f'ERROR: Menu no esta visible'


def test_06_verificar_interfaz_filtro_menu ( driver ):
    filtro = driver.find_element(By.CLASS_NAME, 'product_sort_container')

    assert filtro.is_displayed(), f'ERROR: filtro no esta visible'


def test_07_verificar_agregar_producto_al_carrito ( driver ):
    primer_producto = driver.find_elements(By.CLASS_NAME, 'inventory_item')[0]

    boton_agregar = primer_producto.find_element(By.TAG_NAME,'Button')
    boton_agregar.click()

    boton_remove = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//button[text()="Remove"]'))
    )

    assert boton_remove.text == 'Remove', 'ERROR: el boton no cambio de nombre a "Remove" despues de agregarlo a el carrito'
