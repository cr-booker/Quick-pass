#!/usr/bin/env python3
"""
Quck-Pass is a Python script that
generates a strong password or passphrase that can
be used for just about anything.
It sucks trying to think of a new
password on the fly,
Quick-Pass takes care of that ickyness for you.
"""
import argparse 

try:
    import secrets as random #Python 3.6 or higher
except ImportError:
    import random
    
import string
import sys

def get_args():
    """
    Gets command-line arguments.
    
    Creates the arguments and options the script expects to 
    handle and parses the provided arguments.
    
    All arguments have a single letter "-" version 
    and a longer "--" version.
    Returns
    -------
    Output:(Class)
        returns argparse.Namespace object
    """
    parser = argparse.ArgumentParser(prog='Quick-Pass', description=__doc__)
    parser.add_argument("-l", "--length", type=int, default=10, help="The desired number of characters to be used.")
    parser.add_argument("-a", "--alphanumeric", action='store_false', help="Turns off the use of special characters.")
    parser.add_argument("-q", "--quantity", type=int, default=1, help="The number of passwords/passphrases to generate.")
    p_args =  parser.parse_args()
    if p_args.length < 4:
        parser.error("-length option requires an integer >= 4")
    return p_args
    
def generate_password(length, use_symbols):
    """
    Generates a string from randomly 
    selected characters.
    
    The function verifys the state of the 
    use_symbols argument and concatenates the string of 
    characters accordingly.
    
    The password is built inside a while loop
    continuing until the string contains atleast:
    
    1 number 
    1 uppercase letter
    1 lowercase letter
    and if the use_symbols parameter is set to True
    1 symbol/punctuation
   
    Parameters
    ----------
    length(Int):
        The length of the password to be generated.
        ideally passwords should be have a minimum length 
        of 10, but of course, the longer the better.
       
        *Defaults to a length of 10
        
    use_symbols(Bool):
        Determines whether to use 
        symbols and punctuation
        Ex. (!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~)
        
        *Defaults to True
        
   Returns
   -------
   Output(String):
       Returns Password String
    """
    if use_symbols:
        chars = ''.join((string.ascii_letters, string.digits, string.punctuation))
    else:
        chars = ''.join((string.ascii_letters, string.digits))
    while True:
        password = (''.join(random.SystemRandom().choice(chars)
                    for i in range(length)))
                    
        if (any(ch.isdigit() for ch in password) and
            any(ch.isupper() for ch in password) and
            any(ch.islower() for ch in password)):
            if not use_symbols:
                return password 
            elif any(ch in string.punctuation for ch in password):
                return password
                
def generate_passphrase(wordcount, spaces, path='.'):
   """
   Parameters
   ----------
   wordcount(Int):
       Number of words to be used 
       for the passphrase
       
   spaces(Bool):
       
   
   Returns
   -------
   Output:(String)
   """
   try:
       with open('wordlist.txt') as infile:
           wordlist = infile.read().splitlines()     
   except FileNotFoundError:
       print('Wordlist.txt not found.')
       return
   words = [random.SystemRandom().choice(x) for i in range(wordcount)]
   if spaces:
       passphrase = ' '.join(words)
   else:
       passphrase = ''.join(words)
   

def main():
    """
    Main function: 
    Starting point of script.
    
    The get_args function 
    retrieves the commmand line arguments
    we wil be using.A for-loop is constructed calling and
    printing the return value(string) of the 
    generate_password function, 
    
    with args.quantity being the number of 
    iterations(defaults to 1).
    
    If the args.length is less than 10 a warning 
    is shown advising against generating shorter 
    passwords(but im sure they have their uses).
    
    
    
    Returns
    -------
    Output(None)
    """
    args = get_args()
    print('----------------\n'\
          '[+]Quick-Pass[+]\n'\
          '----------------')
          
    if args.length < 8:
        print('WARNING.\nIt is recommended you use generated \npasswords that are'\
              ' atleast 10 characters long.')
        print('-' * 46)
        
    if not args.alphanumeric:           
        print('WARNING.\nIt is recommended you include symbols \nand punctuation'\
              ' for a more secure password.')
        print('-' * 46)
        
    for i in range(args.quantity):
        print(generate_password(args.length, args.alphanumeric))
    
if __name__ == "__main__":
    main()
