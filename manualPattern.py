from abc import ABCMeta, abstractclassmethod
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class btnTrigger(metaclass=ABCMeta):
    @abstractclassmethod
    def action(self):
        pass
    @abstractclassmethod
    def finish(self):
        pass


class Job(QThread):
    def __init__(self):
        super(Job, self).__init__()
        # Create a TCP/IP socket
        
    

        
        



