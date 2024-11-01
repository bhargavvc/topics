Pytest in testing scenarios.

---

### **Basic Level Questions**

---

#### **1. What is Pytest, and why is it used in Python testing?**

**Answer:**

Pytest is a powerful testing framework for Python that simplifies writing and running tests. It supports simple unit tests as well as complex functional testing for applications and libraries. Pytest is used because it offers:

- **Simple Syntax:** Easy-to-write tests without boilerplate code.
- **Automatic Test Discovery:** Finds tests in your project automatically.
- **Fixtures:** Manages test setup and teardown using fixtures.
- **Parameterization:** Allows running tests with multiple sets of data.
- **Extensibility:** Supports plugins for added functionality.

**Real-Time Use:**

Pytest is widely used in industry projects for unit testing, integration testing, and system testing due to its flexibility and ease of use.

---

#### **2. How do you write a simple test case using Pytest?**

**Answer:**

A simple test case in Pytest is a function whose name starts with `test_`. You use assertions to validate the expected outcomes.

**Syntax Example:**

```python
# test_example.py

def test_addition():
    assert 1 + 1 == 2
```

**Real-Time Use:**

In real projects, you write test functions to validate the behavior of your code modules, ensuring they work as expected.

---

#### **3. How do you run Pytest tests from the command line?**

**Answer:**

You can run tests by executing the `pytest` command in the terminal within your project's directory.

**Syntax Example:**

```bash
pytest
```

To run tests from a specific file:

```bash
pytest test_example.py
```

**Real-Time Use:**

Running tests from the command line is essential in development and continuous integration pipelines to verify that code changes don't break existing functionality.

---

#### **4. What is a fixture in Pytest, and how do you use it?**

**Answer:**

A fixture in Pytest is a reusable piece of code that runs before (and optionally after) your test functions. Fixtures provide a fixed baseline upon which tests can reliably execute.

**Syntax Example:**

```python
import pytest

@pytest.fixture
def sample_data():
    return {"name": "Alice", "age": 30}

def test_sample_data(sample_data):
    assert sample_data["name"] == "Alice"
    assert sample_data["age"] == 30
```

**Real-Time Use:**

Fixtures are used to set up resources like database connections, test data, or configurations needed before tests run.

---

#### **5. How do you parameterize tests in Pytest?**

**Answer:**

You can parameterize tests using the `@pytest.mark.parametrize` decorator to run the same test function with different input values.

**Syntax Example:**

```python
import pytest

@pytest.mark.parametrize("input,expected", [
    (1, 2),
    (2, 3),
    (3, 4),
])
def test_increment(input, expected):
    assert input + 1 == expected
```

**Real-Time Use:**

Parameterized tests are useful for testing functions with multiple sets of inputs to ensure they handle various scenarios correctly.

---

#### **6. How does Pytest discover test files and test functions?**

**Answer:**

Pytest discovers test files and functions based on naming conventions:

- **Test Files:** Files starting with `test_` or ending with `_test.py`.
- **Test Functions:** Functions starting with `test_`.

**Real-Time Use:**

By adhering to these conventions, Pytest automatically finds and runs your tests without additional configuration.

---

#### **7. How do you skip a test in Pytest?**

**Answer:**

You can skip a test using the `@pytest.mark.skip` decorator or by calling `pytest.skip()` within the test function.

**Syntax Example:**

Using a decorator:

```python
import pytest

@pytest.mark.skip(reason="Not implemented yet")
def test_feature():
    assert False
```

Using `pytest.skip()`:

```python
def test_conditionally():
    if not some_condition():
        pytest.skip("Condition not met")
    assert True
```

**Real-Time Use:**

Skipping tests is useful when a test depends on external conditions or features that are not yet implemented.

---

#### **8. How do you expect a test to raise an exception in Pytest?**

**Answer:**

Use `pytest.raises` as a context manager to assert that an exception is raised.

**Syntax Example:**

```python
import pytest

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        result = 1 / 0
```

**Real-Time Use:**

Testing exception handling ensures your code responds correctly to error conditions.

---

#### **9. How do you run only a subset of tests in Pytest?**

**Answer:**

You can specify the test file, directory, or test function to run only a subset of tests.

**Syntax Example:**

Run tests from a specific file:

```bash
pytest test_example.py
```

Run a specific test function:

```bash
pytest test_example.py::test_function_name
```

**Real-Time Use:**

Running specific tests is helpful during development when you want to focus on a particular functionality or fix.

---

#### **10. What is the purpose of the `conftest.py` file in Pytest?**

**Answer:**

The `conftest.py` file is used to share fixtures and hooks across multiple test files in a directory. Pytest automatically detects this file and makes its fixtures available to all tests in the directory hierarchy.

**Real-Time Use:**

Common fixtures like database connections or configuration setups can be placed in `conftest.py` to avoid code duplication.

---

### **Intermediate Level Questions**

---

#### **11. How do you use markers in Pytest, and what are they used for?**

**Answer:**

