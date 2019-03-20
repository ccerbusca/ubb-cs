import datetime
import os
from domain import *

def validateAdd(params):
    if len(params) != 3:
        raise ValueError("Wrong number of parameters.")
    elif not params[0].isdigit():
        raise ValueError("The amount introduced is not entirely composed of digits.")
    elif params[1] != "in" and params[1] != "out":
        raise ValueError("The specified type of trasaction is wrong")
    elif int(params[0]) <= 0:
        raise ValueError("The amount cannot be less or equal to zero")

def validateInsert(params):
    if len(params) != 4:
        raise ValueError("Wrong number of parameters.")
    if not params[0].isdigit():
        raise ValueError("The day specified is not entirely composed of digits.")
    day = int(params[0])
    if day < 1 or day > 31:
        raise ValueError("Please specify a valid day of the month")
    elif not params[1].isdigit():
        raise ValueError("The amount specified is not entirely composed of digits.")
    elif params[2] != "in" and params[2] != "out":
        raise ValueError("The specified type of trasaction is wrong")
    elif int(params[1]) <= 0:
        raise ValueError("The amount cannot be less or equal to zero")

def validateRemove(params):
    if len(params) not in (1, 3):
        raise ValueError("Wrong number of parameters.")
    if len(params) == 1 and params[0] != "in" and params[0] != "out" and not params[0].isdigit():
        raise ValueError("Wrong type of arguments for the remove function")
    if len(params) == 3 and (not params[0].isdigit() or not params[2].isdigit() or params[1] != "to"):
            raise ValueError("Wrong type of arguments for the remove function")

def validateReplace(params):
    if len(params) != 5:
        raise ValueError("Wrong number of parameters.")
    if not params[0].isdigit() or not params[4].isdigit() or params[1] not in ("in", "out") or params[3] != "with":
        raise ValueError("Wrong type of arguments for the remove function")
    if int(params[4]) <= 0:
        raise ValueError("The amount cannot be less or equal to zero")

def validateListTransactions(params):
    if len(params) not in (0, 1, 2):
        raise ValueError("Wrong number of parameters.")
    if len(params) == 1 and params[0] not in ("in", "out"):
        raise ValueError("Wrong type of arguments for the list function")
    if len(params) == 2:
        if params[0] not in ("<", ">", "=", "balance") or not params[1].isdigit():
            raise ValueError("Wrong type of arguments for the list function")
        if params[0] not in ("<", ">", "=") and (int(params[1]) < 1 or int(params[1]) > 31):
            raise ValueError("The day specified is not entirely composed of digits.")

def validateSum(params):
    if len(params) != 1:
        raise ValueError("Incorrect number of arguments")
    if params[0] not in ("in", "out"):
        raise ValueError("You should specify a valid type of transaction")

def validateMax(params):
    if len(params) != 2:
        raise ValueError("Incorrect number of arguments")
    if params[0] not in ("in", "out") or not params[1].isdigit():
        raise ValueError("Incorrect arguments specified")

def validateFilter(params):
    if len(params) not in (1, 2):
        raise ValueError("Wrong amount of parameters")
    if params[0] not in ("out", "in"):
        raise ValueError("Specifiy a valid type of transaction")
    if len(params) == 2 and not params[1].isdigit():
        raise ValueError("The value cannot contain something other than digits")
    if len(params) == 2 and int(params[1]) <= 1:
        raise ValueError("The value cannot be less or equal 1")

def validateUndo(params):
    if len(params) != 0:
        raise ValueError("Wrong function call")

def undo(acc):
    """Function that cancels the last operation entered"""
    if len(undo.list) != 0:
        toUndo = undo.list.pop()
        cmd = next(iter(toUndo))
        if cmd == "add":
            undoAddInsert(acc, toUndo[cmd])
        elif cmd == "insert":
            undoAddInsert(acc, toUndo[cmd])
        elif cmd == "replace":
            undoReplace(acc, toUndo[cmd])
        elif cmd == "remove":
            undoRemove(acc, toUndo[cmd])
        elif cmd == "filter":
            undoFilter(acc, toUndo[cmd])
    else:
        print("Nothing to undo")

def undoAddInsert(acc, params):
    """A function that is called when undo-ing an add or insert operation"""
    for i in acc[params[0]]:
        if int(params[1]) == getAmount(i) and params[2] == getType(i) and params[3] == getDescription(i):
            acc[params[0]].remove(i)
            break

def undoRemove(acc, params):
    """A function that is called when undo-ing a remove operation"""
    for i in params:
        for j in i[1:]:
            acc[i[0]].append(j)

