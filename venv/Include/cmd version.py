import re
import math
import string
import random
import sys

# Methods of en/decrption for example n for program
def encryption(text):
    if(text.__len__()%6!=0):
        trashVal = math.ceil(text.__len__()/6)*6 - text.__len__()
        print(trashVal)
        for x in range(trashVal):
            text+= random.choice(string.ascii_letters)
    print(text)
    encrypt = ""
    for x in range(6):
        encrypt += text[x::6]
    return encrypt

def decryption(text):
    decrypt = ""
    for x in range(math.ceil(text.__len__()/6)):
        decrypt+= text[x::math.ceil(text.__len__()/6)]
    return decrypt

def viewEncryption(text):
    lText = list(text)
    count = 0
    for x in range(lText.__len__()):
        print(lText[x], end='')
        count += 1
        if (count == 6):
            print()
            count = 0
    print()


# Example of encryption and decryption in terminal

print("Start")
text = "hi my name is python_3_7"   #hi my name is python_3_7
text1 = "hi my name is python_and_im_gonna_conq_the_wolrds"
text = re.sub(r'\W+','', text)
text1 = re.sub(r'\W+','', text1)
print(text)
viewEncryption(text)
encrypt = ""
encrypt = encryption(text)
print(encrypt)
print(decryption(encrypt))