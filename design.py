# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(525, 289)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.boxRAM = QtWidgets.QGroupBox(self.centralwidget)
        self.boxRAM.setObjectName("boxRAM")
        self.label_7 = QtWidgets.QLabel(self.boxRAM)
        self.label_7.setGeometry(QtCore.QRect(10, 30, 121, 17))
        self.label_7.setObjectName("label_7")
        self.labTotRAM = QtWidgets.QLabel(self.boxRAM)
        self.labTotRAM.setGeometry(QtCore.QRect(140, 30, 71, 17))
        self.labTotRAM.setObjectName("labTotRAM")
        self.label_8 = QtWidgets.QLabel(self.boxRAM)
        self.label_8.setGeometry(QtCore.QRect(10, 50, 121, 17))
        self.label_8.setObjectName("label_8")
        self.labUsedRAM = QtWidgets.QLabel(self.boxRAM)
        self.labUsedRAM.setGeometry(QtCore.QRect(140, 50, 71, 17))
        self.labUsedRAM.setObjectName("labUsedRAM")
        self.label_9 = QtWidgets.QLabel(self.boxRAM)
        self.label_9.setGeometry(QtCore.QRect(10, 70, 121, 17))
        self.label_9.setObjectName("label_9")
        self.labAvailRAM = QtWidgets.QLabel(self.boxRAM)
        self.labAvailRAM.setGeometry(QtCore.QRect(140, 70, 71, 17))
        self.labAvailRAM.setObjectName("labAvailRAM")
        self.label_10 = QtWidgets.QLabel(self.boxRAM)
        self.label_10.setGeometry(QtCore.QRect(10, 90, 121, 17))
        self.label_10.setObjectName("label_10")
        self.labPercentRAM = QtWidgets.QLabel(self.boxRAM)
        self.labPercentRAM.setGeometry(QtCore.QRect(140, 90, 71, 17))
        self.labPercentRAM.setObjectName("labPercentRAM")
        self.gridLayout.addWidget(self.boxRAM, 1, 0, 1, 2)
        self.boxStorage = QtWidgets.QGroupBox(self.centralwidget)
        self.boxStorage.setObjectName("boxStorage")
        self.label_11 = QtWidgets.QLabel(self.boxStorage)
        self.label_11.setGeometry(QtCore.QRect(10, 30, 121, 17))
        self.label_11.setObjectName("label_11")
        self.labTotStorage = QtWidgets.QLabel(self.boxStorage)
        self.labTotStorage.setGeometry(QtCore.QRect(140, 30, 71, 17))
        self.labTotStorage.setObjectName("labTotStorage")
        self.labUsedStorage = QtWidgets.QLabel(self.boxStorage)
        self.labUsedStorage.setGeometry(QtCore.QRect(140, 50, 71, 17))
        self.labUsedStorage.setObjectName("labUsedStorage")
        self.label_12 = QtWidgets.QLabel(self.boxStorage)
        self.label_12.setGeometry(QtCore.QRect(10, 50, 121, 17))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.boxStorage)
        self.label_13.setGeometry(QtCore.QRect(10, 70, 121, 17))
        self.label_13.setObjectName("label_13")
        self.labAvailStorage = QtWidgets.QLabel(self.boxStorage)
        self.labAvailStorage.setGeometry(QtCore.QRect(140, 70, 71, 17))
        self.labAvailStorage.setObjectName("labAvailStorage")
        self.label_14 = QtWidgets.QLabel(self.boxStorage)
        self.label_14.setGeometry(QtCore.QRect(10, 90, 121, 17))
        self.label_14.setObjectName("label_14")
        self.labPercentStorage = QtWidgets.QLabel(self.boxStorage)
        self.labPercentStorage.setGeometry(QtCore.QRect(140, 90, 71, 17))
        self.labPercentStorage.setObjectName("labPercentStorage")
        self.gridLayout.addWidget(self.boxStorage, 1, 2, 1, 2)
        self.boxCPU = QtWidgets.QGroupBox(self.centralwidget)
        self.boxCPU.setObjectName("boxCPU")
        self.label = QtWidgets.QLabel(self.boxCPU)
        self.label.setGeometry(QtCore.QRect(10, 30, 121, 17))
        self.label.setObjectName("label")
        self.labCPUCount = QtWidgets.QLabel(self.boxCPU)
        self.labCPUCount.setGeometry(QtCore.QRect(140, 30, 21, 17))
        self.labCPUCount.setObjectName("labCPUCount")
        self.labCPUClock = QtWidgets.QLabel(self.boxCPU)
        self.labCPUClock.setGeometry(QtCore.QRect(140, 50, 81, 17))
        self.labCPUClock.setObjectName("labCPUClock")
        self.label_2 = QtWidgets.QLabel(self.boxCPU)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 121, 17))
        self.label_2.setObjectName("label_2")
        self.labCPUUtil = QtWidgets.QLabel(self.boxCPU)
        self.labCPUUtil.setGeometry(QtCore.QRect(140, 70, 81, 17))
        self.labCPUUtil.setObjectName("labCPUUtil")
        self.label_3 = QtWidgets.QLabel(self.boxCPU)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 121, 17))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.boxCPU, 0, 0, 1, 2)
        self.boxPower = QtWidgets.QGroupBox(self.centralwidget)
        self.boxPower.setObjectName("boxPower")
        self.labCPUTemp = QtWidgets.QLabel(self.boxPower)
        self.labCPUTemp.setGeometry(QtCore.QRect(140, 30, 31, 17))
        self.labCPUTemp.setObjectName("labCPUTemp")
        self.label_4 = QtWidgets.QLabel(self.boxPower)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 121, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.boxPower)
        self.label_5.setGeometry(QtCore.QRect(10, 50, 121, 17))
        self.label_5.setObjectName("label_5")
        self.labGPUTemp = QtWidgets.QLabel(self.boxPower)
        self.labGPUTemp.setGeometry(QtCore.QRect(140, 50, 31, 17))
        self.labGPUTemp.setObjectName("labGPUTemp")
        self.labCPUFanSpeed = QtWidgets.QLabel(self.boxPower)
        self.labCPUFanSpeed.setGeometry(QtCore.QRect(140, 70, 81, 17))
        self.labCPUFanSpeed.setObjectName("labCPUFanSpeed")
        self.label_6 = QtWidgets.QLabel(self.boxPower)
        self.label_6.setGeometry(QtCore.QRect(10, 70, 121, 17))
        self.label_6.setObjectName("label_6")
        self.labGPUFanSpeed = QtWidgets.QLabel(self.boxPower)
        self.labGPUFanSpeed.setGeometry(QtCore.QRect(140, 90, 81, 17))
        self.labGPUFanSpeed.setObjectName("labGPUFanSpeed")
        self.label_15 = QtWidgets.QLabel(self.boxPower)
        self.label_15.setGeometry(QtCore.QRect(10, 90, 121, 17))
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.boxPower, 0, 2, 1, 2)
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setObjectName("btnExit")
        self.gridLayout.addWidget(self.btnExit, 2, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PCStatus | Details Under the Hood"))
        self.boxRAM.setTitle(_translate("MainWindow", "RAM"))
        self.label_7.setText(_translate("MainWindow", "Total"))
        self.labTotRAM.setText(_translate("MainWindow", "1024 MB"))
        self.label_8.setText(_translate("MainWindow", "Used"))
        self.labUsedRAM.setText(_translate("MainWindow", "1024 MB"))
        self.label_9.setText(_translate("MainWindow", "Available"))
        self.labAvailRAM.setText(_translate("MainWindow", "1024 MB"))
        self.label_10.setText(_translate("MainWindow", "Percent Utilized"))
        self.labPercentRAM.setText(_translate("MainWindow", "38%"))
        self.boxStorage.setTitle(_translate("MainWindow", "Storage"))
        self.label_11.setText(_translate("MainWindow", "Total"))
        self.labTotStorage.setText(_translate("MainWindow", "1024 GB"))
        self.labUsedStorage.setText(_translate("MainWindow", "1024 GB"))
        self.label_12.setText(_translate("MainWindow", "Used"))
        self.label_13.setText(_translate("MainWindow", "Available"))
        self.labAvailStorage.setText(_translate("MainWindow", "1024 GB"))
        self.label_14.setText(_translate("MainWindow", "Percent Utilized"))
        self.labPercentStorage.setText(_translate("MainWindow", "42%"))
        self.boxCPU.setTitle(_translate("MainWindow", "CPU"))
        self.label.setText(_translate("MainWindow", "Number of CPUs"))
        self.labCPUCount.setText(_translate("MainWindow", "8"))
        self.labCPUClock.setText(_translate("MainWindow", "3500 Mhz"))
        self.label_2.setText(_translate("MainWindow", "Clock Speed"))
        self.labCPUUtil.setText(_translate("MainWindow", "3%"))
        self.label_3.setText(_translate("MainWindow", "CPU Utilization"))
        self.boxPower.setTitle(_translate("MainWindow", "Power"))
        self.labCPUTemp.setText(_translate("MainWindow", "28°"))
        self.label_4.setText(_translate("MainWindow", "CPU Temp."))
        self.label_5.setText(_translate("MainWindow", "GPU Temp"))
        self.labGPUTemp.setText(_translate("MainWindow", "28°"))
        self.labCPUFanSpeed.setText(_translate("MainWindow", "2000 RPM"))
        self.label_6.setText(_translate("MainWindow", "CPU Fan"))
        self.labGPUFanSpeed.setText(_translate("MainWindow", "2000 RPM"))
        self.label_15.setText(_translate("MainWindow", "GPU Fan"))
        self.btnExit.setText(_translate("MainWindow", "Exit"))

