from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtSvg import *
import sys
from random import randint


class RegWindow(QWidget):    
    def __init__(self):
        super(RegWindow, self).__init__()
        self.makeWindow()
        
    def makeWindow(self):
        self.setGeometry(300,300,500,200)
        self.setWindowTitle('Login')
        
        firstStage = FirstStage(self)
        createUser = CreateUser(self)
        emailLogin = EmailLogin(self)
        birthDate = BirthDate(self)
        yourFriends = YourFriends(self)
        yourAdress = YourAdress(self)
        gender = Gender(self)
        
        
        self.pageDisplay = QStackedWidget()
        self.pageDisplay.addWidget(firstStage)
        self.pageDisplay.addWidget(createUser)
        self.pageDisplay.addWidget(emailLogin)
        self.pageDisplay.addWidget(gender)        
        self.pageDisplay.addWidget(birthDate)
        self.pageDisplay.addWidget(yourAdress)        
        self.pageDisplay.addWidget(yourFriends)

        layout = QVBoxLayout()
        layout.addWidget(self.pageDisplay)
        
#        self.firstStage()
        
        self.setLayout(layout)
        self.show()
    
    
    def continueWithEmail(self, event):
        self.setWindowTitle('You Sucker')
        
        self.nextStage()
            
    def openLogin(self):
        self.loginWin = FacebookLogin()
        self.loginWin.show()
        
    def nextStage(self):
        self.actualIndex = self.pageDisplay.currentIndex()
        self.pageDisplay.setCurrentIndex(self.actualIndex+1)
        
        self.fbInstead = []
        for i in range(0,self.actualIndex*3) :
            self.fbInstead.append(AnnoyingWindow(self))
            self.fbInstead[i].show()
        
    def prevStage(self):
        self.actualIndex = self.pageDisplay.currentIndex()
        self.pageDisplay.setCurrentIndex(self.actualIndex-1)
    
class FirstStage(QWidget):
    def __init__(self, mainWindow):
        super(FirstStage, self).__init__()
        self.mainWindow = mainWindow
        self.makeGui()
        
    def makeGui(self):
        self.fbLogin = BlueButton('Login with facebook')
        self.fbLogin.clicked.connect(self.mainWindow.openLogin)
        
        self.emailLink = QLabel(self)
        self.emailLink.setText('login with email')
        self.emailLink.mousePressEvent = self.mainWindow.continueWithEmail
        
        mailbox = QHBoxLayout()
        mailbox.addStretch(1)
        mailbox.addWidget(self.emailLink)
        mailbox.addStretch(1)
        buttonBox = QHBoxLayout()
        buttonBox.addStretch(1)
        buttonBox.addWidget(self.fbLogin)
        buttonBox.addStretch(1)
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(buttonBox)
        vbox.addSpacing(11)
        vbox.addLayout(mailbox)
        vbox.addStretch(1)
        
        self.setLayout(vbox)

class FormWidget(QWidget):
    def __init__(self, mainWindow):
        super(FormWidget, self).__init__()
        self.mainWindow = mainWindow
        self.form = QFormLayout()
        self.makeGui()
        
    def makeGui(self):
        facebookLogin = BlueButton('Use facebook instead')
        facebookLogin.clicked.connect(self.mainWindow.openLogin)
        nextButton = QPushButton('next', self)
        if 'verify' in dir(self):
            nextButton.clicked.connect(self.verify)
        else:
            nextButton.clicked.connect(self.mainWindow.nextStage)
        prevButton = QPushButton('previous', self)
        prevButton.clicked.connect(self.mainWindow.prevStage)

        self.form = QFormLayout()
        
        hBox = QHBoxLayout()
        hBox.addWidget(prevButton)
        hBox.addStretch(1)
        hBox.addWidget(nextButton)
        
        self.vbox = QVBoxLayout()
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.form)
        self.vbox.addSpacing(11)
        self.vbox.addWidget(facebookLogin)
        self.vbox.addSpacing(11)
        self.vbox.addStretch(1)
        self.vbox.addLayout(hBox)
        
        self.setLayout(self.vbox)


class CreateUser(FormWidget):
    def __init__(self, mainWindow):
        super(CreateUser, self).__init__(mainWindow)
        self.mainWindow = mainWindow
        self.addElements()
        
    def addElements(self):
        self.userName = QLineEdit()
        self.email = QLineEdit()
        
        self.form.addRow(QLabel('User Name'), self.userName)
        self.form.addRow(QLabel('Email adress'), self.email)
        
    def verify(self):
        if self.userName.text() == '':
            self.mainWindow.openLogin()
        else:
            self.mainWindow.nextStage()
            
class EmailLogin(FormWidget):
    def __init__(self, mainWindow):
        super(EmailLogin, self).__init__(mainWindow)
        self.addElements()
        
    def addElements(self):
        self.firstNameInput = QLineEdit()
        self.lastNameInput = QLineEdit()
        self.firstNameLabel = QLabel('First name')
        self.lastNameLabel = QLabel('Last name')
                
        self.form.addRow(self.firstNameLabel, self.firstNameInput)
        self.form.addRow(self.lastNameLabel, self.lastNameInput)
                
        
class BirthDate(FormWidget):
    def __init__(self, mainWindow):
        super(BirthDate, self).__init__(mainWindow)
        self.addElements()
        
    def addElements(self):
        calendar = QCalendarWidget()
        birthDate = QLabel('Birth Date')
        
        self.form.addRow(birthDate, calendar)
        
