from flask import render_template,request
from app import app
import requests
url=requests.get("https://free.currencyconverterapi.com/api/v6/currencies")
data=url.json()
currencyName=[]
currencyId=[]
for i in data['results'].keys():
	currencyName.append(data['results'][i]['currencyName'])
	currencyId.append(data['results'][i]['id'])

newDict=dict(zip(currencyName,currencyId))    #this is already sorted




@app.route('/',methods=["POST","GET"])
def index():
	if request.method=="POST":
			currencyFrom=request.form.get("currency1")
			currencyTo=request.form.get("currency2")
			amount=int(request.form.get("enteredAmount"))
			fromid=newDict.get(currencyFrom)
			toid=newDict.get(currencyTo)
			query=fromid+'_'+toid
			result=requests.get("https://free.currencyconverterapi.com/api/v6/convert?q="+query+"&compact=ultra").json()
			for key,value in result.items():
				finalresult=amount*result.get(key)
			return render_template('home.html',currencyName=newDict,res=finalresult)	


    
	return render_template('home.html',currencyName=newDict)
