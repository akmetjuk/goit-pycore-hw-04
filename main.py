from HWTask1.task_1 import total_salary
import pathlib


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
