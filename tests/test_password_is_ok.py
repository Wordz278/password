from password_checker.password_checker import Password

# Testing password is ok
password_test = "De9fdtvdo%"

def test_password_is_ok():
    assert Password(password_test).password_is_ok() == True
