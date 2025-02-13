def human_read_format(size: int):
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


if __name__ == '__main__':
    print(human_read_format(26843545711))
