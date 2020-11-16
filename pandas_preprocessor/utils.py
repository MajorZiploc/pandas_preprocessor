def foreach(action, iterable):
    for element in iterable:
        action(element)


def nc(supplier):
    try:
        return supplier()
    except AttributeError:
        return None
