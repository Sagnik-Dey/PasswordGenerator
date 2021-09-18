from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5 import QtGui
from app.function import functions
from threading import Timer
import sys

class MainWindow(QtWidgets.QMainWindow):
    """
    This is the MainWindow class which will
    load the window and it's widgets and 
    dynamically change it
    """
    def __init__(self):
        """
        Constructor For The MainWindow Class
        It calls the parent's constructor and 
        call the init_window_widgets function
        """
        
        super().__init__()

        self.init_window_widgets()

    def init_window_widgets(self):
        """
        This is a function which will initialize and load
        the ui file and shows the window
        """
        self.mainwindow_gui = uic.loadUi("./ui/mainwindow.ui", self)

        self.mainwindow_gui.generate_button.clicked.connect(self.gen_pass)
        self.mainwindow_gui.length_slider.valueChanged.connect(self.slider_value_updated)
        self.mainwindow_gui.length_slider.sliderReleased.connect(self.slider_released)
        self.mainwindow_gui.copy_button.clicked.connect(self.copy_password)
        self.mainwindow_gui.include_numbers.stateChanged.connect(self.checkBox_state_changed)
        self.mainwindow_gui.exit_button.clicked.connect(lambda: exit())

        self.show()

    def gen_pass(self):
        """
        This is a PyQt Slot that is connected with the 
        generate password button. This function will simply generate
        a random password based on the user preferences
        """

        length = int(self.mainwindow_gui.length_slider.value())
        password = ""

        if (self.mainwindow_gui.include_numbers.isChecked()):
            password = functions.generate_password(length=length, include_numbers=True)
        else:
            password = functions.generate_password(length=length, include_numbers=False)

        self.update_status("status", "Password Generated")
        self.mainwindow_gui.output_edit.setText(password)

    def slider_value_updated(self):
        """
        This is a PyQt Slot that is fired when the slider
        is dragged
        """
        self.slider_value_label.setText(str(self.mainwindow_gui.length_slider.value()))
        self.update_status("status", "Length is changing .....")

    def slider_released(self):
        """
        This is a PyQt Slot that is fired when the slider
        is released
        """
        self.update_status("status", "Length Updated")

    def update_status(self, state, message):
        """
        This is a function that updates the 
        status of the application

        Args:
            state ([string]): [The state of the status. Basically there will 
            be two state: "Success" and "Failure" The success state will be 
            transferred as "status" in the parameter and failure will be
            passed as "error"]

            message ([string]): [The message which should be shown in status]

        Raises:
            Exception: [If the state does not match an error will be raised]
        """
        if (state=="status"):
            self.mainwindow_gui.status.setObjectName("status");
            self.mainwindow_gui.status.setStyleSheet(
                "color: #11ff00; letter-spacing: 1.3px;")
            self.mainwindow_gui.status.setText(str(message))
        elif (state=="error"):
            self.mainwindow_gui.status.setObjectName("error");
            self.mainwindow_gui.status.setStyleSheet(
                "color: red; letter-spacing: 1.3px;")
            self.mainwindow_gui.status.setText(str(message))
        else:
            raise Exception("Invalid state");

    def copy_password(self):
        """
        This is PyQt Slot connected with the Copy Button
        This function will copy the password to the clipboard
        """

        if (self.mainwindow_gui.output_edit.text() == ""):
            self.update_status("error", "No Password to copy")
        else:
            self.mainwindow_gui.copy_button.setIcon(QtGui.QIcon("./assets/images/check.png"))
            
            functions.copy_to_clipboard(str(self.mainwindow_gui.output_edit.text()))
            self.update_status("status", "Copied To Clipboard Successfully ....")

            timer = Timer(1.5, lambda: self.mainwindow_gui.copy_button.setIcon(
                QtGui.QIcon("./assets/svg/clipboard.svg")),
                None)

            timer.start()

    def checkBox_state_changed(self):
        """
        This is again a PyQt Slot which is fired
        when the state of checkbox is changed

        By state I mean if the check box is checked or
        unchecked
        """
        if (self.mainwindow_gui.include_numbers.isChecked()):
            self.update_status("status", "Numbers Are Now Included")
        else:
            self.update_status("status", "Numbers Are Now Excluded")

def start_application():
    """
    This is a function which makes the object of 
    the MainWindow class and starts the application
    """
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
