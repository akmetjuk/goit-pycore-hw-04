import pathlib
from colorama import init, Fore


def print_all_files_and_directories(path):
    """Виводить в консоль всі файли та директорії за вказаним шляхом.

    Args:
        path: Шлях до директорії, з якої потрібно отримати список файлів та піддиректорій

    Returns:
        None: Функція виводить інформацію в консоль, не повертаючи значення.

    Raises:
        FileNotFoundError: Якщо директорія за вказаним шляхом не знайдена
        NotADirectoryError: Якщо вказаний шлях не є директорією
    """
    try:
        p = pathlib.Path(path)
        if not p.exists():
            raise FileNotFoundError(f"Директорія за шляхом {path} не знайдена.")
        if not p.is_dir():
            raise NotADirectoryError(f"Шлях {path} не є директорією.")
        init(autoreset=True)
        paths = sorted(p.rglob('*'))
        print(Fore.BLUE + f"📦 {p.name}/")
        for p in paths:
            # Рівень вкладеності
            level = len(p.relative_to(path).parts)
            indent = "    " * level
            if p.is_dir():
                print(indent + Fore.BLUE + f"📁 {p.name}/")
            else:
                print(indent + Fore.GREEN + f"📜 {p.stem}" + Fore.RED + f"{p.suffix}")
    except FileNotFoundError:
        raise
    except NotADirectoryError:
        raise
