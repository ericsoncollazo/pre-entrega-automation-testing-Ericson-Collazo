# Pruebas Automatizadas - SauceDemo

**Autor:** Ericson Alexis Collazo Vargas

## Propósito del proyecto

Este proyecto consiste en la creación de pruebas automatizadas para **SauceDemo**, una página web de ejemplo que permite simular el proceso de compra de productos en una tienda online.

El objetivo es comprobar que las principales funcionalidades del sitio funcionen correctamente, desde el inicio de sesión hasta la selección de productos y su incorporación al carrito de compras.

Las pruebas se realizaron con Python y herramientas de automatización que permiten interactuar con la página de manera similar a como lo haría una persona.

## Pruebas realizadas

Se desarrollaron 14 pruebas automatizadas para verificar las siguientes funcionalidades:

- **Inicio de sesión:** comprobar que se pueda ingresar correctamente con un usuario y contraseña válidos.
- **Título de la página:** verificar que el título del sitio sea el esperado.
- **Título del inventario:** comprobar que la sección de productos muestre el título correcto.
- **Listado de productos:** verificar que existan productos disponibles para visualizar.
- **Nombre de los productos:** comprobar que los productos muestren su nombre.
- **Precio de los productos:** verificar que los productos tengan un precio visible.
- **Menú de navegación:** comprobar que el menú principal esté visible.
- **Filtro de productos:** verificar que el filtro de ordenamiento esté disponible.
- **Agregar productos al carrito:** comprobar que se pueda incorporar un producto al carrito de compras.
- **Contador del carrito:** verificar que el contador refleje la cantidad de productos agregados.
- **Navegación al carrito:** comprobar que se pueda acceder a la sección del carrito.
- **Productos en el carrito:** verificar que se muestren los productos agregados.
- **Nombre del producto en el carrito:** comprobar que el nombre del producto sea visible.
- **Precio del producto en el carrito:** verificar que el precio del producto sea visible.

## Herramientas utilizadas

Para desarrollar y ejecutar las pruebas se utilizaron las siguientes herramientas:

- **Python:** lenguaje de programación utilizado para desarrollar las pruebas.
- **Pytest:** herramienta utilizada para organizar y ejecutar las pruebas.
- **Selenium WebDriver:** permite automatizar las acciones realizadas en el navegador.
- **Google Chrome:** navegador utilizado para ejecutar las pruebas.
- **WebDriver Manager:** facilita la configuración del controlador del navegador.
- **pytest-html:** permite generar informes HTML con los resultados de las pruebas.

## Estructura del proyecto

El proyecto está organizado en carpetas para facilitar la ubicación de los archivos y mantener ordenado el trabajo.

```text
.
├── datos/                  # Archivos con datos de prueba
├── reports/                # Informes de ejecución
├── tests/
│   └── test_saucedemo.py   # Casos de prueba automatizados
├── utils/                  # Funciones auxiliares
└── README.md               # Documentación del proyecto
```

## Cómo ejecutar las pruebas

Para ejecutar las pruebas en una computadora, es necesario tener Python instalado y descargar el repositorio.

### 1. Instalar las dependencias

Abrir una terminal en la carpeta del proyecto y ejecutar:

```bash
pip install pytest selenium webdriver-manager pytest-html
```

### 2. Ejecutar las pruebas

Para ejecutar todos los casos de prueba, utilizar el siguiente comando:

```bash
pytest
```

### 3. Generar el informe de resultados

Para generar un informe HTML con el detalle de la ejecución, ejecutar:

```bash
pytest --html=reports/reporte.html --self-contained-html
```

Al finalizar, se podrá abrir el archivo HTML generado desde el navegador para consultar los resultados de cada prueba.

Es necesario que la carpeta `reports` exista antes de ejecutar el comando, o crearla previamente.

## Resultados de la ejecución

La última ejecución registrada se realizó el **14 de octubre de 2026**.

| Resultado | Cantidad |
|---|---:|
| Total de pruebas ejecutadas | 14 |
| Pruebas aprobadas | 14 |
| Pruebas fallidas | 0 |
| Pruebas omitidas | 0 |

**Resultado final:** las 14 pruebas ejecutadas finalizaron correctamente, sin errores ni pruebas fallidas.

El tiempo total registrado para la ejecución fue de aproximadamente **7 segundos**.

El informe HTML permite consultar el estado y el tiempo de ejecución de cada caso de prueba.

## Autor

**Ericson Alexis Collazo Vargas**

Proyecto de automatización de pruebas de software realizado sobre la plataforma SauceDemo.
