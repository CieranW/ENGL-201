import textwrap


def main_function(essay_count):
    if essay_count == 0:
        print(lbb + "What shall be your first memory to explore?" + lbb)
        choose_an_essay = essay_selector(essay_choices)
        if essay_choices[choose_an_essay] == "The very first time":
            # Try appending the removed essay into a new list to keep track of what is being added and use that to add a connecting function that links the essays together
            # Perhaps a counter will help keep track of the essays being added. If counter == 1 and the essay in the list is x, and then counter == 2 and essay in the list is y, inlcude a connecting statment in between x and y.
            essay_choices.remove("The very first time")
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
        print(lbb + "What shall be your next memory to explore?" + lbb)
        choose_an_essay = essay_selector(essay_choices)
        if essay_choices[choose_an_essay] == "The very first time":
            essay_choices.remove("The very first time")
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
        input(lbb + "Would you like to read the essays again?" + lbb)
        print(" (1) Yes, I would like to bore myself some more as I have nothing better to do. \n\n (2) No, I have better things to do.\n")
        run_it_back = responder()
        if run_it_back == 1:
            print("\nWrong choice! Back to the start we go.")
            essay_count -= 3
            essay_choices.extend(["The very first memory",
                                 "The concept of muscle memory", "Why do I do this to myself?"])
            main_function(essay_count)
        elif run_it_back == 2:
            finisher()


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
    print(lbb + (header.center(10, " ")) + lbb)


def format_main_text(text):
    input(textwrap.fill('\n' + text + '\n'))

# Essays, introduction, conclusion, and connectors for essays.


def intro():
    # Title needs to be changed, something to do with memory. Also, I need a good intro paragraph into memory and how it relates to the essays.
    format_headers("Another One")
    format_main_text("We all have memories, be they good or bad, they define us and made us the people we are today. Our choices, fears, and desires are all influenced by events that have occurred in the past, no matter the level of significance. There are many different factors when it comes to remembering something: the significance of the event, importance or usefulness of the knowledge acquired, or how it has affected your life. In this short piece, I attempt to acknowledge these three particular areas of memory and the effects that they have.")


def essay1():
    format_headers("My First Time")
    format_main_text("There are plenty of events that have important impacts on one's life. For me, it had to be the very first memory that I can recall: My first trip to Greece with my parents and baby brother. Here it is: ")
    format_main_text("""
    Greece was gorgeous, but how would I know? For one, I was four years old, and my memory is outright terrible, I can barely recall what happened last week, much less hope to remember events that transpired almost fifteen years ago. However, one thing is clear as day, the food was bloody amazing. Fresh seafood, beautifully grown olives made into sensational olive oil, and so much more. It was heaven for the taste buds.
    """)

    format_main_text("""
    Up till that point before I had gone to Greece, I was a rather picky eater, only plain spaghetti would suffice, everything else was a coin toss and my parents never knew if I would eat it. Therefore, it was plausible that there was concern regarding how I would react to a new kind of cuisine on a different continent in a new country. Thankfully, to my parents' delight, I loved the food Greece had to offer; one of my personal favorites that I still crave on a daily basis is grilled octopus.
    """)

    format_main_text("""
    The grilled octopus that I had in Greece was an abomination of flavors. Perfectly tender to the point where it melted in your mouth but still kept this degree of bounce and chewiness desired in shellfish and octopus. Finished with a drizzle of fresh, virgin olive oil and a crank of black pepper, at that time in my life, it was the greatest thing I had ever tasted. Greece had an abundant amount of fresh seafood which I have come to enjoy and appreciate, especially in a place landlocked, like Arizona.
    """)

    format_main_text("""
    Seafood can be a hit or miss for most people, however, when cooked correctly, the meat becomes a perfect symphony of sweet and salty, an orchestra of delight and wonder. It truly was an eye-opening experience, or rather a mouthwatering experience to taste food that paid homage to the quality and freshness of the catch, while playing around and beautifying it further to enhance the flavor and make it define what Greece and Greek food is. That was my first experience with food that I truly remember to this day, and I have strived to experience and appreciate food for what it is: not a mismatch of ingredients hoping to throw out a perfect combo, but rather a dish that preserves the quality of the produce, while enhancing it further to broaden one's horizons.
    """)


