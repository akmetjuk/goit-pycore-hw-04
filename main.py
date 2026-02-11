from HWTask1.task_1 import total_salary
from HWTask2.task2 import get_cats_info
from HWTask3.task3 import print_all_files_and_directories as print_path_info
from HWTask4.MyPersonalAssistance import main as assistant_bot
import pathlib
import sys


if __name__ == "__main__":
    current_dir = pathlib.Path(__file__).parent

    print(f"{'=' * 8} task #1 checking")
    total, average = total_salary(current_dir / "HWTask1" / "sallary.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    try:
        total_salary(current_dir / "HWTask1" / "non_existent_sallary_file.txt")
    except Exception as e:
        print(e)

    try:
        total_salary(current_dir / "HWTask1" / "sallary_nonUTF-8.txt")
    except Exception as e:
        print(e)

    print(f"{'=' * 8} task #2 checking")
    cats_info = get_cats_info(current_dir / "HWTask2" / "cats.txt")
    print(cats_info)

    print(f"{'=' * 8} task #3 checking")

    args = sys.argv[1:]  # Отримуємо аргументи командного рядка, пропускаючи ім'я скрипта
    print(f"Arguments: {args}")
    print_path_info(args[0] if args else current_dir / ".venv")

    try:
        print_path_info(current_dir / "SomeNonExistentDirectory")
    except Exception as e:
        print(e)

    print(f"{'=' * 8} task #4 checking")
    assistant_bot()
