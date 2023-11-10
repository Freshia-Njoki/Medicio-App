import base64
import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from myapp.models import Member
from myapp.forms import ProductsForm
from myapp.models import Product
import requests
from myapp.credentials import MpesaC2bCredential, MpesaAccessToken, LipanaMpesaPpassword
from requests.auth import HTTPBasicAuth


# Create your views here.
def register(request):
    if request.method == 'POST':
        member = Member(firstname=request.POST['firstname'], lastname=request.POST['lastname'],
                        username=request.POST['username'], password=request.POST['password'])
        member.save()
        return redirect('/')
    else:
        return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def index(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'],
                                 password=request.POST['password']).exists():
            member = Member.objects.get(username=request.POST['username'],
                                        password=request.POST['password'])
            return render(request, 'index.html', {'member': member})
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def inner(request):
    return render(request, 'inner-page.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def departments(request):
    return render(request, 'departments.html')


def doctors(request):
    return render(request, 'doctors.html')


def contact(request):
    return render(request, 'contact.html')


def add(request):
    if request.method == 'POST':
        form = ProductsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = ProductsForm()
        return render(request, 'addproduct.html', {'form': form})


def show(request):
    products = Product.objects.all()
    return render(request, 'show.html', {'products': products})


def delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('/show')


def edit(request, id):
    products = Product.objects.get(id=id)
    return render(request, 'edit.html', {'products': products})


def update(request, id):
    product = Product.objects.get(id=id)
    form = ProductsForm(request.POST, instance=product)
    if form.is_valid():
        form.save()
        return redirect('/show')
    else:
        return render(request, 'edit.html', {'product': product})


def token(request):
    consumer_key = 'jGwhIUHzBuLqsMmE4Y9KE0OC2Lfh6c1w'
    consumer_secret = 'tFgqczyjiayK16Hp'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
    return render(request, 'pay.html')

def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Kelcho Tech",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse(response)