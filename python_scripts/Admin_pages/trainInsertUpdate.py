# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'train_insert_update.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import dbQueries as Db
from Admin_Pages.transactionstatus import Ui_transactionSuccessful as transactionStatus

class Ui_trainWindow(object):
    def setupUi(self, MainWindow,type):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(600,600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.trainInsertUpdateLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.trainInsertUpdateLabel.setFont(font)
        self.trainInsertUpdateLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.trainInsertUpdateLabel.setObjectName("trainInsertUpdateLabel")
        self.verticalLayout_4.addWidget(self.trainInsertUpdateLabel)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(778, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.trainId = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.trainId.setFont(font)
        self.trainId.setObjectName("trainId")
        self.verticalLayout.addWidget(self.trainId)
        self.trainName = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.trainName.setFont(font)
        self.trainName.setObjectName("trainName")
        self.verticalLayout.addWidget(self.trainName)
        self.trainSource = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.trainSource.setFont(font)
        self.trainSource.setObjectName("trainSource")
        self.verticalLayout.addWidget(self.trainSource)
        self.trainDestination = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.trainDestination.setFont(font)
        self.trainDestination.setObjectName("trainDestination")
        self.verticalLayout.addWidget(self.trainDestination)
        self.trainFare = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.trainFare.setFont(font)
        self.trainFare.setObjectName("trainFare")
        self.verticalLayout.addWidget(self.trainFare)
        self.trainClass = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.trainClass.setFont(font)
        self.trainClass.setObjectName("trainClass")
        self.verticalLayout.addWidget(self.trainClass)
        self.trainNumberOfSeats = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.trainNumberOfSeats.setFont(font)
        self.trainNumberOfSeats.setObjectName("trainNumberOfSeats")
        self.verticalLayout.addWidget(self.trainNumberOfSeats)
        self.trainJourneyHours = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.trainJourneyHours.setFont(font)
        self.trainJourneyHours.setObjectName("trainJourneyHours")
        self.verticalLayout.addWidget(self.trainJourneyHours)
        self.trainStatus = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.trainStatus.setFont(font)
        self.trainStatus.setObjectName("trainStatus")
        self.verticalLayout.addWidget(self.trainStatus)
        self.trainDepartureDate = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.trainDepartureDate.setFont(font)
        self.trainDepartureDate.setObjectName("trainDepartureDate")
        self.verticalLayout.addWidget(self.trainDepartureDate)
        self.trainDepartureTime = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.trainDepartureTime.setFont(font)
        self.trainDepartureTime.setObjectName("trainDepartureTime")
        self.verticalLayout.addWidget(self.trainDepartureTime)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.trainIdLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.trainIdLineEdit.setFont(font)
        self.trainIdLineEdit.setObjectName("trainIdLineEdit")
        self.verticalLayout_2.addWidget(self.trainIdLineEdit)
        self.trainNameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.trainNameLineEdit.setFont(font)
        self.trainNameLineEdit.setObjectName("trainNameLineEdit")
        self.verticalLayout_2.addWidget(self.trainNameLineEdit)
        self.trainSourceLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.trainSourceLineEdit.setFont(font)
        self.trainSourceLineEdit.setObjectName("trainSourceLineEdit")
        self.verticalLayout_2.addWidget(self.trainSourceLineEdit)
        self.trainDestinationLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.trainDestinationLineEdit.setFont(font)
        self.trainDestinationLineEdit.setObjectName("trainDestinationLineEdit")
        self.verticalLayout_2.addWidget(self.trainDestinationLineEdit)
        self.trainFareLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.trainFareLineEdit.setFont(font)
        self.trainFareLineEdit.setObjectName("trainFareLineEdit")
        self.verticalLayout_2.addWidget(self.trainFareLineEdit)
        self.trainClassLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.trainClassLineEdit.setObjectName("trainClassLineEdit")
        self.verticalLayout_2.addWidget(self.trainClassLineEdit)
        self.trainNumberOfSeatsLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.trainNumberOfSeatsLineEdit.setFont(font)
        self.trainNumberOfSeatsLineEdit.setObjectName("trainNumberOfSeatsLineEdit")
        self.verticalLayout_2.addWidget(self.trainNumberOfSeatsLineEdit)
        self.trainJourneyHoursLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.trainJourneyHoursLineEdit.setFont(font)
        self.trainJourneyHoursLineEdit.setObjectName("trainJourneyHoursLineEdit")
        self.verticalLayout_2.addWidget(self.trainJourneyHoursLineEdit)
        self.trainStatusLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.trainStatusLineEdit.setFont(font)
        self.trainStatusLineEdit.setObjectName("trainStatusLineEdit")
        self.verticalLayout_2.addWidget(self.trainStatusLineEdit)
        self.trainDepartureDateLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.trainDepartureDateLineEdit.setFont(font)
        self.trainDepartureDateLineEdit.setObjectName("trainDepartureDateLineEdit")
        self.verticalLayout_2.addWidget(self.trainDepartureDateLineEdit)
        self.trainDepartureTimeLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.trainDepartureTimeLineEdit.setFont(font)
        self.trainDepartureTimeLineEdit.setObjectName("trainDepartureTimeLineEdit")
        self.verticalLayout_2.addWidget(self.trainDepartureTimeLineEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 90, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.okPushButtonForTrainInsertUpdate = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.okPushButtonForTrainInsertUpdate.setFont(font)
        self.okPushButtonForTrainInsertUpdate.setObjectName("okPushButtonForTrainInsertUpdate")
        self.horizontalLayout_3.addWidget(self.okPushButtonForTrainInsertUpdate)
        self.backPushButtonForTrainInsertUpdate = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.backPushButtonForTrainInsertUpdate.setFont(font)
        self.backPushButtonForTrainInsertUpdate.setObjectName("backPushButtonForTrainInsertUpdate")
        self.horizontalLayout_3.addWidget(self.backPushButtonForTrainInsertUpdate)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
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
        self.okPushButtonForTrainInsertUpdate.clicked.connect(lambda: self.evaluate(type))
        self.backPushButtonForTrainInsertUpdate.clicked.connect(lambda: MainWindow.close())

    def evaluate(self, type):
        if type == 'insert':
            if self.trainClassLineEdit.text() !='' and self.trainIdLineEdit.text() != '' and self.trainNameLineEdit.text() != '' \
                    and self.trainSourceLineEdit.text() != '' and self.trainDestinationLineEdit.text() != '' and self.trainFareLineEdit.text() != '' \
                    and self.trainNumberOfSeatsLineEdit.text() != '' and self.trainJourneyHoursLineEdit.text() != '' and self.trainStatusLineEdit.text() != '' \
                    and self.trainDepartureDateLineEdit.text() != '' and self.trainDepartureTimeLineEdit.text() != '':
                trainId = self.trainIdLineEdit.text()
                trainName = self.trainNameLineEdit.text()
                source = self.trainSourceLineEdit.text()
                destination = self.trainDestinationLineEdit.text()
                fare = self.trainFareLineEdit.text()
                numberOfSeats = self.trainNumberOfSeatsLineEdit.text()
                journeyHours = self.trainJourneyHoursLineEdit.text()
                trainStatus = self.trainStatusLineEdit.text()
                departureDate = self.trainDepartureDateLineEdit.text()
                departureTime = self.trainDepartureTimeLineEdit.text()
                train_class = self.trainClassLineEdit.text()
                res = Db.insertTrain(trainId, trainName, source, destination, fare, numberOfSeats, journeyHours,
                                     trainStatus,
                                     departureDate, departureTime,train_class)
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
            if self.trainClassLineEdit.text() !='' and self.trainIdLineEdit.text() != '' and self.trainNameLineEdit.text() != '' \
                    and self.trainSourceLineEdit.text() != '' and self.trainDestinationLineEdit.text() != '' and self.trainFareLineEdit.text() != '' \
                    and self.trainNumberOfSeatsLineEdit.text() != '' and self.trainJourneyHoursLineEdit.text() != '' and self.trainStatusLineEdit.text() != '' \
                    and self.trainDepartureDateLineEdit.text() != '' and self.trainDepartureTimeLineEdit.text() != '':
                trainId = self.trainIdLineEdit.text()
                trainName = self.trainNameLineEdit.text()
                source = self.trainSourceLineEdit.text()
                destination = self.trainDestinationLineEdit.text()
                fare = self.trainFareLineEdit.text()
                numberOfSeats = self.trainNumberOfSeatsLineEdit.text()
                journeyHours = self.trainJourneyHoursLineEdit.text()
                trainStatus = self.trainStatusLineEdit.text()
                departureDate = self.trainDepartureDateLineEdit.text()
                departureTime = self.trainDepartureTimeLineEdit.text()
                train_class=self.trainClassLineEdit.text()
                res = Db.updateTrain(trainId, trainName, source, destination, fare, numberOfSeats, journeyHours,
                                     trainStatus,
                                     departureDate, departureTime,train_class)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Train Details"))
        self.trainInsertUpdateLabel.setText(_translate("MainWindow", "TRAIN INSERT/ UPDATE FORM-"))
        self.trainId.setText(_translate("MainWindow", "Train ID"))
        self.trainName.setText(_translate("MainWindow", "Train Name"))
        self.trainSource.setText(_translate("MainWindow", "Source"))
        self.trainDestination.setText(_translate("MainWindow", "Destination"))
        self.trainFare.setText(_translate("MainWindow", "Fare"))
        self.trainClass.setText(_translate("MainWindow", "Class"))
        self.trainNumberOfSeats.setText(_translate("MainWindow", "Number of seats"))
        self.trainJourneyHours.setText(_translate("MainWindow", "Jouney hours"))
        self.trainStatus.setText(_translate("MainWindow", "Train Status"))
        self.trainDepartureDate.setText(_translate("MainWindow", "Departure Date"))
        self.trainDepartureTime.setText(_translate("MainWindow", "Departure Time"))
        self.okPushButtonForTrainInsertUpdate.setText(_translate("MainWindow", "Ok"))
        self.backPushButtonForTrainInsertUpdate.setText(_translate("MainWindow", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_trainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())