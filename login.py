# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(421, 551)
        self.Background = QtWidgets.QStackedWidget(Form)
        self.Background.setGeometry(QtCore.QRect(0, 0, 421, 551))
        self.Background.setStyleSheet("border-radius:10px;")
        self.Background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Background.setObjectName("Background")
        self.Login_page = QtWidgets.QWidget()
        self.Login_page.setStyleSheet("#Login_page{\n"
"background-color: rgb(85, 85, 255);\n"
"border:none;\n"
"border-radius:15px;\n"
"}")
        self.Login_page.setObjectName("Login_page")
        self.frame = QtWidgets.QFrame(self.Login_page)
        self.frame.setGeometry(QtCore.QRect(20, 60, 171, 131))
        self.frame.setStyleSheet("border-image: url(:/pic_login/pic_login.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.Login_page)
        self.frame_2.setGeometry(QtCore.QRect(10, 210, 351, 151))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.line_user = QtWidgets.QLineEdit(self.frame_2)
        self.line_user.setGeometry(QtCore.QRect(10, 10, 263, 35))
        self.line_user.setMinimumSize(QtCore.QSize(0, 35))
        self.line_user.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.line_user.setFont(font)
        self.line_user.setStyleSheet("border-radius:10px;")
        self.line_user.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.line_user.setClearButtonEnabled(True)
        self.line_user.setObjectName("line_user")
        self.line_password = QtWidgets.QLineEdit(self.frame_2)
        self.line_password.setGeometry(QtCore.QRect(10, 60, 263, 35))
        self.line_password.setMinimumSize(QtCore.QSize(0, 35))
        self.line_password.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.line_password.setFont(font)
        self.line_password.setStyleSheet("border-radius:10px;")
        self.line_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_password.setClearButtonEnabled(True)
        self.line_password.setObjectName("line_password")
        self.checkBox_show_pass = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_show_pass.setGeometry(QtCore.QRect(160, 110, 172, 25))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.checkBox_show_pass.setFont(font)
        self.checkBox_show_pass.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"color:rgb(255, 255, 255)")
        self.checkBox_show_pass.setObjectName("checkBox_show_pass")
        self.frame_3 = QtWidgets.QFrame(self.Login_page)
        self.frame_3.setGeometry(QtCore.QRect(10, 390, 351, 111))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.login_button = QtWidgets.QToolButton(self.frame_3)
        self.login_button.setEnabled(True)
        self.login_button.setGeometry(QtCore.QRect(20, 30, 120, 36))
        self.login_button.setMinimumSize(QtCore.QSize(120, 35))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.login_button.setFont(font)
        self.login_button.setStyleSheet("QToolButton{\n"
"background-color:rgb(85, 170, 255);\n"
"border-radius:10px;\n"
"border:none;}\n"
"QToolButton::hover{\n"
"background-color:rgb(30, 100, 255);\n"
"}\n"
"")
        self.login_button.setShortcut("")
        self.login_button.setObjectName("login_button")
        self.toolButton_clik_for_sign = QtWidgets.QToolButton(self.frame_3)
        self.toolButton_clik_for_sign.setGeometry(QtCore.QRect(10, 80, 168, 27))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.toolButton_clik_for_sign.setFont(font)
        self.toolButton_clik_for_sign.setStyleSheet("QToolButton{background-color: rgb(85, 0, 255,0);\n"
"color:rgb(255, 255, 255);\n"
"font-size:15px;}\n"
"QToolButton:hover{color:rgb(85, 255, 255);}")
        self.toolButton_clik_for_sign.setObjectName("toolButton_clik_for_sign")
        self.pushButton_close = QtWidgets.QPushButton(self.Login_page)
        self.pushButton_close.setGeometry(QtCore.QRect(370, 20, 35, 35))
        self.pushButton_close.setMaximumSize(QtCore.QSize(35, 35))
        self.pushButton_close.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color:rgb(255, 255, 255);\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"\n"
"")
        self.pushButton_close.setObjectName("pushButton_close")
        self.Background.addWidget(self.Login_page)
        self.Register_page = QtWidgets.QWidget()
        self.Register_page.setStyleSheet("#Register_page{\n"
"background-color: rgb(85, 85, 255);\n"
"border:none;\n"
"border-radius:15px;\n"
"}")
        self.Register_page.setObjectName("Register_page")
        self.frame_4 = QtWidgets.QFrame(self.Register_page)
        self.frame_4.setGeometry(QtCore.QRect(40, 30, 361, 91))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.pushButton_close_1 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_close_1.setGeometry(QtCore.QRect(320, 0, 35, 35))
        self.pushButton_close_1.setMaximumSize(QtCore.QSize(35, 35))
        self.pushButton_close_1.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color:rgb(255, 255, 255);\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"\n"
