def planecost(city):
    if city=="Manchester":
        return 120
    elif  city=='Texas':
        return 300
    elif  city=="Capetown":
        return 500
    else:
        return 700
def Hotelcost(days):
    return 800*5
def carrent(days):
    return 700*days
def tripcost(days,city,extraspending):
    return (Hotelcost(days)+carrent(days)+planecost(city)+extraspending)
print("the total trip cost is",tripcost(7,"Manchester",900))
print("the total trip cost is",tripcost(9,"Instanbul",900000))