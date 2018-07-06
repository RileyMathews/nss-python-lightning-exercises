# defined function
def weird_function(list, num, str="hello"):
    for thing in list:
        print(thing)
    for thing in list[:num]:
        print(f"{str} {thing}")

# define arguments for function
my_list = ["New York", "Dallas", "San Antonio", "Nashville"]   
my_number = 3
my_string = "I have visited"

# call function with and without using the default string parameter
weird_function(my_list, my_number)
weird_function(my_list, my_number, my_string)