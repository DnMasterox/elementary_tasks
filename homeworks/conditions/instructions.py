__author__ = 'nshumakov'


def is_not_empty(entered_value, instructions_to_show) -> bool:
    """
    show instructions if "entered_value" will be empty
    :param entered_value: data to check
    :param instructions_to_show: instruction that must be output with an empty
        input any parameter
    :return: True/False

    """
    if str(entered_value).__len__() == 0:
        print(instructions_to_show)
        return False
    else:
        return True
