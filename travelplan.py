#   Oblig 4, task 4
#1) In this task you will create a program that allows a user to make plans for a trip.
#   You must do this using a nested list, that is, a list of lists.1. Create an empty list
#   of places and give the user the opportunity to fill it with 5 destinations using a for-loop.

destinations = []
for i in range(5):  #for each five times
    d = input("Where do you want to go? ")
    destinations.append(d)   #adds destinations to the end of the list.
#print(destinations) #print to test

#2) Create two lists named clothing and departures, and let the user fill them in the
#   same way, with five items in each list.
clothing = []
departures = []

for i in range(5):
    d = input("What clothes do you want to bring? ")
    clothing.append(d)

for i in range(5):
    d = input("What dates do you want to go? ")
    departures.append(d)
#print(clothing, departures) #print to test

#3) Nå skal du lage en liste som kan inneholde de andre listene du har skrevet.
#   Opprett en liste reiseplan, og legg til steder, klesplagg og avreisedatoeri lista.

travelplan = [destinations, clothing, departures]
#print(travelplan) #print to test

#4) Use a simple loop to print the content of your itinerary and see that tree lists
#   are printed with their own content.

for i in travelplan:
    print(i)

#5) Follow these steps to allow the user to enter a space in the itinerary and print
#   the item in the specified space.

#a) First, retrieve an index i1 which represents one of the three lists in the itinerary,
#   where valid input will be between 0 and the length of itinerary minus 1 (which we have
#   reviewed starts the index at 0, and a list of 5 items will therefore have 4 as the
#   highest index) .

i1 = int(input("Which list do you want to look at? "))
i1 = i1 - 1

if i1 in range(len(travelplan)):
    print(travelplan[i1])
else:
    print("Doesn't exist")

#b) Then an index i2 representing one of the five elements in the selected list, where
#   valid input will be between 0 and the length of the list minus 1.

i2 = int(input("Which item do you want to look at? "))
i2 = i2 - 1



#c) Use an if-check to test that the two numbers the user has entered are valid values.
#   If the numbers are possible places in the lists, they should be used to print
#   itinerary [i1] [i2]. If the numbers are not valid locations, print "Invalid input!"
