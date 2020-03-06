from UI import *
from Controller.Controller import *
from random import randint
from TextFileRepos.GradesText import *
from TextFileRepos.StudentsText import *
from TextFileRepos.DisciplinesText import *
from TextFileRepos.StudentRepoBinary import *
from TextFileRepos.DiscplineRepoBinary import *
from TextFileRepos.GradeRepoBinary import  *
from settings import *

def Main():
    setings=settings('settings.txt')
    if setings.comm()=='inmemory':
        undoController = UndoController()
        studentList = StudentList()
        disciplineList = DisciplinesList()
        l = GradeList()
        controller = Controller(studentList, disciplineList, undoController, l)
        ui = UI(controller, undoController)

        controller.addS("Mihai")
        controller.addS("Daia")
        controller.addS("Andreea")
        controller.addS("Teo")
        controller.addS("Paul")
        controller.addS("Lorena")
        controller.addS("Daniel")
        controller.addS("Olimpiu")
        controller.addS("Nicu")
        controller.addS("Zaltan")

        controller.addD("Math")
        controller.addD("FP")
        controller.addD("ASC")
        controller.addD("Algebra")
        controller.addD("Music")
        controller.addD("Sport")
        controller.addD("Analysis")
        controller.addD("Geometry")
        controller.addD("Vectors")
        controller.addD("Mathematics")
        controller.addD("Comunication")
        controller.addD("Graphs theory")

        controller.addG(1, 1, 8)
        controller.addG(2, 3, 10)
        controller.addG(1, 2, 5)
        controller.addG(4, 3, 5)
        controller.addG(5, 10, 8)
        controller.addG(7, 9, 8)
        controller.addG(1, 5, 8)
        controller.addG(3, 7, 4)
        controller.addG(8, 8, 8)
        controller.addG(9, 6, 9)
        controller.addG(8, 2, 10)
        for i in range(0, 90):
            sid = randint(1, 10)
            did = randint(1, 12)
            grade = randint(1, 10)
            controller.addG(sid, did, grade)
        ui.loop()
    elif setings.comm()=='textFiles':
        undoController = UndoController()
        studentList = StudentTextFileRepo()
        disciplineList = DisciplinesTextFileRepo()
        l = GradesTextFileRepo()
        controller = Controller(studentList, disciplineList, undoController, l)
        ui = UI(controller, undoController)
        ui.loop()
    elif setings.comm()=='binary':
        undoController = UndoController()
        studentList=StudentRepoBinary()
        disciplineList=DisciplinesRepoBinary()
        gradeList=GradesRepoBinary()
        controller=Controller(studentList,disciplineList,undoController,gradeList)
        ui=UI(controller,undoController)

        '''controller.addS("Mihai")
        controller.addS("Daia")
        controller.addS("Andreea")
        controller.addS("Teo")
        controller.addS("Paul")
        controller.addS("Lorena")
        controller.addS("Daniel")
        controller.addS("Olimpiu")
        controller.addS("Nicu")
        controller.addS("Zaltan")

        controller.addD("Math")
        controller.addD("FP")
        controller.addD("ASC")
        controller.addD("Algebra")
        controller.addD("Music")
        controller.addD("Sport")
        controller.addD("Analysis")
        controller.addD("Geometry")
        controller.addD("Vectors")
        controller.addD("Mathematics")
        controller.addD("Comunication")
        controller.addD("Graphs theory")

        controller.addG(1, 1, 8)
        controller.addG(2, 3, 10)
        controller.addG(1, 2, 5)
        controller.addG(4, 3, 5)
        controller.addG(5, 10, 8)
        controller.addG(7, 9, 8)
        controller.addG(1, 5, 8)
        controller.addG(3, 7, 4)
        controller.addG(8, 8, 8)
        controller.addG(9, 6, 9)
        controller.addG(8, 2, 10)
        for i in range(0, 90):
            sid = randint(1, 10)
            did = randint(1, 12)
            grade = randint(1, 10)
            controller.addG(sid, did, grade)'''
        ui.loop()


Main()