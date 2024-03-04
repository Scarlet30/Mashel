# steps/api_steps.py
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests


@given('the API endpoint is "{api_url}"')
def set_api_url(context, api_url):
    context.api_url = api_url


@when('I open the API endpoint in a browser')
def open_api_in_browser(context):
    # Utiliza Selenium para abrir la URL en un navegador
    context.driver = webdriver.Chrome()
    context.driver.get(context.api_url)


@then('the API response should contain "{expected_data}"')
def check_api_response(context, expected_data):
    # Extrae y verifica la respuesta de la API utilizando Selenium
    page_source = context.driver.page_source
    assert expected_data in page_source

    # También podrías realizar solicitudes directas a la API utilizando requests
    api_response = requests.get(context.api_url)
    assert expected_data in api_response.text

    # Cierra el navegador
    # context.driver.quit()
