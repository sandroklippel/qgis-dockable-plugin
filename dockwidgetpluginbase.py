# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DockWidgetPluginBase(object):
    def setupUi(self, DockWidgetPluginBase):
        DockWidgetPluginBase.setObjectName("DockWidgetPluginBase")
        DockWidgetPluginBase.resize(232, 141)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.dockWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        # DockWidgetPluginBase.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidgetPluginBase)
        QtCore.QMetaObject.connectSlotsByName(DockWidgetPluginBase)

    def retranslateUi(self, DockWidgetPluginBase):
        _translate = QtCore.QCoreApplication.translate
        DockWidgetPluginBase.setWindowTitle(_translate("DockWidgetPluginBase", "Test DockWidget"))
        self.label.setText(_translate("DockWidgetPluginBase", "Replace this QLabel\n"
"with the desired\n"
"plugin content."))

