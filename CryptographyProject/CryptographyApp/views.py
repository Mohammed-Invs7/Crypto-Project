from django.shortcuts import render
from .crypto import Caesar, AutoKey, Playfair, DES, RSA


# Create your views here.
# def dashboard(request):
#     return render(request, 'dashboard.html')
# def modulo(request):
#     result = request.GET['number1']
#
#     return render(request, 'modulo.html', {'result': result})
def split_numbers(text):
    return [int(char) for char in text]


def permu(key, permutationList):
    temp = []
    for n in permutationList:
        if n - 1 > len(key):
            n = len(key)
        temp.append(key[n - 1])
    return temp


def index(request):
    return render(request, 'index.html')


def caeser(request):
    if request.method == "GET":
        return render(request, 'caeser.html')
    if request.method == "POST":
        Type = request.POST['type']
        plain = request.POST['plain']
        key = int(request.POST['key'])
        plainList = list(plain.replace(' ', '').lower())
        if Type == "encryption":
            result = ''.join(Caesar.encryption(plainList, key))
        else:
            result = ''.join(Caesar.decryption(plainList, key))
        context = {
            'plain': plain,
            'key': key,
            'result': result
        }
        return render(request, 'caeser.html', context)


def autokey(request):
    if request.method == "GET":
        return render(request, 'autoKey.html')
    if request.method == "POST":
        Type = request.POST['type']
        plain = request.POST['plain']
        key = int(request.POST['key'])
        plainList = list(plain.replace(' ', '').lower())
        if Type == "encryption":
            result = ''.join(AutoKey.encryption(plainList, key))
        else:
            result = ''.join(AutoKey.decryption(plainList, key))
        context = {
            'plain': plain,
            'key': key,
            'result': result
        }
        return render(request, 'autokey.html', context)


def playfair(request):
    if request.method == "GET":
        return render(request, 'autokey.html')
    if request.method == "POST":
        Type = request.POST['type']
        plain = request.POST['plain']
        key = request.POST['key']
        plainList = list(plain.lower().strip().replace(' ', ''))
        keyList = list(key.replace(' ', '').lower())
        if Type == "encryption":
            cypherText, table = Playfair.encryption(plainList, keyList)
            result = ''.join(cypherText)
        else:
            cypherText, table = Playfair.decryption(plainList, keyList)
            result = ''.join(cypherText)
        context = {
            'plain': plain,
            'key': key,
            'result': result,
            'table': table,
        }
        return render(request, 'playfair.html', context)


def des(request):
    if request.method == "GET":
        return render(request, 'des.html')
    if request.method == "POST":
        Type = request.POST['type']
        plain = request.POST['plain']
        key = request.POST['key']
        plainList = list(split_numbers(plain))
        keyList = list(split_numbers(key))
        if Type == "encryption":
            result = DES.encryption(plainList, keyList)
            result = ''.join(map(str, result))
        else:
            result = DES.decryption(plainList, keyList)
            result = ''.join(map(str, result))
        context = {
            'plain': plain,
            'key': key,
            'result': result
        }
        return render(request, 'des.html', context)


def rsa(request):
    if request.method == "GET":
        return render(request, 'rsa.html')
    if request.method == "POST":
        Type = request.POST['type']
        plain = request.POST['plain']
        p = int(request.POST['p'])
        q = int(request.POST['q'])
        e = int(request.POST['e'])
        plainList = int(plain)
        # Get Keys
        publicKey, privateKey = RSA.generateKeys(p, q, e)
        if Type == "encryption":
            result = RSA.encryption(plainList, publicKey)
        else:
            result = RSA.encryption(plainList, privateKey)
        context = {
            'plain': plain,
            'p': p,
            'q': q,
            'e': e,
            'result': result,
        }
        return render(request, 'rsa.html', context)


def modulo(request):
    if request.method == "GET":
        return render(request, 'modulo.html')
    if request.method == "POST":
        # Type = request.POST['type']
        number1 = int(request.POST['plain'])
        number2 = int(request.POST['key'])
        # plainList = list(plain.replace(' ', '').lower())

        result = number1 % number2
        context = {
            'plain': number1,
            'key': number2,
            'result': result
        }
        return render(request, 'modulo.html', context)


def congruence(request):
    if request.method == "GET":
        return render(request, 'congruence.html')
    if request.method == "POST":
        # Type = request.POST['type']
        # number1 % number2 == number3
        number1 = int(request.POST['plain'])
        number2 = int(request.POST['key'])
        number3 = int(request.POST['number3'])
        # plainList = list(plain.replace(' ', '').lower())

        result = RSA.congruence(number1, number2, number3)
        context = {
            'plain': number1,
            'key': number2,
            'number3': number3,
            'result': result,
        }
        return render(request, 'congruence.html', context)


def permutation(request):
    if request.method == "GET":
        return render(request, 'permutation.html')
    if request.method == "POST":
        # Type = request.POST['type']
        numbersText = request.POST['plain']
        orderText = request.POST['key']
        numbersList = split_numbers(numbersText.strip().split())
        orderList = split_numbers(orderText.strip().split())
        result = permu(numbersList, orderList)
        result = ' '.join(map(str, result))
        context = {
            'plain': numbersText,
            'key': orderText,
            'result': result,
        }
        return render(request, 'permutation.html', context)
