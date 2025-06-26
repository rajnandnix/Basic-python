#set intersection after taking input from user

set_1= set(input("Enter elements of first set separated by space(comma seperated): ").split(','))
set_2= set(input("Enter elements of second set separated by space(comma seperated): ").split(','))
set1= {item.strip() for item in set_1}
set2= {item.strip() for item in set_2}
intersection = set1.intersection(set2)
if intersection:
    print("The intersection of the two sets is:", intersection)
else:
    print("There is no intersection between the two sets.")
# This code takes two sets of elements from the user, removes any leading or trailing spaces,
# and then calculates the intersection of the two sets. If there is an intersection, it prints  