"""
    This module contains the Undo Controller used in the UI segment for the undo/redo operations
"""

class UndoController:
    """
        Main Undo Controller class that has a stack of operations. Undo executes the current operation and decreases the index, while redo increments the index
        and then executes the operation. Adding a new operation to the queue, deletes all the operations on top of the current one
    """
    def __init__(self):
        self._operations = []
        self._index = -1
        self._duringUndo = False

    def undo(self):
        if self._index < 0:
            return False
        self._duringUndo = True
        self._operations[self._index].undo()
        self._duringUndo = False
        self._index -= 1
        return True

    def redo(self):
        if self._index + 1 >= len(self._operations):
            return False

        self._index +=1
        self._duringUndo = True
        self._operations[self._index].redo()
        self._duringUndo = False
        return True

    def add(self, operation):
        if self._duringUndo == True:
            return
        self._operations = self._operations[:self._index + 1]
        self._operations.append(operation)
        self._index = len(self._operations) - 1

class FunctionCall:
    """
        This class takes in the constructor a function and a list of parameters.
        It can be called using the provided parameters
    """
    def __init__(self, function, *params):
        self._fun = function
        self._params = params

    def call(self):
        self._fun(*self._params)

class Operation:
    """
        This class contains the undo and redo equivalents for the called operation in the program
    """
    def __init__(self, undoFunction, redoFunction):
        self._undoFunction = undoFunction
        self._redoFunction = redoFunction


    def undo(self):
        self._undoFunction.call()

    def redo(self):
        self._redoFunction.call()

class CascadeOperation:
    """
        This class is used for a sequence of operations that are automatically called when a given operation is executed
    """
    def __init__(self):
        self._oper = []

    def add(self, operation):
        self._oper.append(operation)

    def undo(self):
        for o in self._oper:
            o.undo()

    def redo(self):
        for o in self._oper:
            o.redo()