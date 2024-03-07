# MASHLE

_Mashle 🔮 🧹 🪄 🧙‍♀️is a project to API test automation. 

## Start 🚀

_This instructions help you install in your local machine to testing or development _


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


