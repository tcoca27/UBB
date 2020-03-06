from Entities.Disciplines import *

class DisciplinesList:
    def __init__(self):
        self._list = []

    def IsInListName(self,other):
        '''
        checks if student is already in the list
        :param other: name of student
        :return: t or f
        '''
        for i in self._list:
            if i.getName().lower()==other.getName().lower():
                return True
        return False

    def add(self, other):
        '''
        adds a student in the next id position that is empty
        :param other: student
        '''
        if len(self._list) == 0:
            other.setId(1)
            self._list.append(other)
            return True
        elif other.getId() == -1:
            if self.IsInListName(other):
                raise DisciplineListError('Discipline already in list')
            for i in range(1,len(self._list)+2):
                if self.FindId(i)==-1:
                    other.setId(i)
                    self._list.insert(i-1,other)
                    return True
            other.setId(len(self._list) + 1)
            self._list.append(other)
            return True

    def remove(self, id):
        '''
        removes a student with a certain id
        :param id
        '''
        if self.FindId(id)==-1:
            raise DisciplineListError('No student with this ID')
        i = 0
        while i < len(self._list):
            if self._list[i].getId() == id:
                self._list.pop(i)
                i -= 1
                return True
            i += 1
        return False

    def removeAll(self):
        '''
        removes all students
        :return:
        '''
        self._list.clear()

    def update(self, id, new):
        '''
        updates the name of the student with a certain id
        :param id
        :param new: new name
        '''
        if self.FindId(id)==-1:
            raise DisciplineListError('No student with this ID')
        for i in self._list:
            if i.getId() == id:
                i.setName(new)
                return True

    def Print(self):
        '''
        returns the list of students
        :return:
        '''
        t=[]
        for i in self._list:
            t.append(i)
        return t

    def FindId(self,id):
        '''
        looks to see if there is a student with a certain id
        :param id:
        :return: -1 if not
        '''
        t=[]
        for i in self._list:
            if i.getId()==id:
                t.append(i)
        if len(t)==0:
            return -1
        else:
            return t

    def FindN(self,name):
        l=[]
        for i in self._list:
            if name.lower() in i.getName().lower():
                l.append(i)
        if len(l)==0:
            raise DisciplineListError('no such student')
        else:
            return l

    def GetNamebyID(self,id):
        for i in self._list:
            if i.getId()==id:
                return i.getName()

    def GetIdbyName(self,name):
        for i in self._list:
            if i.getName().lower()==name.lower():
                return i.getId()

    def getIDs(self):
        l=[]
        for i in self._list:
            l.append(i.getId())
        return l

    def GetContent(self):
        l=[]
        for s in self._list:
            l.append(s.__str__())
        return l

    def removeall(self):
        self._list=[]


class DisciplineListError(Exception):
    '''
    an exception created for this class
    '''
    def __init__(self,message):
        self._message=message

    def __str__(self):
        return self._message


import unittest

class TestDR(unittest.TestCase):
    def setUp(self):
        self.list=DisciplinesList()

    def tearDown(self):
        self.list=None

    def test(self):
        self.assertTrue(self.list.add(Discipline('Mate')))
        self.assertTrue(self.list.add(Discipline('Matem')))
        self.assertTrue(self.list.remove(1))
        self.assertTrue(self.list.update(2,'Mate'))
        self.assertNotEqual(self.list.FindId(2),None)
        self.assertNotEqual(self.list.FindN('Mate'),None)
        self.assertEqual(self.list.GetNamebyID(2),'Mate')
        self.assertListEqual(self.list.getIDs(),[2])
