

def get_cats_info(path: str) -> list[dict[str, str | int]]:
    """
    Зчитати інформацію про котів з файлу та повернути її у вигляді списку словників.

    Args:
        path: Шлях до файлу з даними про котів

    Returns:
        list: Список словників, де кожен словник містить інформацію про кота (id, name, age)

    Raises:
        FileNotFoundError: Якщо файл за вказаним шляхом не знайдено
        UnicodeDecodeError: Якщо файл не може бути прочитаний через проблеми з коду
    """
    try:
        with open(path, 'r', encoding="utf-8") as file:
            lines = file.readlines()
            cats = []
            for line in lines:
                parts = line.split(',')
                if len(parts) >= 3:
                    try:
                        cat_id = parts[0].strip()
                        cat_alias = parts[1].strip()
                        cat_age = int(parts[2].strip())

                        cats.append({"id": cat_id, "name": cat_alias, "age": cat_age})
                    except ValueError:
                        continue
            return cats
    except UnicodeDecodeError:
        raise
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл за шляхом {path} не знайдено.")
