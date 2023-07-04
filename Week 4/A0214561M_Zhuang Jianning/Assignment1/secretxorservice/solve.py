#!/usr/bin/env python3
import os

def xor(a, b):
    return bytes([i^j for i,j in zip(a,b)])

def extend_key(key, size):
    return key*(size//len(key)) + key[:size%len(key)]

ciphertext = "83d91269208a2155492adc43af5e84ec1f2da0f05e7fa5553d5017e636e84532c08a205810bd5a383075a473dd01b2dc2872c3826a1cce66592d1d"
key = ciphertext[:54]
flag = ciphertext[64:]
hexflag = xor(bytes.fromhex(flag), bytes.fromhex(key)).hex()

    
print(bytes.fromhex(hexflag).decode())
    

