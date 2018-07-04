#!/usr/bin/env python3
"""
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
    Creates the parameters the script expects to 
    handle and parses the provided arguments.
    
    
    Returns
    -------
    Output:(Class)
        returns argparse.Namespace object
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-length", type=int, default=10, help="The desired number of characters to be used.")
    parser.add_argument("-sc", action='store_false', help="Turns off the use of special characters.")
    parser.add_argument("-n", type=int, default=1, help="The Number of passwords to generate.")
    p_args =  parser.parse_args()
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

def main():
    """
    Main function: 
    Starting point of script.
    
    The get_args function 
    retrieves the commmand line arguments
    we wil be using.A for-loop is constructed calling and
    printing the return value(string) of the 
    generate_password function, 
    
    with args.n being the number of 
    iterations(defaults to 1).
    
    If the args.length is less than 10 a warning 
    is shown advising against generating shorter 
    passwords(but im sure they have their uses).
    
    Returns
    -------
    Output(None)
    """
    args = get_args()
    print('----------------')
    print('[+]Quick-Pass[+]')
    print('----------------')
    if args.length < 8:
        print('WARNING.\nIt is recommended you use generated \npasswords that are atleast 10'\
               ' characters long.')
        print('-' * 46)
    if not args.sc:           
        print('WARNING.\nIt is recommended you include symbols \nand punctuation for a more'\
              ' secure password.')
        print('-' * 46)
        
    for i in range(args.n):
        print(generate_password(args.length, args.sc))
    
if __name__ == "__main__":
    main()
