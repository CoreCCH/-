from manualPattern import btnTrigger, Job
from time import sleep
from tqdm import trange
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import flag

class WorkerSignals(QObject): #Define args 
    finished = pyqtSignal()

class ClickConveyerForward(btnTrigger):
    def __init__(self, mainThread):
        self.__mainThread = mainThread
    def action(self):
        if self.__mainThread.flag.flagConveyerForward == False:
            flag.clearAllFlag(self.__mainThread.flag)
            self.__mainThread.flag.flagConveyerForward = True # forward on
            self.__mainThread.btnConveyerForward.setStyleSheet("color: black;font:bold 30px Arial; background-color:rgba(220,220,220,255)")
            self.__mainThread.__workerConveyerForward = ConveyerForward(self.__mainThread.flag) # 紀錄flag
            self.__mainThread.__workerConveyerForward.signals.finished.connect(lambda: self.finish())
            self.__mainThread.__workerConveyerForward.start()
        elif self.__mainThread.flag.flagConveyerForward == True:
            self.__mainThread.flag.flagConveyerForward = False # forward off
    def finish(self):
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
        if self.__mainThread.flag.flagConveyerBackward == False:
            flag.clearAllFlag(self.__mainThread.flag)
            self.__mainThread.flag.flagConveyerBackward = True # backward on
            self.__mainThread.btnConveyerBackward.setStyleSheet("color: black;font:bold 30px Arial; background-color:rgba(220,220,220,255)")
            self.__mainThread.__workerConveyerBackward = ConveyerBackward(self.__mainThread.flag)
            self.__mainThread.__workerConveyerBackward.signals.finished.connect(lambda: self.finish())
            self.__mainThread.__workerConveyerBackward.start()
        elif self.__mainThread.flag.flagConveyerBackward == True:
            self.__mainThread.flag.flagConveyerBackward = False # backward off
    def finish(self):
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


class ClickConveyerUp(btnTrigger):
    def __init__(self, mainThread):
        self.__mainThread = mainThread
    def action(self):
        if self.__mainThread.flag.flagConveyerUp == False:
            flag.clearAllFlag(self.__mainThread.flag)
            self.__mainThread.flag.flagConveyerUp = True # backward on
            self.__mainThread.btnConveyerUp.setStyleSheet("color: black;font:bold 30px Arial; background-color:rgba(220,220,220,255)")
            self.__mainThread.__workerConveyerUp = ConveyerUp(self.__mainThread.flag)
            self.__mainThread.__workerConveyerUp.signals.finished.connect(lambda: self.finish())
            self.__mainThread.__workerConveyerUp.start()
        elif self.__mainThread.flag.flagConveyerUp == True:
            self.__mainThread.flag.flagConveyerUp = False # backward off
    def finish(self):
        self.__mainThread.btnConveyerUp.setStyleSheet("color: white;font:bold 30px Arial; background-color:rgba(128,128,128,255)")

class ConveyerUp(Job):
    def __init__(self, flag):
        super(ConveyerUp, self).__init__()
        self.signals = WorkerSignals()
        self.flag = flag
    def run(self):
        """模擬輸送帶後退"""
        while 1:
            if self.flag.flagConveyerUp == False: # if flag off
                break
        self.signals.finished.emit()

class ClickConveyerDown(btnTrigger):
    def __init__(self, mainThread):
        self.__mainThread = mainThread
    def action(self):
        if self.__mainThread.flag.flagConveyerDown == False:
            flag.clearAllFlag(self.__mainThread.flag)
            self.__mainThread.flag.flagConveyerDown = True # backward on
            self.__mainThread.btnConveyerDown.setStyleSheet("color: black;font:bold 30px Arial; background-color:rgba(220,220,220,255)")
            self.__mainThread.__workerConveyerDown = ConveyerDown(self.__mainThread.flag)
            self.__mainThread.__workerConveyerDown.signals.finished.connect(lambda: self.finish())
            self.__mainThread.__workerConveyerDown.start()
        elif self.__mainThread.flag.flagConveyerDown == True:
            self.__mainThread.flag.flagConveyerDown = False # backward off
    def finish(self):
        self.__mainThread.btnConveyerDown.setStyleSheet("color: white;font:bold 30px Arial; background-color:rgba(128,128,128,255)")

class ConveyerDown(Job):
    def __init__(self, flag):
        super(ConveyerDown, self).__init__()
        self.signals = WorkerSignals()
        self.flag = flag
    def run(self):
        """模擬輸送帶後退"""
        while 1:
            if self.flag.flagConveyerDown == False: # if flag off
                break
        self.signals.finished.emit()

class ClickBlockUp(btnTrigger):
    def __init__(self, mainThread):
        self.__mainThread = mainThread
    def action(self):
        self.__mainThread.btnBlockUp.setStyleSheet("color: black;font:bold 30px Arial; background-color:rgba(220,220,220,255)")
        self.__mainThread.__workerBlockUp = BlockUp()
        self.__mainThread.__workerBlockUp.signals.finished.connect(lambda: self.finish())
        self.__mainThread.__workerBlockUp.start()
    def finish(self):
        self.__mainThread.flag.flagIsBlockUp = True
        # self.__mainThread.btnConveyerDown.setStyleSheet("color: white;font:bold 30px Arial; background-color:rgba(128,128,128,255)")

class BlockUp(Job):
    def __init__(self):
        super(BlockUp, self).__init__()
        self.signals = WorkerSignals()
    def run(self):
        """模擬輸送帶後退"""
        for i in trange(3):
            sleep(0.5)
        self.signals.finished.emit()

class ClickBlockDown(btnTrigger):
    def __init__(self, mainThread):
        self.__mainThread = mainThread
    def action(self):
        self.__mainThread.btnBlockDown.setStyleSheet("color: black;font:bold 30px Arial; background-color:rgba(220,220,220,255)")
        self.__mainThread.__workerBlockDown = BlockDown()
        self.__mainThread.__workerBlockDown.signals.finished.connect(lambda: self.finish())
        self.__mainThread.__workerBlockDown.start()
    def finish(self):
        self.__mainThread.flag.flagIsBlockDown = True
        # self.__mainThread.btnConveyerDown.setStyleSheet("color: white;font:bold 30px Arial; background-color:rgba(128,128,128,255)")

class BlockDown(Job):
    def __init__(self):
        super(BlockDown, self).__init__()
        self.signals = WorkerSignals()
    def run(self):
        """模擬輸送帶後退"""
        for i in trange(3):
            sleep(0.5)
        self.signals.finished.emit()