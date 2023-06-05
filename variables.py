number1 = 122
print (number1) 
# nombre à virgule flottante, float
number2 = 3,14
print (number2)

# chaine de caractères, string
text1= "foo bar baz "
print (text1)

text2 = "foo bar baz"
print (text2)

# booléen, boolean
python  is cool = True
print (python is cool)

python is boring = false
print(python is boring)

# valeur nulle, null value
accepted terms = None
print (None)

#type de données
print( type(number1))
print(type(number2))
print(type(text1))
print(type(text2))
print(type(python_is_ cool))
print(type(python_is_ boring))
print(type(user_accepted_terms))

#verification du type de données 
print (type(number1)is int)
print (type(number1)is str)

# todo: interroger le type des autres variables...

# transtypage
print (type(bool(number1)))
print (bool(number1))

#convertie en booléen, la valeur 0 donne False
number3 = 0
print (bool(number3 ))

#transtypage str -> int
print (type())

#génère l'erreur : ValueError: Invalid literal for
#print (type(int(text)))

# il ne peut pas y avoir de autre chose qu'un nombre
# dans la chaine de caractéres
# si on veut la convertir en int
text3= "123456789"
print (type (int(text3)))

# les fonctions de transtypage
# str() convertit vers string
# int () convertit vers integer
# float() convertit vers float
# bool () convertit vers boolean