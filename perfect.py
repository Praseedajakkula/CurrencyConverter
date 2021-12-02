print("enter the input currency")
in1=input()
print("enter the currency u want")
in2=input()
print("enter the amount")
in3=int(input())
def converttoinr(currency,amount):
    if (currency.upper()=="USD"):
        return amount*75.05
    elif(currency.upper()=="YEN"):
        return amount*1/1.5
    elif(currency.upper()=="AFG"):
        return amount*1/1.28
    elif(currency.upper()=="DIRHAM"):
        return amount*20.42
    elif (currency.upper()=="INR"):
        return amount


def convertfrominr(currency,amount):
    if(currency.upper()=="YEN"):
        return amount*1.5
    elif(currency.upper()=="AFG"):
        return amount*1.28
    elif(currency.upper()=="DIRHAM"):
        return amount*1/20.42
    elif(currency.upper()=="USD"):
        return amount*1/75.05
    elif(currency.upper()=="INR"):
        return amount

def end_to_end_conversion(from_currency,to_currency,amount):
    if (from_currency==to_currency):
        return amount

    inr_amount = converttoinr(from_currency,amount)
    final_amount = convertfrominr(to_currency,inr_amount)

    return final_amount


print(end_to_end_conversion(in1,in2,in3))
