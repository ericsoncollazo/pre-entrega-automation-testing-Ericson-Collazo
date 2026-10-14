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


def test_05_verificar_existencia_del_pruducto_por_nombre (driver):
    inventory_item = driver.find_elements(By.CLASS_NAME, 'inventory_item')

    primer_producto = inventory_item[0]
    nombre = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text

    assert nombre.strip() != "", ("Error: El primer producto no muestra su nombre")
    print(f"\nPrimer producto: {nombre}")



def test_06_verificar_existencia_del_pruducto_por_precio (driver):
    inventory_item = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    
    primer_producto = inventory_item[0]
    precio = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text

    assert precio.strip() != "", ("Error: El primer producto no muestra su precio")
    print(f"\nPrimer producto: {precio}")


def test_07_verificar_interfaz_burger_menu ( driver ):     
    menu_button = driver.find_element(By.ID, 'react-burger-menu-btn')
    
    assert menu_button.is_displayed(), f'ERROR: Menu no esta visible'


def test_08_verificar_interfaz_filtro_menu ( driver ):
    filtro = driver.find_element(By.CLASS_NAME, 'product_sort_container')

    assert filtro.is_displayed(), f'ERROR: filtro no esta visible'


def test_09_verificar_agregar_producto_al_carrito ( driver ):
    primer_producto = driver.find_elements(By.CLASS_NAME, 'inventory_item')[0]

    boton_agregar = primer_producto.find_element(By.TAG_NAME,'Button')
    boton_agregar.click()

    boton_remove = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//button[text()="Remove"]'))
    )

    assert boton_remove.text == 'Remove', 'ERROR: el boton no cambio de nombre a "Remove" despues de agregarlo a el carrito'


def test_10_verificar_contador_carrito(driver):
    wait = WebDriverWait(driver, 10) 

    contador_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert contador_carrito == "1", f"Error: El contador del carrito debería mostrar '1' pero muestra '{contador_carrito}'"

def test_11_navegar_carrito(driver):
    wait = WebDriverWait(driver, 10) 

    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    carrito.click()

    wait.until(EC.url_contains("/cart.html"), "Error: No se redirigió a la página del carrito")

    assert "/cart.html" in driver.current_url, "Error: No se redirigió a la página del carrito"    

def test_12_verificar_producto_en_carrito(driver):
    wait = WebDriverWait(driver, 10) 

    productos_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")

    assert len(productos_carrito) > 0, "Error: No se encontraron productos en el carrito"


def test_13_verificar_producto_en_carrito_por_nombre(driver):
    wait = WebDriverWait(driver, 10) 
    productos_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")
    primer_producto_carrito = productos_carrito[0]
    nombre_carrito = primer_producto_carrito.find_element(By.CLASS_NAME, "inventory_item_name").text
    
    assert nombre_carrito.strip() != "", "Error: El primer producto en el carrito no muestra su nombre"

    print(f"\nPrimer producto en el carrito: {nombre_carrito}")


def test_14_verificar_producto_en_carrito_por_precio(driver):
    wait = WebDriverWait(driver, 10) 

    productos_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")
    primer_producto_carrito = productos_carrito[0]
    precio_carrito = primer_producto_carrito.find_element(By.CLASS_NAME, "inventory_item_price").text

    assert precio_carrito.strip() != "", "Error: El primer producto en el carrito no muestra su precio"

    print(f"\nPrimer producto en el carrito: Precio: {precio_carrito}")