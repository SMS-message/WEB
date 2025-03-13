def prompter(string_new):
    global strings
    for string in strings:
        if string_new in string:
            return string
    strings.append(string_new)
    return string_new


strings = []
