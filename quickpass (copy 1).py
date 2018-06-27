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
    """
    pass

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
    base_chars= ''.join((string.ascii_letters,string.digits))
    base_and_symbols = ''.join((base_chars,string.punctuation))
    while True:
        if use_symbols:
            password = (''.join(random.SystemRandom(base_and_symbols).choice() 
                        for i in range(length)))
                   
            if (any(ch.isdigit() for ch in password and
                any(ch.isupper() for ch in password and
                any(ch.islower() for ch in password and 
                any(ch in string.punctuation for ch in password):
                
                pass
def password_check(password):
    """
    """
    pass
def generate_passphrase():
    """
    """
    pass

def main():
    """
    """
    generate_password()
    
if __name__ == "__main__":
    main()