def undoReplace(acc, params):
    """A function that is called when undo-ing a replace operation"""
    for i in acc[params[0]]:
        if getType(i) == params[1] and getDescription(i) == params[2]:
            setAmount(i, params[3])
            break

def undoFilter(acc, params):
    """A function that is called when undo-ing a filter operation"""
    for p in params:
        for i in p[1:]:
            acc[p[0]].append(i)

def runTests():
    testAdd()
    testInsert()
    testRemove()
    testReplace()
    testFilter()
    testUndo()
    undo.list.clear()

def testAdd():
    testAcc = initializeData()
    now = datetime.datetime.now()
    add(testAcc, ['100', 'in', 'salary'])
    add(testAcc, ['100', 'out', 'shopping'])
    assert testAcc[now.day] == [{'Amount' : 100, 'Type' : 'in', 'Description' : 'salary'},
                                {'Amount' : 100, 'Type' : 'out', 'Description' : 'shopping'}]

def testInsert():
    testAcc = initializeData()
    insert(testAcc, ['29', '100', 'in', 'salary'])
    insert(testAcc, ['28', '1000', 'out', 'shopping'])
    assert testAcc[29] == [{'Amount' : 100, 'Type' : 'in', 'Description' : 'salary'}]
    assert testAcc[28] == [{'Amount' : 1000, 'Type' : 'out', 'Description' : 'shopping'}]

def testRemove():
    testAcc = initializeData()
    insert(testAcc, ['29', '100', 'in', 'salary'])
    insert(testAcc, ['29', '100', 'in', 'salary'])
    insert(testAcc, ['28', '100', 'out', 'shopping'])
    insert(testAcc, ['27', '100', 'in', 'salary'])
    insert(testAcc, ['1', '100', 'in', 'salary'])
    insert(testAcc, ['2', '100', 'in', 'salary'])
    insert(testAcc, ['5', '100', 'out', 'shopping'])
    insert(testAcc, ['9', '100', 'in', 'salary'])
    insert(testAcc, ['15', '100', 'out', 'salary'])
    insert(testAcc, ['16', '100', 'out', 'salary'])
    insert(testAcc, ['17', '100', 'out', 'shopping'])
    insert(testAcc, ['18', '100', 'out', 'salary'])
    removeDay(testAcc, ['29'])
    assert testAcc[29] == [] and testAcc[28] == [{'Amount' : 100, 'Type' : 'out', 'Description' : 'shopping'}] \
            and testAcc[27] == [{'Amount' : 100, 'Type' : 'in', 'Description' : 'salary'}]
    removeStartEnd(testAcc, ['1', 'to', '10'])
    assert testAcc[1] == [] and testAcc[2] == [] and testAcc[5] == [] and testAcc[9] == []
    removeType(testAcc, ['out'])
    assert testAcc[15] == [] and testAcc[16] == [] and testAcc[17] == [] and testAcc[18] == [] and testAcc[28] == []

def testReplace():
    testAcc = initializeData()
    insert(testAcc, ['29', '100', 'in', 'salary'])
    replace(testAcc, ['29', 'in', 'salary', 'with', '1000'])
    assert getAmount(testAcc[29][0]) == 1000

def testFilter():
    testAcc = initializeData()
    insert(testAcc, ['29', '100', 'in', 'salary'])
    insert(testAcc, ['29', '100', 'in', 'salary'])
    insert(testAcc, ['15', '100', 'out', 'salary'])
    insert(testAcc, ['16', '100', 'out', 'salary'])
    insert(testAcc, ['17', '100', 'out', 'shopping'])
    insert(testAcc, ['18', '100', 'out', 'salary'])
    filterType(testAcc, ['in'])
    assert testAcc[29] == [{'Amount' : 100, 'Type' : 'in', 'Description' : 'salary'}, 
                           {'Amount' : 100, 'Type' : 'in', 'Description' : 'salary'}]
    insert(testAcc, ['15', '1000', 'out', 'shop'])
    insert(testAcc, ['16', '75', 'out', 'shop'])
    insert(testAcc, ['17', '700', 'out', 'shopping'])
    insert(testAcc, ['18', '100', 'out', 'shop'])
    filterTypeValue(testAcc, ['out', '500'])
    assert testAcc[16] == [{'Amount' : 75, 'Type' : 'out', 'Description' : 'shop'}] \
                and testAcc[18] == [{'Amount' : 100, 'Type' : 'out', 'Description' : 'shop'}]

