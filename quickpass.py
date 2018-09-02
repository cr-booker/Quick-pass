#!/usr/bin/env python3
"""
Quck-Pass is a Python script that
generates a decently strong password or passphrase 
that can be used for just about anything.

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
from textwrap import fill as wrap

def get_args():
    """
    Creates the expected command line options 
    and parses the given input.
    
    Password Parser Arguments
    -------------------------
    length(Int)
        Password length.
    
    alphanumeric(Bool)
        Use only letters A-z and 
        numbers 0-9.
        
    quantity(Int)
        Number of passwords to create.
        
    Passphrase Parser Arguments
    ---------------------------
    length(Int)
        Passphrase length.
    
    spaces(Bool)
        Include spaces between words.
    
    quantity(Int)
       Number of passphrases to create.
    
    path(String)
        Path to wordlist.txt
    
    Returns
    -------
    Output:(Argparse Obj)
        argparse.Namespace object.
    """
    parser = argparse.ArgumentParser(prog='Quick-Pass', description=__doc__)
                                             
    subparsers = parser.add_subparsers(help='sub-command help', dest='parser')
    
    password_parser = subparsers.add_parser("password", description="Generates a password.", help='Password Help')

    password_parser.add_argument("-l", "--length", type=int, default=10,
                        help="The desired number of characters to be used.")
                                             
    password_parser.add_argument("-a", "--alphanumeric", action='store_true', 
                        help="Turns off the use of special characters.")
                        
    password_parser.add_argument("-q", "--quantity", type=int, default=1, 
                        help="The number of passwords to generate.")
                        
    passphrase_parser = subparsers.add_parser("passphrase",  description="generates a passphrase", 
                                              help='Passphrase Help')
                                              
    passphrase_parser.add_argument("-l", "--length", type=int, default=4,
                                   help="The number of words to be used for passphrase.")
                                   
    passphrase_parser.add_argument("-s", "--spaces", action='store_true', 
                        help="Use spaces in-between words")
    
    passphrase_parser.add_argument("-q", "--quantity", type=int, default=1, 
                        help="The number of passphrases to generate.")
                        
    passphrase_parser.add_argument("-p", "--path", default='.' ,help="path to wordlist file.")
    
    p_args =  parser.parse_args()
    if p_args.parser == "password" and p_args.length < 4:
        parser.error("-length option requires an integer >= 4")
    
    if p_args.parser == "passphrase" and p_args.length < 2:
        parser.error("-length option requires an integer >= 2")  
        
    if len(sys.argv) > 1: #No arguements given
        return p_args
    parser.print_help()
    sys.exit()
    
def generate_password(length, alphanumeric):
    """
    Creates a string from randomly 
    selected symbols and characters.
    
    The password built must contain:
    
    1 number 
    1 uppercase letter
    1 lowercase letter
    and if the alphanumeric parameter is set to False
    1 symbol/punctuation
   
    Parameters
    ----------
    length(Int):
        The length of the password to be generated.
        ideally passwords should be have a minimum length 
        of 10, but of course, the longer the better.
       
        *Defaults to 10
        
    alphanumeric(Bool):
        Determines whether to exclude symbols/punctuation 
        Ex. (!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~)
        
        and restrict the character pool to
        Upper and Lowercase letter A-Z and 
        numbers 0-9.
        
        *Defaults to False
        
   Returns
   -------
   Output(String):
       Password String.
    """
    if alphanumeric:
        chars = ''.join((string.ascii_letters, string.digits))
    else:   
        chars = ''.join((string.ascii_letters, string.digits, string.punctuation))
    while True:
        password = (''.join(random.SystemRandom().choice(chars)
                    for i in range(length)))
                    
        if (any(ch.isdigit() for ch in password) and
            any(ch.isupper() for ch in password) and
            any(ch.islower() for ch in password)):
            if alphanumeric:
                return password 
            elif any(ch in string.punctuation for ch in password):
                return password
                                
def generate_passphrase(wordcount, spaces, path):
   """
   Randomly selects words from the "wordlist" 
   text file joining them to create a passphrase.
   
   Parameters
   ----------
   wordcount(Int):
       Number of words to be used 
       for the passphrase.
       
       *Defaults to 4
       
   spaces(Bool):
       If set to True, adds a space between each 
       word.
       
       *Defaults to True
   
   path(String):
       Path to wordlist file.
       
       *Defaults to '.'
   
   Returns
   -------
   Output:(String)
       passphrase string.
   """
   try:
       with open('wordlist.txt') as infile:
           wordlist = infile.read().splitlines()     
   except FileNotFoundError:
       print('Wordlist.txt not found.')
       return
   words = [random.SystemRandom().choice(wordlist) for i in range(wordcount)]
   if spaces:
       passphrase = ' '.join(words)
   else:
       passphrase = ''.join(words)
   return passphrase
   
def show_password(args):
    """
    Generates/displays password(s).
    
    args(Argparse Obj)
        Argparse Namespace object
    
    Returns
    -------
    Output(None)
    """
    if args.length < 8:
        print('WARNING.\nIt is recommended you use generated \npasswords that are'\
             ' atleast 10 characters long.')
        print('-' * 46)
        
    if args.alphanumeric:           
        print('WARNING.\nIt is recommended you include symbols \nand punctuation'\
             ' for a more secure password.')
        print('-' * 46)
        
    for index, value in enumerate(range(args.quantity), start=1):
        print(str(index) + ')', generate_password(args.length, args.alphanumeric))

def get_passphrase(args):
    """
    Generates/displays passphrase(s).
    
    args(Argparse Obj)
        Argparse Namespace object
        
    Returns
    -------
    Output(None)
    """
    args.length, args.spaces, args.path
    for index, value in enumerate(range(args.quantity), start=1):
        print(str(index) + ')', generate_passphrase(args.length, args.spaces, args.path))
        
def main():
    """
    Main function.
    
    Gets command line arguments 
    and displays the created 
    password(s)/passphrase(s).
   
    Returns
    -------
    Output(None)
    """
    args = get_args()
    print('----------------\n'\
          '[+]Quick-Pass[+]\n'\
          '----------------')
    if args.parser == 'password':
        get_password(args)      
    else: 
        get_passphrase(args)
if __name__ == "__main__":
    main()
