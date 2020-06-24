2014.12.14
+ 有料記事のコードを利用しているので、使えないかもしれない
___

```bash
$ tree
.
├── pages
│   ├── __init__.py
│   ├── login.py
│   └── todo.py
├── test_login.py
└── test_todo.pyi


$ pip install selenium
```
 
 <br>
 
 test_login.py
```py
#!/usr/bin/env python
# coding=utf8
import unittest

from selenium import webdriver

from pages.login import LoginPage
from pages.todo import TodoPage


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.close()

    def test_login(self):
        """トップにアクセスすると/loginにリダイレクトする"""
        todo_page = TodoPage(self.driver)
        todo_page.open()

        self.assertEqual(self.driver.current_url, LoginPage().url)

    def test_invalid_password(self):
        """username/passwordが間違っていた場合にエラーが表示される"""
        login_page = LoginPage(self.driver)

        self.assertEqual(
            login_page.open().login_with_invalid_user('foo', 'bar').get_error_message(),
            'Invalid username or password.'
        )

    def test_valid_password(self):
        """username/passwordが正しい場合はトップに遷移する"""
        login_page = LoginPage(self.driver)
        login_page.open().login('user', 'pass')

        self.assertEqual(self.driver.current_url, TodoPage().url)

if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

```

<br>

pages/login.py
```py
#!/usr/bin/env python
# coding=utf8
from .todo import TodoPage


class LoginPage:
    url = 'http://localhost:4000/login'

    def __init__(self, driver=None):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)
        return self

    def _login(self, username, password):
        self.driver.find_element_by_name("username").send_keys(username)
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_css_selector(".loginForm").submit()

    def login(self, username, password):
        self._login(username, password)

        todo_page = TodoPage(self.driver)
        return todo_page

    def login_with_invalid_user(self, username, password):
        self._login(username, password)
        return self

    def get_error_message(self):
        return self.driver.find_element_by_css_selector(".message").text

```

<br>

pages/todo.py
```py
#!/usr/bin/env python
# coding=utf8
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TodoPage:
    url = 'http://localhost:4000/'
    item_locator = '.todoList li'

    def __init__(self, driver=None):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)
        return self

    def create_todo(self, text):
        self.driver.find_element_by_name('text').send_keys(text)
        self.driver.find_element_by_css_selector('.createTodoForm').submit()
        return self

    def get_todo_text(self, index):
        elements = self.driver.find_elements_by_css_selector(self.item_locator)
        return elements[index].find_element_by_css_selector('.todoList-text').text

    def remove_todo(self, index):
        elements = self.driver.find_elements_by_css_selector(self.item_locator)
        elements[index].find_element_by_css_selector('.todoList-remove').click()
        return self

    def wait_for_visibility_of_item(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.item_locator)))
        return self

    def accept_confirm(self):
        self.driver.switch_to_alert().accept()
        return self

```

<br>

『入門、Selenium - E2Eテストの記述』 に記載されているSeleniumサンプル を git clone し npm start してサーバーを起動。
+ 見てみたけど、有料記事じゃないですか...

```bash
$ python -V
Python 2.7.8
$ python -m unittest discover -v -p 'test_*.py'
test_invalid_password (test_login.LoginTest)
username/passwordが間違っていた場合にエラーが表示される ... ok
test_login (test_login.LoginTest)
トップにアクセスすると/loginにリダイレクトする ... ok
test_valid_password (test_login.LoginTest)
username/passwordが正しい場合はトップに遷移する ... ok
test_add_todo (test_todo.TodoTest)
Todoを追加する ... ok
test_del_todo (test_todo.TodoTest)
Todoを削除する ... ok

----------------------------------------------------------------------
Ran 5 tests in 23.657s

OK
```

