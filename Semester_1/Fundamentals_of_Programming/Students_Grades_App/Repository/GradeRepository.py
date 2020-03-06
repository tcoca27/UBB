from Entities.Grades import *
from selection_sort import *
from Repository.StudentRepository import *
class GradeList:
    def __init__(self):
        self._list=[]

    def addGrade(self,other):
        '''
        adds a grade to the list
        '''
        if len(self._list) == 0:
            other.setId(1)
            self._list.append(other)
            return True
        elif other.getId() == -1:
            for i in range(1,len(self._list)+2):
                if self.FindId(i)==-1:
                    other.setId(i)
                    self._list.insert(i-1,other)
                    return True
            other.setId(len(self._list) + 1)
            self._list.append(other)
            return True


    def deleteGrade(self,id):
        for i in range (0,len(self._list)):
            if self._list[i].getId()==id:
                self._list.pop(i)
                return True
        raise GradeListError('Grade not in list')


    def FindId(self,id):
        t=[]
        for i in range(0,len(self._list)):
            if self._list[i].getId()==id:
                t.append(i)
        if len(t)==0:
            return None
        else:
            return t

    def insertGrade(self,grade,idx):
        self._list.insert(idx,grade)
        return True

    def removeStud(self,id):
        '''
        removes the grades of a student
        :param id: student id
        '''
        i=0
        while i<len(self._list):
            if self._list[i]._sID==id:
                self._list.pop(i)
                i-=1
            i+=1

    def removeDisc(self,id):
        '''
        removes the grades from a discipline
        :param id: discipline id
        '''
        i=0
        while i<len(self._list):
            if self._list[i]._dID==id:
                self._list.pop(i)
                i-=1
            i+=1

    def removeAll(self):
        '''removes all grades'''
        self._list.clear()

    def Print(self):
        '''returns the list of grades'''
        t=[]
        for i in self._list:
            t.append(i)
        return t

    def EnrolledStudents(self,id):
        '''returns list of all students enrolled in a discipline'''
        l=[]
        for i in self._list:
            if i.getDID()==id and IsNotInList(l,i.getSID()):
                l.append(i.getSID())
        return l

    def AverageGradeS1D(self,SID,DID):
        '''computes the avg of a discipline for a student'''
        avg=0
        avg=float(avg)
        nr=0
        for i in self._list:
            if i.getSID()==SID and i.getDID()==DID:
                avg+=float(i.getGrade())
                nr+=1
        if(nr>0):
            avg=avg/nr
        return avg

    def EnrolledStudentsWithG(self,id):
        '''returns list of enrolled students with their grades'''
        l=[]
        for i in self._list:
            if i.getDID() == id and IsNotInList2(l, i.getSID()):
                l.append([i.getSID(),self.AverageGradeS1D(i.getSID(),id)])
        return l

    def FailingStudentsAtIDWithG(self,id):
        '''returns list of failing students'''
        l=[]
        for i in self._list:
            if i.getDID()==id and IsNotInList3(l,i.getSID()): #and self.AverageGradeS1D(i.getSID(),id)<5:
                l.append(FailingStudent(i.getSID(),i.getDID(),self.AverageGradeS1D(i.getSID(),id)))
                #l.append([i.getSID(),self.AverageGradeS1D(i.getSID(),id)])
        return l

    def BestStudentsAtIDWithG(self,id):
        '''returns list of students with their avg'''
        l=[]
        for i in self._list:
            if i.getDID()==id and IsNotInList2(l,i.getSID()):
                l.append([i.getSID(),self.AverageGradeS1D(i.getSID(),id)])
        return l


    def IndexToInsertGrade(self,grade):
        '''helper for sort functuin'''
        for i in self._list:
            while i.getGrade()>grade:
                i+=1
            return i

    def GetContent(self):
        l=[]
        for g in self._list:
            l.append(g.__str__())
        return l

    def removeall(self):
        self._list=[]


class GradeListError(Exception):
    '''
    an exception created for this class
    '''
    def __init__(self,message):
        self._message=message

    def __str__(self):
        return self._message

def IsNotInList(l,nr):
    for i in l:
        if i==nr:
            return False
    return True

def IsNotInList2(l,nr):
    for i in l:
        if i[0]==nr:
            return False
    return True

def IsNotInList3(l,nr):
    for i in l:
        if i._sid==nr:
            return False
    return True

import unittest

class TestGR(unittest.TestCase):
    def setUp(self):
        self.list=GradeList()

    def tearDown(self):
        self.list=None

    def test(self):
        self.assertTrue(self.list.addGrade(Grades(1,1,8)))
        self.assertTrue(self.list.addGrade(Grades(2,1,5)))
        self.assertTrue(self.list.addGrade(Grades(3,1,5)))
        self.assertTrue(self.list.addGrade(Grades(3,2,5)))
        self.list.removeDisc(2)
        self.list.removeStud(3)
        self.assertEqual(self.list.AverageGradeS1D(1,1),8)
        self.assertListEqual(self.list.EnrolledStudentsWithG(2),[])

class FailingStudent():
    def __init__(self,sid,did,grade):
        self._sid=sid
        self._did=did
        self._grade=grade

    def __str__(self):
        return 'Student id:'+str(self._sid)+" Discipline id:"+str(self._did)+" Grade:"+str(self._grade)
