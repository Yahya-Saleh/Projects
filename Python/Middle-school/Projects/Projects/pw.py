#! python3.

#pw.py - an insecure password locker program

passwards = {'email': 'f73js7s920sa'
            ,'blog': 'g6sj27sia',
            'adobe': 'hs82,sz0ad'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]      # first command line arg is the account name

if account in passwards:
    pyperclip.copy(passwards[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
