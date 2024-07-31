# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1359, 844)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fitButton = QtWidgets.QPushButton(self.centralwidget)
        self.fitButton.setGeometry(QtCore.QRect(20, 300, 93, 28))
        self.fitButton.setObjectName("fitButton")
        self.loadTrainingSampleButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadTrainingSampleButton.setGeometry(QtCore.QRect(20, 260, 93, 28))
        self.loadTrainingSampleButton.setObjectName("loadTrainingSampleButton")
        self.trainingSampleTableView = QtWidgets.QTableView(self.centralwidget)
        self.trainingSampleTableView.setGeometry(QtCore.QRect(20, 370, 641, 351))
        self.trainingSampleTableView.setObjectName("trainingSampleTableView")
        self.virtualSampleModuleGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.virtualSampleModuleGroupBox.setGeometry(QtCore.QRect(10, 150, 251, 91))
        self.virtualSampleModuleGroupBox.setObjectName("virtualSampleModuleGroupBox")
        self.layoutWidget_2 = QtWidgets.QWidget(self.virtualSampleModuleGroupBox)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 30, 141, 51))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.inputVirtualSampleRadioButton = QtWidgets.QRadioButton(self.layoutWidget_2)
        self.inputVirtualSampleRadioButton.setObjectName("inputVirtualSampleRadioButton")
        self.verticalLayout_2.addWidget(self.inputVirtualSampleRadioButton)
        self.manualVirtualSampleRadioButton = QtWidgets.QRadioButton(self.layoutWidget_2)
        self.manualVirtualSampleRadioButton.setObjectName("manualVirtualSampleRadioButton")
        self.verticalLayout_2.addWidget(self.manualVirtualSampleRadioButton)
        self.virtualSampleTableView = QtWidgets.QTableView(self.centralwidget)
        self.virtualSampleTableView.setGeometry(QtCore.QRect(690, 370, 641, 351))
        self.virtualSampleTableView.setObjectName("virtualSampleTableView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 350, 141, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(690, 350, 121, 16))
        self.label_2.setObjectName("label_2")
        self.manualVirtualSampleWidget = QtWidgets.QWidget(self.centralwidget)
        self.manualVirtualSampleWidget.setGeometry(QtCore.QRect(690, 150, 641, 191))
        self.manualVirtualSampleWidget.setObjectName("manualVirtualSampleWidget")
        self.label_3 = QtWidgets.QLabel(self.manualVirtualSampleWidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 181, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.manualVirtualSampleWidget)
        self.label_4.setGeometry(QtCore.QRect(0, 30, 72, 15))
        self.label_4.setObjectName("label_4")
        self.nameComboBox = QtWidgets.QComboBox(self.manualVirtualSampleWidget)
        self.nameComboBox.setGeometry(QtCore.QRect(0, 50, 91, 22))
        self.nameComboBox.setObjectName("nameComboBox")
        self.label_5 = QtWidgets.QLabel(self.manualVirtualSampleWidget)
        self.label_5.setGeometry(QtCore.QRect(0, 90, 72, 15))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.manualVirtualSampleWidget)
        self.label_7.setGeometry(QtCore.QRect(170, 90, 72, 15))
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.manualVirtualSampleWidget)
        self.label_9.setGeometry(QtCore.QRect(0, 140, 72, 15))
        self.label_9.setObjectName("label_9")
        self.stepDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.manualVirtualSampleWidget)
        self.stepDoubleSpinBox.setGeometry(QtCore.QRect(0, 160, 91, 22))
        self.stepDoubleSpinBox.setDecimals(3)
        self.stepDoubleSpinBox.setMaximum(1000000.0)
        self.stepDoubleSpinBox.setObjectName("stepDoubleSpinBox")
        self.okButton = QtWidgets.QPushButton(self.manualVirtualSampleWidget)
        self.okButton.setGeometry(QtCore.QRect(170, 160, 71, 22))
        self.okButton.setObjectName("okButton")
        self.minimumDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.manualVirtualSampleWidget)
        self.minimumDoubleSpinBox.setGeometry(QtCore.QRect(0, 110, 91, 22))
        self.minimumDoubleSpinBox.setDecimals(3)
        self.minimumDoubleSpinBox.setMinimum(-1000000.0)
        self.minimumDoubleSpinBox.setMaximum(1000000.0)
        self.minimumDoubleSpinBox.setObjectName("minimumDoubleSpinBox")
        self.maximumDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.manualVirtualSampleWidget)
        self.maximumDoubleSpinBox.setGeometry(QtCore.QRect(170, 110, 91, 22))
        self.maximumDoubleSpinBox.setDecimals(3)
        self.maximumDoubleSpinBox.setMinimum(-1000000.0)
        self.maximumDoubleSpinBox.setMaximum(1000000.0)
        self.maximumDoubleSpinBox.setObjectName("maximumDoubleSpinBox")
        self.downloadVirtualSampleButton = QtWidgets.QPushButton(self.manualVirtualSampleWidget)
        self.downloadVirtualSampleButton.setGeometry(QtCore.QRect(542, 160, 91, 28))
        self.downloadVirtualSampleButton.setObjectName("downloadVirtualSampleButton")
        self.selectSamplesWidget = QtWidgets.QWidget(self.centralwidget)
        self.selectSamplesWidget.setGeometry(QtCore.QRect(300, 150, 361, 191))
        self.selectSamplesWidget.setObjectName("selectSamplesWidget")
        self.sampleScrollArea = QtWidgets.QScrollArea(self.selectSamplesWidget)
        self.sampleScrollArea.setGeometry(QtCore.QRect(0, 20, 361, 171))
        self.sampleScrollArea.setWidgetResizable(True)
        self.sampleScrollArea.setObjectName("sampleScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 359, 169))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.sampleScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_6 = QtWidgets.QLabel(self.selectSamplesWidget)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 72, 15))
        self.label_6.setObjectName("label_6")
        self.logoLabel = QtWidgets.QLabel(self.centralwidget)
        self.logoLabel.setGeometry(QtCore.QRect(20, 10, 1311, 115))
        self.logoLabel.setText("")
        self.logoLabel.setObjectName("logoLabel")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 730, 71, 16))
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 750, 161, 16))
        self.label_10.setObjectName("label_10")
        self.citation1Label = QtWidgets.QLabel(self.centralwidget)
        self.citation1Label.setGeometry(QtCore.QRect(190, 750, 351, 16))
        self.citation1Label.setObjectName("citation1Label")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(20, 770, 231, 16))
        self.label_12.setObjectName("label_12")
        self.citation2Label = QtWidgets.QLabel(self.centralwidget)
        self.citation2Label.setGeometry(QtCore.QRect(260, 770, 341, 16))
        self.citation2Label.setObjectName("citation2Label")
        self.resultButton = QtWidgets.QPushButton(self.centralwidget)
        self.resultButton.setGeometry(QtCore.QRect(160, 300, 93, 28))
        self.resultButton.setObjectName("resultButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1359, 26))
        self.menubar.setObjectName("menubar")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionParameter = QtWidgets.QAction(MainWindow)
        self.actionParameter.setObjectName("actionParameter")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.menuSetting.addAction(self.actionParameter)
        self.menubar.addAction(self.menuSetting.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.fitButton.setText(_translate("MainWindow", "Fit"))
        self.loadTrainingSampleButton.setText(_translate("MainWindow", "Load Data"))
        self.virtualSampleModuleGroupBox.setTitle(_translate("MainWindow", "Virtual Sample"))
        self.inputVirtualSampleRadioButton.setText(_translate("MainWindow", "Input"))
        self.manualVirtualSampleRadioButton.setText(_translate("MainWindow", "Manual"))
        self.label.setText(_translate("MainWindow", "Training Sample:"))
        self.label_2.setText(_translate("MainWindow", "Virtual Sample:"))
        self.label_3.setText(_translate("MainWindow", "Manual Virtual Sample:"))
        self.label_4.setText(_translate("MainWindow", "Name:"))
        self.label_5.setText(_translate("MainWindow", "Minimum:"))
        self.label_7.setText(_translate("MainWindow", "Maximum:"))
        self.label_9.setText(_translate("MainWindow", "Step:"))
        self.okButton.setText(_translate("MainWindow", "OK"))
        self.downloadVirtualSampleButton.setText(_translate("MainWindow", "Download"))
        self.label_6.setText(_translate("MainWindow", "Samples:"))
        self.label_8.setText(_translate("MainWindow", "Citation: "))
        self.label_10.setText(_translate("MainWindow", "Materials & Design : "))
        self.citation1Label.setText(_translate("MainWindow", "https://doi.org/10.1016/j.matdes.2024.112921"))
        self.label_12.setText(_translate("MainWindow", "NPJ Computational Materials :"))
        self.citation2Label.setText(_translate("MainWindow", "https://doi.org/10.1038/s41524-024-01243-4"))
        self.resultButton.setText(_translate("MainWindow", "Result"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.actionParameter.setText(_translate("MainWindow", "Parameter"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
