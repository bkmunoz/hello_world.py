# 1. TASK: print "Hello World"
print("Hello World!")
# 2. print "Hello Brenna!" with the name in a variable
name = "Brenna"
print("Hello",name)	# with a comma
print("Hello" + name)	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print("Hello",name)	# with a comma
print("Hello" + name)	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "pasta"
fave_food2 = "tacos"
print("I love to eat {} and {}".format(fave_food1, fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}") # with an f string

#NINJA BONUS - 1
name = 42
print("Hello " + str(name))

#NINJA BONUS - 2
amount_of_tacos_left = 20
user_brenna_ate = "16"
total = amount_of_tacos_left + int(user_brenna_ate)
print(total)


x = "Don't code while hungry"
print(x.title())


bonus = "Hello %s" % "world,"
py = "I am learning Python %d" % 3
print(bonus,py)

name = "Brenna"
age = 28
print("My name is %s and I'm %d" % (name, age))