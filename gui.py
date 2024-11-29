from PyQt6 import QtCore, QtWidgets

class UI_TV_REMOTE(object):
    """
    This class sets up the GUI for a television remote control simulator.

    It includes buttons for controlling power, volume, and channels,
    a progress bar for volume, and a QLabel for displaying the current channel image.
    """

    def setupUi(self, TV_REMOTE):
        """
        Initializes and organizes all GUI elements.

        :param TV_REMOTE: The main application window for the remote simulator.
        """
        # Set up the main window
        TV_REMOTE.setObjectName("TV_REMOTE")
        TV_REMOTE.resize(320, 330)
        TV_REMOTE.setMinimumSize(QtCore.QSize(320, 330))
        TV_REMOTE.setMaximumSize(QtCore.QSize(320, 330))
        self.centralwidget = QtWidgets.QWidget(parent=TV_REMOTE)
        self.centralwidget.setObjectName("centralwidget")

        # Call setup functions for modular code
        self.setup_buttons()
        self.setup_labels()
        self.setup_other_widgets()

        # Finalize setup
        TV_REMOTE.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=TV_REMOTE)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 37))
        self.menubar.setObjectName("menubar")
        TV_REMOTE.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=TV_REMOTE)
        self.statusbar.setObjectName("statusbar")
        TV_REMOTE.setStatusBar(self.statusbar)

        # Retranslate UI for setting text on widgets
        self.retranslateUi(TV_REMOTE)
        QtCore.QMetaObject.connectSlotsByName(TV_REMOTE)

    def setup_buttons(self):
        """
        Sets up the buttons for power, mute, volume, and channel controls.
        """
        # Power button
        self.btn_power = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_power.setGeometry(QtCore.QRect(230, 240, 71, 31))
        self.btn_power.setObjectName("btn_power")

        # Mute button
        self.btn_mute = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_mute.setGeometry(QtCore.QRect(130, 150, 61, 31))
        self.btn_mute.setObjectName("btn_mute")

        # Volume controls
        self.btn_volume_up = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_volume_up.setGeometry(QtCore.QRect(220, 140, 51, 32))
        self.btn_volume_up.setObjectName("btn_volume_up")
        self.btn_volume_down = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_volume_down.setGeometry(QtCore.QRect(220, 190, 51, 32))
        self.btn_volume_down.setObjectName("btn_volume_down")

        # Channel controls
        self.btn_channel_up = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_channel_up.setGeometry(QtCore.QRect(50, 140, 51, 32))
        self.btn_channel_up.setObjectName("btn_channel_up")
        self.btn_channel_down = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_channel_down.setGeometry(QtCore.QRect(50, 190, 51, 32))
        self.btn_channel_down.setObjectName("btn_channel_down")

    def setup_labels(self):
        """
        Sets up labels for volume, channel, and the channel image.
        """
        # Channel image display
        self.lbl_channel_image = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_channel_image.setGeometry(QtCore.QRect(90, 0, 141, 81))
        self.lbl_channel_image.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.lbl_channel_image.setLineWidth(1)
        self.lbl_channel_image.setObjectName("lbl_channel_image")

        # Volume and channel indicators
        self.label_channel = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_channel.setGeometry(QtCore.QRect(60, 170, 31, 21))
        self.label_channel.setObjectName("label_channel")

        self.label_volume = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_volume.setGeometry(QtCore.QRect(230, 170, 31, 16))
        self.label_volume.setObjectName("label_volume")

    def setup_other_widgets(self):
        """
        Sets up other widgets, including the channel selector and volume progress bar.
        """
        # Channel selector
        self.channel_selector = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.channel_selector.setGeometry(QtCore.QRect(80, 90, 161, 21))
        self.channel_selector.setWrapping(True)
        self.channel_selector.setObjectName("channel_selector")

        # Volume progress bar
        self.volume_bar = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.volume_bar.setGeometry(QtCore.QRect(90, 110, 118, 23))
        self.volume_bar.setProperty("value", 24)  # Set default volume
        self.volume_bar.setObjectName("volume_bar")

    def retranslateUi(self, TV_REMOTE):
        """
        Sets the text of buttons, labels, and other widgets.
        """
        _translate = QtCore.QCoreApplication.translate
        TV_REMOTE.setWindowTitle(_translate("TV_REMOTE", "Television Remote"))
        self.btn_power.setText(_translate("TV_REMOTE", "Power"))
        self.btn_mute.setText(_translate("TV_REMOTE", "Mute"))
        self.channel_selector.setSpecialValueText(_translate("TV_REMOTE", "Skip to Channel #"))
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
    ui = UI_TV_REMOTE()
    ui.setupUi(TV_REMOTE)
    TV_REMOTE.show()
    sys.exit(app.exec())