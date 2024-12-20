""" 
Python-скрипт, який буде читати всі файли у вказаній користувачем
вихідній папці (source folder) і розподіляти їх по підпапках у директорії
призначення (output folder) на основі розширення файлів. Скрипт повинен
виконувати сортування асинхронно для більш ефективної обробки великої кількості
файлів.
 """

import argparse
import asyncio
import logging
from aiopath import AsyncPath
from aioshutil import copyfile

# todo 2. Створіть об'єкт ArgumentParser для обробки аргументів командного рядка.
parser = argparse.ArgumentParser()

# todo 3. Додайте необхідні аргументи для визначення вихідної та цільової папок.
parser.add_argument("source", type=str, help="Source path")
parser.add_argument("destination", type=str, help="Destination path")
parser.add_argument(
    "--log-level",
    "-l",
    # type=str,
    default="ERROR",
    choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
    help="Set the logging level",
)
args = parser.parse_args()

# налаштування логування
logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s")
logging.getLogger().setLevel(args.log_level.upper())

# todo 4. Ініціалізуйте асинхронні шляхи для вихідної та цільової папок.
source_path = AsyncPath(args.source)
destination_path = AsyncPath(args.destination)


# todo 5. Напишіть асинхронну функцію read_folder, яка рекурсивно читає всі файли у вихідній папці та її підпапках.
async def read_folder(_source_path: AsyncPath):
    """
    Асинхронна функція, яка рекурсивно читає всі файли у вихідній папці та її підпапках.
    Аргументи:
        source_path (AsyncPath): Коренева директорія, з якої починається читання.
    Повертає:
        AsyncPath: Шлях до кожного файлу та директорії, знайдених у вихідному шляху.
    """

    async for path in _source_path.rglob("*"):
        yield path


# todo 6. Напишіть асинхронну функцію copy_file, яка копіює кожен файл у відповідну підпапку у цільовій папці на основі його розширення.
async def copy_file(_file_path: AsyncPath, _destination_path: AsyncPath):
    """
    Асинхронно копіює файл до директорії призначення на основі його розширення.
    Аргументи:
        _file_path (AsyncPath): Шлях до файлу, який потрібно скопіювати.
        _destination_path (AsyncPath): Коренева директорія, куди буде скопійовано файл (в піддиректорію з назвою відповідно розширенню).
    Логи:
        Записує повідомлення про помилку, якщо файл не може бути скопійований через помилку дозволу.
    """
    file_name = _file_path.name
    file_ext = _file_path.suffix

    try:
        dest_file_path = _destination_path / file_ext / file_name
        await dest_file_path.parent.mkdir(parents=True, exist_ok=True)
        await copyfile(_file_path, dest_file_path)
    except PermissionError as e:
        # todo 7. Налаштуйте логування помилок.
        logging.error("%s", e)


if __name__ == "__main__":
    # todo 8. Запустіть асинхронну функцію read_folder та скопіюйте всі файли з вихідної папки в цільову папку.
    async def main():
        """
        Асинхронно обробляє файли в вихідній папці та копіює їх до папки призначення.
        Ця функція читає файли з вказаного шляху вихідної папки та копіює кожен файл до вказаного
        шляху папки призначення. Вона веде журнал обробки кожного файлу.
        Аргументи:
            source_path (str): Шлях до вихідної папки, що містить файли для обробки.
            destination_path (str): Шлях до папки призначення, куди будуть копіюватися файли.
        Повертає:
            None
        """

        # Запустіть асинхронну функцію read_folder у головному блоці.
        async for path in read_folder(source_path):
            if path.is_file():
                logging.debug("processing %s", path)
                await copy_file(path, destination_path)

    asyncio.run(main())
    print("Done")
