def caesar_cipher(input:str, pos_len: int) -> str:
	output = ""
	for char in input:
		if char.isupper():
			output += chr((ord(char) + pos_len - 65)% 26 + 65)  
		elif char.islower():
			output += chr((ord(char) + pos_len - 97)% 26 + 65)  
    return output

print(caesar_cipher("holahola", 3))

def hola(inputs):
    pass
