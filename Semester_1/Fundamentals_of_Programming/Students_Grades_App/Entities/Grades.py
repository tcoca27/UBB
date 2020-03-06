import unittest

class Grades:
    def __init__(self, studID, disID, grade,id=-1):
        if 0<grade<=10:
            self._sID=int(studID)
            self._dID=int(disID)
            self._grade=grade
            self._id=id
        else:
            raise GradeError('Grade not valid')

    def getId(self):
        return self._id

    def getSID(self):
        '''
        gets the id of the student
        :return:
        '''
        return self._sID

    def getDID(self):
        '''
        gets the id of the discipline
        :return:
        '''
        return self._dID

    def getGrade(self):
        '''
        gets the grade
        :return:
        '''
        return self._grade

    def setId(self,new):
        self._id=new

    def setGrade(self, new):
        '''
        sets a new grade
        :return:
        '''
        float(new)
        if 0<float(new)<=10:
            self._grade=float(new)
        else:
            raise GradeError('Not a valid grade')

    def __str__(self):
        return str(self._sID)+' '+str(self._dID)+' '+str(self._grade)


class GradeError(Exception):
    '''
    an exception created for this class
    '''
    def __init__(self,message):
        self._message=message

    def __str__(self):
        return self._message

class TestGrade(unittest.TestCase):
    def setUp(self):
        self.g=Grades(1,1,8)

    def tearDown(self):
        self.g=None

    def testGrade(self):
        self.assertEqual(self.g.getSID(),1)
        self.assertEqual(self.g.getDID(),1)
        self.assertNotEqual(self.g.getDID(),2)
        self.assertNotEqual(self.g.getGrade(),2)
        self.assertEqual(self.g.getGrade(),8)
        self.g.setGrade(9.5)
        self.assertEqual(self.g.getGrade(),9.5)