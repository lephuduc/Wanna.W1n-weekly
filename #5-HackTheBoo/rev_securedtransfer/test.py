from Crypto.Cipher import AES

key = b'supersecretkeyusedforencryption!'
iv = b'someinitialvalue'

cipher = AES.new(key,AES.MODE_CBC,iv)

print(cipher.decrypt(bytes.fromhex('5f558867993dccc99879f7ca39c5e406972f84a3a9dd5d48972421ff375cb18c')))