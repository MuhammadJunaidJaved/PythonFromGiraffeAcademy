print("Giraffe Academy")
print("Giraffe\nAcademy")

phrase = "Giraffe Academy"
print(phrase)

# Concatenation
print(phrase + " is cool")

print(phrase.lower()) # Prints 'giraffe academy'

print(phrase.upper()) # Prints 'GIRAFFE ACADEMY'

print(phrase.isupper()) # Prints Fasle

print(phrase.upper().isupper()) # Prints True

# length of characters
print(len(phrase)) # Prints 15

print(phrase[0]) # Prints 'G'

print(phrase.index("G")) # Prints 0

print(phrase.index("i")) # Prints 1

print(phrase.replace("Giraffe", "Elephant")) # Prints 'Elephant Academy'
