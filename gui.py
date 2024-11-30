from PyQt6 import QtCore, QtWidgets

class Ui_TV_REMOTE:
    """
    A class to define the user interface for a television remote control simulator.

    This interface includes buttons for power, mute, volume, and channel control,
    along with a volume progress bar and a channel display image.
    """

    def setupUi(self, TV_REMOTE: QtWidgets.QMainWindow) -> None:
        """
        Sets up the user interface elements for the television remote.

        :param TV_REMOTE: The main application window for the remote simulator.
        """
        # Configure the main application window
        TV_REMOTE.setObjectName("TV_REMOTE")
        TV_REMOTE.resize(320, 330)
        TV_REMOTE.setMinimumSize(QtCore.QSize(320, 330))
        TV_REMOTE.setMaximumSize(QtCore.QSize(320, 330))

        # Central widget setup
        self.centralwidget = QtWidgets.QWidget(parent=TV_REMOTE)
        self.centralwidget.setObjectName("centralwidget")

        # Power button
        self.btn_power = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_power.setGeometry(QtCore.QRect(230, 240, 71, 31))
        self.btn_power.setObjectName("btn_power")

        # Mute button
        self.btn_mute = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_mute.setGeometry(QtCore.QRect(130, 150, 61, 31))
        self.btn_mute.setObjectName("btn_mute")

        # Channel selector (SpinBox)
        self.channel_selector = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.channel_selector.setGeometry(QtCore.QRect(80, 110, 161, 21))
        self.channel_selector.setWrapping(True)
        self.channel_selector.setFrame(True)
        self.channel_selector.setReadOnly(False)
        self.channel_selector.setSpecialValueText("")
        self.channel_selector.setObjectName("channel_selector")

        # Channel up button
        self.btn_channel_up = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_channel_up.setGeometry(QtCore.QRect(50, 140, 51, 32))
        self.btn_channel_up.setObjectName("btn_channel_up")

        # Channel down button
        self.btn_channel_down = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_channel_down.setGeometry(QtCore.QRect(50, 190, 51, 32))
        self.btn_channel_down.setObjectName("btn_channel_down")

        # Volume up button
        self.btn_volume_up = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_volume_up.setGeometry(QtCore.QRect(220, 140, 51, 32))
        self.btn_volume_up.setObjectName("btn_volume_up")

        # Volume down button
        self.btn_volume_down = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_volume_down.setGeometry(QtCore.QRect(220, 190, 51, 32))
        self.btn_volume_down.setObjectName("btn_volume_down")

        # Channel label
        self.label_channel = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_channel.setGeometry(QtCore.QRect(60, 170, 31, 21))
        self.label_channel.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.label_channel.setObjectName("label_channel")

        # Volume label
        self.label_volume = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_volume.setGeometry(QtCore.QRect(230, 170, 31, 16))
        self.label_volume.setObjectName("label_volume")

        # Channel image display
        self.lbl_channel_image = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_channel_image.setGeometry(QtCore.QRect(80, 0, 161, 101))
        self.lbl_channel_image.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.lbl_channel_image.setLineWidth(1)
        self.lbl_channel_image.setObjectName("lbl_channel_image")

        # Finalize main window layout
        TV_REMOTE.setCentralWidget(self.centralwidget)

        # Menu bar setup
        self.menubar = QtWidgets.QMenuBar(parent=TV_REMOTE)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 37))
        self.menubar.setObjectName("menubar")
        TV_REMOTE.setMenuBar(self.menubar)

        # Status bar setup
        self.statusbar = QtWidgets.QStatusBar(parent=TV_REMOTE)
        self.statusbar.setObjectName("statusbar")
        TV_REMOTE.setStatusBar(self.statusbar)

        # Set text for the UI elements
        self.retranslateUi(TV_REMOTE)

        # Connect UI components to corresponding slots (if any)
        QtCore.QMetaObject.connectSlotsByName(TV_REMOTE)

    def retranslateUi(self, TV_REMOTE: QtWidgets.QMainWindow) -> None:
        """
        Translates the text of the UI elements, ensuring they display the correct labels.

        :param TV_REMOTE: The main application window for the remote simulator.
        """
        _translate = QtCore.QCoreApplication.translate
        TV_REMOTE.setWindowTitle(_translate("TV_REMOTE", "Television Remote"))
        self.btn_power.setText(_translate("TV_REMOTE", "Power"))
        self.btn_mute.setText(_translate("TV_REMOTE", "Mute"))
        self.btn_channel_up.setText(_translate("TV_REMOTE", "+"))
        self.btn_channel_down.setText(_translate("TV_REMOTE", "-"))
        self.btn_volume_up.setText(_translate("TV_REMOTE", "+"))
        self.btn_volume_down.setText(_translate("TV_REMOTE", "-"))
        self.label_channel.setText(_translate("TV_REMOTE", "CH"))
        self.label_volume.setText(_translate("TV_REMOTE", "VOL"))
        self.lbl_channel_image.setText(_translate("TV_REMOTE", "No Channel"))

# Entry point for the application
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TV_REMOTE = QtWidgets.QMainWindow()
    ui = Ui_TV_REMOTE()
    ui.setupUi(TV_REMOTE)
    TV_REMOTE.show()
    sys.exit(app.exec())
