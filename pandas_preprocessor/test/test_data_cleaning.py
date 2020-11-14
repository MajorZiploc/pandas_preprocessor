from build import *


def func(x):
    main()
    return x + 1


def test_answer():
    assert func(3) == 5
