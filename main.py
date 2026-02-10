from HWTask1.task_1 import total_salary
import pathlib


if __name__ == "__main__":
    current_dir = pathlib.Path(__file__).parent
    total, average = total_salary(current_dir / "HWTask1" / "salary.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")