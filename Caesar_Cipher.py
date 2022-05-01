#!/bin/python3

if __name__ == '__main__':
    print("text to ecrypt:",end="")
    s = input()
    print("key=",end="")
    k = int(input())
    for letter in s:
        if ord(letter)>=ord("A") and ord(letter)<=ord("Z"):
            enc_letter = ord(letter)
            enc_letter += k
            while(enc_letter>ord("Z")):
                enc_letter=ord("A")+enc_letter-ord("Z")-1
            print(chr(enc_letter),end="")
        elif ord(letter)>=ord("a") and ord(letter)<=ord("z"): 
            enc_letter = ord(letter)
            enc_letter += k
            while(enc_letter>ord("z")):
                enc_letter=ord("a")+enc_letter-ord("z")-1
            print(chr(enc_letter),end="")
        else:
            print(letter,end="")
    
    print("")









