
# Linux/Mac

### Создание
``` python -m venv venv ```
### Активация
``` source venv/bin/activate ```
### Деактивация
``` deactivate ```

# Windows
## Создание
```python -m venv venv```
### или
```py -3.11 -m venv venv```
## Активация (CMD)
```venv\Scripts\activate```
## Активация (PowerShell)
```venv\Scripts\Activate.ps1```
### Если ошибка в PowerShell:
```Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser```
### Деактивация
deactivate

# VSCode настройка
- Открыть проект в VSCode 

```Ctrl+Shift+P → "Python: Select Interpreter"```
## Выбрать путь к venv:
```Linux: ./venv/bin/python```

```Windows: ./venv/Scripts/python.exe```

# Генерация requirements.txt
### Активируем venv
source venv/bin/activate  # Linux/Mac 

venv\Scripts\activate     # Windows
### Генерируем requirements
```pip freeze > requirements.txt```
## Без venv (все пакеты системы):
```pip freeze > requirements.txt```