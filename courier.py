packPrice = float(raw_input("What is the price of the package? \n"))
dist = int(raw_input("What is the distance in km? \n"))

trans = (raw_input("What transport do you want to use? (air or freight)\n"))

if trans == "freight":
    trans = 0.25
else:
    trans = 0.36

insure = (raw_input("What insurance would you like? (full or limited)\n"))

if insure == "full":
    insure = 50.00
else:
    insure = 25.00

gift = raw_input("Is this a gift? (yes or no)\n")

if gift == "yes":
    gift = 15.00
else:
    gift = 0.00

prior = raw_input("Is this a priority or standard delivery? \n")

if prior == "priority":
    prior = 100.00
else:
    prior = 20.00

total = packPrice + dist + trans + insure + gift + prior

print "Thank you for Shopping with us, \nYour total is: R "+str(total)
