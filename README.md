# E1.12
[![Travis][build-badge]][build]

[build-badge]: https://img.shields.io/travis/ githubname / reponame /master.png?style=flat-square

[build]: https://travis-ci.org/ githubname / reponame

##### ля запуска тестов:
```
pytest -s tests.py
```

##### Для подсчета покрытия кода тестами:
```
coverage run -m pytest -s tests.py
```
```
coverage report -m
```

##### Настроена непрерывная интеграция с TRAVIS CI