from PyQt5.QtWidgets import(
    QApplication,QWidget,QLabel,QPushButton,QLineEdit,QComboBox,QMessageBox,QDateTimeEdit,QScrollArea,QVBoxLayout,QHBoxLayout
)
import mysql.connector

from PyQt5.QtCore import QDateTime

from PyQt5.QtGui import QMovie

import sys

from PyQt5.QtGui import  QPixmap
from PyQt5.QtGui import QIcon, QPixmap
def load_icon(icon_name):
    return QIcon(icon_name)


class PasswordEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.visibleIcon = load_icon("img/image copy.png")
        self.hiddenIcon = load_icon("img/image.png")

        self.setEchoMode(QLineEdit.Password)
        self.togglepasswordAction = self.addAction(self.visibleIcon, QLineEdit.TrailingPosition)
        self.togglepasswordAction.triggered.connect(self.on_toggle_password_Action)
        self.password_shown = False

    def on_toggle_password_Action(self):
        
        if not self.password_shown:
            self.setEchoMode(QLineEdit.Normal)
            self.password_shown = True
            self.togglepasswordAction.setIcon(self.hiddenIcon)
        else:
            self.setEchoMode(QLineEdit.Password)
            self.password_shown = False
            self.togglepasswordAction.setIcon(self.visibleIcon)


def connect_to_db():
    
    try:
        connection = mysql.connector.connect(     
        host='localhost',
        user='root',
        password='bonu2005',
        database='order_a_taxi'
        )
        if connection.is_connected():
            print("Sucsessfully connected ")
        return connection
    except   mysql.connector.Error as err:
        print(f"Your mistace:{err}")
        return None
#--------------------------------------

db_connection=connect_to_db()
db_cursor=db_connection.cursor()

#--------------------------------------

chooses = open("chooses.css")
chooses = chooses.read()

sug_to_Log_in_or_sign_in_for_driver=open("sug_login_or_signin_for_driver.css")
sug_to_Log_in_or_sign_in_for_driver=sug_to_Log_in_or_sign_in_for_driver.read()

sign_up_for_driver=open("signup_for_driver.css")
sign_up_for_driver=sign_up_for_driver.read()

log_in_for_driver=open("login_for_driver.css")
log_in_for_driver=log_in_for_driver.read()

mainWindowForDriver=open("mainWindowForDriver.css")
mainWindowForDriver=mainWindowForDriver.read()

my_data_for_driver=open("my_data_for_driver.css")
my_data_for_driver=my_data_for_driver.read()

my_orders_for_driver=open("my_orders_for_driver.css")
my_orders_for_driver=my_orders_for_driver.read()

#----------------------------------------

sug_to_Log_in_or_sign_in_for_client=open("sug_login_or_signin_for_client.css")
sug_to_Log_in_or_sign_in_for_client=sug_to_Log_in_or_sign_in_for_client.read()

sign_up_for_client=open("signup_for_client.css")
sign_up_for_client=sign_up_for_client.read()

log_in_for_client=open("login_for_client.css")
log_in_for_client=log_in_for_client.read()

mainWindowForClients=open("mainWindowForClients.css")
mainWindowForClients=mainWindowForClients.read()

call_a_Taxi=open("call_a_Taxi.css")
call_a_Taxi=call_a_Taxi.read()

my_data=open("my_data.css")
my_data=my_data.read()

my_orders=open("my_orders.css")
my_orders=my_orders.read()


class Chooses(QWidget):
    def __init__(self):
        super().__init__()
        self.db_connection = db_connection
        self.db_cursor=db_cursor
        self.setGeometry(400,50,850,740)
        self.setWindowTitle("Choose_one")
        self.chooseOne()
        

    def chooseOne(self):
        
        self.write_label=QLabel(self)
        self.write_label.setText("        Statusingizni tanlang--->")
        self.write_label.setGeometry(30,10,450,60)
        self.write_label.setStyleSheet(chooses)

        self.label = QLabel(self)
        self.label.setGeometry(30, 100, 800, 600)  

        self.movie = QMovie('img/91b6bbe376bec2966cc8e88e0dd804c0.gif')  
        self.label.setMovie(self.movie)
        self.movie.start()  
        self.setStyleSheet(chooses)
            
        self.btn_for_driver=QPushButton(self)
        self.btn_for_driver.setText("Men - taksistman")
        self.btn_for_driver.setGeometry(500,15,150,50)
        self.btn_for_driver.clicked.connect(self.next_stage_for_driver)
        self.btn_for_driver.setStyleSheet(chooses)

        self.btn_for_client=QPushButton(self)
        self.btn_for_client.setText("Men - mijozman")
        self.btn_for_client.setGeometry(680,15,150,50)
        self.btn_for_client.clicked.connect(self.next_stage_for_client)
        self.btn_for_client.setStyleSheet(chooses)

    def next_stage_for_driver(self):

        self.go_to_next_Window=Suggest_to_Log_in_or_sign_in_for_driver()
        self.go_to_next_Window.show()
        self.close()
       
        

    def next_stage_for_client(self):

        self.go_to_next_Window=Suggest_to_Log_in_or_sign_in_for_client()
        self.go_to_next_Window.show()
        self.close()


