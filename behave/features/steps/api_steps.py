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


@Given('I count in the following query params "species" and "status"')
def get_params_third(context):
    context.query_params2 = {"status": "Alive"}


@Given('I count in the following query params "name" and "gender"')
def get_params_third(context, param3, value3):
    context.query_params3 = {param3: value3}


@When('I do request with query params')
def request_first(context):
    context.response = requests.get(context.api_url, params=context.query_params)


@When('I do request with different query params')
def request_second(context):
    context.response = requests.get(context.api_url, params=context.query_params1)


@When('I do request with specie and status')
def request_third(context):
    context.response = requests.get(context.api_url, params=context.query_params2)


@When('I do request with name and gender')
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
    if 'error' in message_error and message_error['error']=='There is nothing here':
        print("La respuesta del API contiene el mensaje de error esperado")
    else:
        print("La respuesta del API no contiene el mensaje de error esperado")


@Then('I can to see response specie "{species}" with status "{status}"')
def step_impl_third(context, species, status):
    contents1 = context.response.json()['results']
    content_species = [content['species'] for content in contents1]
    content_status = [content['status'] for content in contents1]

    assert species in content_species, f'la especie es {species}'
    assert status in content_status, f'el estado es {status}'


@Then('The response with name "Alien Googah" with gender "unknown"')
def step_impl_fourth(context, name, gender):
    contents2 = context.response.json()['results']
    content_name = [content['name'] for content in contents2]
    content_gender = [content['gender'] for content in contents2]

    assert name in content_name, f'el personaje es {name}'
    assert gender in content_gender, f'su genero es {gender}'
