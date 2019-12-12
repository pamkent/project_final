
#user is greeted by the recipe for Ginger Snaps 
print("We're making Ginger Snaps!")  
#this is the base recipe with serving size 
baseCookies = 30
cupsFlour = 2 
cupsBrownSugar = 1
cupsVegetableOil = .75
cupsMolasses = .25
egg = 2 
tspBakingSoda = 2
tspSalt = .25
tspGroundClove = .5
tspGroundCinnamon = 1
tspGroundGinger = 1
#prompt the user for amount of cookies and store the integer to userServeAmt   
userServeAmt = int(input('\nHow many cookies would you like to make?\n')) 
#this is all the math done to adjust the servings    
expectedCupsFlour = (userServeAmt / baseCookies) * cupsFlour
expectedCupsBrownSugar = (userServeAmt / baseCookies) * cupsBrownSugar
expectedCupsVegetableOil = (userServeAmt / baseCookies) * cupsVegetableOil
expectedCupsMolasses = (userServeAmt / baseCookies) * cupsMolasses
expectedegg = (userServeAmt / baseCookies) * egg
expectedtspBakingSoda = (userServeAmt / baseCookies) * tspBakingSoda
expectedtspSalt = (userServeAmt / baseCookies) * tspSalt
expectedtspGroundClove = (userServeAmt / baseCookies) * tspGroundClove
expectedtspGroundCinnamon = (userServeAmt / baseCookies) * tspGroundCinnamon
expectedtspGroundGinger = (userServeAmt / baseCookies) * tspGroundGinger
#if statement here to try make sure the recipe can be divided evenly
if userServeAmt %2 == 0: 
#these are the printed results from above 
   print("For", userServeAmt, "cookies you will need ",  expectedCupsFlour, "cups of flour")
   print(expectedCupsBrownSugar, "cups of brown sugar")
   print(expectedCupsVegetableOil, "cups of vegetable oil")
   print(expectedCupsMolasses, "cups of molasses")
   print(expectedegg, "egg(s)")
   print(expectedtspBakingSoda, "tsp baking soda")
   print(expectedtspSalt, "tsp salt") 
   print(expectedtspGroundClove,"tsp ground clove")
   print(expectedtspGroundCinnamon, "tsp ground cinnamon")
   print(expectedtspGroundGinger, "tsp ground ginger") 
#else statement to print message if user enters an odd number 
else: 
   print("I'm sorry, I can't split an egg!") 
#calls the file to print out the directions
with open('recipe.txt', 'r') as f:
   print(open('recipe.txt').read())
 