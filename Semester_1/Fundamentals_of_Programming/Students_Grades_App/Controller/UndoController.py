class UndoController:
    def __init__(self):
        self._operations=[]
        self._index=-1
        self._duringUndo=False

    def add(self,operation):
        if self._duringUndo==True:
            return
        self._operations.append(operation)
        self._index=len(self._operations)-1

    def undo(self):
        if self._index<0:
            raise Exception('No more undos')
        self._duringUndo=True
        self._operations[self._index].undo()
        self._duringUndo = False
        self._index-=1

    def redo(self):
        if self._index>len(self._operations)-2:
            raise Exception("No more redos")
        self._duringUndo=True
        self._operations[self._index+1].redo()
        self._duringUndo = False
        self._index+=1


class FunctionCall:
    def __init__(self,f,*params):
        self._funct=f
        self._params=params

    def call(self):
        self._funct(*self._params)

class Operation:
    def __init__(self,undoF,redoF):
        self._undoF=undoF
        self._redoF=redoF

    def undo(self):
        self._undoF.call()

    def redo(self):
        self._redoF.call()

class CascadeOperation:
    def __init__(self):
        self._list=[]

    def add(self,oper):
        self._list.append(oper)

    def undo(self):
        for op in self._list:
            op.undo()

    def redo(self):
        for op in self._list:
            op.redo()
