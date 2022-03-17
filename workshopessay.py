def intro():
    input("\nGuess I'm doing this again.\n")
    input("However, this time I'll try to incorporate different elements that can be controlled, such as the type of font and size, color of font, and spacing/text appearance.\n")
    input("This should be fun.\n")


def essay1():
    input("First memory goes here.")


def essay2():
    input("Muscle memory goes here.")


def essay3():
    input("Thoughts on Experiment3.py go here.")


intro()
choose_which_essay_to_read_first = input(
    "Which essay would you like to read first? \nOption a) My first memory \nOption b) An objective approach tackling the concept of muscle memory  \nOption c) Why do I do this to myself?\n")
if choose_which_essay_to_read_first == "a":
    essay1()
if choose_which_essay_to_read_first == "b":
    essay2()
if choose_which_essay_to_read_first == "c":
    essay3()
# Need to figure out how to make it so that when no value or an invalid value is entered, the question is asked again.
# if choose_which_essay_to_read_first != "a" and "b" and "c":
#     choose_which_essay_to_read_first
