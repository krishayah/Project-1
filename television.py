class Television:
    """
    Class with basic functionality of TV
    """
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

    def mute(self) -> None:
        """
        Mutes or Unmutes TV
        When muted, Volume = 0
        When unmuted, Volume is restored to previous level.
        """
        if self._status:  # Only works when TV is ON
            if self._muted:
                self._muted = False
                self._volume = self._previous_volume
            else:
                self._muted = True
                self._previous_volume = self._volume
                self._volume = self.MIN_VOLUME

    def channel_up(self) -> None:
        """
        Increments channel # by 1. 
        Wraps around to MINIMUM Channel.
        """
        if self._status:  # Only works when TV is ON
            if self._channel == self.MAX_CHANNEL:
                self._channel = self.MIN_CHANNEL + 1  #skip channel 0 & start @ 1
            else:
                self._channel += 1

    def channel_down(self) -> None:
        """
        Decrements Channel # by 1.
        Wraps around to MAXIMUM Channel.
        """
        if self._status:  # Only works when TV is ON
            self._channel = self.MAX_CHANNEL if self._channel == self.MIN_CHANNEL else self._channel - 1

    def volume_up(self) -> None:
        """
        Increases Volume by 1. 
        If muted, unmute & restore to previous vloume level.
        """
        if self._status:  # Only works when TV is ON
            if self._muted:
                self._muted = False
                self._volume = self._previous_volume
            if self._volume < self.MAX_VOLUME:
                self._volume += 1

    def volume_down(self) -> None:
        """
        Decreases Volume by 1.
        If muted, unmute & restore to previous volume level.
        """
        if self._status:  # Only works when TV is ON
            if self._muted:
                self._muted = False
                self._volume = self._previous_volume
            if self._volume > self.MIN_VOLUME:
                self._volume -= 1

    def __str__(self) -> str:
        """
        Provides a string representation of the Television object.
        Returns str A string indicating the current power status, channel, and volume of the TV.
        """
        return f"Power = {self._status}, Channel = {self._channel}, Volume = {self._volume}"













