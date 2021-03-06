# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plane_insert_update.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import dbQueries as Db
from Admin_Pages.transactionstatus import Ui_transactionSuccessful as transactionStatus


class Ui_planeWindow(object):
    def setupUi(self, MainWindow,type):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600,625)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.planeInsertUpdateLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.planeInsertUpdateLabel.setFont(font)
        self.planeInsertUpdateLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.planeInsertUpdateLabel.setObjectName("planeInsertUpdateLabel")
        self.verticalLayout_3.addWidget(self.planeInsertUpdateLabel)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.planeId = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.planeId.setFont(font)
        self.planeId.setObjectName("planeId")
        self.verticalLayout.addWidget(self.planeId)
        self.planeName = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.planeName.setFont(font)
        self.planeName.setObjectName("planeName")
        self.verticalLayout.addWidget(self.planeName)
        self.planeSource = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.planeSource.setFont(font)
        self.planeSource.setObjectName("planeSource")
        self.verticalLayout.addWidget(self.planeSource)
        self.planeDestination = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.planeDestination.setFont(font)
        self.planeDestination.setObjectName("planeDestination")
        self.verticalLayout.addWidget(self.planeDestination)
        self.Class = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Class.setFont(font)
        self.Class.setObjectName("Class")
        self.verticalLayout.addWidget(self.Class)
        self.planeFare = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.planeFare.setFont(font)
        self.planeFare.setObjectName("planeFare")
        self.verticalLayout.addWidget(self.planeFare)
        self.planeNumberOfSeats = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.planeNumberOfSeats.setFont(font)
        self.planeNumberOfSeats.setObjectName("planeNumberOfSeats")
        self.verticalLayout.addWidget(self.planeNumberOfSeats)
        self.planeJourneyHours = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.planeJourneyHours.setFont(font)
        self.planeJourneyHours.setObjectName("planeJourneyHours")
        self.verticalLayout.addWidget(self.planeJourneyHours)
        self.planeDepartureDate = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.planeDepartureDate.setFont(font)
        self.planeDepartureDate.setObjectName("planeDepartureDate")
        self.verticalLayout.addWidget(self.planeDepartureDate)
        self.planeDepartureTime = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.planeDepartureTime.setFont(font)
        self.planeDepartureTime.setObjectName("planeDepartureTime")
        self.verticalLayout.addWidget(self.planeDepartureTime)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.planeIdLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.planeIdLineEdit.setFont(font)
        self.planeIdLineEdit.setObjectName("planeIdLineEdit")
        self.verticalLayout_2.addWidget(self.planeIdLineEdit)
        self.planeNameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.planeNameLineEdit.setFont(font)
        self.planeNameLineEdit.setObjectName("planeNameLineEdit")
        self.verticalLayout_2.addWidget(self.planeNameLineEdit)
        self.planeSourceLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.planeSourceLineEdit.setFont(font)
        self.planeSourceLineEdit.setObjectName("planeSourceLineEdit")
        self.verticalLayout_2.addWidget(self.planeSourceLineEdit)
        self.planeDestinationLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.planeDestinationLineEdit.setFont(font)
        self.planeDestinationLineEdit.setObjectName("planeDestinationLineEdit")
        self.verticalLayout_2.addWidget(self.planeDestinationLineEdit)
        self.planeClassLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.planeClassLineEdit.setObjectName("planeClassLineEdit")
        self.verticalLayout_2.addWidget(self.planeClassLineEdit)
        self.planeFareLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.planeFareLineEdit.setFont(font)
        self.planeFareLineEdit.setObjectName("planeFareLineEdit")
        self.verticalLayout_2.addWidget(self.planeFareLineEdit)
        self.planeNumberOfSeatsLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.planeNumberOfSeatsLineEdit.setFont(font)
        self.planeNumberOfSeatsLineEdit.setObjectName("planeNumberOfSeatsLineEdit")
        self.verticalLayout_2.addWidget(self.planeNumberOfSeatsLineEdit)
        self.planeJourneyHoursLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.planeJourneyHoursLineEdit.setFont(font)
        self.planeJourneyHoursLineEdit.setObjectName("planeJourneyHoursLineEdit")
        self.verticalLayout_2.addWidget(self.planeJourneyHoursLineEdit)
        self.planeDepartureDateLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.planeDepartureDateLineEdit.setFont(font)
        self.planeDepartureDateLineEdit.setObjectName("planeDepartureDateLineEdit")
        self.verticalLayout_2.addWidget(self.planeDepartureDateLineEdit)
        self.planeDepartureTimeLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.planeDepartureTimeLineEdit.setFont(font)
        self.planeDepartureTimeLineEdit.setObjectName("planeDepartureTimeLineEdit")
        self.verticalLayout_2.addWidget(self.planeDepartureTimeLineEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.okPushButtonForPlaneInsertUpdate = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.okPushButtonForPlaneInsertUpdate.setFont(font)
        self.okPushButtonForPlaneInsertUpdate.setObjectName("okPushButtonForPlaneInsertUpdate")
        self.horizontalLayout_3.addWidget(self.okPushButtonForPlaneInsertUpdate)
        self.backPushButtonForPlaneInsertUpdate = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.backPushButtonForPlaneInsertUpdate.setFont(font)
        self.backPushButtonForPlaneInsertUpdate.setObjectName("backPushButtonForPlaneInsertUpdate")
        self.horizontalLayout_3.addWidget(self.backPushButtonForPlaneInsertUpdate)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 806, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.type = type
        self.okPushButtonForPlaneInsertUpdate.clicked.connect(lambda: self.evaluate(type))
        self.backPushButtonForPlaneInsertUpdate.clicked.connect(lambda: MainWindow.close())

    def evaluate(self, type):
        if type == 'insert':
            if self.planeClassLineEdit.text()!='' and self.planeIdLineEdit.text() != '' and self.planeNameLineEdit.text() != '' \
                    and self.planeSourceLineEdit.text() != '' and self.planeDestinationLineEdit.text() != '' and self.planeFareLineEdit.text() != '' \
                    and self.planeNumberOfSeatsLineEdit.text() != '' and self.planeJourneyHoursLineEdit.text() != '' and self.planeDepartureDateLineEdit.text() != '' \
                    and self.planeDepartureTimeLineEdit.text() != '':
                planeId = self.planeIdLineEdit.text()
                planeName = self.planeNameLineEdit.text()
                source = self.planeSourceLineEdit.text()
                destination = self.planeDestinationLineEdit.text()
                fare = self.planeFareLineEdit.text()
                numberOfSeats = self.planeNumberOfSeatsLineEdit.text()
                journeyHours = self.planeJourneyHoursLineEdit.text()
                departureDate = self.planeDepartureDateLineEdit.text()
                departureTime = self.planeDepartureTimeLineEdit.text()
                plane_class=self.planeClassLineEdit.text()
                res = Db.insertPlane(planeId, planeName, source, destination, fare, numberOfSeats, journeyHours,
                                     departureDate,
                                     departureTime,plane_class)
                if (res == 1):
                    self.tranForm = QtWidgets.QMainWindow()
                    self.tranUi = transactionStatus()
                    self.tranUi.setupUi(self.tranForm,1)
                    self.tranForm.show()
                else:
                    self.tranForm = QtWidgets.QMainWindow()
                    self.tranUi = transactionStatus()
                    self.tranUi.setupUi(self.tranForm,-1)
                    self.tranForm.show()
        elif type == 'update':
            if self.planeClassLineEdit.text()!='' and self.planeIdLineEdit.text() != '' and self.planeNameLineEdit.text() != '' \
                    and self.planeSourceLineEdit.text() != '' and self.planeDestinationLineEdit.text() != '' and self.planeFareLineEdit.text() != '' \
                    and self.planeNumberOfSeatsLineEdit.text() != '' and self.planeJourneyHoursLineEdit.text() != '' and self.planeDepartureDateLineEdit.text() != '' \
                    and self.planeDepartureTimeLineEdit.text() != '':
                planeId = self.planeIdLineEdit.text()
                planeName = self.planeNameLineEdit.text()
                source = self.planeSourceLineEdit.text()
                destination = self.planeDestinationLineEdit.text()
                fare = self.planeFareLineEdit.text()
                numberOfSeats = self.planeNumberOfSeatsLineEdit.text()
                journeyHours = self.planeJourneyHoursLineEdit.text()
                departureDate = self.planeDepartureDateLineEdit.text()
                departureTime = self.planeDepartureTimeLineEdit.text()
                plane_class = self.planeClassLineEdit.text()
                res = Db.updatePlane(planeId, planeName, source, destination, fare, numberOfSeats, journeyHours,
                                     departureDate,
                                     departureTime,plane_class)
                if (res == 1):
                    self.tranForm = QtWidgets.QMainWindow()
                    self.tranUi = transactionStatus()
                    self.tranUi.setupUi(self.tranForm,1)
                    self.tranForm.show()
                else:
                    self.tranForm = QtWidgets.QMainWindow()
                    self.tranUi = transactionStatus()
                    self.tranUi.setupUi(self.tranForm,-1)
                    self.tranForm.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Plane Details"))
        self.planeInsertUpdateLabel.setText(_translate("MainWindow", "PLANE INSERT/ UPDATE FORM-"))
        self.planeId.setText(_translate("MainWindow", "Plane ID"))
        self.planeName.setText(_translate("MainWindow", "Plane Name"))
        self.planeSource.setText(_translate("MainWindow", "Source"))
        self.planeDestination.setText(_translate("MainWindow", "Destination"))
        self.Class.setText(_translate("MainWindow", "Class"))
        self.planeFare.setText(_translate("MainWindow", "Fare"))
        self.planeNumberOfSeats.setText(_translate("MainWindow", "Number of seats"))
        self.planeJourneyHours.setText(_translate("MainWindow", "Jouney hours"))
        self.planeDepartureDate.setText(_translate("MainWindow", "Departure Date"))
        self.planeDepartureTime.setText(_translate("MainWindow", "Departure Time"))
        self.okPushButtonForPlaneInsertUpdate.setText(_translate("MainWindow", "Ok"))
        self.backPushButtonForPlaneInsertUpdate.setText(_translate("MainWindow", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_planeWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
