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

def number_to_full_name__month_1(input_month_number):
    month = None
    if input_month_number == 1:
        month = "January"
    return month

def number_to_full_name__month_3(input_month_number):
    month = None
    if input_month_number == 3:
        month = "March"
    return month

def number_to_full_month_name(input_month_number):
    month = None
    if input_month_number == 9:
        month = "September"
    return month

def number_to_short_month_name__month_1(month_input):
    month = None
    if month_input == 1:
        month = "Jan"
    
    return month

def number_to_short_month_name__month_4(month_input):
    month = None

    if month_input == 4:
        month = "Apr"
    
    return month

def number_to_short_month_name__month_10(month_input):
    month = None
    
    if month_input == 10:
        month = "Oct"

    return month

def volume_of_cube(side_length):
    return side_length ** 3

def reverse_string(string_input):
    return string_input[::-1]

def farenheit_to_celsius(temperature_in_farenheit):
    return int((temperature_in_farenheit - 32)/1.8)