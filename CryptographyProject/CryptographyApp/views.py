from django.shortcuts import render
from .crypto import Caesar, AutoKey, Playfair, DES, RSA
# Create your views here.
# def dashboard(request):
#     return render(request, 'dashboard.html')
# def modulo(request):
#     result = request.GET['number1']
#
#     return render(request, 'modulo.html', {'result': result})
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
        key = int(request.POST['key'])
        plainList = list(plain.replace(' ', '').lower())
        if Type == "encryption":
            result = ''.join(Playfair.encryption(plainList, key))
        else:
            result = ''.join(Playfair.decryption(plainList, key))
        context = {
            'plain': plain,
            'key': key,
            'result': result
        }
        return render(request, 'playfair.html', context)

def split_numbers(text):
    return [int(char) for char in text]

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

