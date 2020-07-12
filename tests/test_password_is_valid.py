from password_checker.password_checker import Password

# Testing password is valid
password_test = "De9fdtvdo%"


def test_password_exist():
    assert Password(password_test).password_exist() == True


def test_password_length():
    assert Password(password_test).password_length() == True


def test_password_lowercase():
    assert Password(password_test).password_lowercase() == True


def test_password_uppercase():
    assert Password(password_test).password_uppercase() == True


def test_password_digit():
    assert Password(password_test).password_digit() == True


def test_password_special_charcter():
    assert Password(password_test).password_special_character() == True
