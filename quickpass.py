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
    parser.add_argument("-sc", action='store_false', help="Name to be used for archive.")
    parser.add_argument("-n", type=int, default=1, help="The Number of passwords to generate.")
    p_args =  parser.parse_args()
    return p_args
    
def generate_password(length, use_symbols):
    """
    Generates a string from randomly 
    selected characters to be used as 
    a password.
    
    The function verifys the state of the 
    use_symbols parameter and concatenates the string of 
    characters accordingly.
    
    The password is built inside the while loop
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
        The sequence of characters to be used 
        when generating the password.
        
        *Defaults to a concatenated string containing :
        letters A-Z(upper & lowercase)
        digits 0-9
        punctuation and symbols(!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~)
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
    
    Gets commandline arguments 
    and calls the generate_password function.
    
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
    for i in range(args.n):
        print(generate_password(args.length, args.sc))
    
if __name__ == "__main__":
    main()
