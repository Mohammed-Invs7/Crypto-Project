alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z')


class Caesar:

    # Caesar
    @staticmethod
    def encryption(plainText, key):
        cypherText = []

        for char in plainText:
            cypherText.append(alphabet[(alphabet.index(char) + key) % 26])
        return cypherText

    @staticmethod
    def decryption(plainText, key):
        cypherText = []

        for char in plainText:
            cypherText.append(alphabet[(alphabet.index(char) - key) % 26])
        return cypherText
        #########


class AutoKey:
    # autoKey
    @staticmethod
    def encryption(plainText, key):
        cypherText = []

        for char in plainText:
            cypherText.append(alphabet[(alphabet.index(char) + key) % 26])
            key = alphabet.index(char)
        return cypherText

    @staticmethod
    def decryption(cypherText, key):
        plainText = []

        for char in cypherText:
            key = (alphabet.index(char) - key) % 26
            plainText.append(alphabet[key])
        return plainText
        #########


class DES:
    # DES    
    # Define variables
    p10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    p8 = [6, 3, 7, 4, 8, 5, 10, 9]
    p4 = [2, 4, 3, 1]
    ip = [2, 6, 3, 1, 4, 8, 5, 7]
    ip_1 = [4, 1, 3, 5, 7, 2, 8, 6]
    E_P = [4, 1, 2, 3, 2, 3, 4, 1]
    s_box0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
    s_box1 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]

    # #######
    @classmethod
    def encryption(cls, bits, key):
        # steps to find Key1 and key2
        key1, key2 = cls.getKeys(key)
        # we find Key1 and Key2
        # Encryption phase
        p_ip = cls.permutation(bits, cls.ip)
        liftP, rightP = cls.cutHalf(p_ip)
        # Round 1
        left, right = cls.funcKey(liftP, rightP, key1)
        # Round 2
        left, right = cls.funcKey(right, left, key2)
        return cls.permutation(left + right, cls.ip_1)

    @classmethod
    def decryption(cls, bits, key):
        # steps to find Key1 and key2
        key1, key2 = cls.getKeys(key)
        # we find Key1 and Key2
        # Decryption phase
        p_ip = cls.permutation(bits, cls.ip)
        liftP, rightP = cls.cutHalf(p_ip)
        # Round 1
        left, right = cls.funcKey(liftP, rightP, key2)
        # Round 2
        left, right = cls.funcKey(right, left, key1)
        return cls.permutation(left + right, cls.ip_1)

    @staticmethod
    def permutation(key, permutationList):
        temp = []
        for n in permutationList:
            temp.append(key[n - 1])
        return temp

    @staticmethod
    def shiftLeft(List, numShift=1):
        return List[numShift:] + List[:numShift]

    @classmethod
    def getKeys(cls, key):
        # steps to find key1 and key2
        p10_key = cls.permutation(key, cls.p10)
        liftKey, rightKey = cls.cutHalf(p10_key)
        liftKey = cls.shiftLeft(liftKey)
        rightKey = cls.shiftLeft(rightKey)
        key1 = cls.permutation(liftKey + rightKey, cls.p8)
        liftKey = cls.shiftLeft(liftKey, 2)
        rightKey = cls.shiftLeft(rightKey, 2)
        key2 = cls.permutation(liftKey + rightKey, cls.p8)
        return key1, key2

    @staticmethod
    def XOR(L1, L2):
        for i in range(len(L1)):
            L1[i] ^= L2[i]
        return L1

    @staticmethod
    def cutHalf(L):
        return L[:len(L) // 2], L[len(L) // 2:]

    @staticmethod
    def sBox(bits, sBox):
        # get rows and columns
        row = int('0b' + ''.join(map(str, [bits[0], bits[3]])), 2)
        column = int('0b' + ''.join(map(str, [bits[1], bits[2]])), 2)
        # convert sBox value to binary output (list)
        return [int(char) for char in f"{sBox[row][column]:02b}"]

    @classmethod
    def funcKey(cls, left, right, key):
        rightFunc = cls.permutation(right, cls.E_P)
        rightFunc = cls.XOR(rightFunc, key)
        rightFuncL, rightFuncR = cls.cutHalf(rightFunc)
        # calc sBox
        l_sBox = cls.sBox(rightFuncL, cls.s_box0)
        r_sBox = cls.sBox(rightFuncR, cls.s_box1)
        # new left
        sBox_p4 = cls.permutation(l_sBox + r_sBox, cls.p4)
        newLiftP = cls.XOR(sBox_p4, left)
        return newLiftP, right


class RSA:
    # This method uses for Encryption and Decryption
    @staticmethod
    def encryption(massage, key):
        return (massage ** key[0]) % key[1]

    @staticmethod
    def congruence(n, n2, nm):
        # Number1 === Number2 (mod Nm)
        return n % nm == n2 % nm

    # RSA Private key Public key
    @classmethod
    def generateKeys(cls, p, q, e):
        n = p * q
        c_n = (p - 1) * (q - 1)
        d = 0
        # e: 1 < e < c_n prime
        # if 1 >= e and e >= c_n:
        #    return None
        # e * d === 1 (mod c_n)
        for i in range(n):
            if cls.congruence(e * i, 1, c_n, ):
                d = i
                break
        # Public key, Private key
        return (e, n), (d, n)


class Playfair:
    # playfair
    alphabetNew = list(alphabet)
    alphabetNew.remove('j')

    # remove doubling chars
    @staticmethod
    def RemoveDouble(List):
        temp = []

        for i in range(len(List)):
            if List[i] in temp:
                continue
            temp.append(List[i])
        return temp

    # replace object with another object
    @staticmethod
    def replace(List, old, new):
        for i in range(len(List)):
            if List[i] == old:
                List[i] = new
        return List

    @classmethod
    def intiateKey(cls, key):
        key = cls.RemoveDouble(key)
        # edit key to get i and j together (replace j with i)
        key = cls.replace(key, 'j', 'i')
        key = cls.RemoveDouble(key)
        # remove key chars from alphabet list
        alpha = []
        alpha += cls.alphabetNew
        for char in key:
            alpha.remove(char)
        key += alpha
        return key

    @staticmethod
    def intiateTable(key):
        table = [[], [], [], [], []]  # table[raw][column]

        # fill key + subAlphabet to the table
        for raw in range(5):
            table[raw] += key[raw * 5:(raw + 1) * 5]
        return table

    @staticmethod
    def intiatePlaintext(plainText):
        # plaintext split similar characters with 'x'
        temp = plainText
        i = 0
        while i < len(plainText) - 1:
            if plainText[i] == plainText[i + 1]:
                temp.insert(i + 1, 'x')
            i += 2
        plainText = temp
        if len(plainText) % 2 != 0:
            plainText.append('x')
        return plainText

    @staticmethod
    def deIntiatePlaintext(plainText):
        # plaintext remove 'x' between similar characters
        temp = plainText
        i = 0
        while i < len(plainText) - 2:
            if plainText[i] == plainText[i + 2]:
                temp.remove(i + 1)
            i += 2
        return temp

    # find row and column for the two chars
    @staticmethod
    def getCharIndex(char, table):
        index = []
        for i in range(len(table)):
            if table[i].count(char) == 1:
                index += i, table[i].index(char)
                break
        return index

    @classmethod
    def encryption(cls, plainText, key):
        key = cls.intiateKey(key)
        table = cls.intiateTable(key)
        plainText = cls.intiatePlaintext(plainText)

        # encryption: →↓
        # three possible
        # raw raw      [a,x] [a,y] ,(char[x] x: 0 row, 1 column)
        # column column [x,a] [y,a] ,
        # raw column    [a,x] [b,y]

        # find row and column for the two chars
        cypherText = []

        for p in range(0, len(plainText), 2):
            char1 = cls.getCharIndex(plainText[p], table)
            char2 = cls.getCharIndex(plainText[p + 1], table)
            # same row
            if char1[0] == char2[0]:
                if char1[1] == len(table[0]) - 1:
                    cypherText += table[char1[0]][0], table[char2[0]][char2[1] + 1]
                    continue
                if char2[1] == len(table[0]) - 1:
                    cypherText += table[char1[0]][char1[1] + 1], table[char2[0]][0]
                    continue
                cypherText += table[char1[0]][char1[1] + 1], table[char2[0]][char2[1] + 1]
            # same column
            elif char1[1] == char2[1]:
                if char1[0] == len(table[0]) - 1:
                    cypherText += table[0][char1[1]], table[char2[0] + 1][char2[1]]
                    continue
                if char2[0] == len(table[0]) - 1:
                    cypherText += table[char1[0] + 1][char1[1]], table[0][char2[1]]
                    continue
                cypherText += table[char1[0] + 1][char1[1]], table[char2[0] + 1][char2[1]]
            # different row and column
            else:
                cypherText += table[char1[0]][char2[1]], table[char2[0]][char1[1]]

        return cypherText, table

    @classmethod
    def decryption(cls, cypherText, key):
        key = cls.intiateKey(key)
        table = cls.intiateTable(key)

        # decryption: ↑←
        # three possible
        # raw raw      [a,x] [a,y] ,(char[x] x: 0 row, 1 column)
        # column column [x,a] [y,a] ,
        # raw column    [a,x] [b,y]

        # find row and column for the two chars
        plainText = []

        for p in range(0, len(cypherText), 2):
            char1 = cls.getCharIndex(cypherText[p], table)
            char2 = cls.getCharIndex(cypherText[p + 1], table)
            # same row
            if char1[0] == char2[0]:
                if char1[1] == 0:
                    plainText += table[char1[0]][4], table[char2[0]][char2[1] - 1]
                    continue
                if char2[1] == 0:
                    plainText += table[char1[0]][char1[1] - 1], table[char2[0]][4]
                    continue
                plainText += table[char1[0]][char1[1] - 1], table[char2[0]][char2[1] - 1]
            # same column
            elif char1[1] == char2[1]:
                if char1[0] == 0:
                    plainText += table[4][char1[1]], table[char2[0] - 1][char2[1]]
                    continue
                if char2[0] == 0:
                    plainText += table[char1[0] - 1][char1[1]], table[4][char2[1]]
                    continue
                plainText += table[char1[0] - 1][char1[1]], table[char2[0] - 1][char2[1]]
            # different row and column
            else:
                plainText += table[char1[0]][char2[1]], table[char2[0]][char1[1]]

        return cls.deIntiatePlaintext(plainText), table
#########################################
# playfair
# alphabet
# plainText = list("instruments".lower().replace(' ', ''))
# key = list("monarchy".lower().replace(' ', ''))
# print(f"plaintext:\n{plainText}")
# print(f"key:\n{key}")
# cypherText, table = encryption(plainText, key)
# print(f"table:\n{table}")
# print(f"cypherText:\n{cypherText}")
# plainText, table = decryption(cypherText, key)
# print(f"table:\n{table}")
# print(f"plaintext:\n{plainText}")
####################################
# 'append', 'clear', 'copy', 'count', 'extend',
# 'index', 'insert', 'pop', 'remove',
#  'reverse', 'sort'

# plainText = list("attack is today".replace(' ',''))
# 8 bit plaintext
# plainText = [0,0,1,0,1,0,0,0]
# plainText = [1,0,0,0,1,0,1,0]
# 10 bit key
# key = [1,1,0,0,0,1,1,1,1,0]
# cypherText = []


# #result = encryption(plainText, key)
# #print(f" plain: {plainText}")
# #print(f"Cypher: {result}")
# #result = desD(result, key)
# #print(f" plain: {result}")
# bin() int(bin(n), 2)
# print("".join(str(
#
#
# massage = 5
# p = 7
# q = 11
# e = 13
#
# #publicKey, privateKey = generateKeys(p, q, e)
# #Cypher = RSA.encryption(massage, publicKey)
# #print(Cypher)
# #print(RSA.encryption(Cypher, privateKey))
