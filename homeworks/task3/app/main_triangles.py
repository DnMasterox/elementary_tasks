"""

3. Sorting triangles
Develop a console program that performs the output of triangles in descending
    order of their area.
After adding each new triangle, the program asks if the user wants to add one
    more.
If the user answers "y" or "yes" (not case sensitive), the program will ask to
    enter data for another triangle,otherwise - print the result to the
        console.
Calculation of the area of ​​the triangle should be made according to Heron's
    formula.
• Each triangle is defined by the name and lengths of its sides.
Input format (comma delimited):
<name>, <side length>, <side length>, <side length>
• The application must handle the input of floating-point numbers.
• Input must be case-insensitive, spaces, and tobacco.
• The output of the data should be the following example:
============= Triangles list: ===============
1. [Triangle first]: 17.23 cm
2. [Triangle 22]: 13 cm
3. [Triangle 1]: 1.5 cm

"""

from homeworks.task3.app.triangles import Triangle
from homeworks.conditions.instructions import is_not_empty

INSTRUCTION = 'For correct working of this program,please! Enter ' \
              'triangle`s name and it`s sides separated by "," : '
__author__ = 'nshumakov'


def start_function() -> None:
    triangles_array = []
    run = True  # running flag
    while run:
        input_data = input('Enter triangle`s name and it`s sides separated'
                           ' by "," : ' + "\n")
        if is_not_empty(input_data, INSTRUCTION):
            try:
                input_data = input_data.split(',')
                if is_triangle(float(input_data[1]), float(input_data[2]),
                               float(input_data[3])):
                    my_triangle = Triangle(str(input_data[0]),
                                           float(input_data[1]),
                                           float(input_data[2]),
                                           float(input_data[3]))
                    my_triangle.calculate_area()
                    triangles_array.append(my_triangle)
                    print("Triangle was added")
                else:
                    print("Triangle with sides " + input_data[1] + " " +
                          input_data[2] + " " + input_data[
                        3] + " can not exist!")
            except IndexError:
                print("Entered data is incorrect, please  enter the correct "
                      "data!")
            run = is_not_exit()
        else:
            quit()

    print("=====Triangle list:====")
    # sort triangles by their area
    x = sorted(triangles_array, key=lambda x: x.get_area(), reverse=True)
    for i in x:
        i.to_print()


def is_triangle(side_a, side_b, side_c) -> bool:
    """

    check for the existence of a triangle
    :param side_a: triangle side
    :param side_b: triangle side
    :param side_c: triangle side

    """
    try:
        if side_a + side_b > side_c and side_a + side_c > side_b and side_b \
                + side_c > side_a > 0 and side_b > 0 and side_c > 0:
            return True
        else:
            return False
    except ValueError:
        print("Entered not int values")
        return False


def is_not_exit() -> bool:
    """
    requirement of condition

    """
    continue_str = input("Do you want to continue?")
    if "y" in continue_str.lower():
        return True
    else:
        return False


if __name__ == '__main__':
    start_function()
