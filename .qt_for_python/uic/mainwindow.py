# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\Python Projects\Python GUI Projects\PyQt5 Projects\PyQt5 Password Generator\src\ui\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(912, 468)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(912, 468))
        MainWindow.setMaximumSize(QtCore.QSize(912, 468))
        MainWindow.setStyleSheet("QMainWindow, QWidget {\n"
"    background-color: rgb(31, 31, 31);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(900, 0))
        self.frame.setSizeIncrement(QtCore.QSize(971, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 300))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label = QtWidgets.QLabel(self.frame_5)
        self.label.setGeometry(QtCore.QRect(40, 50, 471, 51))
        self.label.setMaximumSize(QtCore.QSize(10000, 80))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"    letter-spacing: 2px\n"
"}")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 381, 61))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel { \n"
"    color: rgb(159, 159, 159);\n"
"    letter-spacing: 2px;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.frame_4 = QtWidgets.QFrame(self.frame_5)
        self.frame_4.setGeometry(QtCore.QRect(640, -10, 131, 131))
        self.frame_4.setStyleSheet("QFrame { \n"
"    background-color: rgb(255, 35, 15);\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setGeometry(QtCore.QRect(770, 120, 131, 131))
        self.frame_6.setStyleSheet("QFrame { \n"
"    background-color: rgb(55, 202, 255);\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.length_slider = QtWidgets.QSlider(self.frame_5)
        self.length_slider.setGeometry(QtCore.QRect(40, 220, 207, 22))
        self.length_slider.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: none;\n"
"    height: 3px; \n"
"    background:rgb(81, 81, 81);\n"
"    margin: 2px 0;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(47, 182, 255);\n"
"    width: 10px;    \n"
"    margin: -7px 0; \n"
"    border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover{\n"
"    background-color: rgb(34, 111, 255)\n"
"}")
        self.length_slider.setMinimum(8)
        self.length_slider.setMaximum(40)
        self.length_slider.setOrientation(QtCore.Qt.Horizontal)
        self.length_slider.setObjectName("length_slider")
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setGeometry(QtCore.QRect(40, 190, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel {\n"
"    color: rgb(175, 175, 175);\n"
"    letter-spacing: 1px;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.include_numbers = QtWidgets.QCheckBox(self.frame_5)
        self.include_numbers.setGeometry(QtCore.QRect(340, 220, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        self.include_numbers.setFont(font)
        self.include_numbers.setStyleSheet("QCheckBox {\n"
"    color: rgb(175, 175, 175);\n"
"    letter-spacing: 1px;\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"   \n"
"     background: rgb(47, 182, 255);\n"
"}\n"
"QCheckBox::indicator:unchecked:hover {\n"
"  \n"
"    background-color: rgb(34, 111, 255);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    \n"
"    image: url(./assets/svg/check.svg);\n"
"    background: rgb(47, 182, 255);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    \n"
"    background-color: rgb(34, 111, 255);\n"
"}\n"
"")
        self.include_numbers.setObjectName("include_numbers")
        self.slider_value_label = QtWidgets.QLabel(self.frame_5)
        self.slider_value_label.setGeometry(QtCore.QRect(260, 220, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        self.slider_value_label.setFont(font)
        self.slider_value_label.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.slider_value_label.setObjectName("slider_value_label")
        self.verticalLayout_2.addWidget(self.frame_5)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_3.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.generate_button = QtWidgets.QPushButton(self.frame_3)
        self.generate_button.setGeometry(QtCore.QRect(40, 20, 207, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(8)
        self.generate_button.setFont(font)
        self.generate_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.generate_button.setWhatsThis("")
        self.generate_button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(79, 158, 255);\n"
"    border: none;\n"
"    color: white;\n"
"    letter-spacing: 1px;\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(34, 111, 255);\n"
"}\n"
"QPushButton::pressed {\n"
"    background-color: rgb(34, 111, 255);\n"
"}")
        self.generate_button.setObjectName("generate_button")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(40, 80, 201, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel {\n"
"    color: rgb(175, 175, 175);\n"
"    letter-spacing: 1px;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.exit_button = QtWidgets.QPushButton(self.frame_3)
        self.exit_button.setGeometry(QtCore.QRect(300, 20, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(8)
        self.exit_button.setFont(font)
        self.exit_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exit_button.setWhatsThis("")
        self.exit_button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(239, 49, 1);\n"
"    border: none;\n"
"    color: white;\n"
"    letter-spacing: 1px;\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(209, 0, 0);\n"
"}\n"
"QPushButton::pressed {\n"
"    background-color: rgb(209, 0, 0);\n"
"}")
        self.exit_button.setObjectName("exit_button")
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.output_edit = QtWidgets.QLineEdit(self.frame_2)
        self.output_edit.setGeometry(QtCore.QRect(40, 10, 431, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        self.output_edit.setFont(font)
        self.output_edit.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.output_edit.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(74, 74, 74);\n"
"    border: none;\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    letter-spacing: 1px;\n"
"    padding: 5px;\n"
"}\n"
"QLineEdit::focus {\n"
"    border-bottom: 1px solid white;\n"
"}")
        self.output_edit.setReadOnly(True)
        self.output_edit.setObjectName("output_edit")
        self.status = QtWidgets.QLabel(self.frame_2)
        self.status.setGeometry(QtCore.QRect(40, 65, 271, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        self.status.setFont(font)
        self.status.setStyleSheet("QLabel#status {\n"
"    color: rgb(17, 255, 0);\n"
"    letter-spacing: 1.3px;\n"
"}\n"
"QLabel#error {\n"
"    color: red;\n"
"    letter-spacing: 1.3px;\n"
"}\n"
"")
        self.status.setObjectName("status")
        self.copy_button = QtWidgets.QPushButton(self.frame_2)
        self.copy_button.setGeometry(QtCore.QRect(480, 11, 41, 41))
        self.copy_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.copy_button.setStyleSheet("")
        self.copy_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("f:\\Python Projects\\Python GUI Projects\\PyQt5 Projects\\PyQt5 Password Generator\\src\\ui\\../assets/svg/clipboard.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.copy_button.setIcon(icon)
        self.copy_button.setIconSize(QtCore.QSize(24, 24))
        self.copy_button.setFlat(True)
        self.copy_button.setObjectName("copy_button")
        self.verticalLayout_2.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password Generator"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Generate Password Which You Want</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "The one and only Password Generator <br> which will help you to be more secure <br> Beacause Your PRIVACY is our PRIORITY"))
        self.length_slider.setToolTip(_translate("MainWindow", "<html><head/><body><p>Change the length of the password by just sliding the slider</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Slide the length of the password"))
        self.include_numbers.setToolTip(_translate("MainWindow", "<html><head/><body><p>Check if you want to include numbers in your password</p></body></html>"))
        self.include_numbers.setText(_translate("MainWindow", "Include Numbers"))
        self.slider_value_label.setText(_translate("MainWindow", "8"))
        self.generate_button.setToolTip(_translate("MainWindow", "<html><head/><body><p>This is a button to generate <span style=\" color:#000000;\">password a</span>ccording to your choice</p></body></html>"))
        self.generate_button.setText(_translate("MainWindow", "Generate Password"))
        self.label_4.setText(_translate("MainWindow", "Generated Password :"))
        self.exit_button.setToolTip(_translate("MainWindow", "<html><head/><body><p>This button will help to <span style=\" font-weight:600;\">exit</span> the Application</p></body></html>"))
        self.exit_button.setText(_translate("MainWindow", "Exit"))
        self.output_edit.setToolTip(_translate("MainWindow", "<html><head/><body><p>The generated password will be shown here</p></body></html>"))
        self.output_edit.setPlaceholderText(_translate("MainWindow", "The Generated Password will be shown here"))
        self.status.setToolTip(_translate("MainWindow", "<html><head/><body><p>Shows the status of the application</p></body></html>"))
        self.status.setText(_translate("MainWindow", "App Loaded Successfully ...."))
        self.copy_button.setToolTip(_translate("MainWindow", "<html><head/><body><p>Copy to Clipboard</p></body></html>"))
