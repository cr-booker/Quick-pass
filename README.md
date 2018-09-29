# Quick-Pass
Quick-Pass is a Python script that generates a strong  
password that can be used for just about anything.  

The aim here is to provide users with a  
decent password with just few keystrokes.  
Coming up with a decent password on your own sucks,  
especially on the fly,
let Quick-Pass take care of that ickyness for you.


## The importance of a strong password
I'm sure you've seen the occasional article or news report,  
where it's found that employees of "X" company or "Y" Corp  
had their security practices audited.

Janice in accounting used ***"password"*** as her password.  
hmmm, not bad Janice, but we need you to actually try.

John, well he's a clever boy. He stepped it up a notch:   
***"Password123"*** .  
I did say he was clever.  
And then there's Bill,

because there's always a Bill.

Bill's password is ***"Nr?r7]04Z\"*** .  
Wow Bill, that sounds like a decently strong password!  
Good Job Pal.

Bill gets a promotion and that new corner office hes been eyeing,

while John and Janice have to attend the super important mandatory  
meeting on why hiding your password under your family guy mouse pad,  
(Who still uses mouse pads) is a bad idea.  
We should all strive to be more like Bill.

## Installation 
Getting Quick-Pass up and running is easy.

1. Open a terminal window and enter:  
`git clone https://github.com/syst3m-failur3/Quick-pass.git`  

2. Navigate to the cloned Quick-pass directory and enter:  
`sudo pip install .` 

3. We're Done!


## Usage
Quick-pass is comprised of two sub-commands:  
#### password
    usage: Quick-Pass password [-h] [-a] [-l LENGTH] [-m] [-q QUANTITY]

    optional arguments:
      -h, --help
          show this help message and exit
          
      -a, --alphanumeric
          Turns off the use of special characters.
          
      -l LENGTH, --length LENGTH
          The desired number of characters to be used. (Default: 10).
                        
      -m, --mute
          Disables warning message about password length and character usage.
          
      -q QUANTITY, --quantity QUANTITY
          The number of passwords to generate. (Default: 1)

Entering in `quick-pass password`  
will give you a single 10 character password.  
something like **pyIsq*7}eb**

Simple enough, yeah?
#### passphrase
    usage: Quick-Pass passphrase [-h]
                                 [-c [all, first-letter, alt-word, alt-letter]]
                                 [-l LENGTH] [-q QUANTITY] [-p PATH]
                                 [-pad [PADDING]] [-pd PADDING_DEPTH]
                                 [-s [! @ $ # % ? * : + - = . s]]
                                 [-sd SEPERATOR_DEPTH]

    optional arguments:
      -h, --help
          show this help message and exit
          
      -c [all, first-letter, alt-word, alt-letter], 
      --capitalize [all, first-letter, alt-word, alt-letter]
          Word casing pattern. (Default: None)
          
      -l LENGTH, --length LENGTH
          The number of words for passphrase. (Default: 4)
          
      -q QUANTITY, --quantity QUANTITY
                        The number of passphrases to generate. (Default: 1)
                        
      -p PATH, --path PATH  path to wordlist file. (Default: Current Dir)
      
      -pad [PADDING], --padding [PADDING]
                        Character to add at the beginning and end of
                        passphrase. (Default: Random)
                        
      -pd PADDING_DEPTH, --padding-depth PADDING_DEPTH
                        Number of characters for padding. (Default: 2)
                        
      -s [! @ $ # % ? * : + - = . s], --seperator [! @ $ # % ? * : + - = . s]
                        Character to insert between words. (Default: Single
                        Space)
                        
      -sd SEPERATOR_DEPTH, --seperator-depth SEPERATOR_DEPTH
                        Number of characters for seperator. (Default: 1)

`quick-pass passphrase`  
This will give you a 4 word password seperated by a single space  
like: **Honor sweet yams afterglow** which would make a decent band name.


## Password Tips
I thought i'd just toss in some helpful password  
and security tips, because i like you so much.

- Password is not a good password.  
  Adding 123 doesn't make it better, i promise.
  
- Go ahead and turn on two-factor authentication.  
  [List of websites and whether or not they support 2FA. ](https://twofactorauth.org/)
  
- Don't neglect software updates!
  
- Never share your passwords with co-workers or really anyone for that matter.  
  [1 in 5 employees share their email passwords with coworkers](https://nakedsecurity.sophos.com/2018/09/11/yikes-1-in-5-employees-share-their-email-passwords-with-coworkers/)
  
- If you believe one of your accounts as been compromised,  
  don't hesitate,change your password, like right now, like now now  
  Why are you still reading this.
  
- Do not use the same passwords across all you accounts, if someone manages  
  to get that one password, they have access to everything,  
  and that's what we like to call, BAD.
  
- If you have a lot of long, complicated passwords to remember,  
  consider using a trusted password manager.  
  [How to evaluate a password manager?](https://security.stackexchange.com/questions/32536/how-to-evaluate-a-password-manager)  
      **A few password mangers to get you started.**  
      - [KeePass](https://keepass.info/)  
      - [BitWarden](https://bitwarden.com/)  
      - [Pass](https://www.passwordstore.org/)  
      - [1password](https://1password.com/)  
      
      
## License
Quick-pass is available under the GNU General Public License v3 (GPLv3)  
Check out [License](LICENSE) for more details.


## Contact Info
Have Questions, comments, complaints,  
concerns, predictions, spam?  
Send it my way.  
Email: cryanb91@gmail.com

