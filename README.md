# Introduction

Create simple unit testing sample and understand good naming and generation of samples ...

The inspiration for this is taken from this article https://testdriven.io/blog/modern-tdd/ 

# Setup

1. Install `pip install -U pytest`

2. [pytest](https://docs.pytest.org/en/stable/) is the test framework used by the article

3. Documentation can be found https://docs.pytest.org/en/stable/getting-started.html

4. Running the tests through python I setup `python3 -m pytest `. **NOTE:** the test name always needs to start with **test_** or end with **_test** or the test discovery will not happen 

5. VSCode Tips and tricks:

   - With **vscode**, I needed to setup my interpreter path to utilise Python 3.9.1 for everythign to work with the correct version of Python. This can be found on the bottom left panel of your IDE footer

   - Setting up **text explorer**, add the extension python test explorer and then see this [https://code.visualstudio.com/docs/python/testing](https://code.visualstudio.com/docs/python/testing) for more information

   - Configure settings with [Pytest](https://docs.pytest.org/en/stable/contents.html)

     ```json
     {
         "python.pythonPath": "/opt/local/bin/python3",
         "python.testing.pytestArgs": [
             "tests"
         ],
         "python.testing.unittestEnabled": false,
         "python.testing.nosetestsEnabled": false,
         "python.testing.pytestEnabled": true,
         "python.testing.autoTestDiscoverOnSaveEnabled": true
     }
     ```

6. Install pip with python 3 or upgrade pip to the latest

   ```shell
   python3 -m pip install
   python3 -m pip install --upgrade pip
   ```


7. Create a virtual environment using ` python3 -m venv ./opt/local`

8. Setting up a project structure should resemble https://docs.python-guide.org/writing/structure/

9. Make sure if you have folder that you always include `__init__.py`files which can include paths, setting variables or just logging - see more [here]( https://www.datacamp.com/community/tutorials/role-underscore-python)

10. **Pytest** install all things needed:

    ```
    pip install pytest
    pip install pytest-sugar
    pip install pytest-cov
    ```
    - `pytest --fixtures` gives a list of fixtures, including one built up with setup fixtures that may have doc comments
    - `pytest --markers` gives a list of markers to help decorate functions with
    - `pip install pytest-html` and output html to show reports and output an html report `pytest --html=report.html`
    - 

