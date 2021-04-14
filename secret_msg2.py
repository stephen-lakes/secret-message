aphabet = "abcdefghijklmnopqrtsuvwxyz"
input_string = input("Your msg> ")
input_string = input_string.lower()

for letter in input_string:
    if letter not in aphabet:
        input_string = input_string.replace(letter, " ")
    else:
        input_string = input_string.replace(letter, str(aphabet.find(letter) + 1) + "-")
    
input_string = input_string[: -1]
    
print(input_string)
