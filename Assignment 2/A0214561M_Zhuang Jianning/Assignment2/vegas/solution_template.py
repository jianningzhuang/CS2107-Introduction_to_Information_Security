from pwn import *
from subprocess import *

context.log_level = 'debug'

#p = process("./vegas") # use this to test locally first
p = remote("cs2107-ctfd-i.comp.nus.edu.sg", "4008") # connect to the server when u have found the exploit. Change the port/IP according to challenge description.

name = "JN\n" # change this to the name you want to enter
p.sendlineafter("name: ", name)

change_fate = True # change to "True" if you want to change your fate
if change_fate:
    p.sendlineafter("fate?\n", "yes!yes!yes!")
    p.sendafter("name: ", name)
else:
    p.sendlineafter("fate?\n", "no")


nums = ["0", "0", "0", "0", "0", "0", "0"] # change to the number you want to guess
for j in range(7):
    p.sendlineafter("100: ", nums[j])
    if (b"Unlucky!" in p.recvline()):
        break
