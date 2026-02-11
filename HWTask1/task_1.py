

def total_salary(path: str) -> tuple[int, int]:
    """Обчислити загальну та середню суму заробітної плати..

    Args:
        path: Шлях до файлу з даними про заробітну плату

    Returns:
        tuple: Загальна сума заробітної плати та середня сума заробітної плати

    Raises:
        FileNotFoundError: Якщо файл за вказаним шляхом не знайдено
        UnicodeDecodeError: Якщо файл не може бути прочитаний через проблеми з кодуванням
    """
    try:
        with open(path, 'r', encoding="utf-8") as file:
            lines = file.readlines()
            total = 0
            for line in lines:
                parts = line.split(',')
                if len(parts) >= 2:
                    try:
                        salary = int(parts[1].strip())
                        total += salary if salary > 0 else 0
                    except ValueError:
                        continue
            average_salary = total / len(lines) if lines else 0
            return total, average_salary
    except UnicodeDecodeError:
        raise
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл за шляхом {path} не знайдено.")
