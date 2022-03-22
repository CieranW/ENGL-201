import textwrap


def main_function(essay_count):
    if essay_count == 0:
        print(lbb + "Which essay would you like to read first?" + lbb)
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
        print(lbb + "Which essay would you like to read next?" + lbb)
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

    elif essay_count == 3:
        print("Thank you for tagging along, I hope you enjoyed that little journey.")
        input("Would you like to read the essays again?")
        print("\n (a) Yes, I would like to bore myself some more as I have nothing better to do. \n (b) No, I have better things to do.\n")
        run_it_back = str(
            input("Indulge me and enter a letter that suits your satisfaction: "))
        a = "a"
        b = "b"
        for value in run_it_back:
            if value == a:
                print("Wrong choice! Back to the start we go.")
                essay_count -= 3
                essay_choices.extend(["My first memory",
                                     "The concept of muscle memory", "Why do I do this to myself?"])
                main_function(essay_count)
            elif value == b:
                print("I understand, enjoy the time you have left.")
            break


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


# def responder():
#     response = int(input("Enter the number of your choice: "))
#     if response not in [1, 2]:
#         print("Please enter a valid number.")
#         responder()
#     return response


def format_headers(header):
    print(lbb + (header.center(24, " ")) + lbb)


def format_main_text(text):
    input(textwrap.fill('\n' + text + '\n'))


# Essays, introduction, conclusion, and connectors for essays.


def intro():
    format_headers("Another One")
    format_main_text(
        "How do I even begin? The last time I did this, I'll admit it was a little rough.")
    format_main_text("However, this time I'll try to incorporate different elements that can be controlled, such as the type of font and size, color of font, and spacing/text appearance.")
    format_main_text("This should be fun, so hang tight.")


def essay1():
    # Title, needs to be centered, bold font, size 12, Times New Roman.
    format_headers("Sexualizing Food")
    format_main_text("Perhaps it needs to be said, the title is incorrect and simply an act of humor, I will not be sexualizing food in this part of the essay. I can not stress that enough.")
    format_main_text("""
    Greece was gorgeous, but how would I know? For one, I was four years old, and my memory is outright terrible, I can barely recall what happened last week, much less hope to remember events that transpired almost fifteen years ago. However, one thing is clear as day, the food was bloody amazing. Fresh seafood, beautifully grown olives made into sensational olive oil, and so much more. It was heaven for the taste buds.""")

    format_main_text("""
    Up till that point before I had gone to Greece, I was a rather picky eater, only plain spaghetti would suffice, everything else was a coin toss and my parents never knew if I would eat it. Therefore, it was plausible that there was concern regarding how I would react to a new kind of cuisine on a different continent in a new country. Thankfully, to my parents' delight, I loved the food Greece had to offer; one of my personal favorites that I still crave on a daily basis is grilled octopus.""")

    format_main_text("""
    The grilled octopus that I had in Greece was an abomination of flavors. Perfectly tender to the point where it melted in your mouth but still kept this degree of bounce and chewiness desired in shellfish and octopus. Finished with a drizzle of fresh, virgin olive oil and a crank of black pepper, at that time in my life, it was the greatest thing I had ever tasted. Greece had an abundant amount of fresh seafood which I have come to enjoy and appreciate, especially in a place landlocked, like Arizona.""")

    format_main_text("""
    Seafood can be a hit or miss for most people, however, when cooked correctly, the meat becomes a perfect symphony of sweet and salty, an orchestra of delight and wonder. It truly was an eye-opening experience, or rather a mouthwatering experience to taste food that paid homage to the quality and freshness of the catch, while playing around and beautifying it further to enhance the flavor and make it define what Greece and Greek food is. That was my first experience with food that I truly remember to this day, and I have strived to experience and appreciate food for what it is: not a mismatch of ingredients hoping to vomit out a perfect combo, but rather a dish that preserves the quality of the produce, while enhancing it further to broaden one's horizons.""")


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

lbb = "\n------------------------------------------------------------\n"
lb = "------------------------------------------------------------\n"
essay_count = 0
# Calling on the functions in order.
intro()
main_function(essay_count)
