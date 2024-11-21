class Television:
    #default values
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self._status = False
        self._muted = False
        self._volume = self.MIN_VOLUME
        self._channel = self.MAX_VOLUME

    def power(self):
            self._status == self._status #??

    def mute(self):
            if self._status: #only works when TV's ON
                if self._muted:
                    self._muted = False
                    self._volume = self._previous_volume
            else:
                self._muted = True
                self._previous_volume = self._volume
                self._volume = self.MIN_VOLUME #set volume to 0

    def channel_up(self):
            if self._status: #only works when TV's ON
                self._channel = self.MIN_CHANNEL if self._channel == self.MAX_CHANNEL else self.channel + 1

    def channel_down(self):
            if self._status:
                self._channel = self.MAX_CHANNEL if self._channel ==self._MIN_CHANNEL else self._channel - 1
            
    def volume_up (self):
            if self._status:
                if self._muted:
                    self._muted = False
                    self._volume = self._previous_volume
                if self._volume < self.MAX_VOLUME:
                    self._volume += 1

    def volume_down(self):
            if self._status:
                if self._muted:
                    self._muted = False
                    self._volume = self._previous_volume
                if self._volume > self.MIN_VOLUME:
                    self._volume -= 1

    def __str__(self):
            return f"Power = {self._status}, Channel = {self._channel}, Volume = {self._volume}"












