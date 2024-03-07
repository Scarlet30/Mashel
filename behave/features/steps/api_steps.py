import requests
from behave import Given, When, Then


@Given('I have an endpoint "{url}"')
def end_point(context, url):
    context.api_url = url


@Given('I count in the following query params "{param}" and its value "{value}"')
def get_params_first(context, param, value):
    context.query_params = {param: value}


@Given('I count in other query params "name" and its fail value "643"')
def get_params_second(context):
    context.query_params1 = {"name": "643"}


@Given('I count in the following query params')
def get_params_third(context):
    context.query_params = {}
    for row in context.table:
        key = row['key']
        value = row['value']
        context.query_params[key] = value


@Given('I count in the following query params "{param3}" with "{value3}"')
def get_params_four(context, param3, value3):
    context.query_params3 = {param3: value3}


@When('I do request with query params')
def request_first(context):
    context.response = requests.get(context.api_url, params=context.query_params)


@When('I do request with different query params')
def request_second(context):
    context.response = requests.get(context.api_url, params=context.query_params1)


@When('I do request with status')
def request_third(context):
    url = context.api_url
    if context.query_params:
        context.api_url += "?" + "&".join([f"{key}={value}" for key, value in context.query_params.items()])

    context.response = requests.get(url)


@When('I do request with gender')
def request_third(context):
    context.response = requests.get(context.api_url, params=context.query_params3)


@Then('I see the statuscode 200')
def status_first(context):
    status_code = context.response.status_code
    assert status_code == 200, f'statuscode: {status_code}'


@Then('I see the statuscode 404')
def status_second(context):
    status_code = context.response.status_code
    assert status_code == 404, f'statuscode: {status_code}'


@Then('replies me with name "{name}"')
def step_impl_first(context, name):
    contents = context.response.json()['results']
    content_names = [content['name'] for content in contents]
    assert name in content_names, f'te llamas {name}'


@Then('response me with an error "{error}"')
def step_impl_second(context, error):
    message_error = context.response.json()
    if 'error' in message_error and message_error['error'] == error:
        print("La respuesta del API contiene el mensaje de error esperado")
    else:
        print("La respuesta del API no contiene el mensaje de error esperado")


@Then('I can see responses with status "{expected_status}" and specie "{expected_specie}"')
def step_impl_third(context,  expected_specie, expected_status):
    contents = context.response.json().get('results', [])
    content_species = [content.get('species', '') for content in contents]
    content_status = [content.get('status', '') for content in contents]

    assert expected_specie in content_species, f'la especie {expected_specie}'
    assert expected_status in content_status, f'el estado {expected_status}'


@Then('The response with gender "{gender}"')
def step_impl_fourth(context, gender):
    contents = context.response.json()['results']
    content_gender = [content['gender'] for content in contents]

    assert gender in content_gender, f'su genero es {gender}'
