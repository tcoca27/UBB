class Node:
    def __init__(self,root=None):
        self._root=root
        self._children=[]
        self._value=0

    def addChild(self,child):
        self._children.append(child)

    def getChildren(self):
        return self._children

    def getRoot(self):
        return self._root

    def setRoot(self,root):
        self._root=root

    def setValue(self,value):
        self._value=value

    def getValue(self):
        return self._value

    # def __str__(self):
    #     s=""
    #     if self._value!=0:
    #         s+="is attribute "+str(self._root)+" equal to "+str(self._value)+"\n\tYes:\n"
    #         for child in self._childrenTrue:
    #             s+=str(child)+'\n'
    #         s+='\t No: \n'
    #         for child in self._childrenFalse:
    #             s+=str(child)+'\n'
    #     else:
    #         s+="class "+str(self._root)+'\n'
    #         if len(self._childrenTrue)!=0:
    #             for child in self._childrenTrue:
    #                 s += str(child) + '\n'
    #         if len(self._childrenFalse)!=0:
    #             for child in self._childrenFalse:
    #                 s += str(child) + '\n'
    #     return s