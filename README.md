# MASHLE

_Mashle 🔮 🧹 🪄 🧙‍♀️is a project to API test automation. 

## Start 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas_


### Pre-requeriments 📋

_First: You need to install behave, selenium and locust, with the commands next you can to run in your console_

_1. Install behave_

```
pip3 install behave
```

_2. Install Selenium

```
pip3 install selenium
```

_3. Install locust_

```
pip3 install locust
```
_3. Install allure_

```
pip3 install allure
```

### Running 🕹️

_Exmaple:_

_For executing the test cases with behave, just you have that run the command next in your consola_

```
behave
```

_For generate report with allure: _

```
behave -f allure_behave.formatter:AllureFormatter -o allure-results
```

_For watching report: _

```
allure serve allure-results
```
_For executing load test with locust, just you have that run the command next in your consola_

```
locust
```



_Finaliza con un ejemplo de cómo obtener datos del sistema o como usarlos para una pequeña demo_