class Suggest_to_Log_in_or_sign_in_for_driver(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tizimga kirasizmi? yoki royhatdan o'tasizmi?")
        self.setGeometry(400,50,530,830)

        self.image_label = QLabel(self)
        self.image_label.setPixmap(QPixmap("img/6e5dbcd238f26ee7d03ce58867a3f352.jpg"))
        self.image_label.setScaledContents(True)
        self.image_width = 10
        self.image_height =10
        self.image_label.setGeometry(0, 0, self.width(), self.height())

        self.back1=QPushButton(self)
        self.back1.setText("Orqaga")
        self.back1.setGeometry(220,470,100,50)
        self.back1.clicked.connect(self.back)
        self.back1.setStyleSheet(sug_to_Log_in_or_sign_in_for_driver)

        self.log_in_btn=QPushButton(self)
        self.log_in_btn.setText("Tizimga Kirish")
        self.log_in_btn.setGeometry(170,590,200,50)
        self.log_in_btn.clicked.connect(self.next_stage_for_log_in)
        self.log_in_btn.setStyleSheet(sug_to_Log_in_or_sign_in_for_driver)


        self.sign_in_btn=QPushButton(self)
        self.sign_in_btn.setText("Royhatdan o'tish")
        self.sign_in_btn.setGeometry(120,710,300,50)
        self.sign_in_btn.clicked.connect(self.next_stage_for_sign_in)
        self.sign_in_btn.setStyleSheet(sug_to_Log_in_or_sign_in_for_driver)

        
    
    def back(self):
        self.go_to_the_back=Chooses()
        self.go_to_the_back.show()
        self.close()
    

    def next_stage_for_log_in(self):
        self.go_to_the_log_in=Log_in_for_driver()
        self.go_to_the_log_in.show()
        self.close()

    def next_stage_for_sign_in(self):
        self.go_to_the_sign_in=Sign_up_for_driver() 
        self.go_to_the_sign_in.show()
        self.close()

   
class Sign_up_for_driver(QWidget):
    def __init__(self):
        super().__init__()
        self.db_connection = db_connection
        self.db_cursor = db_cursor
        self.setGeometry(400,50,530,830)
        self.setWindowTitle("Taksist uchun royhatdan otish oynasi")
        self.sign_in_for_driver()

    def sign_in_for_driver(self):
        
        self.image_label = QLabel(self)
        self.image_label.setPixmap(QPixmap("img/db97283d9eafe3eb062aa5daf53e6e64.jpg"))
        self.image_label.setScaledContents(True)
        self.image_width = 0
        self.image_height =0
        self.image_label.setGeometry(0, 0, self.width(), self.height())

        self.full_name_line=QLineEdit(self)
        self.full_name_line.setPlaceholderText("Toliq ismingizni kiriting")
        self.full_name_line.setGeometry(110,200,300,50)
        self.full_name_line.setStyleSheet(sign_up_for_driver)

        self.age_line=QLineEdit(self)
        self.age_line.setPlaceholderText("Yoshingizni kiriting ")
        self.age_line.setGeometry(110,260,300,50)
        self.age_line.setStyleSheet(sign_up_for_driver)

        self.gender_line=QComboBox(self)
        self.gender_line.addItems(["Erkak","Ayol","Noaniq"])
        self.gender_line.setGeometry(110,320,300,50)
        self.gender_line.setStyleSheet(sign_up_for_driver)

        self.model_of_car_line=QLineEdit(self)
        self.model_of_car_line.setPlaceholderText("mashinanig modeli")
        self.model_of_car_line.setGeometry(110,380,300,50)
        self.model_of_car_line.setStyleSheet(sign_up_for_driver)

        self.phone_number_line=QLineEdit(self)
        self.phone_number_line.setPlaceholderText("Telefon raqam")
        self.phone_number_line.setGeometry(110,440,300,50)
        self.phone_number_line.setStyleSheet(sign_up_for_driver)

        self.password_line = PasswordEdit(self)
        self.password_line.setPlaceholderText("Parol yarating")
        self.password_line.setGeometry(110, 500, 300, 50)
        self.password_line.setStyleSheet(sign_up_for_driver)


        self.sign_up_btn=QPushButton(self)
        self.sign_up_btn.setGeometry(110,660,300,50)
        self.sign_up_btn.setText("Ro'hatdan o'tish")
        self.sign_up_btn.clicked.connect(self.sign_up_for_driver)
        self.sign_up_btn.setStyleSheet(sign_up_for_driver)

        self.text_label=QLabel(self)
        self.text_label.setText("~~ Sign up ~~")
        self.text_label.setGeometry(130,100,450,50)
        self.text_label.setStyleSheet(sign_up_for_driver)
        
        self.back1=QPushButton(self)
        self.back1.setText(">>>")
        self.back1.setGeometry(100,50,60,50)
        self.back1.clicked.connect(self.back)
        self.back1.setStyleSheet(sign_up_for_driver)
    
    def back(self):
        self.go_to_the_back=Suggest_to_Log_in_or_sign_in_for_driver()
        self.go_to_the_back.show()
        self.close()
    def is_strong_password(self, password):
        
        min_length = 6
        if len(password) < min_length:
            return False, "Parol kamida 6 ta belgidan iborat bo'lishi kerak."
        return True, "Parol kuchli."
    
    def show_error_message(self, message):
        
        """ertyuiop"""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec_()

    def sign_up_for_driver(self):

        if not self.full_name_line.text() or not self.age_line.text() or not self.model_of_car_line.text() or not self.phone_number_line.text() or not self.password_line.text():
            self.show_error_message("Iltimos hamma bo'sh joylarni toldiring")
        else:    
            self.name_catch=self.full_name_line.text()
            self.age_catch=self.age_line.text()
            self.gender_catch=self.gender_line.currentText()
            self.model_of_car_catch=self.model_of_car_line.text()
            self.phone_number_catch=self.phone_number_line.text()
            self.password_catch=self.password_line.text()
            is_strong, message = self.is_strong_password(self.password_catch)
            if not is_strong:
                QMessageBox.warning(self, "Xato", message)
                return 
            

            sql_query="""
            INSERT INTO for_driver(name,age,gender,model_of_car,phone_number,password)
            VALUES (%s,%s,%s,%s,%s,%s)
            """
            values=(self.name_catch,self.age_catch,self.gender_catch,self.model_of_car_catch,self.phone_number_catch,self.password_catch)
            print(values)
            
            try:
                self.db_cursor.execute(sql_query, values)
                self.db_connection.commit()
                QMessageBox.information(self,"Muvaffaqiyar","Malumot muvaffaqiyatli saqlandi!")
                print("Data stored successfully!")
            except mysql.connector.Error as err:
                QMessageBox.warning(self,"xato",f"xato:{err}")
                print(f"Error: {err}")
            
            self.go_to_the_MeinWindowForDrivers=MainWindowForDriver()
            self.go_to_the_MeinWindowForDrivers.show()
            self.close()         


class Log_in_for_driver(QWidget):
    def __init__(self):
        super().__init__()
        self.db_connection = db_connection
        self.db_cursor = db_cursor
        self.setWindowTitle("Tizimga kirish")
        self.setGeometry(400,50,530,830)
        self.lines_to_enter()

    def lines_to_enter(self):
        
        self.image_label = QLabel(self)
        self.image_label.setPixmap(QPixmap("img/db97283d9eafe3eb062aa5daf53e6e64.jpg"))
        self.image_label.setScaledContents(True)
        self.image_width = 0
        self.image_height =0
        self.image_label.setGeometry(0, 0, self.width(), self.height())

        self.phone_number_line=QLineEdit(self)
        self.phone_number_line.setPlaceholderText("Telefon raqami")
        self.phone_number_line.setGeometry(120,320,300,50)
        self.phone_number_line.setStyleSheet(log_in_for_driver)

        self.password_line=PasswordEdit(self)
        self.password_line.setPlaceholderText("Parol kiriting")
        self.password_line.setGeometry(120,420,300,50)
        self.password_line.setStyleSheet(log_in_for_driver)

        self.enter_btn=QPushButton(self)
        self.enter_btn.setText("Kirish")
        self.enter_btn.setGeometry(120,620,300,50)
        self.enter_btn.clicked.connect(self.check_lines)
        self.enter_btn.setStyleSheet(log_in_for_driver)

        self.text_label=QLabel(self)
        self.text_label.setText("~~ Log in ~~")
        self.text_label.setGeometry(150,200,450,50)
        self.text_label.setStyleSheet(log_in_for_driver)
        
        self.back1=QPushButton(self)
        self.back1.setText("<<<")
        self.back1.setGeometry(100,50,60,50)
        self.back1.clicked.connect(self.back)
        self.back1.setStyleSheet(log_in_for_driver)
    
    def back(self):
        self.go_to_the_back=Suggest_to_Log_in_or_sign_in_for_driver()
        self.go_to_the_back.show()
        self.close()

    def check_lines(self):

        self.phone_number_check=self.phone_number_line.text()
        self.password_check=self.password_line.text()
        sql_query="Select *from for_driver where phone_number =%s and password=%s"
        values=(self.phone_number_check,self.password_check)
        self.db_cursor.execute(sql_query,values)
        result=self.db_cursor.fetchone()
        if result:
            self.go_to_the_MainWindowForDriver=MainWindowForDriver(result[0])
            self.go_to_the_MainWindowForDriver.show()
            self.close()
        else:
            QMessageBox.warning(self,"Xato","Foydalanuvchi nomi yoki parol noto'g'ri!")


class MainWindowForDriver(QWidget):
    def __init__(self,name):
        super().__init__()
        self.setGeometry(400,50,700,600)
        self.setWindowTitle("Taksistning asosiy oynasi")
        self.drivername=name
        print(self.drivername)
        self.buttons_for_drivers()

    def buttons_for_drivers(self):

        self.label = QLabel(self)
        self.label.setGeometry(0, 0, 900, 600)  

        self.movie = QMovie('videos/63b8a20773677516d1409061d4bba25c copy.gif')  
        self.label.setMovie(self.movie)
        self.movie.start()  
        self.setStyleSheet(chooses)

        self.my_data_btn=QPushButton(self)
        self.my_data_btn.setText("Ma'lumotlarim")
        self.my_data_btn.setGeometry(60,500,280,50)
        self.my_data_btn.clicked.connect(self.my_data)
        self.my_data_btn.setStyleSheet(mainWindowForDriver)
        
        self.my_orders_btn=QPushButton(self)
        self.my_orders_btn.setText("Buyurtmalar")
        self.my_orders_btn.setGeometry(350,500,280,50)
        self.my_orders_btn.clicked.connect(self.my_orders)
        self.my_orders_btn.setStyleSheet(mainWindowForDriver)

        self.back1=QPushButton(self)
        self.back1.setText("Orqaga")
        self.back1.setGeometry(80,350,100,50)
        self.back1.clicked.connect(self.back)
    
    def back(self):
        self.go_to_the_back=Chooses()
        self.go_to_the_back.show()
        self.close()

    def my_data(self):
        
        self.go_to_the_my_data=My_data_for_driver(self.drivername)
        self.go_to_the_my_data.show()
        self.close()
    
    def my_orders(self):
        self.go_to_the_my_orders=My_orders_for_driver(self.drivername)
        self.go_to_the_my_orders.show()
        self.close()


class My_data_for_driver(QWidget):
    def __init__(self, name):
        super().__init__()
        self.db_connection = db_connection
        self.db_cursor = db_cursor
        self.drivername = name 
  
        self.setWindowTitle("Ma'lumotlarim")
        self.setGeometry(400, 50, 640, 600)
        self.display_data()

        
    def display_data(self):
        
        sql_query = "SELECT name,age,gender,model_of_car,phone_number FROM for_driver WHERE name = %s"
        values = (self.drivername,) 
        
        try:
            self.db_cursor.execute(sql_query, values)
            data = self.db_cursor.fetchone()

            if data:
                name,age,gender,model_of_car, phone_number = data
                info_label = QLabel(f"Ismingiz: {name}\nYoshingiz: {age}\nJinsingiz: {gender}\nMoshinangiz_Modeli: {model_of_car}\nTelefon raqamingiz: {phone_number}", self)
                info_label.setGeometry(50, 0, 535, 550)  
                info_label.setStyleSheet(my_data_for_driver)
            else:
                QMessageBox.warning(self, "Ma'lumotlar topilmadi", "Foydalanuvchi ma'lumotlari topilmadi.")
        except mysql.connector.Error as err:
            QMessageBox.warning(self, "Xato", f"xato: {err}")
        
        self.back1=QPushButton(self)
        self.back1.setText("Orqaga")
        self.back1.setGeometry(250,390,100,50)
        self.back1.clicked.connect(self.back)
        self.back1.setStyleSheet(my_data_for_driver)
    
    def back(self):
        self.go_to_the_back=MainWindowForDriver(self.drivername)
        self.go_to_the_back.show()
        self.close()

class My_orders_for_driver(QWidget):
    def __init__(self,name):
        super().__init__()
        self.db_connection = db_connection
        self.db_cursor = db_cursor
        self.drivername=name
        self.setGeometry(400, 50, 530, 630)
        self.setWindowTitle("Taksistning asosiy oynasi")
        
        self.orders_label = QLabel(self)
        self.orders_label.setGeometry(20, 50, 400, 400)  

        self.load_orders()  
    
    def load_orders(self):

        try:
            sql_query = "SELECT id, from_where, where_to, date_of_order FROM orders WHERE status_of_order = %s order by id desc"
            values = ('Kutyapti',)
            self.db_cursor.execute(sql_query, values)
            orders = self.db_cursor.fetchall()
            self.layout=QVBoxLayout()
            self.scroll_area=QScrollArea()
            self.scroll_area.setWidgetResizable(True)
            self.scroll_widget=QWidget()
            self.scroll_layout=QVBoxLayout(self.scroll_widget)

            for order in orders:
                order_id, from_where, where_to, date_of_order = order
                order_layout = QHBoxLayout()
               
                button = QLabel(f"{from_where}-{where_to} ({date_of_order})")
                button.setStyleSheet(my_orders_for_driver)
                self.btn=QPushButton(self)
                self.btn.setText("Qabul qilish")
                
                self.btn.setProperty("order_id", order_id)  
                self.btn.clicked.connect(self.change_waiting_to_close)
                self.btn.setStyleSheet(my_orders_for_driver)
                order_layout.addWidget(button)
                order_layout.addWidget(self.btn)

                self.scroll_layout.addLayout(order_layout)
                

            self.scroll_area.setWidget(self.scroll_widget)
            self.layout.addWidget(self.scroll_area)
            self.setLayout(self.layout)
            self.back1=QPushButton(self)
            self.back1.setText("Orqaga")
            self.back1.setGeometry(200,440,100,50)
            self.back1.clicked.connect(self.back)
            self.back1.setStyleSheet(my_orders_for_driver)
            
            
            
            self.layout.addWidget(self.back1)
            self.setLayout(self.layout)

            if orders:
                orders_list = "\n".join([f"{order[0]} dan {order[1]} ga ({order[2]})" for order in orders])
                self.orders_label.setText(orders_list)
            else:
                self.orders_label.setText("Hozircha buyurtmalar yo'q.")
        except mysql.connector.Error as err:
            QMessageBox.warning(self, "Xato", f"Buyurtmalarni olishda xato: {err}")

        
          
    
    def back(self):
        self.go_to_the_back=MainWindowForDriver(self.drivername)
        self.go_to_the_back.show()
        self.close()

    def change_waiting_to_close(self):

        self.btn = self.sender() 
        self.order_id = self.btn.property("order_id")
        
          

        if self.order_id is not None:
            sql_query = "UPDATE orders SET status_of_order='Yopilgan' WHERE id=%s"
            self.db_cursor.execute(sql_query, (self.order_id,))
            self.db_connection.commit()
            QMessageBox.information(self, "Tabriklaymiz", "Buyurtma rasmiylashtirildi")
            self.load_orders()  
        else:
            QMessageBox.warning(self, "Xato", "ID buyurtma topilmadi")
        self.btn

#------------------------------------------------------------------------------------


class Suggest_to_Log_in_or_sign_in_for_client(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tizimga kirasizmi? yoki royhatdan o'tasizmi?")
        self.setGeometry(400,50,530,830)

        self.image_label = QLabel(self)
        self.image_label.setPixmap(QPixmap("img/6e5dbcd238f26ee7d03ce58867a3f352.jpg"))
        self.image_label.setScaledContents(True)
        self.image_width = 10
        self.image_height =10
        self.image_label.setGeometry(0, 0, self.width(), self.height())

        self.back1=QPushButton(self)
        self.back1.setText("Orqaga")
        self.back1.setGeometry(220,470,100,50)
        self.back1.clicked.connect(self.back)
        self.back1.setStyleSheet(sug_to_Log_in_or_sign_in_for_client)
    
        self.log_in_btn=QPushButton(self)
        self.log_in_btn.setText("Tizimga Kirish")
        self.log_in_btn.setGeometry(170,590,200,50)
        self.log_in_btn.clicked.connect(self.next_stage_for_log_in)
        self.log_in_btn.setStyleSheet(sug_to_Log_in_or_sign_in_for_client)

        self.sign_in_btn=QPushButton(self)
        self.sign_in_btn.setText("Royhardan o'tish")
        self.sign_in_btn.setGeometry(120,710,300,50)
        self.sign_in_btn.clicked.connect(self.next_stage_for_sign_in)
        self.sign_in_btn.setStyleSheet(sug_to_Log_in_or_sign_in_for_client)

        
    def back(self):
        self.go_to_the_back=Chooses()
        self.go_to_the_back.show()
        self.close()

    def next_stage_for_log_in(self):

        self.go_to_the_log_in=Log_in_for_client()
        self.go_to_the_log_in.show()
        self.close()

    def next_stage_for_sign_in(self):

        self.go_to_the_sign_in=Sign_up_for_client() 
        self.go_to_the_sign_in.show()
        self.close()


class Sign_up_for_client(QWidget):
    def __init__(self):
        super().__init__()
        self.db_connection = db_connection
        self.db_cursor = db_cursor
        self.setGeometry(400,50,530,830)
        self.setWindowTitle("Mijoz uchun royhatdan otish oynasi")
        self.sign_up_for_client()

    def sign_up_for_client(self):
        
        self.image_label = QLabel(self)
        self.image_label.setPixmap(QPixmap("img/db97283d9eafe3eb062aa5daf53e6e64.jpg"))
        self.image_label.setScaledContents(True)
        self.image_width = 0
        self.image_height =0
        self.image_label.setGeometry(0, 0, self.width(), self.height())


        self.name_line=QLineEdit(self)
        self.name_line.setPlaceholderText("ismingizni kiriting")
        self.name_line.setGeometry(110,200,300,50)
        self.name_line.setStyleSheet(sign_up_for_client)

        self.phone_number_line=QLineEdit(self)
        self.phone_number_line.setPlaceholderText("Telefon raqamizni kiriting ")
        self.phone_number_line.setGeometry(110,260,300,50)
        self.phone_number_line.setStyleSheet(sign_up_for_client)

        self.password_line = PasswordEdit(self)
        self.password_line.setPlaceholderText("Parol yarating")
        self.password_line.setGeometry(110, 320, 300, 50)
        self.password_line.setStyleSheet(sign_up_for_client)

        self.sign_up_btn=QPushButton(self)
        self.sign_up_btn.setText("Ro'yxatdan o'tish")
        self.sign_up_btn.setGeometry(110,660,300,50)
        self.sign_up_btn.clicked.connect(self.sign_up_for_client_check)
        self.sign_up_btn.setStyleSheet(sign_up_for_client)

        self.text_label=QLabel(self)
        self.text_label.setText("~~ Sign up ~~")
        self.text_label.setGeometry(130,100,450,50)
        self.text_label.setStyleSheet(sign_up_for_client)

        self.back1=QPushButton(self)
        self.back1.setText("<<<")
        self.back1.setGeometry(100,50,60,50)
        self.back1.clicked.connect(self.back)
        self.back1.setStyleSheet(sign_up_for_client)
    
    def back(self):
        self.go_to_the_back=Suggest_to_Log_in_or_sign_in_for_client()
        self.go_to_the_back.show()
        self.close()

    def is_strong_password(self, password):

        min_length = 6
        if len(password) < min_length:
            return False, "Parol kamida 6 ta belgidan iborat bo'lishi kerak."
        return True, "Parol kuchli."
    
    def show_error_message(self, message):
        """Функция для вывода сообщения  ошибке"""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec_()

    def sign_up_for_client_check(self):

        if not self.name_line.text() or not self.phone_number_line.text() or not self.password_line.text():
            self.show_error_message("Iltimos hamma bosh joylarni to'ldiring ")
        else:  
            self.name_catch=self.name_line.text()
            self.phone_number_catch=self.phone_number_line.text()
            self.password_catch=self.password_line.text()
            is_strong, message = self.is_strong_password(self.password_catch)
            if not is_strong:
                QMessageBox.warning(self, "Xato", message)
                return 
            
            sql_query="""
            INSERT INTO for_client(name,phone_number,password)
            VALUES(%s,%s,%s)
            """
            values=(self.name_catch,self.phone_number_catch,self.password_catch)
            try:
                self.db_cursor.execute(sql_query,values)
                self.db_connection.commit()
                QMessageBox.information(self,"Muvaffaqiyar","Malumot muvaffaqiyatli saqlandi!")
                self.go_to_the_MeinWindowForClients=MainWindowForClients(self.name_catch)
                self.go_to_the_MeinWindowForClients.show()
            except mysql.connector.Error as err:
                QMessageBox.warning(self,"xato",f"xato:{err}")


class Log_in_for_client(QWidget):
    def __init__(self):
        super().__init__()
        self.db_connection = db_connection
        self.db_cursor = db_cursor
        self.setWindowTitle("Tizimga kirish")
        self.setGeometry(400,50,530,830)
        self.lines_to_enter()

    def lines_to_enter(self):
        
        self.image_label = QLabel(self)
        self.image_label.setPixmap(QPixmap("img/db97283d9eafe3eb062aa5daf53e6e64.jpg"))
        self.image_label.setScaledContents(True)
        self.image_width = 0
        self.image_height =0
        self.image_label.setGeometry(0, 0, self.width(), self.height())


        self.phone_number_line=QLineEdit(self)
        self.phone_number_line.setPlaceholderText("Telefon raqami")
        self.phone_number_line.setGeometry(120,320,300,50)
        self.phone_number_line.setStyleSheet(log_in_for_client)

        self.password_line=PasswordEdit(self)
        self.password_line.setPlaceholderText("Parol kiriting")
        self.password_line.setGeometry(120,420,300,50)
        self.password_line.setStyleSheet(log_in_for_client)

        self.enter_btn=QPushButton(self)
        self.enter_btn.setText("Kirish")
        self.enter_btn.setGeometry(120,620,300,50)
        self.enter_btn.clicked.connect(self.check_lines)
        self.enter_btn.setStyleSheet(log_in_for_client)

        self.text_label=QLabel(self)
        self.text_label.setText("~~ Log in ~~")
        self.text_label.setGeometry(150,200,450,50)
        self.text_label.setStyleSheet(log_in_for_client)

        self.back1=QPushButton(self)
        self.back1.setText("<<<")
        self.back1.setGeometry(100,50,60,50)
        self.back1.clicked.connect(self.back)
        self.back1.setStyleSheet(log_in_for_client)
    
    def back(self):
        self.go_to_the_back=Suggest_to_Log_in_or_sign_in_for_client()
        self.go_to_the_back.show()
        self.close()

    def check_lines(self):

        self.phone_number_check=self.phone_number_line.text()
        self.password_check=self.password_line.text()
        sql_query="Select *from for_client where phone_number =%s and password=%s"
        values=(self.phone_number_check,self.password_check)
        self.db_cursor.execute(sql_query,values)
        result=self.db_cursor.fetchone()
        
        if result:
            self.go_to_the_MainWindowForClients=MainWindowForClients(result[0])
            self.go_to_the_MainWindowForClients.show()
            self.close()
        else:
            QMessageBox.warning(self,"Xato","Foydalanuvchi nomi yoki parol noto'g'ri!")


class MainWindowForClients(QWidget):
    def __init__(self,name):
        super().__init__()
        self.setGeometry(400,50,700,800)
        self.setWindowTitle("Mijozning asosiy oynasi")
        self.clientname=name
        print(self.clientname)
        self.buttons_for_clients()

    def buttons_for_clients(self):
        
        self.image_label = QLabel(self)
        self.image_label.setPixmap(QPixmap("img/60d17bd3594d08262a76f9b880956367.jpg"))
        self.image_label.setScaledContents(True)
        self.image_width = 100
        self.image_height =100
        self.image_label.setGeometry(0, 0, self.width(), self.height())

        self.call_a_taxi_btn=QPushButton(self)
        self.call_a_taxi_btn.setText("Taksi chaqirish")
        self.call_a_taxi_btn.setGeometry(20,650,200,50)
        self.call_a_taxi_btn.clicked.connect(self.call_a_taxi)
        self.call_a_taxi_btn.setStyleSheet(mainWindowForClients)

        self.my_data_btn=QPushButton(self)
        self.my_data_btn.setText("Mening ma'lumotlarim")
        self.my_data_btn.setGeometry(250,730,200,50)
        self.my_data_btn.clicked.connect(self.my_data)
        self.my_data_btn.setStyleSheet(mainWindowForClients)
        
        self.my_orders_btn=QPushButton(self)
        self.my_orders_btn.setText("Mening buyurtmalarim")
        self.my_orders_btn.setGeometry(480,650,200,50)
        self.my_orders_btn.clicked.connect(self.my_orders)
        self.my_orders_btn.setStyleSheet(mainWindowForClients)

        self.back1=QPushButton(self)
        self.back1.setText("<<<")
        self.back1.setGeometry(310,650,100,50)
        self.back1.clicked.connect(self.back)
        self.back1.setStyleSheet(mainWindowForClients)
    
    def back(self):
        self.go_to_the_back=Chooses()
        self.go_to_the_back.show()
        self.close()

    def call_a_taxi(self):
        self.go_to_the_call_a_taxi=Call_a_Taxi(self.clientname)
        self.go_to_the_call_a_taxi.show()
        self.close()
    
    def my_data(self):
        
        self.go_to_the_my_data=My_data(self.clientname)
        self.go_to_the_my_data.show()
        self.close()
    
    def my_orders(self):
        self.go_to_the_my_orders=My_orders(self.clientname)
        self.go_to_the_my_orders.show()
        self.close()


class Call_a_Taxi(QWidget):
    def __init__(self, name):
        super().__init__()
        self.clientname=name
        self.db_connection = db_connection
        self.db_cursor = db_cursor

        self.setWindowTitle("Taksi chaqirish")
        self.setGeometry(400,50,530,830)
        self.location()

    def location(self):
        
        self.image_label = QLabel(self)
        self.image_label.setPixmap(QPixmap("img/e81eeb3008195760b48b13a12fc8c44d copy.jpg"))
        self.image_label.setScaledContents(True)
        self.image_width = 10
        self.image_height =10
        self.image_label.setGeometry(0, 0, self.width(), self.height())


        self.is_being_called_line=QLineEdit(self)
        self.is_being_called_line.setPlaceholderText("Qayerga kelishi k-k")
        self.is_being_called_line.setGeometry(120,200,300,50)
        self.is_being_called_line.setStyleSheet(call_a_Taxi)

        self.should_take_line=QLineEdit(self)
        self.should_take_line.setPlaceholderText("Qayerga Yetkazish k-k")
        self.should_take_line.setGeometry(120,300,300,50)
        self.should_take_line.setStyleSheet(call_a_Taxi)

        self.call_taxi_btn=QPushButton(self)
        self.call_taxi_btn.setText("Chaqirish")
        self.call_taxi_btn.setGeometry(120,750,300,50)
        self.call_taxi_btn.clicked.connect(self.check_location)
        self.call_taxi_btn.setStyleSheet(call_a_Taxi)

        self.datetime_edit=QDateTimeEdit(self)
        self.datetime_edit.setDateTime(QDateTime.currentDateTime())
        self.datetime_edit.setGeometry(120,400,300,50)
        self.datetime_edit.setStyleSheet(call_a_Taxi)

        self.back1=QPushButton(self)
        self.back1.setText("<<<")
        self.back1.setGeometry(10,10,60,50)
        self.back1.clicked.connect(self.back)
        self.back1.setStyleSheet(call_a_Taxi)
    
    def back(self):
        self.go_to_the_back=MainWindowForClients(self.clientname)
        self.go_to_the_back.show()
        self.close()

    def show_error_message(self, message):
        """Функция для вывода сообщения  ошибке"""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec_()

    def check_location(self):
        if not self.is_being_called_line.text() or not self.should_take_line.text() :
            self.show_error_message("Iltimos hamma bo'sh joylarni toldiring")
        else:
            self.is_being_called = self.is_being_called_line.text()
            self.should_take = self.should_take_line.text()
            self.order_time = self.datetime_edit.dateTime().toString('yyyy-MM-dd HH:mm:ss')
            self.status="Kutyapti"
            self.driver_name=""

            sql_query = """
            INSERT INTO orders (client_name, from_where, where_to, date_of_order, status_of_order, driver_name)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            values = (self.clientname, self.is_being_called, self.should_take, self.order_time, self.status, self.driver_name)

            try:
                self.db_cursor.execute(sql_query, values)
                self.db_connection.commit()
                QMessageBox.information(self, "Muvaffaqiyat", "Buyurtma muvaffaqiyatli joylandi!")
            except mysql.connector.Error as err:
                QMessageBox.warning(self, "Xato", f"xato: {err}")
            

        
class My_data(QWidget):
    def __init__(self, name):
        super().__init__()
        self.db_connection = db_connection
        self.db_cursor = db_cursor
        self.clientname = name 

        self.image_label = QLabel(self)
        self.image_label.setPixmap(QPixmap("img/461c704f9868cbffed2dd088a30d93b8.jpg"))
        self.image_label.setScaledContents(True)
        self.image_width = 0
        self.image_height =0
        self.image_label.setGeometry(0, 0, self.width(), self.height())
        
        self.setWindowTitle("Ma'lumotlarim")
        self.setGeometry(400, 50, 640, 500)
        self.display_data()
        
        
    
    def show_gif(self):

        self.label = QLabel(self)
        self.label.setGeometry(600, 700, 880, 700)  
        self.movie = QMovie('img/63b8a20773677516d1409061d4bba25c.gif')  
        self.label.setMovie(self.movie)
        self.movie.start()  
        self.setStyleSheet(chooses)

    def display_data(self):
        
        sql_query = "SELECT name, phone_number FROM for_client WHERE name = %s"
        values = (self.clientname,) 
        
        try:
            self.db_cursor.execute(sql_query, values)
            data = self.db_cursor.fetchone()

            if data:
                name, phone_number = data
                
                info_label = QLabel(f"Ismingiz: {name}\nTelefon raqamingiz: {phone_number}", self)
                info_label.setGeometry(50, 170, 535, 150)  
                info_label.setStyleSheet(my_data)
            else:
                QMessageBox.warning(self, "Ma'lumotlar topilmadi", "Foydalanuvchi ma'lumotlari topilmadi.")
        except mysql.connector.Error as err:
            QMessageBox.warning(self, "Xato", f"xato: {err}")
        
        self.back1=QPushButton(self)
        self.back1.setText("Orqaga")
        self.back1.setGeometry(270,400,100,50)
        self.back1.clicked.connect(self.back)
        self.back1.setStyleSheet(my_data_for_driver)
    
    def back(self):
        self.go_to_the_back=MainWindowForClients(self.clientname)
        self.go_to_the_back.show()
        self.close()


class My_orders(QWidget):
    def __init__(self, name):
        super().__init__()
        self.client_name = name
        self.db_connection = connect_to_db() 
        self.db_cursor = self.db_connection.cursor()  
        self.setGeometry(400, 50, 530, 830)
        self.setWindowTitle(" buyurtmalar")

        self.image_label = QLabel(self)
        self.image_label.setPixmap(QPixmap("img/bae89f468dd8abf86e6d6f31f16fd7b9.jpg"))
        self.image_label.setScaledContents(True)
        self.image_width = 10
        self.image_height =10
        self.image_label.setGeometry(0, 0, self.width(), self.height())

        self.layout = QVBoxLayout(self)

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)

        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)

        self.scroll_area.setWidget(self.scroll_widget)

        self.layout.addWidget(self.scroll_area)

        self.orders_label = QLabel(self.scroll_widget)
        self.orders_label.setGeometry(40, 85, 450, 680)
        self.orders_label.setStyleSheet(my_orders)  
        self.scroll_layout.addWidget(self.orders_label)

        self.orders_label = QLabel(self)
        self.orders_label.setGeometry(40, 85, 450, 680)
        self.orders_label.setStyleSheet(my_orders)  

        self.load_orders()  

    def load_orders(self):
        
        try:
            sql_query = "SELECT id, from_where, where_to, date_of_order FROM orders WHERE client_name = %s order by id desc"
            values = (self.client_name,)  
            self.db_cursor.execute(sql_query, values)
            orders = self.db_cursor.fetchall()

           
            if orders:
                orders_list = "\n".join( f" {order[1]} dan {order[2]} ga \n---------------------------------" for order in orders)
                self.orders_label.setText(orders_list)
            else:
                self.orders_label.setText("Hozircha buyurtmalar yo'q.")
        except mysql.connector.Error as err:
            QMessageBox.warning(self, "Xato", f"Buyurtmalarni olishda xato: {err}")

        self.back1=QPushButton(self)
        self.back1.setText("Orqaga")
        self.back1.setGeometry(220,700,100,50)
        self.back1.clicked.connect(self.back)
        self.back1.setStyleSheet(my_orders_for_driver)
    
    def back(self):
        self.go_to_the_back=MainWindowForClients(self.client_name)
        self.go_to_the_back.show()
        self.close()

    def closeEvent(self, event):
        self.db_cursor.close()
        self.db_connection.close()
        event.accept()

app=QApplication(sys.argv)
win=Chooses()
win.show()
app.exec_()
