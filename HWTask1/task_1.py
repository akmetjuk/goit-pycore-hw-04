

def total_salary(path: str) -> tuple[int, int]:
    """Обчислити загальну та середню суму заробітної плати..

    Args:
        path: Шлях до файлу з даними про заробітну плату

    Returns:
        tuple: Загальна сума заробітної плати та середня сума заробітної плати

    Raises:
        ValueError: Якщо формат даних у файлі неправильний або якщо файл не існує
    """
    with open(path, 'r', encoding="utf-8") as file:
        lines = file.readlines()
        total = 0
        for line in lines:
            parts = line.split(',')
            if len(parts) >= 2:
                try:
                    salary = int(parts[1].strip())
                    total += salary
                except ValueError:
                    continue
        average_salary = total / len(lines) if lines else 0
        return total, average_salary