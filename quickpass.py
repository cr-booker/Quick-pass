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
    
    
    Returns
    -------
    Output:(Class)
        returns argparse.Namespace object
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-len", help="The desired number of characters to be used.")
    parser.add_argument("-sc", help="Name to be used for archive.")
    parser.add_argument("-n", help="The Number of passwords to generate.")
    return p_args
    
def generate_password(length=10, use_symbols=True):
    """
    Generates a string of randomly 
    selected characters to be used as 
    a password.
    
    Parameters
    ----------
    length(Int):
        The length of the password to be generated.
        ideally passwords should be have a minimum length 
        of 8, but of course, the longer the better.
        
        *Defaults to a length of 10
        
    use_symbols(Bool):
        The sequence of characters to be used 
        when generating the password.
        
        *Defaults to a concatnated string containing :
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
    
def generate_passphrase():
    """
    """
    pass

def main():
    """
    """
    args = get_args()
    for i in range(20):
        print(generate_password(15,False))
    
if __name__ == "__main__":
    main()