class YourFriends(FormWidget):
    def __init__(self, mainWindow):
        super(YourFriends, self).__init__(mainWindow)
        self.addElements()
        
    def addElements(self):
        intro = QLabel('Name your five best friends, so we can analyze our users')
        addFriendButton = QPushButton('Add more Friends')
        addFriendButton.clicked.connect(self.addFriend)
        
        self.vbox.insertWidget(0,intro)
        
        self.form.addRow(addFriendButton)
        friends = []
        for self.i in range(0,5):
            friends.append(QLineEdit())
            self.form.addRow(QLabel(str(self.i+1)),friends[self.i])
        
    def addFriend(self):
        self.i += 1
        self.form.insertRow(self.i+1 ,QLabel(str(self.i+1)),QLineEdit())

class YourAdress(FormWidget):
    def __init__(self,mainWindow):
        super(YourAdress, self).__init__(mainWindow)
        self.addElements()
        
    def addElements(self):
        intro = QLabel('What is your adress?')
        streetInput = QLineEdit()
        zipInput = QLineEdit()
        townInput = QLineEdit()
        
        self.vbox.insertWidget(0,intro)
        
        self.form.addRow(QLabel('Street'), streetInput)
        self.form.addRow(QLabel('Zip-Code'), zipInput)
        self.form.addRow(QLabel('Town'), townInput)
        
class Gender(FormWidget):
    def __init__(self, mainWindow):
        super(Gender, self).__init__(mainWindow)
        self.addElements()
        
    def addElements(self):
        choose = QGroupBox('Your Gender')
        male = QRadioButton('male', choose)
        female = QRadioButton('female', choose)
        
        hBox = QHBoxLayout(choose)
        hBox.addWidget(male)
        hBox.addWidget(female)
        
        choose.setLayout(hBox)
        
        self.form.addRow(choose)
        
class FacebookLogin(QWidget):
    def __init__(self):
        super(FacebookLogin, self).__init__()
        self.makeWindow()
        
    def makeWindow(self):
        self.setGeometry(400,400,500,300)
        self.setWindowTitle('Login wit Facebook')
        
        headerLabel = QLabel()
        headerLabel.setText('facebook')
        headerLabel.setStyleSheet('color:#ffffff')
        logo = QSvgWidget()
        logo.load('fb.svg')
        logo.setMaximumHeight(16)
        logo.setMaximumWidth(16)
#        img = QPixmap('fb.png')
#        logo.setPixmap(img)
        
        headerLayout = QHBoxLayout()
        headerLayout.addWidget(logo)
        headerLayout.addWidget(headerLabel)
        
        header = QFrame()
        header.setStyleSheet('background-color:#4267b2; font-size:14px; font-weight: 500;')
        header.setMinimumHeight(50)
        header.setLayout(headerLayout)
        
        inputUser = QLineEdit(self)
        inputPass = QLineEdit(self)
        labelUser = QLabel(self)
        labelPass = QLabel(self)
        buttonLogin = BlueButton('login')
        
        labelUser.setText('Email or phone number')
        labelPass.setText('Password')
        
        formLayout = QFormLayout()
        formLayout.addRow(labelUser, inputUser)
        formLayout.addRow(labelPass, inputPass)
        formLayout.addRow('', buttonLogin)
        
        vlayout = QVBoxLayout()
        vlayout.addStretch(1)
        vlayout.addLayout(formLayout)
        vlayout.addStretch(1)
        vlayout.setContentsMargins(11,11,11,11)
        
        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(0,0,0,0)
        mainLayout.addWidget(header)
        mainLayout.addLayout(vlayout)
        
        self.setLayout(mainLayout)
        
class AnnoyingWindow(QDialog):
    def __init__(self, mainWindow):
        super(AnnoyingWindow, self).__init__(mainWindow)
        self.availableHeight = QApplication.desktop().availableGeometry().height()
        self.availableWidth = QApplication.desktop().availableGeometry().width()
        self.mainWindow = mainWindow
        self.makeWindow()
        
    def makeWindow(self):
        self.setGeometry(randint(50, self.availableWidth - self.width()), randint(50, self.availableHeight- self.height()),300,100)
        
        self.button = BlueButton('Use Facebook!')
        self.button.clicked.connect(self.mainWindow.openLogin)
        
        vbox= QVBoxLayout()
        vbox.addWidget(self.button)
        
        self.setLayout(vbox)
        self.setWindowTitle('Use Facebook!')
                
        self.setWindowModality(Qt.WindowModal)
        
        self.show()
        
        
        
class BlueButton(QPushButton):
    def __init__(self, text):
        super (BlueButton, self).__init__()
        self.setText(text)
        self.setStyleSheet("""
            QPushButton{
                background-color:#4267b2;
                padding:10px 50px;
                color:#fff;
                border:0;
                border-radius:5px;
                font-size: 18px;
            }
        """)
        self.setCursor(Qt.PointingHandCursor)
        logo = QSvgWidget()
        logo.load('fb.svg')
        logo.setMaximumHeight(20)
        logo.setMaximumWidth(20)
        self.layout = QHBoxLayout()
        self.layout.addSpacing(8)
        self.layout.addWidget(logo)
        self.layout.addStretch(1)
        self.setLayout(self.layout)

    
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywin = RegWindow()
    sys.exit(app.exec_())