def essay2():  # Did not flow with the rest of the piece, need to change how much I put in.
    format_headers("The Mind and Body in all its glory")
    format_main_text("""
    Knowledge is power, as the saying goes. This particular memory has a more direct effect as it is an exploration of what memory may truly be. In particular, I attempt to identify the true nature of muscle memory as it has long been a concept or an idea that I was aware of but never attempted to put any extra effort into discovering until a research paper prompted it. With this particular piece, I recognize the importance of memory and how it has helped to dictate certain philosophies and experiences. """)
    format_main_text(
        "I present an excerpt of the mind and body string theory: ")
    format_main_text("""
    We begin by addressing the idea of mind and body. René Descartes, a French philosopher in the 1600s, wrote Meditations on First Philosophy, a series of meditations on first philosophy, with the sixth part being the distinction between mind and body. In the sixth meditation, he mentions that the mind and body are two extended substances with the key difference being the mind is an extended thinking thing and the body is not (Descartes, Cress translation, 98). He further goes on to mention that in order to achieve a complete being — the human person — harmonization between mind and body would be needed as only through achieving this connection would they now no longer be two extended substances but a complete being -- as shown in Descartes' example of a sailor and his ship being two separate substances but together are constituted as one single thing (Descartes, Cress translation, 98). And as they are now conjoined in harmonization, theory would surface that if one extended substance was limited in development, it would inhibit the other from developing as the connection between mind and body is like a theoretical string, one can only get so far ahead of the other before it is pulled back, reaching the limit on the string's pull or worse, snapping, severing the bridge between both extended substances and thus rendering the human body no longer a complete being but two extended substances living in close proximity to one another. It is also applicable that the string could initially be shown as a thin piece of string, our starting weak connection between mind and body, and as we continue to grow and develop, the string increases in layers of connection, eventually becoming a thick rope with a heightened, layered connection. We can conclude from this that the parallel development of mind and body is necessary; sports or physical activities and academics would need to support one another through the developmental stages of a child as they progressed into becoming a young adult. Therefore, as shown earlier, if the mind portion of the human body is being developed through the pursuit of academic excellence, but the body portion is neglected due to external conflicts such as scheduling or parental pressure, then eventually the mind would cease to continue development at the same rate unless changes are made to the developmental rate of the body. This I coin the mind and body string theory. """)  # Expand on the narrator portion. Check notes/feedback forms.
    format_main_text("""
    I present a visualization and metaphor for the mind and body string theory to better aid you: we begin with two runners running in a straight line at a constant pace and a piece of string connecting the two runners to one another, if one should falter and change his pace, the string will soon find maximum tension and the other will be forced to change his pace to match the first runner. Think of it this way, if one runner were to increase or decrease his pace, eventually the string must find maximum tension, thus resulting in the runner in front being unable to widen the distance between him and the second runner. This tension would remain present until either the runner ahead decreases his pace, or the runner behind increases his pace; if not done as so, the runner in front would have to work harder to pull the runner behind along, a scenario that would quickly result in fatigue and burnout. If they both were to progress at the same rate, it would be logical that they will eventually have a higher form of connection such as compatibility to each one's unique assets. A scenario for the development of mind and body: if our body is developed but our minds are left behind, eventually, we will reach a point where development of the body will slow down until the development of the mind catches up; and if the mind does not catch up, the body will slowly burn out. And if forced to continue at the same pace, the substance in front would eventually burn out from extended fatigue and exhaustion from pulling the other substance along. """)
    format_main_text("""
    If that visualization was not enough to satisfy, take for example a basketball player attempting to learn how to shoot a three-point shot. In the first 100 attempts, it is probable that he would make less than 50 percent of the shots taken; as he continues with his attempts, he will eventually improve in accuracy and precision resulting in the percentage of successful attempts increasing. This progression and development can be defined as muscle memory and it is the result of “changes that occur in the brain during skill learning and memory [that] alter the information that the brain sends out to the muscles, thereby changing the movements that are produced” as defined by Oxford University in an article titled “The amazing phenomenon of muscle memory” (Oxford). This would help us better visualize and comprehend the distinct bridge between mind and body as it would prove that when the body improves and engages in activity, so does the mind. This idea would give rise to the theory that while training the body to recognize the motions required to perform a certain action, we are simultaneously training our mind to help our body recognize the signals that initiate and carry out the desired action; and this would be further proof of the aforementioned connection between mind and body. We see evidence of the string connecting mind and body as it would be the signals sent between the two that trigger the muscles to initiate and carry out the three-point shot, and the nerves collecting the data and preserving it. The repeated motions would build upon the previously mentioned theoretical string with each successful attempt creating another layer on top of the string; with hundreds of successful shots, there would now be a rope connecting the mind and body a representation of a heightened connection. """)
    format_main_text("""
    The knowledge behind understanding the importance and connection between mind and body is powerful yet confusing. Think of the possibilities that await us should we better understand the concept of mind and body. Imagine how life would differ if we could mentally see the theoretical string, visualize that connection which would allow us to better understand our own bodies. We could prevent disease like Alzheimer's. Could this be the key to a higher power? Could understanding the true effects of the mind allow us to communicate more effectively with other organisms? Would this lead to an era of consciousness?""")
    format_main_text("Knowledge is power, and power comes from knowledge. Muscle memory may be but a small area surrounding the concept of memory, however, that does not diminish its importance any more than peanut butter and jelly is to a PB&J sandwich. Perhaps understanding that connection between mind and body is the key to higher understanding, and perhaps it is not.")


