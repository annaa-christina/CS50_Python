"""
WRITING IN ALL CAPS IS LIKE YELLING.

Best to use your “indoor voice” sometimes, writing entirely in lowercase.

In a file called indoor.py, implement a program in Python that prompts the user 
for input and then outputs that same input in lowercase. 
Punctuation and whitespace should be outputted unchanged. 
You’re welcome, but not required, to prompt the user explicitly, as by passing a str 
of your own as an argument to input.
"""

output1 = input ('what do you want to say?')

lowercase_output = output1.lower()

print (output1)
print (lowercase_output)


#die Methode kann auch direkt an die Definition der Variable angehängt werden, ohne Komma dazwischen!
output2 = input ('what do you want to say? 2') .lower ()

print (output2)

