def createTransaction(amount, tType, description):
    return {"Amount" : amount, "Type" : tType, "Description" : description}

def getAmount(l):
    return l["Amount"]

def getType(l):
    return l["Type"]

def getDescription(l):
    return l["Description"]

def setAmount(l, amount):
    l["Amount"] = amount

def setType(l, type):
    l["Type"] = type

def setDescription(l, description):
    l["Description"] = description