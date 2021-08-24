"""
I have read in a comma separated values file using .readlines().
I have used the .strip() method to get rid of the \n.
In my csv_occupation txt file I wanted to skip the first line since that line was just for headings.
For this I used list slicing.
Then I looped through the lines from index 1 to the end.
Inside the for loop I split each item at the ',' so they could be manipulated.
I then assigned each item to a variable and printed out a formatted string
containing the items displayed the way I wanted them.
"""
with open("csv_occupation.txt", "r") as file:
    read = [line.strip() for line in file.readlines()]
    read = read[1:]
    for line in read:
        data = line.split(",")
        name = data[0].title()
        age = data[1]
        occupation = data[2].title()
        workplace = data[3].title()
        print(f"{name} is {age} and is a {occupation} working at {workplace}  ")