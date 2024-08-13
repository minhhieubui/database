import sys
import mysql.connector
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIntValidator
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget,QPushButton,QFrame,QMessageBox,QTreeWidgetItem
from PyQt5.QtCore import QUrl
from product import Ui_Form_2
from connect_database import ConnectDatabase




class MainWindow_1(QWidget):
    def __init__(self):
        super().__init__()
        self.uic = Ui_Form_2()  # Tạo đối tượng UI
        self.uic.setupUi(self)  # Thiết lập giao diện

        # Create a database connection object
        self.db = ConnectDatabase()

        # Connect UI elements to class variables
        self.qrcode_id = self.uic.lineEdit
        # # Restrict input to integers
        # self.qrcode_id.setValidator(QIntValidator)

        self.location = self.uic.lineEdit_2
        self.quantity = self.uic.lineEdit_3
        self.type = self.uic.lineEdit_4
        self.status = self.uic.lineEdit_5
        self.date = self.uic.lineEdit_6

        self.add_btn = self.uic.add_btn
        self.update_btn = self.uic.update_btn
        self.select_btn = self.uic.select_btn
        self.search_btn = self.uic.search_btn
        self.clear_btn = self.uic.clear_btn
        self.delete_btn = self.uic.delete_btn

        self.result_table = self.uic.tableWidget
        self.result_table.setSortingEnabled(False)
        self.buttons_list = self.uic.function_frame.findChildren(QPushButton)

        # Initialize signal-slot conections
        self.init_signal_slot()

        # Populate the initial data in the table and Type of goods/ Status dropdowns
        self.search_info()
        # self.update_type_status()

    def init_signal_slot(self):
        # Connect buttons to their respective functions
        self.add_btn.clicked.connect(self.add_info)
        self.search_btn.clicked.connect(self.search_info)
        self.clear_btn.clicked.connect(self.clear_form_info)
        self.select_btn.clicked.connect(self.select_info)
        self.update_btn.clicked.connect(self.update_info)
        self.delete_btn.clicked.connect(self.delete_info)

    # def update_type_status(self):
    #     # Function to populate the type and status dropdowns
    #     type_result = self.db.get_all_types()
    #     status_result = self.db.get_all_status()
    #
    #     self.type.clear()
    #     self.status.clear()
    #
    #     type_list =[""]
    #     for item in type_result:
    #         for k,v in item.items():
    #             if v != "":
    #                 type_list.append(v)
    #
    #     status_list = [""]
    #     for item in status_result:
    #         for k,v in item.items():
    #             if v != "":
    #                 status_list.append(v)
    #
    #     if len(type_list) > 1:
    #         self.type.addItem(type_list)
    #
    #     if len(status_list) > 1:
    #         self.status.addItem(status_list)

    def search_info(self):
        # Function to search for qrcode information and populate the table
        # self.update_type_status()
        qrcode_info = self.get_qrcode_info()

        qrcode_result = self.db.search_info(
            qrcode_id=str(qrcode_info["qrcode_id"]),
            location=qrcode_info["location"],
            quantity=qrcode_info["quantity"],
            date=qrcode_info["date"],
            type=qrcode_info["type"],
            status=qrcode_info["status"],
        )

        self.show_data(qrcode_result)





    def add_info(self):
        # Function to add qrcode information
        self.disable_buttons()

        qrcode_info = self.get_qrcode_info()

        if qrcode_info["qrcode_id"] and qrcode_info["location"]:
            check_result = self.check_qrcode_id(qrcode_id=str(qrcode_info["qrcode_id"]))    # Kiểm tra xem đã tồn tại qrcode hay chưa

            if check_result:
                QMessageBox.information(self,"Warning","Please input a new QR Code ID",QMessageBox.StandardButton.Ok)
                self.enable_buttons()
                return

            add_result = self.db.add_info(qrcode_id=str(qrcode_info["qrcode_id"]),
                                          location=qrcode_info["location"],
                                          quantity=qrcode_info["quantity"],
                                          date=qrcode_info["date"],
                                          type=qrcode_info["type"],
                                          status=qrcode_info["status"],
                                          )
            if add_result:
                QMessageBox.information(self,"Warning",f"Add fail:{add_result}, Please try again.",QMessageBox.StandardButton.Ok)

        else:
            QMessageBox.Information(self,"Warning","Please input QR Code ID and location",QMessageBox.StandardButton.Ok)

        self.search_info()
        self.enable_buttons()
    def clear_form_info(self):
        # Function to clear the form
        # self.update_type_status()
        self.qrcode_id.clear()
        self.qrcode_id.setEnabled(True)
        self.location.clear()
        self.quantity.clear()
        self.type.clear()
        self.status.clear()
        self.date.clear()


    # def update_info(self):
    #     # Function to update qrcode information
    #     new_qrcode_info = self.get_qrcode_info()
    #
    #     if new_qrcode_info["qrcode_id"]:
    #         update_result = self.db.update_info(
    #             qrcode_id=str(new_qrcode_info["qrcode_id"]),
    #             location=new_qrcode_info["location"],
    #             quantity=new_qrcode_info["quantity"],
    #             date=new_qrcode_info["date"],
    #             type=new_qrcode_info["type"],
    #             status=new_qrcode_info["status"],
    #         )
    #
    #         if update_result:
    #             QMessageBox.information(self,"Warning", f"Fail to update the information:{update_result}, Please try again.",
    #                                     QMessageBox.StandardButton.Ok)
    #         else:
    #             self.search_info()
    #
    #     else:
    #         QMessageBox.information(self,"Warning", "Please select one qrcode information to update.")
    #
    #
    # def delete_info(self):
    #     # Function to delete qrcode information
    #     select_row = self.result_table.currentRow()     # Nếu không có hàng nào được chọn thì index = -1
    #     if select_row != -1:      # Kiểm tra xem có hàng nào được chọn hay không (!= -1 : tức là có 1 hàng được chọn )
    #         select_option = QMessageBox.warning(self,"Warning", "Are you sure to delete it?",
    #                                             QMessageBox.StandardButton.Ok)
    #         if select_option == QMessageBox.StandardButton.Yes:
    #             qrcode_id = self.result_table.item(select_row,0).text().strip()
    #
    #             delete_result = self.db.delete_info(qrcode=qrcode_id)
    #             if not delete_result:
    #                 self.search_info()
    #             else:
    #                 QMessageBox.information(self,"Warning", f"Fail to delete the information: {delete_result},please try again",
    #                                         QMessageBox.StandardButton.Ok)
    #         else:
    #             select_option == QMessageBox.StandardButton.Cancel
    #             self.search_info()
    #     else:
    #         QMessageBox.information(self,"Warning","Please select one qrcode information to delete",QMessageBox.StandardButton.Ok)
    #
    def delete_info(self):
        select_row = self.result_table.currentRow()
        if select_row != -1:
            select_option = QMessageBox.warning(self, "Warning", "Are you sure to delete it?",
                                                QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
            if select_option == QMessageBox.StandardButton.Ok:
                qrcode_id = self.result_table.item(select_row, 0).text().strip()
                print(f"Deleting QR Code ID: {qrcode_id}")
                delete_result = self.db.delete_info(qrcode_id=qrcode_id)
                print(f"Delete Result: {delete_result}")
                if not delete_result:
                    self.search_info()
                else:
                    QMessageBox.information(self, "Warning",
                                            f"Fail to delete the information: {delete_result}, please try again",
                                            QMessageBox.StandardButton.Ok)
            else:
                self.search_info()
        else:
            QMessageBox.information(self, "Warning", "Please select one qrcode information to delete",
                                    QMessageBox.StandardButton.Ok)

    def update_info(self):
        new_qrcode_info = self.get_qrcode_info()
        print(f"Updating QR Code Info: {new_qrcode_info}")
        if new_qrcode_info["qrcode_id"]:
            update_result = self.db.update_info(
                qrcode_id=str(new_qrcode_info["qrcode_id"]),
                location=new_qrcode_info["location"],
                quantity=new_qrcode_info["quantity"],
                date=new_qrcode_info["date"],
                type=new_qrcode_info["type"],
                status=new_qrcode_info["status"],
            )
            print(f"Update Result: {update_result}")
            if update_result:
                QMessageBox.information(self, "Warning",
                                        f"Fail to update the information: {update_result}, Please try again.",
                                        QMessageBox.StandardButton.Ok)
            else:
                self.search_info()
        else:
            QMessageBox.information(self, "Warning", "Please select one qrcode information to update.")

    def select_info(self):
        # Function to select and populate student information in the form
        select_row = self.result_table.currentRow()
        if select_row != -1:      # Nếu có hàng được chọn
            self.qrcode_id.setEnabled(False)
            qrcode_id = self.result_table.item(select_row,0).text().strip()
            location = self.result_table.item(select_row, 1).text().strip()
            quantity = self.result_table.item(select_row, 2).text().strip()
            type = self.result_table.item(select_row, 3).text().strip()
            status = self.result_table.item(select_row, 4).text().strip()
            date = self.result_table.item(select_row, 5).text().strip()

            self.qrcode_id.setText(qrcode_id)
            self.location.setText(location)
            self.quantity.setText(quantity)
            self.type.setText(type)
            self.status.setText(status)
            self.date.setText(date)

        else:
            QMessageBox.information(self,"Warning", "Please select one qrcode information",
                                    QMessageBox.StandardButton.Ok)


    def disable_buttons(self):
        # Disable all the buttons
        for button in self.buttons_list:
            button.setDisabled(True)

    def enable_buttons(self):
        # enable all the buttons
        for button in self.buttons_list:
            button.setDisabled(False)

    def get_qrcode_info(self):
        # Function to retrieve qrcode information from the form
        qrcode_id = self.qrcode_id.text().strip()
        location = self.location.text().strip()
        quantity = self.quantity.text().strip()
        date = self.date.text().strip()
        type = self.type.text().strip()
        status = self.status.text().strip()

        qrcode_info = {
            "qrcode_id": qrcode_id,
            "location": location,
            "quantity": quantity,
            "date": date,
            "type": type,
            "status": status,
        }

        return qrcode_info

    def check_qrcode_id(self,qrcode_id):
        # Function to check if a qrcode_id already exists
        result = self.db.search_info(qrcode_id=qrcode_id)

        return result

    def show_data(self,result):    # Hiển thị dữ liệu trong bảng kết quả
        # Function to populate the table with qrcode information
        if result:
            self.result_table.setRowCount(0)
            self.result_table.setRowCount(len(result))

            for row, info in enumerate(result):
                info_list =[
                    info["qrcode"],
                    info["location"],
                    info["quantity"],
                    info["type"],
                    info["status"],
                    info["date"],
                ]

                for column, item in enumerate(info_list):
                    cell_item = QTableWidgetItem(str(item))
                    self.result_table.setItem(row,column,cell_item)
        else:
            self.result_table.setRowCount(0)
            return


if __name__ == "__main__":
    # Chạy ứng dụng
    app = QApplication(sys.argv)
    main_win = MainWindow_1()
    main_win.show()
    sys.exit(app.exec())


    # def show_data(self):
    #     try:
    #         # clear error on the screen
    #         self.uic.textEdit_data.setText('')
    #
    #         # read text from combobox database
    #         choose_database = self.uic.comboBox_choose_database.currentText()
    #         print(choose_database)
    #
    #         # real text from comboBox table
    #         choose_table = self.uic.comboBox_choose_table.currentText()
    #         print(choose_table)
    #
    #         # command to choose table custom
    #         code_8 = 'SELECT * FROM {}'.format(choose_table)
    #
    #         # Lệnh chạy code
    #         mycursor = db.cursor()  # create mycursor
    #         mycursor.execute(code_8)  # execute command
    #         result = mycursor.fetchall()  # result
    #         print(result)
    #
    #         # Update db
    #         db.commit()
    #
    #         # Load dữ liệu lên
    #         a = 0
    #         for row in result:
    #             a = len(row)
    #             self.uic.tableWidget.setRowCount(len(result))  # Tạo table với số hàng
    #             self.uic.tableWidget.setColumnCount(a)  # Tạo table với số cột
    #
    #         # Fill data to tabWidget
    #         for row_number, row_data in enumerate(result):
    #             for column_number, data in enumerate(row_data):
    #                 self.uic.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
    #
    #     except:
    #         self.uic.textEdit_data.setText("no data")
    #         print("no data")
    #
    #
    # def save_data(self):
    #     # Tìm ra tọa độ của item cần thay thế
    #     currentItems = 0
    #     for currentItems in self.uic.tableWidget.selectedItems():
    #         print("row: ", currentItems.row())
    #         print("column: ", currentItems.column())
    #         print("value: ", currentItems.text())
    #
    #     try:
    #         # connect to MySQL
    #         db = mysql.connector.connect(user='root', password='123456', host='127.0.0.1', database='qlsv1')
    #
    #         ID_value = self.uic.tableWidget.item(currentItems.row(), 0).text()
    #         print("ID:", ID_value)
    #
    #         # take value
    #         row_val = currentItems.text()
    #         row_po = ID_value
    #
    #         if currentItems.column() == 2:
    #             sql = "UPDATE `sinh_vien` SET `age`= %s WHERE `ID` = %s"
    #             val = (row_val, row_po)
    #             mycursor = db.cursor()
    #             mycursor.execute(sql, val)
    #             db.commit()
    #             print(mycursor.rowcount, "record(s) affected")
    #
    #         if currentItems.column() == 1:
    #             sql = "UPDATE `sinh_vien` SET `age`= %s WHERE `ID` = %s"
    #             val = (row_val, row_po)
    #             mycursor = db.cursor()
    #             mycursor.execute(sql, val)
    #             db.commit()
    #             print(mycursor.rowcount, "record(s) affected")
    #     except:
    #         print("no data")