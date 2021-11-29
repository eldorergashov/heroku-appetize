## Tools:
<details>

  <summary>Click to expand</summary>

  | Tool | Description | How to Installation | 
  | ----------- | ----------- | ----------- 
  | Pycharm IDE | IDE  |[PyCharm – The Python IDE Installation](#pycharm--the-python-ide-installation)   
  | Python | Programming Language | Installed by default in Unix| 
  | Pytest  | Testing Framework |[Prepare Project](#prepare-project) 
  | Selenium  | Library to talk with WebDriver |[Prepare Project](#prepare-project)
  | Allure  | Report Library |[Prepare Project](#prepare-project)


  ### PyCharm – The Python IDE Installation:
  https://www.jetbrains.com/pycharm/

   1. Download the pycharm-2020.1.2.dmg macOS Disk Image file (Community)
   2. Mount it as another disk in your system
   3. Copy PyCharm to your Applications folder

### Prepare project
1. Open project folder in terminal
2. To create virtual environment for project you need execute following command in terminal:
```
python -m venv venv
```
3. Activate virtual env you need execute following command in terminal:

Windows
```bash
.\venv\bin\activate
```
Mac/Linux
```bash
source venv\bin\activate
```

5. To install dependencies you need execute following command in terminal:
```
pip install -r requirements.txt
```
</details>

## Project Structure
<details>

1. All test cases located in `project_root/tests/`
2. Test runner behavior (pytest) can be tweaked by editing `pytest.ini`
3. By default, fixtures (setup, teardown functions) located in `conftest.py`
4. Page object models located in `пропиши тут сам путь до моделей`
5. Можешь добавить чтото еще если хочешь
</details>

## Test Execution 
<details>
1.Open project folder in terminal<br>
2.To execute all tests you need execute following command in terminal:

  ```bash
  pytest tests/
  ```

3.To execute module/suite  you need execute following command in terminal:
  ```bash
  pytest tests/test_some.py
  ```
</details>

# Report

  ### Used Libs
  1. pytest-json-report
  2. allure-pytest

These libs included in requirements.txt 

  ### Reports Type
  
  Framework able to create 4 type of reports:
   1. Allure report
   2. Standard Pytest Html report
   3. Json Report (to export to other report system)
   4. Xml Report ( to export to other report system)

  ### How can see reports

  **Allure report**
  1. You need install `Allure` in your system to render report locally.
     1. Execute following command in terminal:
     ```bash
     brew install allure
     ```
  2. To get local "allure report" you need to execute this command:
   ```bash
   allure serve {allure-results_path} 
   ```
  Where `{allure-results_path}` is path to `allure-results` folder. Default path is `project/reports/allure-results`
  3. Default browser will render allure report

  **Standard Pytest Html report**
  1. To get this report you need to open `report.html` file inside `{root_project]/reports/v2`

  **Json Report**
  1. To get json report you need to open `report.json` file inside `{root_project]/reports/`

  **Xml Report**
  1. To get xml report you need to open `report.xml` file inside `{root_project]/reports/`


  ### How reports are generated
  - After test execution all 4 types of reports will be generated automatically by default.
  - Pytest are holding arguments for each type of report such as:

  **Allure Report**
  ```
  --alluredir=./reports/allure-results
  ```
  **Standard Pytest Html report**
  ```
  --html=./reports/v2/report.html --self-contained-html
  ```
  **Json Report**
  ```
  --json-report --json-report-file=./reports/report.json
  ```
  **XMl Report**
  ```
  --junitxml ./reports/report.xml
  ```
