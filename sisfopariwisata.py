import sys
from this import s
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget, QWidget, QTableWidget
import pymysql
import ast
import mysql.connector as mc
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from pymysql import connect, connections
from PyQt5.QtGui import QTextCursor
from PyQt5 import QtWidgets, QtCore, QtPrintSupport, QtGui

class WelcomeScreen(QDialog):

    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("welcomescreen.ui", self)
        self.pbLoginX.clicked.connect(self.gotologin)
        self.pbCreateX.clicked.connect(self.gotocreate)
        self.pbConnectX.clicked.connect(self.gotoconnect)
        self.pbQuitX.clicked.connect(self.gotoQuit)

    def gotologin(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotocreate(self):
        create = CreateAccScreen()
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoconnect(self):
        con = pymysql.connect(db='dbapotek', user='root', passwd='', host='localhost', port=3306, autocommit=True)
        cur = con.cursor()
        if(cur):
            self.messagebox("Koneksi", "Koneksi Berhasil")
        else:
            self.messagebox("Koneksi", "Koneksi Gagal")

    def messagebox(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def gotoQuit(self):
        sys.exit()

class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("login.ui", self)

        self.pbLoginX.clicked.connect(self.login)
        self.pbCancelX.clicked.connect(self.Hapus)
        self.bLogout.clicked.connect(self.logout)

    def login(self):
        try:
            username = self.username.text()
            password = self.password.text()
            mydb = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="dbwisata"
            )
 
            mycursor = mydb.cursor()
            mycursor.execute("SELECT username, password from datauser where username like '"+ username + "'and password like '"+ password +"'")
            result = mycursor.fetchone()
 
            if result == None:
                self.labelResult.setText("Incorrect username & Password")
 
            else:
                self.labelResult.setText("You are logged in")    
                mydialog = MAIN_MENU()
                widget.addWidget(mydialog)
                widget.setCurrentIndex(widget.currentIndex()+1)

        except pymysql.Error as e:
            self.labelResult.setText("Error")
    
    def Hapus(self):
        username = self.username.setText(" ")
        password = self.password.setText(" ")

    def logout(self):
        mydialog = WelcomeScreen()
        widget.addWidget(mydialog)
        widget.setCurrentIndex(widget.currentIndex()+1)



class CreateAccScreen(QDialog):
    def __init__(self):
        super(CreateAccScreen, self).__init__()
        loadUi("CreateAccScreen.ui", self)

        self.bClear.clicked.connect(self.Hapus)
        self.bLogout.clicked.connect(self.logout)
        self.bSave.clicked.connect(self.save)
        self.bCheck.clicked.connect(self.Tampil)
        self.bUpdate.clicked.connect(self.update)  
        self.bDelete.clicked.connect(self.delete)                         

    def save(self):
        username = self.username.text()
        password = self.password.text()
        insert = (username, password)
        print(insert)
        con = pymysql.connect(db='dbwisata', user='root', passwd='', host='localhost', port=3306, autocommit=True)
        cur = con.cursor()
        sql = "INSERT INTO datauser(username, password)" + \
                  "VALUES"+str(insert)
        datauser = cur.execute(sql)
        if(datauser):
            self.messagebox("SUKSES", "Data user Tersimpan")
        else:
             self.messagebox("GAGAL", "Data user Gagal Tersimpan")    

    def messagebox(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()


    def Tampil(self):
        username = self.username.text()
        db = pymysql.connect(db='dbwisata', user='root', passwd='', host='localhost', port=3306, autocommit=True)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM datauser WHERE username='"+str(username)+"'")

        datauser = cursor.fetchall()
        if (datauser):
            for tp in datauser:
                self.username.setText("" + tp[0])
                self.password.setText("" + tp[1])
                self.messagebox("INFO","Data Ada")
        else:
                self.messagebox("INFO", "Data belum ada")  


    def update(self):
        username = self.username.text()
        password = self.password.text()
        con = pymysql.connect(db='dbwisata', user='root', passwd='', host='localhost', port=3306, autocommit=True)
        cur = con.cursor()
        sql = "UPDATE datauser SET password=%s, username=%s"
        datauser = cur.execute(sql, (password, username))
        if (datauser):
             self.messagebox("SUKSES", "Data Berhasil Di Update")
        else:
            self.messagebox("GAGAL", "Data Gagal Di Update")    

    def delete(self):
        username = self.username.text()
        con = pymysql.connect(db='dbwisata', user='root', passwd='', host='localhost', port=3306, autocommit=True)
        cur = con.cursor()
        sql = "DELETE FROM datauser where username=%s"
        datauser= cur.execute(sql, (username))
        if (datauser):
            self.messagebox("SUKSES", "Data Berhasil Di HAPUS")
        else:
            self.messagebox("GAGAL", "Data GAGAL Di HAPUS")           
  
    def Hapus(self):
        self.username.setText(" ")
        self.password.setText(" ")

    def logout(self):
        mydialog = WelcomeScreen()
        widget.addWidget(mydialog)
        widget.setCurrentIndex(widget.currentIndex()+1)

class MAIN_MENU (QDialog):
    def __init__(self):
        super(MAIN_MENU, self).__init__()
        loadUi("MainMenu.ui", self)

        self.pbKaryawan.clicked.connect(self.Karyawan)
        self.pbwisata.clicked.connect(self.Wisata)  
        self.pbAbout.clicked.connect(self.about)  
        self.pbLogout.clicked.connect(self.logout)  
        self.pbLayanan.clicked.connect(self.layanan)


    def Karyawan (self):
        mydialog = DATA_KARYAWAN()
        widget.addWidget(mydialog)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def Wisata (self):
        mydialog = WISATA()
        widget.addWidget(mydialog)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def about (self):
        mydialog = ABOUT_PROGRAM ()
        widget.addWidget(mydialog)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def layanan (self):
        mydialog = LAYANAN ()
        widget.addWidget(mydialog)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def logout (self):
        mydialog = WelcomeScreen ()
        widget.addWidget(mydialog)
        widget.setCurrentIndex(widget.currentIndex()+1)

class DATA_KARYAWAN (QDialog):
    def __init__(self):
        super(DATA_KARYAWAN, self).__init__()
        loadUi("dbkaryawan.ui", self)

        self.bClear.clicked.connect(self.Hapus)
        self.bSave.clicked.connect(self.save)
        self.bCheck.clicked.connect(self.Tampil)
        self.bUpdate.clicked.connect(self.update)  
        self.bDelete.clicked.connect(self.delete)  
        self.bLogout.clicked.connect(self.backX)  
        self.bSearch.clicked.connect(self.SearchData)
        #self.bPrintFileX.clicked.connect(self.PrintFile)  
        #self.bPrintPreviewX.clicked.connect(self.printPreviewDialog)  
        self.bLoadDataX.clicked.connect(self.LoadDataX)

        self.LoadDataX()

    def LoadDataX(self):
        db = mc.connect(db='dbwisata', user='root', passwd='', host='localhost', port=3306, autocommit=True)        
        mycursor = db.cursor()
        mycursor.execute("SELECT * FROM datakaryawan")
        result = mycursor.fetchall()
        self.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        mycursor.close()

    def save(self):
        Nama = self.Nama.text()
        Hobby = self.Hobby.text()
        Alamat = self.Alamat.text()
        Nomor = self.Nomor.text()
        TanggalLahir = self.dateEdit.text()
        insert = (Nama, Hobby, Alamat, Nomor, TanggalLahir,)
        print(insert)
        con = pymysql.connect(db='dbwisata', user='root', passwd='', host='localhost', port=3306, autocommit=True)
        cur = con.cursor()
        sql = "INSERT INTO datakaryawan (Nama, Hobby, Alamat, Nomor, Tanggal_lahir)" + \
                  "VALUES"+str(insert)
        datakaryawan = cur.execute(sql)

        if(datakaryawan):
            self.messagebox("SUKSES", "Data Karyawan Tersimpan")
        else:
             self.messagebox("GAGAL", "Data Karyawan Gagal Tersimpan")    

    def messagebox(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def Tampil(self):
        Nama = self.Nama.text()
        db = pymysql.connect(db='dbwisata', user='root', passwd='', host='localhost', port=3306, autocommit=True)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM datakaryawan WHERE Nama='"+str(Nama)+"'")
        datakaryawan = cursor.fetchall()
        if (datakaryawan):
            for tp in datakaryawan:
                self.Nama.setText("" + tp[0])
                self.Hobby.setText("" + tp[1])
                self.Alamat.setText("" + tp[2])
                self.Nomor.setText("" + tp[3])
 

                self.messagebox("INFO","Data Ada")
        else:
                self.messagebox("INFO", "Data belum ada")  


    def update(self):
        Nama = self.Nama.text()
        Hobby = self.Hobby.text()
        Alamat = self.Alamat.text()
        Nomor = self.Nomor.text()
   

        con = pymysql.connect(db='dbwisata', user='root', passwd='', host='localhost', port=3306, autocommit=True)
        cur = con.cursor()
        sql = "UPDATE datakaryawan SET Hobby=%s, Alamat=%s, Nomor=%s WHERE Nama=%s"
        datakaryawan = cur.execute(sql, (Hobby, Alamat, Nomor, Nama))
        if (datakaryawan):
             self.messagebox("SUKSES", "Data Berhasil Di Update")
        else:
            self.messagebox("GAGAL", "Data Gagal Di Update")    

    def delete(self):
        Nama = self.Nama.text()
        con = pymysql.connect(db='dbwisata', user='root', passwd='', host='localhost', port=3306, autocommit=True)
        cur = con.cursor()
        sql = "DELETE FROM datakaryawan where Nama=%s"
        datakaryawan = cur.execute(sql, (Nama))
        if (datakaryawan):
            self.messagebox("SUKSES", "Data Berhasil Di HAPUS")
        else:
            self.messagebox("GAGAL", "Data GAGAL Di HAPUS")           
    
    def SearchData(self):

        Nama = self.leSearch.text()
        db = mc.connect(db='dbwisata', user='root', passwd='', host='localhost', port=3306, autocommit=True)
        cursor = db.cursor()

        cursor.execute("SELECT * FROM datakaryawan WHERE Nama='"+str(Nama)+"'")        

        datakaryawan = cursor.fetchall()

        if (datakaryawan):
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(datakaryawan):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    cell = QtWidgets.QTableWidgetItem(str(data))
                    self.tableWidget.setItem(row_number, column_number,cell)
        else:
                self.messagebox("INFO", "Data belum ada")  
  
    def Hapus(self):
        self.Nama.setText(" ")
        self.Hobby.setText(" ")
        self.Alamat.setText(" ")
        self.Nomor.setText(" ")

    def backX(self):
        mydialog = MAIN_MENU()
        widget.addWidget(mydialog)
        widget.setCurrentIndex(widget.currentIndex()+1)

class WISATA (QDialog):
    def __init__(self):
        super(WISATA, self).__init__()
        loadUi("daftarwisata.ui", self)

        self.pbA.clicked.connect(self.paketA)
        self.pbB.clicked.connect(self.paketB)
        self.pbC.clicked.connect(self.paketC)
        #self.pbAbout.clicked.connect(self.about)  
        self.pbLogout.clicked.connect(self.logout)  


    def paketA (self):
        mydialog =MALINO()
        widget.addWidget(mydialog)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def paketB (self):
        mydialog =LembahRamma()
        widget.addWidget(mydialog)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def paketC (self):
        mydialog =RumahKurcaci()
        widget.addWidget(mydialog)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def logout (self):
        mydialog = MAIN_MENU()
        widget.addWidget(mydialog)
        widget.setCurrentIndex(widget.currentIndex()+1)


class  MALINO(QDialog):
    def __init__(self):
        super(MALINO, self).__init__()
        loadUi("Paket A.ui", self)

        
        self.bLogout.clicked.connect(self.backX)  


    def backX(self):
        mydialog = WISATA()
        widget.addWidget(mydialog)
        widget.setCurrentIndex(widget.currentIndex()+1)

class  LembahRamma(QDialog):
    def __init__(self):
        super(LembahRamma, self).__init__()
        loadUi("Paket B.ui", self)

        
        self.bLogout.clicked.connect(self.backX)  


    def backX(self):
        mydialog = WISATA()
        widget.addWidget(mydialog)
        widget.setCurrentIndex(widget.currentIndex()+1)

class  RumahKurcaci(QDialog):
    def __init__(self):
        super(RumahKurcaci, self).__init__()
        loadUi("Paket C.ui", self)

        
        self.bLogout.clicked.connect(self.backX)  


    def backX(self):
        mydialog = WISATA()
        widget.addWidget(mydialog)
        widget.setCurrentIndex(widget.currentIndex()+1)



app = QApplication(sys.argv)
welcome=WelcomeScreen()
widget = QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()
try:
   sys.exit(app.exec_())  
except:
    print("Exiting")     