with open("output.txt", "a") as db:
    a = "Hello" + str(1)
    b = "How do you do?"
    db.write(a + ", " + b + "\n")

#In Code Snippet 1, a TypeError occurs because a string and an integer cannot be added,
#converting the integer to a string fixes this. The file is also not closed, which can cause access issues; using with open(...) ensures proper closure.