Markers are used to categorize tests and can be used to selectively run subsets of tests. You can use built-in markers or define custom ones.

**Syntax Example:**

Defining and using a custom marker:

```python
import pytest

@pytest.mark.slow
def test_heavy_computation():
    # test code
```

Running tests with a specific marker:

```bash
pytest -m slow
```

**Real-Time Use:**

Markers help in organizing tests, such as separating fast unit tests from slow integration tests, and running them accordingly.

---

#### **12. How do you capture log output in Pytest?**

**Answer:**

Use the `caplog` fixture to capture log messages emitted during test execution.

**Syntax Example:**

```python
def test_logging(caplog):
    import logging
    logger = logging.getLogger()
    logger.warning("This is a warning")
    assert "This is a warning" in caplog.text
```

**Real-Time Use:**

Capturing logs is essential for verifying that your application logs the correct messages at the appropriate log levels.

---

#### **13. What are Pytest plugins, and how do you use them?**

**Answer:**

Pytest plugins are add-ons that extend Pytest's functionality. They can provide additional fixtures, markers, or command-line options.

**Syntax Example:**

Installing a plugin:

```bash
pip install pytest-cov
```

Using the plugin:

```bash
pytest --cov=my_package
```

**Real-Time Use:**

Plugins like `pytest-cov` for coverage reporting, `pytest-mock` for mocking, and `pytest-xdist` for parallel execution enhance testing capabilities.

---

#### **14. How do you write setup and teardown code in Pytest?**

**Answer:**

You can write setup and teardown code using fixtures with the `yield` statement.

**Syntax Example:**

```python
import pytest

@pytest.fixture
def resource():
    # Setup code
    res = setup_resource()
    yield res
    # Teardown code
    teardown_resource(res)
```

**Real-Time Use:**

Setting up and tearing down resources like files, databases, or network connections is crucial for tests that require specific environments.

---

#### **15. How do you share fixtures across multiple test files?**

**Answer:**

Place the fixture in a `conftest.py` file located in the directory containing the test files. Pytest will make these fixtures available to all tests in that directory and subdirectories.

**Syntax Example (`conftest.py`):**

```python
import pytest

@pytest.fixture
def shared_fixture():
    # Fixture code
    yield data
```

**Real-Time Use:**

Shared fixtures promote code reuse and consistency across your test suite.

---

#### **16. How do you mock objects or functions in Pytest?**

**Answer:**

You can use the `unittest.mock` module or the `pytest-mock` plugin to mock objects or functions.

**Syntax Example with `unittest.mock`:**

```python
from unittest.mock import patch

def test_mock_function():
    with patch('module.function_to_mock') as mock_func:
        mock_func.return_value = 'mocked value'
        result = function_under_test()
        assert result == 'expected result'
```

**Real-Time Use:**

Mocking is essential for isolating the code under test and controlling the behavior of external dependencies.

---

#### **17. How do you parameterize fixtures in Pytest?**

**Answer:**

Use the `params` argument in the `@pytest.fixture` decorator to parameterize fixtures.

**Syntax Example:**

```python
import pytest

@pytest.fixture(params=[0, 1, 2])
def number(request):
    return request.param

def test_is_even(number):
    assert number % 2 == 0
```

**Real-Time Use:**

Parameterizing fixtures allows you to run tests with different setups, enhancing test coverage.

---

#### **18. How do you use the `tmpdir` fixture in Pytest?**

**Answer:**

The `tmpdir` fixture provides a temporary directory unique to the test invocation.

**Syntax Example:**

```python
def test_temp_file(tmpdir):
    file = tmpdir.join("sample.txt")
    file.write("hello world")
    assert file.read() == "hello world"
```

**Real-Time Use:**

Useful for testing code that reads from or writes to the filesystem without affecting the real environment.

---

#### **19. How do you write tests for code that interacts with databases using Pytest?**

**Answer:**

Use fixtures to set up a test database or mock the database interactions.

**Syntax Example:**

```python
@pytest.fixture
def db_session():
    session = setup_test_db()
    yield session
    teardown_test_db(session)

def test_db_query(db_session):
    result = db_session.query(User).all()
    assert len(result) == expected_count
```

**Real-Time Use:**

Testing database interactions ensures your data access layer works correctly and handles data as expected.

---

#### **20. How can you run tests in parallel using Pytest?**

**Answer:**

Use the `pytest-xdist` plugin to run tests in parallel.

**Syntax Example:**

Install the plugin:

```bash
pip install pytest-xdist
```

Run tests in parallel:

```bash
pytest -n 4  # Runs tests on 4 CPUs
```

**Real-Time Use:**

Parallel test execution reduces overall testing time, which is beneficial in large projects and CI pipelines.

---

### **Advanced Level Questions**

---

#### **21. Explain the concept of fixtures scope in Pytest.**

**Answer:**

Fixture scope determines how often a fixture is executed:

