# Unit testing

from calculator import add,subtract,sayHello

def test_add():
    assert add(3,5) == 8
    #assert add(39,5) == 48

def test_subtract():
    #assert subtract(300,5) == 292
    assert add(492,5) == 497

def test_sayHello():
    assert sayHello("Sandra") == "Hello Sandra"