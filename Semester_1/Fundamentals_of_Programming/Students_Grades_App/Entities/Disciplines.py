import unittest

class Discipline:
    def __init__(self, name, id=-1):
        try:
            int(id)
            self._id = int(id)
            self._name = name
        except:
            raise DisciplineError('ID must be integer')

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



class DisciplineError(Exception):
    '''
    an exception created for this class
    '''
    def __init__(self,message):
        self._message=message

    def __str__(self):
        return self._message

class DisciplineTest(unittest.TestCase):

    def setUp(self):
        self.d=Discipline('Mate')

    def tearDown(self):
        self.d=None

    def testDiscipline(self):
        self.assertEqual(self.d.getId(),-1)
        self.assertEqual(self.d.getName(),'Mate')
        self.assertNotEqual(self.d.getName(),'Matem')
        self.d.setName('Matem')
        self.assertEqual(self.d.getName(),'Matem')
        self.d.setId(2)
        self.assertEqual(self.d.getId(),2)
