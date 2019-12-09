
userServe = input("Would you like to make some Ginger Snaps? (y/n)")
if userServe != "y":
   print("Maybe later.  See you then!")
   exit() 
userServe = True
userServeAmt = float(input('\nHow many servings would you like to make? \n')) 
calcServeAmtDivisor = (userServeAmt / userServe)                         
calcrecipe = (calcServeAmtDivisor * userServe)                
print ('cookie yields',userServeAmt,'servings',)
with open('recipe.txt', 'r') as f:
   print(open('recipe.txt').read())
print (calcrecipe,"enjoy!")
#if userServeAmt 

