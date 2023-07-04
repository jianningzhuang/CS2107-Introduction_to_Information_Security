from pwn import *
from subprocess import *

context.log_level = 'debug'

found = 0
while found == 0:
    found = 1
    #p = process("./vegas") # use this to test locally first
    p = remote("cs2107-ctfd-i.comp.nus.edu.sg", "4008") # connect to the server when u have found the exploit. Change the port/IP according to challenge description.

    name = "JN" # change this to the name you want to enter
    p.sendlineafter("name: ", name)
    guess = check_output(["./generate"])
    change_fate = True # change to "True" if you want to change your fate
    if change_fate:
        p.sendlineafter("fate?\n", "yes!yes!yes!")
        guess = check_output(["./generate"])
        p.sendlineafter("name: ", name)
    else:
        p.sendlineafter("fate?\n", "no")

	#print(guess)

    nums = [guess[0:2], guess[2:4], guess[4:6], guess[6:8], guess[8:10], guess[10:12], guess[12:14]] # change to the number you want to guess
    for j in range(7):
        p.sendlineafter("100: ", nums[j])
    #print(nums[j])
        if (b"Unlucky!" in p.recvline()):
            found = 0
            break
        
#CS2107{f473_15_1n_y0ur_0wn_h4nd5}
