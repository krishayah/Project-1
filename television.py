class Television:
    # Default values
    MIN_VOLUME = 0
    MAX_VOLUME = 25
    MIN_CHANNEL = 0
    MAX_CHANNEL = 7

    def __init__(self):
        self._status = False
        self._muted = False
        self._volume = self.MIN_VOLUME
        self._channel = self.MIN_CHANNEL  # Start at minimum channel
        self._previous_volume = self.MIN_VOLUME

    def power(self):
        self._status = not self._status  # Toggle power

    def mute(self):
        if self._status:  # Only works when TV is ON
            if self._muted:
                self._muted = False
                self._volume = self._previous_volume
            else:
                self._muted = True
                self._previous_volume = self._volume
                self._volume = self.MIN_VOLUME

    def channel_up(self):
        if self._status:  # Only works when TV is ON
            if self._channel == self.MAX_CHANNEL:
                self._channel = self.MIN_CHANNEL + 1  #skip channel 0 & start @ 1
            else:
                self._channel += 1

    def channel_down(self):
        if self._status:  # Only works when TV is ON
            self._channel = self.MAX_CHANNEL if self._channel == self.MIN_CHANNEL else self._channel - 1

    def volume_up(self):
        if self._status:  # Only works when TV is ON
            if self._muted:
                self._muted = False
                self._volume = self._previous_volume
            if self._volume < self.MAX_VOLUME:
                self._volume += 1

    def volume_down(self):
        if self._status:  # Only works when TV is ON
            if self._muted:
                self._muted = False
                self._volume = self._previous_volume
            if self._volume > self.MIN_VOLUME:
                self._volume -= 1

    def __str__(self):
        return f"Power = {self._status}, Channel = {self._channel}, Volume = {self._volume}"













