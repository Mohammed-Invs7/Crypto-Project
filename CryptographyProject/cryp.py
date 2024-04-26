from CryptographyApp.crypto import Caesar, AutoKey, DES, RSA, Playfair
plain = list("attack is today".replace(' ', '').lower())
k = 2
cc = Caesar.encryption(plain, k)
print("Caesar:")
print(f" plain: {''.join(plain)}")
print(f"Cypher: {''.join(cc)}")
cc2 = Caesar.decryption(cc, k)
print(f"dec(Cypher): {''.join(cc2)}")
print('#' * 50)
# ###############

# AutoKey
print("AutoKey:")
plain2 = list("attack is today".replace(' ', '').lower())
k2 = 2
cc2 = AutoKey.encryption(plain2, k2)
print(f" plain: {''.join(plain2)}")
print(f"Cypher: {''.join(cc2)}")
cc2 = AutoKey.decryption(cc2, k2)
print(f"dec(Cypher): {''.join(cc2)}")
print('#' * 50)
# ###############
print("DES:")
# 8 bit plaintext
plainText = [0, 0, 1, 0, 1, 0, 0, 0]
# for char in l:
#     lis.append(int(char))
# plainText = [1,0,0,0,1,0,1,0]
# 10 bit key
key = [1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
# cypherText = []
result = DES.encryption(plainText, key)
print(f" plain: {''.join(map(str, plainText))}")
print(f"Cypher: {''.join(map(str, result))}")
# print(f"Cypher: {result}")
result = DES.decryption(result, key)
# print(f"dec(Cypher): {''.join(result)}")
print(f"dec(Cypher): {''.join(map(str, result))}")
print('#' * 50)
# ###############
#print("".join(cypherText).upper())
# RSA
print("RSA:")

massage = 5
p = 7
q = 11
e = 13
publicKey, privateKey = RSA.generateKeys(p, q, e)
Cypher = RSA.encryption(massage, publicKey)
print(Cypher)
print(RSA.encryption(Cypher, privateKey))
print(f" plain: {massage}")
print(f"Cypher: {Cypher}")
print(f"dec(Cypher): {massage}")
print('#' * 50)
##############################
# playfair
# alphabet
print("playfair:")
plainText = list("instruments".lower().replace(' ', ''))
key = list("monarchy".lower().replace(' ', ''))
print(f"plaintext:\n{plainText}")
print(f"key:\n{key}")
cypherText, table = Playfair.encryption(plainText, key)
print(f"table:\n{table}")
print(f"cypherText:\n{cypherText}")
plainText, table = Playfair.decryption(cypherText, key)
print(f"table:\n{table}")
print(f"plaintext:\n{plainText}")
###################################