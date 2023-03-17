from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
import time
# Ruta fichero del driver de microsoft edge 
PATH="C:/ruta dirver/msedgedriver.exe"

driver_options = webdriver.EdgeOptions()
# Configurar las opciones de descarga
driver_options.add_experimental_option("prefs", {
    "download.default_directory": "C:ruta_guardar"})

driver = webdriver.Edge(executable_path=PATH, options=driver_options)
# driver = webdriver.Edge(PATH)
driver.get("https://acme-test.uipath.com/login")

input_usuario=driver.find_element(By.ID,"email")
input_usuario.send_keys("usuario")

input_contrasena=driver.find_element(By.ID,"password")
input_contrasena.send_keys("contraseña")

input_boton=driver.find_element(By.CLASS_NAME,"btn-primary")
input_boton.click()

input_boton_1 = driver.find_elements(By.CLASS_NAME,'btn-default')[0]
input_boton_1.click()

input_boton_2=driver.find_element(By.LINK_TEXT,"Download Client and Support")
input_boton_2.click()

time.sleep(5)

input_boton_3 = driver.find_elements(By.XPATH, '//*[@id="pagetext"]/div[1]/div/div[2]/div/a')[0]
input_boton_3.click()

time.sleep(5)

driver.quit()
