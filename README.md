# Тема 4. Асинхронне програмування в Python

Напишіть Python-скрипт, який буде читати всі файли у вказаній користувачем вихідній папці (source folder) і розподіляти їх по підпапках у директорії призначення (output folder) на основі розширення файлів. Скрипт повинен виконувати сортування асинхронно для більш ефективної обробки великої кількості файлів.

## Технічний опис завдання

1. Імпортуйте необхідні асинхронні бібліотеки.
2. Створіть об'єкт `ArgumentParser` для обробки аргументів командного рядка.
3. Додайте необхідні аргументи для визначення вихідної та цільової папок.
4. Ініціалізуйте асинхронні шляхи для вихідної та цільової папок.
5. Напишіть асинхронну функцію `read_folder`, яка рекурсивно читає всі файли у вихідній папці та її підпапках.
6. Напишіть асинхронну функцію `copy_file`, яка копіює кожен файл у відповідну підпапку у цільовій папці на основі його розширення.
7. Налаштуйте логування помилок.
8. Запустіть асинхронну функцію `read_folder` у головному блоці.

## Рішення
Основний код  
[goit_pythonweb_hw_04/main.py](goit_pythonweb_hw_04/main.py)

Запуск: `main.py [-h] [--log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}] source destination` 
- source - вихідна директорія (source folder)
- destination - директорія призначення (output folder)
```bash
usage: main.py [-h] [--log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}] source destination

positional arguments:
  source                Source path
  destination           Destination path

options:
  -h, --help            show this help message and exit
  --log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}, -l {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        Set the logging level

```