###
# Draw GUI Layout in this file.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Ui_Main(QObject):
    def setupUi(self, Form):
        Form.setWindowTitle("ICT Function GUI")

class Page_Testing(QObject):
    def setupUi(self, Form):

        #底部格局
        __bottomLayout = QGridLayout(Form)
        __bottomLayout.setSpacing(10)
        __bottomLayout.setContentsMargins(10, 10, 10, 10)
        __Block1 = QLabel(Form)
        __Block1.setStyleSheet("border:2px solid white")
        __Block2 = QLabel(Form)
        __Block2.setStyleSheet("border:2px solid white")
        __Block3 = QLabel(Form)
        __bottomLayout.addWidget(__Block1,2,7,6,3)
        __bottomLayout.addWidget(__Block2,0,0,2,10)
        __bottomLayout.addWidget(__Block3,2,0,6,7)

        #btn
        __buttonPartsLayout = QGridLayout()
        __bottomLayout.addLayout(__buttonPartsLayout,2,7,6,3)
        __buttonPartsLayout.setContentsMargins(10,10,10,10)
        self.btnTestItemLoad = QPushButton()
        self.btnSetting(self.btnTestItemLoad, "Load\nTest item", __buttonPartsLayout, [0,0,1,3],"QPushButton{color: white;font:bold 30px Arial; background-color:rgba(60,128,60,128)}") 
        self.btnTestItemSave = QPushButton()
        self.btnSetting(self.btnTestItemSave, "Save\nTest item", __buttonPartsLayout, [0,3,1,3],"QPushButton{color: white;font:bold 30px Arial; background-color:rgba(128,60,60,128)}") 
        self.btnTestingUpdate = QPushButton()
        self.btnSetting(self.btnTestingUpdate, "Update\nto Sever", __buttonPartsLayout, [1,0,1,3])
        self.btnRestore = QPushButton()
        self.btnSetting(self.btnRestore, "Restore", __buttonPartsLayout, [1,3,1,3])
        self.btnDoICT = QPushButton()
        self.btnSetting(self.btnDoICT, "ICT &\nFcn Test", __buttonPartsLayout, [2,0,1,3])
        self.btnDoAutoRun = QPushButton()
        self.btnSetting(self.btnDoAutoRun, "AUTO\nRUN", __buttonPartsLayout, [2,3,1,3])
        self.btnStop = QPushButton()
        self.btnSetting(self.btnStop, "STOP", __buttonPartsLayout, [3,0,1,6])

        #工作資訊Layout
        __InformLayout = QGridLayout()
        __bottomLayout.addLayout(__InformLayout,0,0,2,10)
        __InformLayout.setSpacing(10)
        __InformLayout.setContentsMargins(10,10,10,10)

        #firmware
        __label = QLabel("待測基板:")
        __label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        __label.setStyleSheet("color: white;font:bold 35px Microsoft JhengHei")
        __InformLayout.addWidget(__label, 0,0,1,3)
        self.comboFW = QLabel("TEST")
        self.comboFW.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.comboFW.setStyleSheet("color: white;font:bold 35px Arial;max-width: 4em;background-color:rgba(255,255,255,0)")
        __InformLayout.addWidget(self.comboFW,1,0,1,3)
        self.btnConfirmFW = QPushButton("Confirm")
        self.btnConfirmFW.setStyleSheet("color: white;font:bold 35px Arial")
        self.btnConfirmFW.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        __InformLayout.addWidget(self.btnConfirmFW,1,14,1,3)
        self.comboFW.setEnabled(False)

        #工單號
        __label = QLabel("工單號:")
        __label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        __label.setStyleSheet("color: white;font:bold 35px Microsoft JhengHei")
        __InformLayout.addWidget(__label, 0,4,1,10)
        self.comboOrder = QLabel("2023-02-07_work_order_0001")
        self.comboOrder.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.comboOrder.setStyleSheet("color: white;font:bold 35px Arial;min-width: 2em;background-color:rgba(255,255,255,0)")
        __InformLayout.addWidget(self.comboOrder,1,4,1,10)

        #表格Layout
        __testItemLayout = QGridLayout()
        __bottomLayout.addLayout(__testItemLayout,2,0,6,7)

        #TableWidget
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.tableWidget.setStyleSheet("background-color: rgba(211,211,211,255);color: black;font: 25px Arial; gridline-color:rgba(211,211,211,255);")
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.chkBoxHeader = QCheckBox("All")
        self.tableWidget.setCellWidget(0,0,self.chkBoxHeader)
        self.chkBoxHeader.setChecked(True)
        self.chkBoxHeader.setStyleSheet("background-color: rgba(255,115,0,255);color: black;font: 25px Arial;gridline-color:rgba(211,211,211,255);")
        #self.Chkbox_Header.stateChanged.connect(self.Chkbox_state)#勾選ALL的情況
        self.tableWidget.horizontalHeader().setSectionResizeMode(1,QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2,QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3,QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(4,QHeaderView.Stretch)
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Item"))
        self.tableWidget.setItem(0, 2, QTableWidgetItem("Min"))
        self.tableWidget.setItem(0, 3, QTableWidgetItem("Value"))
        self.tableWidget.setItem(0, 4, QTableWidgetItem("Max"))
        self.tableWidget.setItem(0, 5, QTableWidgetItem("P/F"))
        self.tableWidget.item(0, 1).setBackground(QColor(255,115,0,255)) 
        self.tableWidget.item(0, 2).setBackground(QColor(255,115,0,255))
        self.tableWidget.item(0, 3).setBackground(QColor(255,115,0,255)) 
        self.tableWidget.item(0, 4).setBackground(QColor(255,115,0,255))
        self.tableWidget.item(0, 5).setBackground(QColor(255,115,0,255)) 
        self.tableWidget.item(0, 2).setTextAlignment(Qt.AlignRight)
        self.tableWidget.item(0, 3).setTextAlignment(Qt.AlignRight)
        self.tableWidget.item(0, 4).setTextAlignment(Qt.AlignRight)  
        self.tableWidget.item(0, 5).setTextAlignment(Qt.AlignRight)  
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        __testItemLayout.addWidget(self.tableWidget,0,0,1,1)
        
    def btnSetting(self, __btn,__name: str, __layout, __pos: list, __style: str = "QPushButton{color: white;font:bold 30px Arial; background-color:rgba(128,128,128,255)}"):
        __btn.setText(__name)
        __btn.setStyleSheet(__style)
        __btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        __layout.addWidget(__btn,__pos[0],__pos[1],__pos[2],__pos[3])
        
    def chkboxSetting(self, __chkbox, __name: str, __layout, __pos: list, __checked: bool):
        __chkbox.setText(__name)
        __chkbox.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        __chkbox.setStyleSheet("color: white;font: 20px Arial;border:2px solid white")
        __chkbox.setChecked(__checked)
        __layout.addWidget(__chkbox,__pos[0],__pos[1],__pos[2],__pos[3])
        
class Page_Manual(QObject):
    def setupUi(self, Form):
        #底部格局
        __bottomLayout = QGridLayout(Form)
        __bottomLayout.setSpacing(20)
        __bottomLayout.setContentsMargins(20, 20, 20, 20)
        
        #Conveyer Forward & Backward
        __label = QLabel()
        self.labelSetting(__bottomLayout, __label, "Conveyer", [0,0,2,2])
        __layout = QGridLayout()
        self.layoutSetting(__bottomLayout, __layout, 20, [20,150,20,60], [0,0,2,2])
        self.btnConveyerBackward = QPushButton()
        self.btnSetting(self.btnConveyerBackward, "◀\nBackward", __layout, [0,0,1,1])
        self.btnConveyerForward = QPushButton()
        self.btnSetting(self.btnConveyerForward, "▶\nForward", __layout, [0,1,1,1])
        
        #Conveyer Up & Down
        __label = QLabel()
        self.labelSetting(__bottomLayout, __label, "Conveyer", [0,2,2,1])
        __layout = QGridLayout()
        self.layoutSetting(__bottomLayout, __layout, 20, [20,60,20,20], [0,2,2,1])
        self.btnConveyerUp = QPushButton()
        self.btnSetting(self.btnConveyerUp, "▴\nUp", __layout, [0,0,1,1])
        self.btnConveyerDown = QPushButton()
        self.btnSetting(self.btnConveyerDown, "▾\nDown", __layout, [1,0,1,1])

        #Block
        __label = QLabel()
        self.labelSetting(__bottomLayout, __label, "Block", [0,3,2,1])
        __layout = QGridLayout()
        self.layoutSetting(__bottomLayout, __layout, 20, [20,60,20,20], [0,3,2,1])
        self.btnBlockUp = QPushButton()
        self.btnSetting(self.btnBlockUp, "▴\nUp", __layout, [0,0,1,1])          
        self.btnBlockDown = QPushButton()
        self.btnSetting(self.btnBlockDown, "▾\nDown", __layout, [1,0,1,1])
        
        #Probe Board
        __label = QLabel()
        self.labelSetting(__bottomLayout, __label, "ProbeBoard", [0,4,2,1])
        __layout = QGridLayout()
        self.layoutSetting(__bottomLayout, __layout, 20, [20,60,20,20], [0,4,2,1])
        self.btnProbeBoardUp = QPushButton()
        self.btnSetting(self.btnProbeBoardUp, "▴\nUp", __layout, [0,0,1,1]) 
        self.btnProbeBoardDown = QPushButton()
        self.btnSetting(self.btnProbeBoardDown, "▾\nDown", __layout, [1,0,1,1]) 
        
        #Fix Vehicle
        __label = QLabel()
        self.labelSetting(__bottomLayout, __label, "FixVehicle", [0,5,2,1])
        __layout = QGridLayout()
        self.layoutSetting(__bottomLayout, __layout, 20, [20,60,20,20], [0,5,2,1])
        self.btnFixedVehicleUp = QPushButton()
        self.btnSetting(self.btnFixedVehicleUp, "▴\nUp", __layout, [0,0,1,1]) 
        self.btnFixedVehicleDown = QPushButton()
        self.btnSetting(self.btnFixedVehicleDown, "▾\nDown", __layout, [1,0,1,1]) 
        
        #Tray Base
        __label = QLabel()
        self.labelSetting(__bottomLayout, __label, "TrayBase", [0,6,2,1])
        __layout = QGridLayout()
        self.layoutSetting(__bottomLayout, __layout, 20, [20,60,20,20], [0,6,2,1])
        self.btnTrayBaseUp = QPushButton()
        self.btnSetting(self.btnTrayBaseUp, "▴\nUp", __layout, [0,0,1,1]) 
        self.btnTrayBaseDown = QPushButton()
        self.btnSetting(self.btnTrayBaseDown, "▾\nDown", __layout, [1,0,1,1]) 
        
        #OP Mode
        __layout = QGridLayout()
        self.layoutSetting(__bottomLayout, __layout, 20, [20,60,20,20], [2,2,2,1])
        __label = QLabel()
        self.labelSetting(__bottomLayout, __label, "OP Mode", [2,2,2,1])
        self.btnCalibration = QPushButton()
        self.btnSetting(self.btnCalibration, "Do K", __layout, [0,0,1,1]) 
        self.btnSleep = QPushButton()
        self.btnSetting(self.btnSleep, "Sleep", __layout, [1,0,1,1]) 
        
        #Power
        __label = QLabel()
        self.labelSetting(__bottomLayout, __label, "Power", [2,3,2,1])
        __layout = QGridLayout()
        self.layoutSetting(__bottomLayout, __layout, 10, [20,50,20,10], [2,3,2,1])
        self.btnProbePower = QPushButton()
        self.btnSetting(self.btnProbePower, "Probe\nBoard", __layout, [0,0,1,1],"QPushButton{color: white;font:bold 30px Arial; background-color:rgba(128,60,60,128)}") 
        self.btnIndoorPower = QPushButton()
        self.btnSetting(self.btnIndoorPower, "Indoor", __layout, [1,0,1,1],"QPushButton{color: white;font:bold 30px Arial; background-color:rgba(128,128,60,128)}") 
        self.btnHVWVT = QPushButton()
        self.btnSetting(self.btnHVWVT, "HV\nWVT", __layout, [2,0,1,1],"QPushButton{color: white;font:bold 30px Arial; background-color:rgba(60,128,60,128)}") 

        #Alarm
        __label = QLabel()
        self.labelSetting(__bottomLayout, __label, "Alarm", [2,4,2,1])
        __layout = QGridLayout()
        self.layoutSetting(__bottomLayout, __layout, 10, [20,50,20,10], [2,4,2,1])
        self.btnAlarmR = QPushButton()
        self.btnSetting(self.btnAlarmR, "Red\nLight", __layout, [0,0,1,1],"QPushButton{color: white;font:bold 30px Arial; background-color:rgba(128,60,60,128)}") 
        self.btnAlarmY = QPushButton()
        self.btnSetting(self.btnAlarmY, "Yellow\nLight", __layout, [1,0,1,1],"QPushButton{color: white;font:bold 30px Arial; background-color:rgba(128,128,60,128)}") 
        self.btnAlarmG=QPushButton()
        self.btnSetting(self.btnAlarmG, "Green\nLigh", __layout, [2,0,1,1],"QPushButton{color: white;font:bold 30px Arial; background-color:rgba(60,128,60,128)}") 
        
        #Barcode
        __label = QLabel()
        self.labelSetting(__bottomLayout, __label, "", [2,0,2,2])
        __layout = QGridLayout()
        self.layoutSetting(__bottomLayout, __layout, 20, [20,40,20,40], [2,0,2,2])
        self.btnBarcode = QPushButton("Read\nBarcode")
        self.btnSetting(self.btnBarcode, "Read\nBarcode", __layout, [0,0,1,2]) 
        self.lineBarcode=QLineEdit() 
        self.lineBarcode.setStyleSheet("QLineEdit{color: black;font:bold 30px Arial;max-height: 2em;background-color:rgba(255,255,255,255)}")
        self.lineBarcode.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        __layout.addWidget(self.lineBarcode,1,0,1,2)

        #LAMP FAN Buzzer Rst
        __label = QLabel()
        self.labelSetting(__bottomLayout, __label, "", [2,5,2,2])
        __layout = QGridLayout()
        self.layoutSetting(__bottomLayout, __layout, 20, [20,40,20,40], [2,5,2,2])
        self.btnLamp = QPushButton()
        self.btnSetting(self.btnLamp, "💡\nLAMP", __layout, [0,0,1,1]) 
        self.btnCoolingFan=QPushButton()
        self.btnSetting(self.btnCoolingFan, "💨\nFAN", __layout, [1,0,1,1]) 
        self.btnBuzzer = QPushButton("Buzzer")
        self.btnSetting(self.btnBuzzer, "Buzzer", __layout, [0,1,1,1]) 
        self.btnBoardReset=QPushButton("Board\nReset")
        self.btnSetting(self.btnBoardReset, "Board\nReset", __layout, [1,1,1,1]) 
        
    def layoutSetting(self,  __bottomLayout, __layout, __spacing: int, __margins: list, __pos: list):
        __layout.setSpacing(__spacing)
        __layout.setContentsMargins(__margins[0],__margins[1],__margins[2],__margins[3])
        __bottomLayout.addLayout(__layout,__pos[0],__pos[1],__pos[2],__pos[3])

    def btnSetting(self, __btn,__name: str, __layout, __pos: list, __style: str = "QPushButton{color: white;font:bold 30px Arial; background-color:rgba(128,128,128,255)}"):
        __btn.setText(__name)
        __btn.setStyleSheet(__style)
        __btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        __layout.addWidget(__btn,__pos[0],__pos[1],__pos[2],__pos[3])
        
    def labelSetting(self, __bottomLayout, __label, __name: str, __pos: list, __style: str = "QLabel{color: white;font:bold 30px Arial;background-color:rgba(105,105,105,255)}"):
        __label.setText(__name)
        __label.setStyleSheet(__style)
        __label.setAlignment(Qt.AlignHCenter)
        __bottomLayout.addWidget(__label,__pos[0],__pos[1],__pos[2],__pos[3])
    

    
        
        
        