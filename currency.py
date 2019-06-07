f=open("C:/Users/vishm/PycharmProjects/currency exchange/exchanges")
exchangeRates=f.readlines()

currencyDict={}
for line in exchangeRates:
    x=line.split("\t")
    currencyDict[x[0]]=x[1]

print("Exchange Rates : \n")
print(currencyDict)
amount=int(input("Enter the amount in rupees"))
print("Enter the currency type in which you want to convert. \n "
      "Available options :")
[print(item) for item in currencyDict.keys()]
currency=input("Please enter the currency type : ")
print(amount," INR is equal to ",amount*float(currencyDict[currency]), currency)


