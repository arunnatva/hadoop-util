#!/bin/python

import subprocess as sp
import sys

def get_key(str_alias, str_provider_path):
    cp = sp.check_output(['hadoop', 'classpath']) 
    cp = cp + ':decrypt.jar'
    return sp.check_output(['java', '-cp', cp, 'DecryptionUtilDriver', str_alias, str_provider_path]).split(":")[1].strip()
   


a = sys.argv[1]
b = sys.argv[2]

print get_key(a,b)
