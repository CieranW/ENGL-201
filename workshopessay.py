import textwrap


def main_body(essay_count):
    intro()
    if essay_count == 0:
        print(
            "Which essay would you like to read first? \nOption a) My first memory \nOption b) An objective approach tackling the concept of muscle memory  \nOption c) Why do I do this to myself?\n")

        choose_essay_to_read = input("Enter the letter of your choice: ")


def intro():
    input("\nGuess I'm doing this again\n")
    input("How do I even begin? The last time I did this, I'll admit it was a little rough.\n")
    input("However, this time I'll try to incorporate different elements that can be controlled, such as the type of font and size, color of font, and spacing/text appearance.\n")
    input("This should be fun, so hang tight.\n")


def essay1():
    # Title, needs to be centered, bold font, size 12, Times New Roman.
    input("Sexualizing Food")


def essay2():
    # Title, needs to be centered, bold font, size 12, Times New Roman.
    input("The Mind and Body in all glory")


def essay3():
    # Title, needs to be centered, bold font, size 12, Times New Roman.
    input("Pain and Agony bring Beauty and Appreciation into play")


essay_choices = ["Sexualizing Food", "The Mind and Body in all glory",
                 "Pain and Agony bring Beauty and Appreciation into play"]
essay_count = 0
main_body(essay_count)
