def foreach(action, iterable):
    for element in iterable:
        action(element)


def nc(supplier):
    try:
        v = supplier()
    except AttributeError:
        v = None
