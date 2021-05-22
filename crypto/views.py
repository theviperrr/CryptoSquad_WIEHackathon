from django.shortcuts import render, redirect
import requests
import json

# Create your views here.

def index(request):
	return render(request, 'index.html')

def price(request):
	price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,BNB,USDT,ADA,DOGE,TRX&tsyms=USD")
	price = json.loads(price_request.content)
	return render(request, 'price.html', {'price': price})

