def return_10():
    return 10

def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    return num_1 / num_2

def length_of_string(string_input):
    return len(string_input)

def join_string(str_1, str_2):
    return str_1 + str_2

def add_string_as_number(str_1, str_2):
    return int(str_1) + int(str_2)

def number_to_full_name__month(input_month_number):
    month = None
    if input_month_number == 1:
        month = "January"
    elif input_month_number == 3:
        month = "March"
    elif input_month_number == 4:
        month = "April"
    elif input_month_number == 9:
        month = "September"
    elif input_month_number == 10:
        month = "October"
    return month


def number_to_short_month_name__month(month_number_input):
    short_number = number_to_full_name__month(month_number_input)[0:3]
    return short_number


def volume_of_cube(side_length):
    return side_length ** 3

def reverse_string(string_input):
    string_reversed = ""
    index = len(string_input)
    while index > 0:
        string_reversed += string_input[index - 1]
        index = index - 1
    return string_reversed

def farenheit_to_celsius(temperature_in_farenheit):
    return int((temperature_in_farenheit - 32)/1.8)