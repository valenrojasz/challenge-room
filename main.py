def contar_fs(word):
    count = 0
    for i in range(len(word)):
        if word[i] == "F":
            count += 1
    return count

def contar_caracteres(word, letter):
    count = 0
    for i in range(len(word)):
        if word[i] == letter:
            count += 1
    return count

print(contar_caracteres("FFffffFC", "f"))
print(contar_caracteres("FFffffFC", "C"))
print(contar_caracteres("FFffffFC", "F"))

        
        
        
