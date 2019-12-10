
#user is greeted by the recipe for Ginger Snaps 
print("We're making Ginger Snaps!")  
#this is the base recipe with serving size 
baseCookies = 36 
cupsFlour = 2 
cupsBrownSugar = 1
cupsVegetableOil = .75
cupsMolasses = .25
Egg = 1 
tspBakingSoda = 2
tspSalt = .25
tspGroundClove = .5
tspGroundCinnamon = 1
tspGroundGinger = 1
#prompt the user for amount of cookies and store float to userServeAmt   
userServeAmt = int(input('\nHow many cookies would you like to make?\n')) 
#this is all the math done to adjust the servings    
expectedCupsFlour = (userServeAmt / baseCookies) * cupsFlour
expectedCupsBrownSugar = (userServeAmt / baseCookies) * cupsBrownSugar
expectedCupsVegetableOil = (userServeAmt / baseCookies) * cupsVegetableOil
expectedCupsMolasses = (userServeAmt / baseCookies) * cupsMolasses
expectedEgg = (userServeAmt / baseCookies) * Egg
expectedtspBakingSoda = (userServeAmt / baseCookies) * tspBakingSoda
expectedtspSalt = (userServeAmt / baseCookies) * tspSalt
expectedtspGroundClove = (userServeAmt / baseCookies) * tspGroundClove
expectedtspGroundCinnamon = (userServeAmt / baseCookies) * tspGroundCinnamon
expectedtspGroundGinger = (userServeAmt / baseCookies) * tspGroundGinger
#these are the printed results from above 
print("For", userServeAmt, "you will need ",  round(expectedCupsFlour, 1), "cups of flour")
print(round(expectedCupsBrownSugar, 1), "cups of brown sugar")
print(round(expectedCupsVegetableOil, 1), "cups of vegetable oil")
print(round(expectedCupsMolasses, 1), "cups of molasses")
print(round(expectedEgg, 1), "egg(s)") 
print(round(expectedtspBakingSoda, 1), "tsp baking soda")
print(round(expectedtspSalt, 1), "tsp salt") 
print(round(expectedtspGroundClove, 1),"tsp ground clove")
print(round(expectedtspGroundCinnamon, 1), "tsp ground cinnamon")
print(round(expectedtspGroundGinger, 1), "tsp ground ginger")
#prints out the directions
with open('recipe.txt', 'r') as f:
   print(open('recipe.txt').read())