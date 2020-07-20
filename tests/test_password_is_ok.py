from password_checker.password_checker import Password

def test_password_is_ok():
    assert Password("De9fdtvdo%").password_is_ok() == True