def testUndo():
    testAcc = initializeData()
    add(testAcc, ['100', 'in', 'salary'])
    undo(testAcc)
    now = datetime.datetime.now()
    assert testAcc[now.day] == []
    testAcc = initializeData()
    insert(testAcc, ['29', '100', 'in', 'salary'])
    undo(testAcc)
    assert testAcc[29] == []
    testAcc = initializeData()
    insert(testAcc, ['29', '100', 'in', 'salary'])
    insert(testAcc, ['29', '100', 'in', 'salary'])
    removeDay(testAcc, ['29'])
    undo(testAcc)
    assert testAcc[29] == [{'Amount' : 100, 'Type' : 'in', 'Description' : 'salary'},
                           {'Amount' : 100, 'Type' : 'in', 'Description' : 'salary'}]
    testAcc = initializeData()
    insert(testAcc, ['1', '100', 'in', 'salary'])
    insert(testAcc, ['2', '100', 'in', 'salary'])
    insert(testAcc, ['3', '100', 'in', 'salary'])
    insert(testAcc, ['4', '100', 'in', 'salary'])
    removeStartEnd(testAcc, ['1', 'to', '4'])
    undo(testAcc)
    assert testAcc[1] == [{'Amount' : 100, 'Type' : 'in', 'Description' : 'salary'}] and \
            testAcc[2] == [{'Amount' : 100, 'Type' : 'in', 'Description' : 'salary'}] and \
            testAcc[3] == [{'Amount' : 100, 'Type' : 'in', 'Description' : 'salary'}] and \
            testAcc[4] == [{'Amount' : 100, 'Type' : 'in', 'Description' : 'salary'}]
    testAcc = initializeData()
    insert(testAcc, ['15', '100', 'out', 'shopping'])
    insert(testAcc, ['16', '100', 'out', 'shopping'])
    insert(testAcc, ['17', '100', 'out', 'shopping'])
    insert(testAcc, ['18', '100', 'out', 'shopping'])
    removeType(testAcc, ['out'])
    undo(testAcc)
    assert testAcc[15] == [{'Amount' : 100, 'Type' : 'out', 'Description' : 'shopping'}] and \
            testAcc[16] == [{'Amount' : 100, 'Type' : 'out', 'Description' : 'shopping'}] and \
            testAcc[17] == [{'Amount' : 100, 'Type' : 'out', 'Description' : 'shopping'}] and \
            testAcc[18] == [{'Amount' : 100, 'Type' : 'out', 'Description' : 'shopping'}]
    testAcc = initializeData()
    insert(testAcc, ['29', '100', 'in', 'salary'])
    insert(testAcc, ['28', '100', 'in', 'salary'])
    insert(testAcc, ['15', '100', 'out', 'salary'])
    filterType(testAcc, ['in'])
    undo(testAcc)
    assert testAcc[29] == [{'Amount' : 100, 'Type' : 'in', 'Description' : 'salary'}] and \
            testAcc[28] == [{'Amount' : 100, 'Type' : 'in', 'Description' : 'salary'}] and \
            testAcc[15] == [{'Amount' : 100, 'Type' : 'out', 'Description' : 'salary'}]
    testAcc = initializeData()
    insert(testAcc, ['15', '1000', 'out', 'shop'])
    insert(testAcc, ['16', '75', 'out', 'shop'])
    insert(testAcc, ['17', '700', 'out', 'shopping'])
    filterTypeValue(testAcc, ['out', '500'])
    undo(testAcc)
    assert testAcc[15] == [{'Amount' : 1000, 'Type' : 'out', 'Description' : 'shop'}] and \
            testAcc[16] == [{'Amount' : 75, 'Type' : 'out', 'Description' : 'shop'}] and \
            testAcc[17] == [{'Amount' : 700, 'Type' : 'out', 'Description' : 'shopping'}]

def add(acc, params):
    """A function that adds a transaction on the current day"""
    now = datetime.datetime.now()
    acc[now.day].append(createTransaction(int(params[0]), params[1], params[2]))
    undo.list.append({"add" : [now.day] + params})

def insert(acc, params):
    """A function that adds a transaction on the specified day"""
    day = int(params[0])
    acc[day].append(createTransaction(int(params[1]), params[2], params[3]))
    undo.list.append({"insert" : [day] + params[1:]})

def removeStartEnd(acc, params):
    """A function that removes all transactions between the specified start and end date"""
    startDate = int(params[0])
    endDate = int(params[2])
    removeList = []
    for i in range(startDate, endDate + 1):
        if len(acc[i]) != 0:
            removeList.append([i] + acc[i])
        acc[i].clear()
    if len(removeList) != 0:
        undo.list.append({"remove" : removeList})

