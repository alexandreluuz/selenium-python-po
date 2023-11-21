import pytest
from selenium.webdriver.common.by import By
import conftest
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
@pytest.mark.smoke
class TestCT02:
    def test_ct02_login_valido(self):
        # Instancia os objetos a serem usados no teste
        driver = conftest.driver
        login_page = LoginPage()
        home_page = HomePage()

        # Faz o login
        login_page.fazer_login("standard_user", "secret_sauce")

        # Verifica se o login foi realizado
        home_page.verificar_login_com_sucesso()

        # assert driver.find_elements(By.XPATH, "//span[@class='title']") is not None
