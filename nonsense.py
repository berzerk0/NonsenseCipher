#!/usr/bin/python3
import random, os, sys, string
from numpy.random import choice
from sys import argv

def wordLengthNonsense():
    lengths = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    weights = [0.037264254570273500,0.175318842199986000,0.236406451194256000,0.189381282342557000,0.111243932166923000,0.078605655153973800,0.063440861055711100,0.040783187304009700,0.029444577786707800,0.017499282688117500,0.009119047190912850,0.006025419813131460,0.002855956737689010,0.001300152218663240,0.000620758184978121,0.000373705809092622,0.000136816980316337,0.000092253735299016,0.000057072226074815,0.000030490641327641]

    return (choice(lengths, p=weights))

def nonsenseWords(num_of_words):
    result = ""

    for i in range(1,num_of_words+1):
        addition = ''.join(random.SystemRandom().choice(string.ascii_uppercase) for _ in range(wordLengthNonsense()))
        if i == 1:
            result = addition
        else:
            result = result+" "+addition
    return result


#Are the number of words provided?
if len(argv) < 2:
     print ('\nUsage: python3 nonsense.py (number of \"words\" to generate to std output)')
     sys.exit()

#Is the argument an integer, though?
try:
   val = int(argv[1])
except ValueError:
   print ('\nUsage: python3 nonsense.py (number of \"words\" to generate to std output)')
   sys.exit()


print (nonsenseWords((int(argv[1]))))
