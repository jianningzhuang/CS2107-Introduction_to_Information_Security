import requests
from bs4 import BeautifulSoup

ciphertext = 'b12c3f6a001ab28eb3dafbfa2d634dc20419370e98feeedfdb2d679bddf49f3047525527b5dbf890ae7bb8edcbc33b82b652a8d4b7d6dedb343b605e0d340d48ac0b5f7190fe1bc7156962f88367d098c60e7e1815dbc964a5784a7f908142bb3c5f80f9917b982de84f6da930d6fe85'

cipherbytes = bytearray.fromhex(ciphertext)

url = 'http://cs2107-ctfd-i.comp.nus.edu.sg:4004/'

def xor(a, b):
    return bytes([i^j for i,j in zip(a,b)])

def padding():
	iv = bytearray.fromhex('00000000000000000000000000000000')
	paddingblock = cipherbytes[-16:]
	for i in range(256):
		iv[-1] = i
		#print(iv)
		test = iv + paddingblock
		data = {'data': test.hex()}
		request = requests.post(url, data=data).text
		answer = BeautifulSoup(request, 'html.parser')
		success = answer.find(id="result").string
		if success == "Successful!":
			print(success)
			print(i)
			one = bytes.fromhex('01')
			length = 1 ^ iv[-1] ^ cipherbytes[-17]
			print(cipherbytes[-17])
			print(length)

# let T be Dk(ciphertext[-16:]), X be original plaintext padding block, IV be cipherbytes[-32:-16], IV' be 16 bytes of 0 testing padding with last byte from 0 to 255
# T = X xor IV
# T xor IV' with last byte 179 returns successful meaning \x01 in new plaintext X'			
# last byte of X = last byte of (X' xor IV' xor IV) = 9 = length of padding

#padding()

def generateNewPadding(length):
	padding = bytearray.fromhex('00000000000000000000000000000000')
	for i in range(17-length, 16):
		curr = (i + length - 16) ^ (i + length - 15)
		padding[i] = curr
	print(padding)
	return padding


# X' = X xor ....t[new padding]

flag = []

def decryptblock(IV, block, start):
	curr = IV
	for i in range(start, 16):
		padding = generateNewPadding(i + 1)
		for j in range(256):
			padding[15-i] = j
			iv = xor(curr, padding)
			test = iv + block
			data = {'data': test.hex()}
			request = requests.post(url, data=data).text
			answer = BeautifulSoup(request, 'html.parser')
			success = answer.find(id="result").string
			if success == "Successful!":
				print(success)
				print(chr(j^1))
				flag.insert(0, chr(j^1))
				curr = iv
				break

decryptblock(cipherbytes[-32:-16], cipherbytes[-16:], 9)
decryptblock(cipherbytes[-48:-32], cipherbytes[-32:-16], 0)
decryptblock(cipherbytes[-64:-48], cipherbytes[-48:-32], 0)
decryptblock(cipherbytes[-80:-64], cipherbytes[-64:-48], 0)

print(''.join(flag))

#CS2107{1_l1k3_7h15_p4dd1n6_0r4cl3_53rv1c3}




