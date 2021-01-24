#!/usr/bin/env python

hello_str = "Hello World"

hello_int = 21

hello_bool = True

hello_tuple = (21, 32)

hello_list1 = ["Hello,", "this", "is", "a", "list"]

hello_list2 = list()
hello_list2.append("Hello,")
hello_list2.append("this")
hello_list2.append("is")
hello_list2.append("a")
hello_list2.append("list")

hello_dict = {"first_name" : "John",
    "last_name" : "Lunn",
    "eye_colour" : "Brown"}


print(hello_list1[4])
hello_list1[4] += "!"
print(hello_list1[4])

print(str(hello_tuple[0]))

print(hello_dict["first_name"] + " " + hello_dict["last_name"] + " has " + hello_dict["eye_colour"] + " eyes.")
print("{0} {1} has {2} eyes.".format(hello_dict["first_name"], hello_dict["last_name"], hello_dict["eye_colour"]))