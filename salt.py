#!/usr/bin/python3
# salt for having different values

from termcolor import colored
import crypt

# example
# crypted = crypt.crypt("word", "salt")
# print(crypted)

# force-bruter for crypt passwords w/ salt
def main():
    passwords = open('passwords.txt', 'r')
    for line in passwords.readlines():
        if ":" in line:
            # spliting the user from the hashed password
            user = line.split(":")[0]
            password = line.split(":")[1].strip(" ").strip('\n')
            print(colored("[+] Cracking password for: %s" % user, 'red'))
            # cracking process
            crack(password)

def crack(password):
    # declaring what is the natural salt
    salt = password[0:2] # first two elements
    dictionary = open('dictionary.txt', 'r')
    for word in dictionary.readlines():
        word = word.strip("\n")
        # crypt the word with the actual Salt
        crypted = crypt.crypt(word,salt)
        # comparing password and crypted word
        if(password == crypted):
            print(colored("[!] Password found: %s" % word, 'green'))
            return



if __name__ == "__main__":
    main()
