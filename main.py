from PyQt5 import QtGui, QtCore, QtWidgets
import sys, os, psutil
import design, modules

class MainApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.setupUi(self)
        self.update_ui()
        self.btnRefresh.clicked.connect(self.update_ui)
        self.btnExit.clicked.connect(self.exit_program)
        
    def update_ui(self):
        self.labCPUCount.setText(modules.cpu_count())
        self.labCPUClock.setText(modules.cpu_clock())
        self.labCPUUtil.setText(modules.cpu_utilization())
        self.labCPUTemp.setText(modules.cpu_temp())
        self.labTotRAM.setText(modules.ram_total())
        self.labAvailRAM.setText(modules.ram_available())
        self.labUsedRAM.setText(modules.ram_used())
        self.labPercentRAM.setText(modules.ram_utilization())
        self.labTotStorage.setText(modules.storage_total())
        self.labAvailStorage.setText(modules.storage_available())
        self.labUsedStorage.setText(modules.storage_used())
        self.labPercentStorage.setText(modules.storage_utilization())
        self.labGPUFanSpeed.setText(modules.gpu_fan_speed())
        self.labCPUFanSpeed.setText(modules.cpu_fan_speed())
        self.labGPUTemp.setText(modules.gpu_temp())

    def exit_program(self):
        # correct way to quit qt app instance
        self.close()
        

def main():
    app = QtWidgets.QApplication(sys.argv)
    pcstatus = MainApp()
    pcstatus.show()
    timer = QtCore.QTimer()
    timer.timeout.connect(pcstatus.update_ui)
    timer.start(3000)
    app.exec_()  # exec is a python reserve keyword

if __name__ == "__main__":
    main()