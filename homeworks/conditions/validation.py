__author__ = 'nshumakov'


def is_validated(int_value):
    """
    if entered value > 0 "True" will be returned, else will be returned
        "False" for all variations
    :param int_value: entered value for validation
    :return:True/False

    """
    try:
        if int(int_value) > 0:
            return True
        else:
            print("Incorrect value was entered")
            return False
    except ValueError:
        print("Incorrect value was entered")
        return False


def is_validated_fibonacci(int_value):
    """

    if entered value >= 0 "True" will be returned, else will be returned
        "False" for all variations
    :param int_value: entered value for validation
    :return:True/False

    """
    try:
        if int(int_value) >= 0:
            return True
        else:
            print("Incorrect value was entered")
            return False
    except ValueError:
        print("Incorrect value was entered")
        return False
