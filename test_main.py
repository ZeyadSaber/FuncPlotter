import main

app = main.MyAPP

def test_validate_x():
    assert app.validate_x(app, "sda", 3) == -1
    assert app.validate_x(app, 4, 3) == 0
    assert app.validate_x(app, 1, 3) == 1

def test_validate_y():
    assert app.validate_y(app, [0, 1, 2], "e^x") == -1
    assert app.validate_y(app, [0, 1, 2], "s^2") == -2
    assert app.validate_y(app, [0, 1, 2], "exp(x") == 0
    assert app.validate_y(app, [0, 1, 2], "sin(x)") == "sin(x)"
