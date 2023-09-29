import random #needed for the burn out function

class lightbulb:
    #Defaulted to be off already and not burned. The color variable is the only variable it's being given once it's instantiated 
    def __init__(self, color):
        self.IsOn = False
        self.color = color
        self.burned = False
    #Prints out whether or not it is turned on or off, the color of the lightbulb, and if it's burned out or not
    def printinfo(self):
        if self.IsOn == False:
            print("\nMy light is turned off")
        elif self.IsOn == True:
            print("\nMy light is turned on")
        print("The color of my light bulb is", self.color)
        if self.burned == False:
            print("Hey I'm not burnt out... yet")
        else:
            print(":( I am burnt out\n")
    #TurnOn function that sets IsOn to True
    def turnOn(self):
        self.IsOn = True
        print(self.color, "just turned on.")
    #burn_out function that sets burned to True and since it burned out, it'll set the IsOn to False
    def burn_out(self):
        i = random.randrange(1, 101)
        if i <= 5:
            self.burned = True
            self.IsOn = False
            print(self.color, "lightbulb burned out.\n\n")
        else:
            #This is purely just for myself to test what integers are pulled from the random.randrange function
            #I can remove this section and the code will work just fine
            print("Testing:", i)

#Instantiated 3 different lightbulbs
red_lightbulb = lightbulb("Red")
blue_lightbulb = lightbulb("Blue")
yellow_lightbulb = lightbulb("Yellow")


#Call the class functions for the three different lightbulbs. 
red_lightbulb.printinfo()
red_lightbulb.turnOn()
red_lightbulb.burn_out()

blue_lightbulb.printinfo()
blue_lightbulb.turnOn()
blue_lightbulb.burn_out()

yellow_lightbulb.printinfo()
yellow_lightbulb.turnOn()
yellow_lightbulb.burn_out()

blue_lightbulb.printinfo()
