from password_checker.password_checker import Password

# Testing password is valid
special_character = ['%', '&', '*', '"', "'"]

password_test = "DemonHybrid%8"
password_valid = Password(password_test)


def test_password_exist():
    assert password_valid.password_exist() == True


def test_password_length():
    assert password_valid.password_length() == True


def test_password_lowercase():
    assert password_valid.password_lowercase() == True


def test_password_uppercase():
    assert password_valid.password_uppercase() == True


def test_password_digit():
    assert password_valid.password_digit() == True


def test_password_special_charcter():
    assert password_valid.password_special_character() == True
