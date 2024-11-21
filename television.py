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
                self._channel = self.MIN












