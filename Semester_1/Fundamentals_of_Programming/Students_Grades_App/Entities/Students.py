import unittest

class Student:
    '''
    here the student class id defined
    '''
    def __init__(self, name, id=-1):
        try:
            int(id)
            self._id = int(id)
            self._name = name
        except:
            raise StudentsError('ID must be integer')

    def getName(self):
        '''
        gets the name of the student
        :return:
        '''
        return self._name

    def getId(self):
        '''
        gets the id of the student
        :return:
        '''
        return self._id

    def setId(self, new):
        '''
        sets the id of the student
        :return:
        '''
        self._id=int(new)

    def setName(self, new):
        '''
        sets the name of the student
        :return:
        '''
        self._name=new

    def __str__(self):
        return str(self._id)+' '+str(self._name)

    def lower(self):
        return self.getName().lower()


class StudentsError(Exception):
    '''
    an exception created for this class
    '''
    def __init__(self,message):
        self._message=message

    def __str__(self):
        return self._message

class StudentsTest(unittest.TestCase):

    def setUp(self):
        self.d=Student('Matei')

    def tearDown(self):
        self.d=None

    def testDiscipline(self):
        self.assertEqual(self.d.getId(),-1)
        self.assertEqual(self.d.getName(),'Matei')
        self.assertNotEqual(self.d.getName(),'Matem')
        self.d.setName('Mateo')
        self.assertEqual(self.d.getName(),'Mateo')
        #self.assertRaises(StudentsError,self.d.setId('i'))
        self.d.setId(2)
        self.assertEqual(self.d.getId(),2)

