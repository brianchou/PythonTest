def f_products(prodNum):
    i = 0
    products=[]

    for i in range(prodNum):
        inputItem = input("Please enter Product Name :\n")
        products.append(inputItem)
    return products


def f_productPrices(prodNum):
    j=0    
    productPrices=[]

    for j in range(prodNum):
        inputPrice = input("Please enter Product Price :\n")
        inputPrice=float(inputPrice)
        productPrices.append(inputPrice)
    return productPrices


def f_productSold(prodSoldNum):
    m=0
    productSold=[]
    
    for m in range(prodSoldNum):
        inputSoldItem = input("Please enter Product Sold Name :\n")
        productSold.append(inputSoldItem)
    return  productSold

def f_soldPrice(prodSoldNum):              
    n=0
    soldPrice = []

    for n in range(prodSoldNum):
        inputSoldPrice = input("Please enter Product Sold Price :\n")
        inputSoldPrice=float(inputSoldPrice)
        soldPrice.append(inputSoldPrice)
    return soldPrice


def priceCheck():

    prodNum=input("Please enter Product Numbers :\n")

    prodNum=int(prodNum)

    products = f_products(prodNum)

    productPrices = f_productPrices(prodNum)

    prodSoldNum = input("Please enter Product Sold Numbers :\n")
    
    prodSoldNum=int(prodSoldNum)

    productSold = f_productSold(prodSoldNum)

    soldPrice = f_soldPrice(prodSoldNum)
        
    x = 0
    y = 0
    error = 0
    
    for x in range(prodSoldNum):
        for y in range(prodNum):
            if products[y] == productSold[x]:
                if productPrices[y] != soldPrice[x]:
                    error = error + 1               

    error = str(error)
    
    print("error is " + error)

priceCheck()