def essay3():  # Expand upon.
    format_headers("Pain and Agony brings Beauty and Appreciation into play")
    format_main_text("""
    This next part may be a little confusing, so I'm here to help. You want to read in between the double quotation marks. So any text after the format_main_text is part of the essay. I am simply using this format as a shell to further emphasize the usage of Python to write an essay, as well as show you what it may look like typing it out in a code editor. The first thing you are going to see is [def format_main_text(text):] This is a function that I used to ensure that the text, when printed in the terminal, prints out in a nice, easy to read format. [def first_part():] and so on are going to be where the essay is located. In between the format_main_text()
    """)

    format_main_text("""
    This specific piece revolves around the memory of information and processing that information in a manner that will allow for better understanding, comprehension, and application in future scenarios that will require the specific information being practiced. In part, this piece has connections with "The Mind and Body in all its Glory", as it utilizes muscle memory in application as it attempts to ensure that the information is not forgotten, nor are the skills out of practice. """)

    input("""
    def format_main_text(text):
        print(textwrap.fill(text))
        
    def first_part():
        format_main_text("Writing an essay in a code editor has to be one of 
        the dumbest things that I have ever decided to do. For starters, it is 
        slower, there is no AutoCorrect, I find it extremely challenging to 
        visually see the flow of the essay, and I can not for the life of me 
        even begin to know how many pages I have or if the formatting is 
        correct. Yet I still do this to myself.")
        format_main_text("So why would I do this to myself, you may ask? Well, 
        the answer is simple and concise: Memory. What is memory in this 
        context, you wonder? In short, it is the application and practice of 
        skills learned, in an attempt to try and ingrain it in my memory to the 
        point where it becomes second nature. ")
        format_main_text("The first time I did this was for Experiment 3.
        I'll admit the experience was a little rough as I was attempting to 
        write a full-on essay in a code editor, as I found out,
        not exactly the smartest thing to do as there were plenty of challenges
        that I encountered along the way. The hardest part about writing an 
        essay in a programming language is getting it to run as smooth as you 
        envision it to. Nevertheless, I had extra time on my hand and I had 
        already made that initial commitment, I was not backing down from this, 
        nor would I stop till it was complete. The beauty of writing in code is 
        seeing the fruits of your labor. When it runs perfectly, the 
        satisfaction is immeasurable.")
    """)
    input("""
    def second_part():
        format_main_text("When presented with the opportunity to write my essay 
        in a code editor, I immediately knew that I would encounter several 
        problems. These included trying to figure out how to properly format
        the words so that they appeared in a coherent and readable format,
        as well as ensuring that the flow made sense. In short, the essay 
        was a description of how I built the program and the challenges I faced.
        ")
        format_main_text("No doubt a tedious experience, in order to ensure 
        that I had the correct format throughout the entire essay,
        I had to continuously run it through the terminal so that I could 
        visually see the results and the fruits of my labor come to life.
        Another big challenge that I encountered which made this whole 
        experience rather difficult, was the backbone, or the shell of the
        program. In this particular program, of which I am currently editing,
        I have about 8 different functions and variables dedicated to 
        the backbone of my program. Obviously, when running the program, the 
        reader does not see this backbone at all, rather they are witness to 
        the results of the backbone, hopefully, a fluid flow of words that 
        make sense.")
        format_main_text("Coming back to the first time I wrote an essay in a 
        code editor, I had mentioned that it was for practice, trying to 
        put theory into application, a usage of memory. Memory plays a large 
        role in the world of programming; you often times need to know how 
        much memory your program will use up, how much memory it takes to keep 
        it running, and how much memory can it process when handling large 
        sets of data. These are all factors that we need to look at when 
        writing code. However, in this instance, memory is also a mental 
        attribute. It can be difficult at times to know the correct 
        functions to use, where certain variables should be placed,
        or when a function should be called. Correct visualization of 
        the project is needed, and more often than not, I would 
        find myself writing it out on a piece of paper before 
        applying it on the computer.")
    """)
    input("""
    def third_part():
        format_main_text("Wrapping this up now as I appear to have lost track 
        of where I was going with this. In short, writing an essay in 
        a code editor is not impossible, but it certainly provides a range 
        of difficulty and challenges. It was a good challenge, and applying it 
        in the manner seen above and right now was an insight into how the 
        text may be formatted when in a code editor. I quite enjoyed this 
        little journey of a more applicable approach rather than a 
        theoretical one. ") 
    """)  # Need to come back and brainstorm again. Lost the direction for a bit.


def finisher():
    format_main_text("""
    That concludes our trip down memory lane, I hope you enjoyed exploring the different aspects of memory and what it means to me. Thanks for playing along.
    """)


# Global variables/lists
essay_titles = ["My First Time", "The Mind and Body in all its glory",
                "Pain and Agony brings Beauty and Appreciation into play"]

essay_choices = ["The very first time",
                 "The concept of muscle memory", "Why do I do this to myself?"]

lbb = "\n------------------------------------------------------------\n"

essay_count = 0
# Calling on the functions in order.
intro()
main_function(essay_count)
