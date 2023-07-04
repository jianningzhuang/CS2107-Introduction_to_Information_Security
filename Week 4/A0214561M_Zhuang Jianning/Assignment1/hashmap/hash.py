from hashlib import sha1

uppercase = ['A', 'B', 'C','D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

print('073158933d0377d419cd1e5dfcb4eafde8d1dd8a' == sha1(b'P@ssw0rd1!').hexdigest())

for i in range(26):
	for j in range(26):
		for k in range(26):
			for l in range(26):
				for m in range(26):
					for n in range(26):
						key = bytes(uppercase[i] + uppercase[j] + uppercase[k] + uppercase[l] + uppercase[m] + uppercase[n], 'ascii')
						hashval = sha1(b'CS2107{P@ssw0rd1!_' + key + b'}').hexdigest()
						#print(hashval)
						if hashval == '9d9eea545804f3a4edf7315c5325a4e55268420d':
							print("FOUND!")
							print(key)
							print(b'CS2107{P@ssw0rd1!_' + key + b'}')
							
print("done")


