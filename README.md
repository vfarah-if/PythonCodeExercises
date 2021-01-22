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

6. Install pip with python 3 or upgrade pip to the latest

   ```
   python3 -m pip install
   python3 -m pip install --upgrade pip
   ```