- **Function (default):** The fixture is executed for each test function.
- **Class:** The fixture is executed once per test class.
- **Module:** The fixture is executed once per module (test file).
- **Package:** The fixture is executed once per package.
- **Session:** The fixture is executed once per test session.

**Syntax Example:**

```python
@pytest.fixture(scope="module")
def db_connection():
    conn = create_connection()
    yield conn
    conn.close()
```

**Real-Time Use:**

Using appropriate fixture scopes optimizes resource usage and test execution time, especially when setup is expensive.

---

#### **22. How do you customize Pytest's test discovery?**

**Answer:**

You can customize test discovery by modifying the `pytest.ini` configuration file or using command-line options.

**Syntax Example (`pytest.ini`):**

```ini
[pytest]
python_files = test_*.py check_*.py
python_functions = test_* check_*
```

**Real-Time Use:**

Customization is helpful when integrating Pytest into projects with existing naming conventions that differ from the defaults.

---

#### **23. How do you write a plugin for Pytest?**

**Answer:**

Create a module or package that implements Pytest hooks and entry points.

**Syntax Example:**

```python
# myplugin.py
def pytest_addoption(parser):
    parser.addoption("--myopt", action="store", default="default", help="My custom option")

def pytest_configure(config):
    myopt = config.getoption("--myopt")
    # Plugin logic using myopt
```

Register the plugin in `setup.py`:

```python
setup(
    # ...
    entry_points={
        'pytest11': [
            'myplugin = myplugin',
        ],
    },
)
```

**Real-Time Use:**

Custom plugins extend Pytest's functionality, allowing integration with other tools or frameworks.

---

#### **24. How do you perform code coverage analysis with Pytest?**

**Answer:**

Use the `pytest-cov` plugin to measure code coverage.

**Syntax Example:**

Install the plugin:

```bash
pip install pytest-cov
```

Run tests with coverage:

```bash
pytest --cov=your_package tests/
```

Generate an HTML report:

```bash
pytest --cov=your_package --cov-report=html tests/
```

**Real-Time Use:**

Code coverage helps identify untested parts of your codebase, ensuring comprehensive testing.

---

#### **25. How do you integrate Pytest with Continuous Integration tools like Jenkins or Travis CI?**

**Answer:**

Add the `pytest` command to your CI configuration file.

**Syntax Example (Jenkins Pipeline):**

```groovy
pipeline {
    stages {
        stage('Test') {
            steps {
                sh 'pytest'
            }
        }
    }
}
```

**Real-Time Use:**

Automated testing in CI pipelines ensures code quality and detects issues early in the development process.

---

#### **26. How do you handle flaky tests in Pytest?**

**Answer:**

Use the `pytest-rerunfailures` plugin to automatically rerun failed tests.

**Syntax Example:**

Install the plugin:

```bash
pip install pytest-rerunfailures
```

Run tests with reruns:

```bash
pytest --reruns 3
```

**Real-Time Use:**

Rerunning flaky tests helps reduce false negatives due to intermittent failures caused by timing issues or external dependencies.

---

#### **27. What is the difference between `yield` and `return` in Pytest fixtures?**

**Answer:**

- **`return`:** Ends the fixture function; no teardown code can be added after.
- **`yield`:** Pauses the fixture, runs the test, and then resumes for teardown code after the `yield` statement.

**Syntax Example with `yield`:**

```python
@pytest.fixture
def resource():
    setup_resource()
    yield
    teardown_resource()
```

**Real-Time Use:**

`yield` allows you to include teardown logic in the same fixture, ensuring resources are cleaned up after tests run.

---

#### **28. How do you use command-line options to configure Pytest behavior?**

**Answer:**

Use built-in or custom command-line options when running Pytest.

**Syntax Example:**

```bash
pytest -v --tb=short  # Verbose output with short traceback
```

Define custom options in `conftest.py`:

```python
def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", help="Environment to run tests against")

@pytest.fixture
def env(request):
    return request.config.getoption("--env")
```

**Real-Time Use:**

Command-line options allow you to customize test runs dynamically, such as selecting environments or enabling debug modes.

---

#### **29. How do you write parameterized tests with multiple parameters in Pytest?**

**Answer:**

Use `@pytest.mark.parametrize` with multiple arguments.

**Syntax Example:**

```python
import pytest

@pytest.mark.parametrize("input1, input2, expected", [
    (2, 3, 5),
    (1, -1, 0),
    (0, 0, 0),
])
def test_addition(input1, input2, expected):
    assert input1 + input2 == expected
```

**Real-Time Use:**

Testing functions with various combinations of inputs ensures they handle all expected cases.

---

#### **30. How do you debug failing tests in Pytest?**

**Answer:**

Use the `--pdb` option to invoke the Python debugger on test failure.

**Syntax Example:**

```bash
pytest --pdb
```

Alternatively, insert a breakpoint in your code:

```python
def test_function():
    import pdb; pdb.set_trace()
    # Test code
```

**Real-Time Use:**

Debugging failing tests helps identify and fix issues by inspecting the state of the application at the point of failure.

---
