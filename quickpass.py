#!/usr/bin/env python3
"""
Quick-Pass is a Python script that
generates a strong password or passphrase 
that can be used for just about anything.
"""
import argparse 
import os
try:
    import secrets as random #Python 3.6 or higher
except ImportError:
    import random  
import string
import sys

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
    parser.add_argument('--version', action='version', version='%(prog)s 1.0.0') 
                                           
    subparsers = parser.add_subparsers(help='sub-command help', dest='parser')
    
    ##################Password Parser####################
    password_parser = subparsers.add_parser("password", 
                                            description="Generates a password.", 
                                            help='Password Help')
                                                                                     
    password_parser.add_argument("-a", "--alphanumeric", 
                                 action='store_true', 
                                 help="Turns off the use of special characters.")
                        
    password_parser.add_argument("-l", "--length", 
                                 type=int, 
                                 default=10,
                                 help="The desired number of characters to be used. (Default: %(default)s).")
                                               
    password_parser.add_argument("-m", "--mute", 
                                 action='store_true', 
                                 help="Disables warning message about password length and character usage.")   
                                     
    password_parser.add_argument("-q", "--quantity", 
                                 type=int, 
                                 default=1, 
                                 help="The number of passwords to generate. (Default: %(default)s)")
                       
    ###############Passphrase Parser###################      
    seperators = '!@$#%&?*:+=.s'
    casing_options = ("none", "all", "first-letter", "alt-word", "alt-letter")
    passphrase_parser = subparsers.add_parser("passphrase",  
                                              description="generates a passphrase", 
                                              help='Passphrase Help')
    passphrase_parser.add_argument("-c", "--capitalize", default="none",
                                   nargs='?', choices= casing_options, 
                                   help="Word casing pattern. (Default: %(default)s)")
                                              
    passphrase_parser.add_argument("-l", "--length", 
                                   type=int, 
                                   default=4,
                                   help="The number of words for passphrase. (Default: %(default)s)")
    
    passphrase_parser.add_argument("-q", "--quantity", 
                                   type=int, 
                                   default=1, 
                                   help="The number of passphrases to generate. (Default: %(default)s)")

    
    passphrase_parser.add_argument("-p", "--path", 
                                   default='.',
                                   help="path to wordlist file.")
    
    passphrase_parser.add_argument("-pad", "--padding", 
                                   default='none',
                                   help="Character to add at the beginning and end of passphrase. (Default: Random)")
    
    passphrase_parser.add_argument("-pad-d", "--padding-depth", 
                                   type=int, 
                                   default='2' ,
                                   help="Number of characters for padding. (Default: %(default)s)")
                           
    passphrase_parser.add_argument("-sep", "--seperator", 
                                   
                                   default=random.choice('!@$#%&?*-:+=.'), 
                                   nargs='?', choices=list('!@$#%&?-*:+=.'),
                                   help="Character to insert between words. (Default: Random)", 
                                   metavar=seperators)
                           
    passphrase_parser.add_argument("-s", "--spaces", 
                                   action='store_false', 
                                   help="Use spaces in-between words")
              
    p_args =  parser.parse_args()
    if p_args.parser == "password" and p_args.length < 4:
        parser.error("-length option requires an integer >= 4")
    
    if p_args.parser == "passphrase" and p_args.length < 2:
        parser.error("-length option requires an integer >= 2")  
        
    if len(sys.argv) > 1: #No arguements given
        return vars(p_args)
    parser.print_help()
    sys.exit()
    
def generate_password(length=10, alphanumeric=False, **kwargs):
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
                    
def get_words(wordcount, path='.'):
   """
   Randomly selects words from the 
   "wordlist" text file. 
   
   Parameters
   ----------
   wordcount(Int):
       Number of words to 
       pull from text file.
   
   path(String):
       Path to wordlist file.
       
       *Defaults to '.'
       
   Returns
   -------
   Output:(List)
       List of strings to build
       passphrase with.
   """
   try:
       with open(os.path.join(path,'wordlist.txt')) as infile:
           wordlist = infile.read().splitlines()     
       words = [random.SystemRandom().choice(wordlist) for i in range(wordcount)]
       return words
   except IndexError:
       print('wordlist.txt empty.')
       sys.exit(1)
   except FileNotFoundError:
       print('wordlist.txt not found.')
       sys.exit(1)
       
def word_casing(words, casing):
    """
    Takes a list
    Parameters
    ----------
    words(List):
    
    casing(String)
    
    
    Returns
    -------
    Output:(List)
        list of strings with new casing pattern
    """
    #if casing not in ("all", "first-letter", "alt-word, alt-letter"):
     #   raise TypeError
        
    if casing ==  "all":
        new_casing = [entry.upper() for entry in words]
    elif casing == "first-letter":
        new_casing = [entry.capitalize() for entry in words]
    elif casing == "alt-word": 
        new_casing = [entry.upper() if entry in words[1::2] else entry for entry in words]       
    elif casing == "alt-letter":
        for index, word in enumerate(words):
            split_word = list(word)
            split_word[1::2] = [i.upper() for i in split_word[1::2]]
            words[index] = ''.join((split_word))
        return words
    return new_casing
    
def generate_passphrase(**kwargs):
    """
    """
    valid_keys = ("parser", "length", "spaces", 
                  "quantity", "seperator", "capitalize",
                  "padding", "paddepth") 
                  
    words = get_words(kwargs['length'],kwargs['path'])
    if kwargs["capitalize"] != "none":
        words = word_casing(words, kwargs["capitalize"])
   
    if kwargs['padding'] != "none":
        pad = kwargs['padding'] * kwargs['padding_depth']
        words[0] = ''.join((pad, words[0]))
        words[-1] = ''.join((words[-1], pad))        
    if kwargs['spaces'] == True:
        return ' '.join(words)
    if kwargs['seperator'] != "none":
        return kwargs['seperator'].join(words)
    return ''.join(words)
    
def password_warnings(length, alphanumeric):
    """
    Displays warning for password parser
    
    Parameters
    ----------
    pass_arg(Argparse obj)
        Argparse Namespace object
    
    Returns
    -------
    Output(None)  
    """
    if length < 8:
        print('WARNING.\nIt is recommended you use generated \npasswords that are'\
             ' atleast 10 characters long.')
        print('-' * 46)
        
    if alphanumeric:           
        print('WARNING.\nIt is recommended you include symbols \nand punctuation'\
             ' for a more secure password.')
        print('-' * 46)

def display(args):
    """
    Generates/displays passphrase(s).
    
    args(Argparse Obj)
        Argparse Namespace object
        
    Returns
    -------
    Output(None)
    """
    if args['parser'] == 'password':
        if not args['mute']:
            password_warnings(args['length'], args['alphanumeric'])
        pass_function = generate_password
    else:
        pass_function = generate_passphrase
        
    for index, value in enumerate(range(args['quantity']), start=1):
        print(str(index) + ')', pass_function(**args))
        
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
    #print(args)
    print('----------------\n'\
          '[+]Quick-Pass[+]\n'\
          '----------------')
    display(args)
        
if __name__ == "__main__":
    main()
