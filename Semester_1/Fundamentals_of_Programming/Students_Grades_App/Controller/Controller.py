from Repository.DisciplineRepository import DisciplinesList
from Repository.StudentRepository import StudentList
from Repository.GradeRepository import GradeList
from Entities.Students import Student
from Entities.Grades import Grades
from Entities.Disciplines import Discipline
from Controller.UndoController import *
from TextFileRepos.StudentRepoBinary import *
from TextFileRepos.DiscplineRepoBinary import *
from TextFileRepos.GradeRepoBinary import *
from selection_sort import *

class Controller:
    '''calls all the functions from their respective modules and prepares data for printing'''
    def __init__(self, StudentsList, DisciplineList,undoController, GradeList):
        self._StudentsList=StudentsList
        self._DisciplineList=DisciplineList
        self._GradeList=GradeList
        self._undoController=undoController

    def addS(self,other,id=-1):
        s = Student(other, id)
        self._StudentsList.add(s)
        redo = FunctionCall(self.addS, s._name)
        undo=FunctionCall(self._StudentsList.remove, self._StudentsList.GetIdbyName(other))
        op=Operation(undo,redo)
        self._undoController.add(op)

    def addG(self, sid, did,grade,id=-1):
        try:
            grade=float(grade)
            sid=int(sid)
            did=int(did)
            id=id
        except:
            raise Exception('Grade not a number')
        if GradeList.FindId(self._StudentsList, sid)==-1 or GradeList.FindId(self._DisciplineList, did)==-1:
            raise IndexError('Student or discipline invalid')
        g=Grades(sid, did, grade,id)
        self._GradeList.addGrade(g)
        redo=FunctionCall(self.addG,g._sID,g._dID,g._grade)
        undo=FunctionCall(self._GradeList.deleteGrade,g._id)
        op=Operation(undo,redo)
        self._undoController.add(op)


    def addD(self,other,id=-1):
        self._DisciplineList.add(Discipline(other, id))
        redo = FunctionCall(self.addD, other)
        undo = FunctionCall(self._DisciplineList.remove, self._DisciplineList.GetIdbyName(other))
        op = Operation(undo, redo)
        self._undoController.add(op)

    def removeS(self,id):
        name=self._StudentsList.GetNamebyID(id)
        self._StudentsList.remove(id)
        undo=FunctionCall(self._StudentsList.add,Student(name))
        redo=FunctionCall(self.removeS,id)
        op=Operation(undo,redo)
        cascade=CascadeOperation()
        cascade.add(op)
        i=0
        while i<len(self._GradeList._list):
            if self._GradeList._list[i]._sID==id:
                g=Grades(id,self._GradeList._list[i]._dID,self._GradeList._list[i]._grade)
                undo=FunctionCall(self._GradeList.addGrade,g)
                redo=FunctionCall(self._GradeList.deleteGrade,i)
                ope=Operation(undo,redo)
                cascade.add(ope)
                self._GradeList._list.pop(i)
                i-=1
            i+=1
        self._undoController.add(cascade)


    def removeD(self,id):
        name=self._DisciplineList.GetNamebyID(id)
        self._DisciplineList.remove(id)
        undo=FunctionCall(self._DisciplineList.add,Discipline(name))
        redo=FunctionCall(self.removeD,id)
        op = Operation(undo, redo)
        cascade = CascadeOperation()
        cascade.add(op)
        i = 0
        while i < len(self._GradeList._list):
            if self._GradeList._list[i]._dID == id:
                g = Grades(self._GradeList._list[i]._sID, id, self._GradeList._list[i]._grade)
                undo = FunctionCall(self._GradeList.addGrade, g)
                redo = FunctionCall(self._GradeList.deleteGrade, i)
                ope = Operation(undo, redo)
                cascade.add(ope)
                self._GradeList._list.pop(i)
                i -= 1
            i += 1
        self._undoController.add(cascade)


    def updateS(self,id,new):
        name=self._StudentsList.GetNamebyID(id)
        self._StudentsList.update(id, new)
        redo=FunctionCall(self.updateS,id,new)
        undo=FunctionCall(self.updateS,id,name)
        op = Operation(undo, redo)
        self._undoController.add(op)


    def updateD(self,id,new):
        name = self._DisciplineList.GetNamebyID(id)
        self._DisciplineList.update(id, new)
        redo = FunctionCall(self.updateD, id, new)
        undo = FunctionCall(self.updateD, id, name)
        op = Operation(undo, redo)
        self._undoController.add(op)

    def showS(self):
        return self._StudentsList.Print()

    def showD(self):
        return self._DisciplineList.Print()

    def showG(self):
        return self._GradeList.Print()

    def searchDID(self,id):
        return self._DisciplineList.FindId(id)

    def searchSID(self,id):
        return self._StudentsList.FindId(id)

    def searchDN(self,name):
        return self._DisciplineList.FindN(name)

    def searchSN(self,name):
        return self._StudentsList.FindN(name)


    '''selection sort used'''



    def EnrolledStudents(self,id):
        def TakeSecond(elem):
            return elem[1]
        l=self._GradeList.EnrolledStudents(id)
        li=[]
        for i in l:
            li.append([i, self._StudentsList.GetNamebyID(i)])
        if len(li)==0:
            raise Exception('no student at discipline')
        else:
            li=selectionSort(li,key=TakeSecond)
            return li

    def EnrolledStudentsWithG(self,id):
        def TakeThird(elem):
            return elem[1]
        l=self._GradeList.EnrolledStudentsWithG(id)
        li=[]
        for i in l:
            i.append(self._StudentsList.GetNamebyID(i[0]))
            li.append(i)
        if len(li)==0:
            raise Exception('no student at discipline')
        else:
            li.sort(key=TakeThird)
            return li

    def FailingStudents(self):
        li=[]
        ls=self._DisciplineList.getIDs()
        for i in ls:
            l=self._GradeList.FailingStudentsAtIDWithG(i)
            for j in l:
                j.append(self._StudentsList.GetNamebyID(j[0]))
                j.append(self._DisciplineList.GetNamebyID(i))
            li=li+l
        if len(li)==0:
            raise Exception('no failing student')
        else:
            return li



    '''FILTER USED'''




    def FailingStudents1(self):
        li=[]
        ls = self._DisciplineList.getIDs()
        for i in ls:
            l = self._GradeList.FailingStudentsAtIDWithG(i)
            l=filter(l,smaller5)
            li+=l
        if len(li)==0:
            raise Exception('no failing student')
        else:
            return li


    def BestStudentsHelper(self):
        li = []
        ls = self._DisciplineList.getIDs()
        for i in ls:
            l = self._GradeList.BestStudentsAtIDWithG(i)
            for j in l:
                j.append(self._StudentsList.GetNamebyID(j[0]))
                j.append(self._DisciplineList.GetNamebyID(i))
            li = li + l
        if len(li) == 0:
            raise Exception('no student not failing')
        else:
            return li

    def BestStudents(self):
        def TakeSecond(elem):
            return elem[1]
        l=self.BestStudentsHelper()
        i=0
        while i<len(l)-1:
            l[i].append(1)
            j=i+1
            while j <len(l):
                if l[i][0]==l[j][0]:
                    l[i][1]+=l[j][1]
                    l[i][4]+=1
                    del l[j]
                    j-=1
                j+=1
            i+=1
        #l[i].append(1)
        for i in range(0,len(l)):
            l[i][1]=l[i][1]/float(l[i][4])
        l.sort(key=TakeSecond)
        return l

    def BestDiscipline(self):
        def TakeSecond(elem):
            return elem[1]
        l=self.BestStudentsHelper()
        i=0
        while i<len(l)-1:
            l[i].append(1)
            j=i+1
            while j <len(l):
                if l[i][3]==l[j][3]:
                    l[i][1]+=l[j][1]
                    l[i][4]+=1
                    del l[j]
                    j-=1
                j+=1
            i+=1
        #l[i].append(1)
        for i in range(0,len(l)):
            l[i][1]=l[i][1]/float(l[i][4])
        l.sort(key=TakeSecond)
        return l

    def add(self,name):
        self._StudentsList.addS(Student(name))

    def saveDS(self):
        self._DisciplineList.writeToBinaryFile()

    def saveGS(self):
        self._GradeList.writeToBinaryFile()


def smaller5 (a):
    if a._grade<5:
        return True

import unittest

class TestController(unittest.TestCase):
    def setUp(self):
        self.SL=StudentList()
        self.DL=DisciplinesList()
        self.GL=GradeList()
        self.ctrl=Controller(self.SL,self.DL,self.GL)

    def tearDown(self):
        self.SL=None
        self.DL=None
        self.GL=None

    def test(self):
        self.assertTrue(self.ctrl.addS('Matei'))
        self.assertTrue(self.ctrl.addS('Mateo'))
        self.assertTrue(self.ctrl.addD('Mate'))
        self.assertTrue(self.ctrl.addD('Matem'))
        self.assertTrue(self.ctrl.addG(1,1,8.8))
        self.assertTrue(self.ctrl.addG(2,2,8.8))