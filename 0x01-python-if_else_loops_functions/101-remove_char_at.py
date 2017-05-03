def remove_char_at(str, n):
    newstring = str[:n] + str[n + 1:]
    if n < 0:
        return(str)
    else:
        return(newstring)
