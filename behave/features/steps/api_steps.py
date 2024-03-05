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


@When('I do request with query params')
def request_first(context):
    context.response = requests.get(context.api_url, params=context.query_params)


@When('I do request with different query params')
def request_second(context):
    context.response = requests.get(context.api_url, params=context.query_params1)


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



