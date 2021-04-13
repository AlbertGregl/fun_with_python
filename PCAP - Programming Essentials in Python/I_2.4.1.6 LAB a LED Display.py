# dictionary that represents 7-segment LED display
display = { "1": ("   #", "   #", "   #", "   #", "   #"),
            "2": (" ###", "   #", " ###", " #  ", " ###"),
            "3": (" ###", "   #", " ###", "   #", " ###"),
            "4": (" # #", " # #", " ###", "   #", "   #"),
            "5": (" ###", " #  ", " ###", "   #", " ###"),
            "6": (" ###", " #  ", " ###", " # #", " ###"),
            "7": (" ###", "   #", "   #", "   #", "   #"),
            "8": (" ###", " # #", " ###", " # #", " ###"),
            "9": (" ###", " # #", " ###", "   #", " ###"),
            "0": (" ###", " # #", " # #", " # #", " ###") }

# take input from user
x = input("Enter the number: ")

# store this input in a list of strings
number = []
for n in x:
    number.append(n)

# print numbers on display row by row, total five (5) rows
for i in range(len(display["0"])): 
    # display length, i.e. how many display digits have to be used
    for j in range(len(number)):
        # search all numbers (keys) in display dictionary
        for key in display.keys():
            if number[j] == key:                          
                # print on each row
                print(display[key][i], end="")
    # when printig finished on first row, continue on next...
    print()
