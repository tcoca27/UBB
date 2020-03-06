from Entities.Students import StudentsError
from Entities.Grades import GradeError
from Entities.Disciplines import DisciplineError
from Repository.DisciplineRepository import DisciplineListError
from Repository.StudentRepository import StudentsListError
from Repository.GradeRepository import GradeListError

class UI:
    def __init__(self, controller,undoController):
        self.controller=controller
        self._undoController=undoController

    def PrintCommands(self):
        str='\n Commands: \n'
        str += '0.Quit \n'
        str+='1.Add a student \n'
        str += '2.Remove a student with the ID: \n'
        str += '3.Update a student with the ID: \n'
        str += '4.Display the students \n'
        str += '5.Add a discipline \n'
        str += '6.Remove a discipline with ID: \n'
        str += '7.Update a dsicipline with ID: \n'
        str += '8.Display the disciplines \n'
        str += '9.Add a grade \n'
        str += '10.Display the grades list \n'
        str += '11.Search discipline by id \n'
        str += '12.Search student by id \n'
        str += '13.Search discipline by name \n'
        str += '14.Search student by name \n'
        str += '15.Show all students enrolled at a discipline sorted aplhabetically \n'
        str += '16.Show all students enrolled at a discipline sorted by their average \n'
        str += '17.Show all failing students \n'
        str += '18.Show best students \n'
        str += '19.Show best Disciplines \n'
        str += '20.Undo \n'
        str += '21.Redo \n'
        return str

    def loop(self):

        while True:
            print(self.PrintCommands())
            command=input('Enter a command: ').strip()
            try:
                if isNotInt(command):
                    raise ValueError('Command not valid')
                elif command=='1':
                    name=input('Enter a name:')
                    self.controller.addS(name)
                elif command=='2':
                    id=input("enter id to be removed:")
                    self.controller.removeS(int(id))
                elif command=='3':
                    id=input('enter id to be updated: ')
                    new=input('new name for stud:')
                    self.controller.updateS(int(id),new)
                elif command=='4':
                    p=self.controller.showS()
                    Printl(p)
                elif command == '5':
                    name = input('Enter a name:')
                    self.controller.addD(name)
                elif command == '6':
                    id = input("enter id to be removed:")
                    self.controller.removeD(int(id))
                elif command == '7':
                    id = input('enter id to be updated: ')
                    new=input('enter new name of discipline ')
                    self.controller.updateD(int(id),new)
                elif command == '8':
                    p = self.controller.showD()
                    Printl(p)
                elif command=='9':
                    sid=(input('enter student id: '))
                    did=(input('enter discipline id: '))
                    grade=(input('enter grade: '))
                    self.controller.addG(sid,did,grade)
                elif command=='10':
                    p=self.controller.showG()
                    Print(p)
                elif command=='11':
                    id=int(input('Enter a discipline id: '))
                    l=self.controller.searchDID(id)
                    Printl(l)
                elif command=='12':
                    id=int(input('Enter a student id: '))
                    l=self.controller.searchSID(id)
                    Printl(l)
                elif command=='13':
                    name=input('Enter a discipline name: ')
                    l=self.controller.searchDN(name)
                    Printl(l)
                elif command=='14':
                    name=input('Enter a student name: ')
                    l=self.controller.searchSN(name)
                    Printl(l)
                elif command=='15':
                    id=int(input('Enter a discipline id: '))
                    l=self.controller.EnrolledStudents(id)
                    print1(l)
                elif command=='16':
                    id = int(input('Enter a discipline id: '))
                    l = self.controller.EnrolledStudentsWithG(id)
                    print2(l)
                #elif command=='19':
                    #l=self.controller.FailingStudents()
                    #print3(l)
                elif command=='17':
                    l=self.controller.FailingStudents1()
                    print6(l)
                elif command=='18':
                    l=self.controller.BestStudents()
                    print4(l)
                elif command=='19':
                    l=self.controller.BestDiscipline()
                    print5(l)
                elif command=='20':
                    self._undoController.undo()
                elif command=='21':
                    self._undoController.redo()
                elif command=='0':
                    break
                else:
                    print('Command invalid')
            except ValueError as ve:
                print('not an integer')
            except StudentsError as se:
                print(se)
            except GradeError as ge:
                print(ge)
            except DisciplineError as de:
                print(de)
            except StudentsListError as sl:
                print(sl)
            except DisciplineListError as dl:
                print(dl)
            except GradeListError as gl:
                print(gl)
            except IndexError as ie:
                print(ie)
            except Exception as e:
                print(e)


def Print(p):
    for i in p:
        print("stud id:", i.getSID(), ', disc id:', i.getDID(), ', grade:', i.getGrade())

def Printl(p):
    for i in p:
        print(i.getId(), ' ', i.getName())

def print1(l):
    for i in l:
        print(i[0],' ',i[1])

def print2(l):
    for i in reversed(l):
        print(i[0],' ',i[2],' ',i[1])

def print3(l):
    for i in l:
        print(i[0],' ',i[2],' ',i[3],':',i[1])

def print4(l):
    for i in reversed(l):
        print(i[0],' ',i[2],' ',i[1])

def print5(l):
    for i in reversed(l):
        print(i[3],' ',i[1])
def print6(l):
    for i in l:
        print(i.__str__())

def isNotInt(x):
    try:
        int(x)
        return False
    except:
        return True