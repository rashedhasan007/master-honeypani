from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404, redirect
from django.template.context import RequestContext
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


def hello(request):
   text = """<h1>welcome to my app !</h1>"""
   return HttpResponse(text)

def index(request):
   
    return render(request,'index.html')
def product(request):
   time_series_json="my name is rashed"
   context={}
   context['Shop_name']="hey welcome to my store"
   return render(request,'product-detail.html',context)
def cart(request):

    b = """{u'1': u'xxxxx', u'2': u'yyyyy'}"""
    a = json.loads(b)
    return render(request,'cart.html',a)


def myindex(request,my_id):
    # initializations
    cred = credentials.Certificate('try.json')
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    # Reading the data

    emp_ref = db.collection(my_id)
    docs = emp_ref.stream()
    print(docs)

    for doc in docs:
        print('{} => {} '.format(doc.id, doc.to_dict()))

    return render(request,'index.html')
