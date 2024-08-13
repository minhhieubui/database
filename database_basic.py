import mysql.connector
from openpyxl import Workbook
from mysql.connector import errorcode

db = mysql.connector.connect(user='root',password='123456',host='127.0.0.1',database= 'data_login')


# code_1 = 'CREATE SCHEMA ` data_login` ;'          # Tạo new_database trong MySQL
# # code_2 = 'DROP DATABASE ` new_database_2` ;'          # Xóa new_database trong MySQL
# code_3 = 'CREATE TABLE ` qlsv1`.`login` (`ID` INT NOT NULL AUTO_INCREMENT,`Fullname` VARCHAR(45) NULL,`Username` VARCHAR(45) NULL,`Email` VARCHAR(45) NULL,`Password` VARCHAR(45) NULL,`Role` VARCHAR(45) NULL,PRIMARY KEY (`ID`));'

# code_4 = "DROP TABLE `new_database`.`food_t`;"
#
# # Đổi tên table
# code_5 = "ALTER TABLE `new_database`.`food`" \
#           " RENAME TO `new_database`.`customer`;"

# # Tìm kiếm tất cả databases hiện có
# code_6 = 'SHOW DATABASES'

# # Tìm kiếm tất cả table trong database được chọn
# code_7 = 'SHOW TABLES'
#
# # Tìm kiếm dữ liệu trong table
# code_8 = 'SELECT id,age FROM customer'
#
# # Tìm một dữ liệu đơn l
# code_9 = 'SELECT name FROM customer WHERE id = 5'
#
# # Tìm ra một dữ liệu tương tự
# code_10 = 'SELECT * FROM customer WHERE age LIKE "%4%"'



code = 'CREATE SCHEMA `data_login`;'

code1= 'CREATE TABLE `history_access` (Date DATE NOT NULL,`Time` TIME NULL,`Username` VARCHAR(45) NULL,`Role` VARCHAR(45) NULL,PRIMARY KEY (Date));'

code2= 'CREATE TABLE  `login` (ID INT NOT NULL AUTO_INCREMENT,`Fullname` VARCHAR(45) NULL,`Username` VARCHAR(45) NULL,`Email` VARCHAR(45) NULL,`Password` VARCHAR(45) NULL,`Role` VARCHAR(45) NULL,PRIMARY KEY (ID));'

code3= 'CREATE TABLE `data_login`.`history_access` (`Date` DATE NOT NULL,`Time` TIME NULL,`Username` VARCHAR(45) NULL,`Role` VARCHAR(45) NULL);'


code = 'ALTER TABLE `qrcodes_info` DROP PRIMARY KEY;'
# # Lệnh chạy code
# mycursor = db.cursor()
# mycursor.execute(code3)   #make database
#
# # Update db
# db.commit()
