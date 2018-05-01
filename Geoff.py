import os, timew
import random
import sys

nameIn = ['what is your name?', 'Whats your name?', 'What is your name?', 'whats your name?']
greetIn = ['Hello !', 'hi !', 'Hello there !', 'hi there !']
bith = ['What is your date of birth ?', 'what is your DOB ?', 'what is your date of birth ?', 'What is your DOB ?']
bootmaster = ['Who is your bootmaster ?', 'Who is your bootmaster']

greetOut = ['hello there, im Geoff', 'Hello, Im Geoff', 'Greetings, Im Geoff']
nameOut = ['Im Geoff, nice to meet you !', 'Im Geoff ', 'Im called Geoff'

B = 'Geoff is online'
print (B)
while True:
        H = raw_input('=>').strip()
        HLower = H.lower()

        if H == ''
                print ('=> Pleasure meeting you !')
                time.sleep(1)
                cs.system("")
                break
        elif HLower in nameIn:
                print '=>' + (random.choice(nameOut))
        elif HLower in greetIn:
                 print '=>' + (random.choice(greetOut))
        elif HLower in bootmaster:
                 print '=> My Bootmaster is Dave !'
        elif HLower in bith:
                 print '=> i was activated for a Dissertation !'
    
