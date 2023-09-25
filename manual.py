from manualPattern import btnTrigger, Job
from time import sleep
from tqdm import trange
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class WorkerSignals(QObject): #Define args 
    finished = pyqtSignal()

class ClickConveyerForward(btnTrigger):
    def __init__(self, mainThread):
        self.__mainThread = mainThread
    def action(self):
        print("Conveyer Forward")
        if self.__mainThread.flag.flagConveyerForward == False:
            self.__mainThread.flag.flagConveyerForward = True # forward on
            self.__mainThread.flag.flagConveyerBackward = False # backward off
            self.__mainThread.btnConveyerForward.setStyleSheet("color: black;font:bold 30px Arial; background-color:rgba(220,220,220,255)")
            self.__mainThread.__workerConveyerForward = ConveyerForward(self.__mainThread.flag) # 紀錄flag
            self.__mainThread.__workerConveyerForward.signals.finished.connect(lambda: self.finish())
            self.__mainThread.__workerConveyerForward.start()
        elif self.__mainThread.flag.flagConveyerForward == True:
            self.__mainThread.flag.flagConveyerForward = False # forward off
    def finish(self):
        print("Conveyer Stop")
        self.__mainThread.flagConveyerForward = False
        self.__mainThread.btnConveyerForward.setStyleSheet("color: white;font:bold 30px Arial; background-color:rgba(128,128,128,255)")

class ConveyerForward(Job):
    def __init__(self, flag):
        super(ConveyerForward, self).__init__()
        self.signals = WorkerSignals()
        self.flag = flag
    def run(self):
        """模擬輸送帶前進"""
        while 1:
            if self.flag.flagConveyerForward == False: # if flag off
                break
        self.signals.finished.emit()

class ClickConveyerBackward(btnTrigger):
    def __init__(self, mainThread):
        self.__mainThread = mainThread
    def action(self):
        print("Conveyer Backward")
        if self.__mainThread.flag.flagConveyerBackward == False:
            self.__mainThread.flag.flagConveyerBackward = True # backward on
            self.__mainThread.flag.flagConveyerForward = False # forward off
            self.__mainThread.btnConveyerBackward.setStyleSheet("color: black;font:bold 30px Arial; background-color:rgba(220,220,220,255)")
            self.__mainThread.__workerConveyerBackward = ConveyerBackward(self.__mainThread.flag)
            self.__mainThread.__workerConveyerBackward.signals.finished.connect(lambda: self.finish())
            self.__mainThread.__workerConveyerBackward.start()
        elif self.__mainThread.flag.flagConveyerBackward == True:
            self.__mainThread.flag.flagConveyerBackward = False # backward off
    def finish(self):
        print("Conveyer Stop")
        self.__mainThread.btnConveyerBackward.setStyleSheet("color: white;font:bold 30px Arial; background-color:rgba(128,128,128,255)")
    
class ConveyerBackward(Job):
    def __init__(self, flag):
        super(ConveyerBackward, self).__init__()
        self.signals = WorkerSignals()
        self.flag = flag
    def run(self):
        """模擬輸送帶後退"""
        while 1:
            if self.flag.flagConveyerBackward == False: # if flag off
                break
        self.signals.finished.emit()

