from domain import *
from ui import *
from functions import *

def clear(commands):
    """Clears the terminal and writes specifications for the supported commands"""
    os.system("cls")
    help(commands)

def printMessage(msj, type):
    """Special function for printing colored messages"""
    colors = {
        "HEADER": '\033[95m',
        "OKBLUE": '\033[94m',
        "OKGREEN": '\033[92m',
        "WARNING": '\033[93m',
        "FAIL": '\033[91m',
        "ENDC": '\033[0m',
    }
    if type in colors.keys():
        print(colors[type]+msj+colors["ENDC"])
    else:
        print(colors["HEADER"] + msj + colors["ENDC"])

def help(commands):
    for key in commands.keys():
        printMessage("=> " + commands[key].__doc__, "OKBLUE")

def testInit(acc):
    acc[1].append(createTransaction(1000, "in", "salary"))
    acc[1].append(createTransaction(100, "out", "shopping"))
    acc[10].append(createTransaction(500, "in", "garage-sale"))
    acc[11].append(createTransaction(75, "out", "cake"))
    acc[20].append(createTransaction(2000, "in", "nigerian-prince"))
    acc[20].append(createTransaction(350, "out", "jewelry"))
    acc[15].append(createTransaction(1000, "in", "salary"))
    acc[16].append(createTransaction(100, "in", "loan-interest"))
    acc[7].append(createTransaction(100, "in", "gift"))
    acc[8].append(createTransaction(200, "in", "tip"))

def start():
    undo.list = []
    runTests()
    commands = {"add" : add_UI, "insert" : insert_UI, "remove" : remove_UI, "replace" : replace_UI,
                "list" : listTransactions_UI, "sum" : sum_UI, "max" : max_UI, "filter" : filter_UI, "undo" : undo_UI}
    acc = initializeData()
    testInit(acc)
    clear(commands)
    while True:
        cmd = listenCommand()
        if cmd[0] in commands.keys():
            try:
                commands[cmd[0]](acc, cmd[1:])
            except ValueError as e:
                print(e)
        elif cmd[0] == "exit":
            return
        elif cmd[0] == "clear":
            clear(commands)
        else:
            print("Please enter a valid command")

start()