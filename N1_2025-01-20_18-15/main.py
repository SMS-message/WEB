import os
import os.path


def human_read_format(size: int) -> str:
    if size < 1024:
        return f"{size}Б"
    size /= 1024
    size = round(size)
    if size < 1024:
        return f"{size}КБ"
    size /= 1024
    size = round(size)
    if size < 1024:
        return f"{size}МБ"
    size /= 1024
    size = round(size)
    return f"{size}ГБ"


def get_files_sizes() -> str:
    names = [*filter(lambda x: os.path.isfile(x), os.listdir())]
    # Данные должны быть возвращены в виде одной строки
    return " ".join(sorted([f"{name} {human_read_format(os.path.getsize(name))}" for name in names]))


if __name__ == "__main__":
    get_files_sizes()
