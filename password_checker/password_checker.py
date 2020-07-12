import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    '%(levelname)s - %(asctime)s -  %(message)s')

file_handler = logging.FileHandler('error.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)


logger.addHandler(file_handler)
logger.addHandler(stream_handler)


class Password:

    def __init__(self, password):
        self.password = password

    def password_exist(self):
        if not self.password:
            raise NameError("Password should exist")
        else:
            return True

    def password_length(self):
        if len(self.password) < 8:
            raise ValueError(
                "Password should be longer or equal than 8 characters")
        else:
            return True

    def password_lowercase(self):
        if not any(char.islower() for char in self.password):
            raise ValueError(
                "Password should have atleast one lowercase letter")
        else:
            return True

    def password_uppercase(self):
        if not any(char.isupper() for char in self.password):
            raise ValueError(
                "Password should have at least one uppercase letter")
        else:
            return True

    def password_digit(self):
        if not any(char.isdigit() for char in self.password):
            raise ValueError(
                "Password should at least have one digit")
        else:
            return True

    def password_special_character(self):
        special_character = ['%', '&', '*', '"', "'"]

        if not any(char in special_character for char in self.password):
            raise ValueError(
                f"Password should have at least one of the special characters {special_character}")
        else:
            return True

    def password_is_ok(self):
        pass_gauge = 0         
        if self.password_exist() == True:
            pass_gauge += 1
        if self.password_length() == True:
            pass_gauge += 1
        if self.password_digit() == True:
            pass_gauge += 1
        if self.password_lowercase() == True:
            pass_gauge += 1
        if self.password_uppercase() == True:
            pass_gauge += 1
        if self.password_special_character() == True:
            pass_gauge += 1
        if pass_gauge > 3:
            return True


if __name__ == '__main__':

    password = "fsgjdgD<%4"

    try:
        if (Password(password).password_is_ok() == True):
            logger.debug("User password is ok")
        else:
            logger.debug("User password is not ok")
    except (NameError, ValueError) as error:
        logger.error(error)
