artist = "Daft Punk"
discography = "Albums and Songs"
bio ="""Daft Punk were a French electronic music duo formed in 1993 in Paris by Guy-Manuel de Homem-Christo and Thomas Bangalter.
Widely regarded as one of the most influential acts in dance music history, they achieved popularity in the late 1990s as part of the French house movement.
They garnered critical acclaim and commercial success in the years following, combining elements of house music with funk, techno, disco, indie rock and pop.
They released 4 studio albums, namely : \"Homework\", \"Discovery\", \"Human after all\" and \"Random Access Memories\"."""""
print(bio)
alb0 = {}
alb0["Name"] = "Homework"
alb0["Date"] = "17 January 1997."
alb0["Trivia"] = "The album was written and released before the robot helmets."
alb0["Extra"] = """The most successful single from Homework was \"Around the World\", which is known for the repeating chant of the song's title.
In 1998, Bangalter's side project Stardust released the chart hit \"Music Sounds Better With You\"."""
alb1 = {}
alb1["Name"] = "Discovery"
alb1["Date"] = "26 February 2001."
alb1["Trivia"] = "The album was recorded entirely in Thomas' house."
alb1["Extra"] = """Discovery created a new generation of Daft Punk fans.
It also saw Daft Punk debut their distinctive robot costumes; they had previously worn Halloween masks or bags for promotional appearances.
The singles \"Digital Love\" and \"Harder, Better, Faster, Stronger\" were also successful in the UK and on the United States dance chart."""
alb2 = {}
alb2["Name"] = "Human after all"
alb2["Date"] = "14 March 2005."
alb2["Trivia"] = "The duo considers Human After All to be their best work. Fans disagree."
alb2["Extra"] ="""In March 2005, Daft Punk released their third album, Human After All, the result of six weeks of writing and recording. 
Reviews were mixed, with criticism for its repetitiveness and darker mood. 
The singles were \"Robot Rock\", \"Technologic\", \"Human After All\", and \"The Prime Time of Your Life\"."""

alb3 = {}
alb3["Name"] = "Random Access Memories"
alb3["Date"] = "17 May 2013."
alb3["Trivia"] = "The album also came in Vinyl edition. "
alb3["Extra"] ="""The lead single, \"Get Lucky\", became Daft Punk's first UK number-one single and became the most-streamed new song in the history of Spotify.
At the 56th Annual Grammy Awards, Random Access Memories won the Grammy for Best Dance/Electronica Album, Album of the Year and Best Engineered Album.
Also, \"Get Lucky\" received the Grammy for Best Pop Duo/Group Performance and Record of the Year."""

q0 = "Which album do you want some information about? "
q1 = "Would you like to learn more about it? "
q2 = "Would you like to listen to it? "
q3 = "Would you like to know a fun fact about this release? "
q4 = "Would you like some information on another album? "


loop = True
while loop:
    q00 = str(input(q0).casefold())
    if q00 in alb0["Name"].casefold():
        print(alb0["Name"] + " was released on " + alb0["Date"])
    elif q00 in alb1["Name"].casefold():
        print(alb1["Name"] + " was released on " + alb1["Date"])
    elif q00 in alb2["Name"].casefold():
        print(alb2["Name"] + " was released on " + alb2["Date"])
    elif q00 in alb3["Name"].casefold():
        print(alb3["Name"] + " was released on " + alb3["Date"])
    else:
        continue

    q11 = input(q1).casefold()
    if q11 == "yes":
        if q00 in alb0["Name"].casefold():
            print(alb0["Extra"])
        elif q00 in alb1["Name"].casefold():
            print(alb1["Extra"])
        elif q00 in alb2["Name"].casefold():
            print(alb2["Extra"])
        elif q00 in alb3["Name"].casefold():
            print(alb3["Extra"])
    else:
        continue

    listen = input(q2).casefold()
    if listen == "yes":
        if q00 in alb0["Name"].casefold():
            link = "https://www.youtube.com/watch?v=yuoghR-5-Xs&list=PLSdoVPM5Wnne3Q2AxosemsThywhraJ0su"
            yt = "There you go! \nEnjoy {}".format(link)
            print(yt)
        elif q00 in alb1["Name"].casefold():
            link = "https://www.youtube.com/watch?v=A2VpR8HahKc&list=PLSdoVPM5WnndSQEXRz704yQkKwx76GvPV"
            yt = "There you go! \nEnjoy {}".format(link)
            print(yt)
        elif q00 in alb2["Name"].casefold():
            link = "https://www.youtube.com/watch?v=A8Z3vJgB8kw"
            yt = "There you go! \nEnjoy {}".format(link)
            print(yt)
        elif q00 in alb3["Name"].casefold():
            link = "https://www.youtube.com/watch?v=P_r9KNTGlTY"
            yt = "There you go! \nEnjoy {}".format(link)
            print(yt)


    trivia = input(q3).casefold()
    if trivia == "yes":
        if q00 in alb0["Name"].casefold():
            print(alb0["Trivia"])
        elif q00 in alb1["Name"].casefold():
            print(alb1["Trivia"])
        elif q00 in alb2["Name"].casefold():
            print(alb2["Trivia"])
        elif q00 in alb3["Name"].casefold():
            print(alb3["Trivia"])


    choice = input(q4).casefold()
    if choice != ("yes"):
        loop = False