"")
        self.pushButton_close_1.setObjectName("pushButton_close_1")
        self.label_register = QtWidgets.QLabel(self.frame_4)
        self.label_register.setGeometry(QtCore.QRect(110, 40, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_register.setFont(font)
        self.label_register.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_register.setObjectName("label_register")
        self.frame_5 = QtWidgets.QFrame(self.Register_page)
        self.frame_5.setGeometry(QtCore.QRect(40, 140, 331, 211))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.line_user_1 = QtWidgets.QLineEdit(self.frame_5)
        self.line_user_1.setGeometry(QtCore.QRect(30, 70, 263, 35))
        self.line_user_1.setMinimumSize(QtCore.QSize(0, 35))
        self.line_user_1.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.line_user_1.setFont(font)
        self.line_user_1.setStyleSheet("border-radius:10px;")
        self.line_user_1.setClearButtonEnabled(True)
        self.line_user_1.setObjectName("line_user_1")
        self.line_password_1 = QtWidgets.QLineEdit(self.frame_5)
        self.line_password_1.setGeometry(QtCore.QRect(30, 120, 263, 35))
        self.line_password_1.setMinimumSize(QtCore.QSize(0, 35))
        self.line_password_1.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.line_password_1.setFont(font)
        self.line_password_1.setStyleSheet("border-radius:10px;")
        self.line_password_1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_password_1.setClearButtonEnabled(True)
        self.line_password_1.setObjectName("line_password_1")
        self.line_email = QtWidgets.QLineEdit(self.frame_5)
        self.line_email.setGeometry(QtCore.QRect(30, 170, 263, 35))
        self.line_email.setMinimumSize(QtCore.QSize(0, 35))
        self.line_email.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.line_email.setFont(font)
        self.line_email.setStyleSheet("border-radius:10px;")
        self.line_email.setText("")
        self.line_email.setClearButtonEnabled(True)
        self.line_email.setObjectName("line_email")
        self.line_fullname = QtWidgets.QLineEdit(self.frame_5)
        self.line_fullname.setGeometry(QtCore.QRect(30, 20, 263, 35))
        self.line_fullname.setMinimumSize(QtCore.QSize(0, 35))
        self.line_fullname.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.line_fullname.setFont(font)
        self.line_fullname.setStyleSheet("border-radius:10px;")
        self.line_fullname.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_fullname.setClearButtonEnabled(True)
        self.line_fullname.setObjectName("line_fullname")
        self.frame_6 = QtWidgets.QFrame(self.Register_page)
        self.frame_6.setGeometry(QtCore.QRect(30, 400, 341, 171))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.toolButton_account = QtWidgets.QToolButton(self.frame_6)
        self.toolButton_account.setGeometry(QtCore.QRect(10, 100, 325, 27))
        self.toolButton_account.setStyleSheet("QToolButton{background-color: rgb(85, 0, 255,0);\n"
"color:rgb(255, 255, 255);\n"
"font-size:15px;}\n"
"QToolButton:hover{color:rgb(85, 255, 255);}")
        self.toolButton_account.setObjectName("toolButton_account")
        self.toolButton_sign_up = QtWidgets.QToolButton(self.frame_6)
        self.toolButton_sign_up.setEnabled(True)
        self.toolButton_sign_up.setGeometry(QtCore.QRect(40, 50, 261, 36))
        self.toolButton_sign_up.setMinimumSize(QtCore.QSize(120, 35))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.toolButton_sign_up.setFont(font)
        self.toolButton_sign_up.setStyleSheet("QToolButton{\n"
"background-color: rgb(85, 255, 255);\n"
"border-radius:10px;\n"
"border:none;}\n"
"QToolButton::hover{\n"
"background-color:rgb(30, 100, 255);\n"
"}\n"
"")
        self.toolButton_sign_up.setShortcut("")
        self.toolButton_sign_up.setObjectName("toolButton_sign_up")
        self.comboBox_admin = QtWidgets.QComboBox(self.frame_6)
        self.comboBox_admin.setGeometry(QtCore.QRect(130, 10, 73, 22))
        self.comboBox_admin.setStyleSheet("background-color: rgb(255, 255, 255,200);")
        self.comboBox_admin.setObjectName("comboBox_admin")
        self.Background.addWidget(self.Register_page)

        self.retranslateUi(Form)
        self.Background.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.line_user.setPlaceholderText(_translate("Form", "Username"))
        self.line_password.setPlaceholderText(_translate("Form", "Password"))
        self.checkBox_show_pass.setText(_translate("Form", "Show the Password"))
        self.login_button.setText(_translate("Form", "Log In"))
        self.toolButton_clik_for_sign.setText(_translate("Form", "Click Here For Sign Up "))
        self.pushButton_close.setText(_translate("Form", "X"))
        self.pushButton_close_1.setText(_translate("Form", "X"))
        self.label_register.setText(_translate("Form", "REGISTER"))
        self.line_user_1.setPlaceholderText(_translate("Form", "Username"))
        self.line_password_1.setPlaceholderText(_translate("Form", "Password"))
        self.line_email.setPlaceholderText(_translate("Form", "Email"))
        self.line_fullname.setPlaceholderText(_translate("Form", "Fullname"))
        self.toolButton_account.setText(_translate("Form", "Already Have an Account? Click Here to Log In"))
        self.toolButton_sign_up.setText(_translate("Form", "SIGN UP"))

import pic_login


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
