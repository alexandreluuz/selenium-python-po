import pytest
from selenium.webdriver.common.by import By
import conftest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.carrinho_page import CarrinhoPage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.carrinho

class TestCT01:
    def test_ct01_adicionar_produtos_carrinho(self):
        driver = conftest.driver
        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()

        produto_1 = "Sauce Labs Backpack"
        produto_2 = "Sauce Labs Bolt T-Shirt"

        # Fazendo login
        login_page.fazer_login("standard_user", "secret_sauce")

        # Adicionando a mochila ao carrinho

        home_page.adicionar_ao_carrinho(produto_1)

        # Verificando que a mochila foi adicionada
        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe(produto_1)

        # Clicando para voltar para a tela de produtos
        carrinho_page.clicar_continuar_comprando()

        # # Adicionando mais um produto ao carrinho
        home_page.adicionar_ao_carrinho(produto_2)

        # # Verificando que os dois produtos estão no carrinho
        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe(produto_1)
        carrinho_page.verificar_produto_carrinho_existe(produto_2)

        # driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()
        # assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()
        # assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Bike Light']").is_displayed()
        #
        # driver.find_element(By.ID, "checkout").click()
        # driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("João")
        # driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Silva")
        # driver.find_element(By.XPATH, "//input[@placeholder='Zip/Postal Code']").send_keys("12345678")
        # driver.find_element(By.ID, "continue").click()
        #
        # driver.find_element(By.XPATH, "//*[@class='title' and text()='Checkout: Overview']").is_displayed()
        #
        # elementos_val = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        #
        # total = 0
        #
        # for elemento_val in elementos_val:
        #     texto_val = elemento_val.text
        #     # Faça a extração do valor numérico da string e some-o ao total
        #     valor = float(texto_val.strip('$'))
        #     total += valor
        #
        # valor_esperado = driver.find_element(By.XPATH, "//*[@class='summary_subtotal_label']")
        # texto_valor_esperado = valor_esperado.text
        # valor_esperado = float(texto_valor_esperado.strip('Item total: $'))
        #
        # print("Valor esperado:", valor_esperado)
        # assert total == valor_esperado
        #
        # driver.find_element(By.ID, "finish").click()
        #
        # assert driver.find_element(By.XPATH, "//img[@alt='Pony Express']").is_displayed(), "A imagem não está sendo exibida"
        # driver.find_element(By.ID, "back-to-products").click()
