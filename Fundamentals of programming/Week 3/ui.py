from functions import *

def add_UI(acc, params):
    """add <amount> <type> <description>"""
    validateAdd(params)
    add(acc, params)

def insert_UI(acc, params):
    """insert <day> <amount> <type> <description>"""
    validateInsert(params)
    insert(acc, params)

def remove_UI(acc, params):
    """remove <day>  ||  remove <start day> to <end day>  ||  remove <type>"""
    validateRemove(params)
    if len(params) == 1:
        if params[0].isdigit():
            removeDay(acc, params)
        elif params[0] == "in" or params[0] == "out":
            removeType(acc, params)
    elif len(params) == 3:
        removeStartEnd(acc, params)

def replace_UI(acc, params):
    """replace <day> <type> <description> with <value>"""
    validateReplace(params)
    found = replace(acc, params)
    if not found:
        raise ValueError("No transactions with the specified entries found")

def listTransactions_UI(acc, params):
    """list  ||  list <type>  ||  list [ < | = | > ] <value>  ||  list balance <day>"""
    validateListTransactions(params)
    if len(params) == 0:
        l = listTransactionsZeroParameters(acc)
        for i in l:
            print(i)
    elif len(params) == 1:
        l = listTransactionsOneParameter(acc, params)
        for i in l:
            print(i)
    else:
        if params[0] in ("<", ">", "="):
            l = listTransactionsComparison(acc, params)
            for i in l:
                print(i)
        else:
            l = listTransactionsBalance(acc, params)
            print(l)

def sum_UI(acc, params):
    """sum <type>"""
    validateSum(params)
    s = calcSum(acc, params)
    print("The total amount of {} transactions is: {}".format(params[0], s))

def max_UI(acc, params):
    """max <type> <day>"""
    validateMax(params)
    m = calcMax(acc, params)
    print("The maximum {} transaction on day {} is: {}".format(params[0], params[1], m))

def filter_UI(acc, params):
    """filter <type> || filter <type> <value>"""
    validateFilter(params)
    if len(params) == 1:
        filterType(acc, params)
    else:
        filterTypeValue(acc, params)

def undo_UI(acc, params):
    """undo"""
    validateUndo(params)
    undo(acc)