def removeType(acc, params):
    """A function that removes all the transaction of a specified type"""
    removeList = []
    for key in acc.keys():
        finalList = [i for i in acc[key] if getType(i) != params[0]]
        removed = [i for i in acc[key] if i not in finalList]
        if len(removed) != 0:
            removeList.append([key] + removed)
        acc[key] = finalList
    if len(removeList) != 0:
        undo.list.append({"remove" : removeList})

def removeDay(acc, params):
    """A function that removes all the transactions on a specified day"""
    day = int(params[0])
    removeList = []
    if len(acc[day]) != 0:
        for i in acc[day]:
            removeList.append(i)
        undo.list.append({"remove" : [[day] + removeList]})
    acc[day].clear()

def replace(acc, params):
    """A function that replaces the amount of money for a specified transaction"""
    day = int(params[0])
    amount = int(params[4])
    found = False
    for i in acc[day]:
        if getType(i) == params[1] and getDescription(i) == params[2]:
            found = True
            undo.list.append({"replace" : [day, params[1], params[2], getAmount(i)]})
            setAmount(i, amount)
            break
    return found

def compare(a, b, operation):
    if operation == "=":
        return a == b
    elif operation == "<":
        return a < b
    else:
        return a > b

def listTransactionsZeroParameters(acc):
    """The function call for the list option with zero parameteres that prints out all the transactions"""
    l = []
    for key in acc:
        for i in acc[key]:
            l.append("Day {:2d} [ Amount: {}; Type: {}; Description: \"{}\"]".format(key, getAmount(i), getType(i), getDescription(i)))
    return l

def listTransactionsOneParameter(acc, params):
    """The function call for the list option with one parameter that prints out all the transactions of a specified type"""
    l = []
    for key in acc:
        for i in acc[key]:
            if getType(i) == params[0]:
                l.append("Day {:2d} [ Amount: {}; Type: {}; Description: \"{}\"]".format(key, getAmount(i), getType(i), getDescription(i)))
    return l

def listTransactionsComparison(acc, params):
    """The function call for the list option with two parameteres that prints out all the transactions that satisfy the specified condition"""
    l = []
    for key in acc:
        for i in acc[key]:
            if compare(getAmount(i), int(params[1]), params[0]):
                l.append("Day {:2d} [ Amount: {}; Type: {}; Description: \"{}\"]".format(key, getAmount(i), getType(i), getDescription(i)))
    return l

def listTransactionsBalance(acc, params):
    """The function call for 'list balance' that prints out the account balance on the specified day"""
    day = int(params[1])
    sumTrans = 0
    for i in range(1, day + 1):
        for j in acc[i]:
            sumTrans += getAmount(j) if getType(j) == "in" else -getAmount(j)
    return "Balance on day {}: {}".format(day, sumTrans)

def calcSum(acc, params):
    """This function returns the sum of all transactions of specified type"""
    s = 0
    for key in acc.keys():
        for i in acc[key]:
            if getType(i) == params[0]:
                s += getAmount(i)
    return s

def calcMax(acc, params):
    """The function returns the maximum transaction amount for the specified type and day"""
    m = -1
    for i in acc[int(params[1])]:
        if getType(i) == params[0] and getAmount(i) > m:
            m = getAmount(i)
    return m
    
def filterType(acc, params):
    """The function keeps all the transactions of the specified type"""
    filterList = []
    for key in acc.keys():
        filtered = [i for i in acc[key] if getType(i) == params[0]]
        removed = [item for item in acc[key] if item not in filtered]
        if len(removed) != 0:
            filterList.append([key] + removed)
        acc[key] = filtered
    if len(filterList) > 0:
        undo.list.append({"filter" : filterList})

def filterTypeValue(acc, params):
    """The function keeps all the transactions of the specified type that have an amount of money smaller than the specified value"""
    filterList = []
    for key in acc.keys():
        filtered = [i for i in acc[key] if getType(i) == params[0] and getAmount(i) < int(params[1])]
        removed = [item for item in acc[key] if item not in filtered]
        if len(removed) != 0:
            filterList.append([key] + removed)
        acc[key] = filtered
    if len(filterList) > 0:
        undo.list.append({"filter" : filterList})

def listenCommand():
    """This function reads user input and returns the command and its parameters"""
    userInput = input()
    firstSpace = userInput.find(' ')
    if firstSpace != -1:
        command = userInput[0:firstSpace].lower()
        params = userInput[firstSpace:len(userInput)].split()
        params = [i.strip() for i in params]
        return [command] + params
    return [userInput]

def initializeData():
    """Initialize the account dictionary for the further use in the program"""
    acc = {}
    for i in range(1, 32):
        acc[i] = []
    return acc