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
        self.__mainThread.btnConveyerForward.setStyleSheet("color: black;font:bold 30px Arial; background-color:rgba(220,220,220,255)")
        self.__mainThread.__workerConveyerForward = ConveyerForward()
        self.__mainThread.__workerConveyerForward.signals.finished.connect(lambda: self.finish())
        self.__mainThread.__workerConveyerForward.start()
    def finish(self):
        print("Conveyer Stop")
        self.__mainThread.btnConveyerForward.setStyleSheet("color: white;font:bold 30px Arial; background-color:rgba(128,128,128,255)")

class ConveyerForward(Job):
    def __init__(self):
        super(ConveyerForward, self).__init__()
        self.signals = WorkerSignals()
    def run(self):
        """模擬輸送帶前進"""
        for i in trange(3):
            sleep(1)
        self.signals.finished.emit()

