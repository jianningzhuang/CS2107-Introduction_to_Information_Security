from Crypto.Cipher import AES

key1 = '6F738g9Zz'
key2 = 'S3j4g'

message = b'I have been blocked everywhereee'

ciphertext1 = '0df67cc18cdfc7f7605596e159d1102d'

for i in range(128):
	for j in range(128):
		key = bytes(key1 + chr(i)+ chr(j) + key2, 'ascii')
		#print(key)
		cbc = AES.new(key, AES.MODE_CBC, message[16:])
		C1 = bytes.fromhex(ciphertext1)
		C0prime = cbc.decrypt(C1).hex()
		#print(m1)
		if C0prime[6:8] == 'c2' and C0prime[18:20] == 'f8' and C0prime[28:30] == '2a':
			print("FOUND KEY")
			print(C0prime)
			print(key)
			print(i, j)
			
keyfound = b'6F738g9Zzc1S3j4g'
i = 99
j = 49

ciphertext0 = '3c8aabc2edfc8afe35f81dacff232a83'


cbc1 = AES.new(keyfound, AES.MODE_CBC, message[:16])
C0 = bytes.fromhex(ciphertext0)
flag1 = cbc1.decrypt(C0)
print(bytes(chr(i)+ chr(j), 'ascii') + flag1)
