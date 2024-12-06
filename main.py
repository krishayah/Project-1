import sys
from PyQt6 import QtWidgets, QtGui
from gui import Ui_TV_REMOTE  # Import GUI
from television import Television  # Import logic


class TVRemoteApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TV_REMOTE()
        self.ui.setupUi(self)

        # Initialize Television Logic
        self.tv = Television()

        # Dictionary to store channel images
        self.channel_images = {
            0: "images/channel0.png",
            1: "images/channel1.png",
            2: "images/channel2.png",
            3: "images/channel3.png",
            4: "images/channel4.png",
            5: "images/channel5.png",
            6: "images/channel6.png",
            7: "images/channel7.png",
        }

        # Restrict SpinBox to valid channel range
        self.ui.channel_selector.setMinimum(1)  # Minimum channel
        self.ui.channel_selector.setMaximum(7)  # Maximum channel

        # Connect Buttons to Methods
        self.ui.btn_power.clicked.connect(self.toggle_power)
        self.ui.btn_mute.clicked.connect(self.toggle_mute)
        self.ui.btn_channel_up.clicked.connect(self.channel_up)
        self.ui.btn_channel_down.clicked.connect(self.channel_down)
        self.ui.btn_volume_up.clicked.connect(self.volume_up)
        self.ui.btn_volume_down.clicked.connect(self.volume_down)

        # Connect SpinBox (channel_selector) to channel change
        self.ui.channel_selector.valueChanged.connect(self.channel_selector_changed)

        # Set initial UI state
        self.update_ui()

    def toggle_power(self):
        self.tv.power()
        self.update_ui()

    def toggle_mute(self):
        self.tv.mute()
        self.update_ui()

    def channel_up(self):
        self.tv.channel_up()
        self.update_ui()

    def channel_down(self):
        self.tv.channel_down()
        self.update_ui()

    def volume_up(self):
        self.tv.volume_up()
        self.update_ui()

    def volume_down(self):
        self.tv.volume_down()
        self.update_ui()

    def channel_selector_changed(self, value):
        """
        This function is called when the channel selector (SpinBox) value changes.
        It updates the channel on the Television instance based on the selector value.
        """
        # Ensure the value is within the min/max channel range defined in Television
        if value <= self.tv.MAX_CHANNEL and value >= self.tv.MIN_CHANNEL:
            self.tv._channel = value
            self.update_ui()

    def update_ui(self):
        """
        Updates the UI elements based on the current state of the television.
        """
        # Update power state
        if self.tv._status:
            self.ui.btn_power.setText("ON")
            # Update channel image
            if self.tv._channel == 0:
                self.ui.lbl_channel_image.clear()  # Keep the image area blank
                self.ui.lbl_channel_image.setStyleSheet("background-color: black;")  # Black background
            else:
                channel_image_path = self.channel_images.get(self.tv._channel, "")
                if channel_image_path:
                    pixmap = QtGui.QPixmap(channel_image_path)
                    self.ui.lbl_channel_image.setPixmap(pixmap)
                    self.ui.lbl_channel_image.setScaledContents(True)
                else:
                    self.ui.lbl_channel_image.clear()

        else:
            self.ui.btn_power.setText("OFF")
            # Power off: reset channel to black
            self.ui.lbl_channel_image.clear()
            self.ui.lbl_channel_image.setStyleSheet("background-color: black;")

        # Enable or disable channel selector based on TV power status
        self.ui.channel_selector.setEnabled(self.tv._status)

        # Enable or disable channel selector based on TV power status
        self.ui.channel_selector.setEnabled(self.tv._status)

        # Update mute state
        if self.tv._muted:
            self.ui.btn_mute.setText("Unmute")  # click to unmute
        else:
            self.ui.btn_mute.setText("Mute")  # click to mute

        # Update channel image
        if self.tv._status:
            channel_image_path = self.channel_images.get(self.tv._channel)
            if channel_image_path:
                pixmap = QtGui.QPixmap(channel_image_path)
                self.ui.lbl_channel_image.setPixmap(pixmap)
                self.ui.lbl_channel_image.setScaledContents(True)
            else:
                self.ui.lbl_channel_image.setText("No Image")
        else:
            self.ui.lbl_channel_image.setText("")

        # Update channel selector
        self.ui.channel_selector.setValue(self.tv._channel)

        # Update volume label
        if self.tv._muted:
            self.ui.label_volume.setText("Muted")
        else:
            self.ui.label_volume.setText(f"VOL: {self.tv._volume}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TVRemoteApp()
    window.show()
    sys.exit(app.exec())

