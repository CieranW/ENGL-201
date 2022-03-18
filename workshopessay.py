import textwrap


def main_function(essay_count):
    if essay_count == 0:
        print(
            "Which essay would you like to read first?\n")
        choose_an_essay = essay_selector(essay_choices)
        if essay_choices[choose_an_essay] == "My first memory":
            essay_choices.remove("My first memory")
            essay_count += 1
            essay1()
            main_function(essay_count)

        elif essay_choices[choose_an_essay] == "The concept of muscle memory":
            essay_choices.remove("The concept of muscle memory")
            essay_count += 1
            essay2()
            main_function(essay_count)

        elif essay_choices[choose_an_essay] == "Why do I do this to myself?":
            essay_choices.remove("Why do I do this to myself?")
            essay_count += 1
            essay3()
            main_function(essay_count)

    elif essay_count < 3:
        input("Which essay would you like to read next?\n")
        choose_an_essay = essay_selector(essay_choices)
        if essay_choices[choose_an_essay] == "My first memory":
            essay_choices.remove("My first memory")
            essay_count += 1
            essay1()
            main_function(essay_count)

        elif essay_choices[choose_an_essay] == "The concept of muscle memory":
            essay_choices.remove("The concept of muscle memory")
            essay_count += 1
            essay2()
            main_function(essay_count)

        elif essay_choices[choose_an_essay] == "Why do I do this to myself?":
            essay_choices.remove("Why do I do this to myself?")
            essay_count += 1
            essay3()
            main_function(essay_count)

    else:
        input("Thank you for tagging along, I hope you enjoy that little journey.")


# Functions to help connect/modify appearances of main body.


def essay_selector(essay_choices):
    for number in range(0, len(essay_choices)):
        print("("+str(number+1)+") " + essay_choices[number] + '\n')
    selected = chooser(essay_choices)
    return selected


def chooser(essay_choices):
    try:
        selected = int(input("Enter the number of your choice: ")) - 1
        if selected >= len(essay_choices):
            print("Invalid input, try again.")
            selected = chooser(essay_choices)
        return selected
    except (NameError, SyntaxError, ValueError):
        print("Invalid input, try again.")
        selected = chooser(essay_choices)
    return selected


def responder():
    response = int(input("Enter the number of your choice: "))
    if response not in [1, 2]:
        print("Please enter a valid number.")
        responder()
    return response


def format_headers(header):
    pass


def format_main_text(text):
    pass


# Essays, introduction, conclusion, and connectors for essays.


def intro():
    input("\nGuess I'm doing this again\n")
    input("How do I even begin? The last time I did this, I'll admit it was a little rough.\n")
    input("However, this time I'll try to incorporate different elements that can be controlled, such as the type of font and size, color of font, and spacing/text appearance.\n")
    input("This should be fun, so hang tight.\n")


def essay1():
    # Title, needs to be centered, bold font, size 12, Times New Roman.
    format_headers("Sexualizing Food")
    input("Perhaps it needs to be said, the title is incorrect and simply an act of humor, I will not be sexualizing food in this part of the essay. I can not stress that enough.")


def essay2():
    # Title, needs to be centered, bold font, size 12, Times New Roman.
    format_headers("The Mind and Body in all its glory")


def essay3():
    # Title, needs to be centered, bold font, size 12, Times New Roman.
    format_headers("Pain and Agony brings Beauty and Appreciation into play")


# Global variables/lists
essay_titles = ["Sexualizing Food", "The Mind and Body in all its glory",
                "Pain and Agony brings Beauty and Appreciation into play"]

essay_choices = ["My first memory",
                 "The concept of muscle memory", "Why do I do this to myself?"]
essay_count = 0
# Calling on the functions in order.
intro()
main_function(essay_count)
