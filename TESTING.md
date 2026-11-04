# Testing

The project uses `pytest` and `pytest-asyncio`.


## 1 Test Run

To run the tests, you need to specify the name of the test database

### Available databases

**postgresql**
**sqlite**

***

Run api tests

```bash
run_test_api.py postgresql
```

Run integration tests

```bash
run_test_integration.py sqlite
```

Run page tests

```bash
run_test_page.py postgresql
```

```bash
run_test_unit.py sqlite
```

Running all tests; by default, the sqlite database is used.

```bash
poetry run pytest tests
```


## 2. Test structure

The tests use the UnitOfWorkProtocol, so the tests themselves do not depend on a specific database implementation.

***

## 3. Cleaning the test database

After each test, the database is cleared via a fixture:

```python
get_uwo
```

**At the same time, the role table is preserved, since roles are the initial data of the test database.**

The databases that are created in the project directory after the test will be deleted.

***
# 4. Adding a new driver for tests

1. Install the driver
2. Add the driver name to the DriverName class [follow the link](.\src\domain\db\constants.py)
3. Add the DriverName class property of your driver to the corresponding database type in SUPPORTED_DATABASE_DRIVERS [follow the link](.\src\domain\db\constants.py)
4. Replace the driver in .env.test [follow the link](.env.test)

When using a new driver, errors may occur; the application was tested with default drivers.
