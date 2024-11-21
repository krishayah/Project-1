class Television:
    """
    Class with basic functionality of TV
    """
    # Default values
        self._status = False
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Initialize TV with Default settings
        """
        self._status: bool = False
        self._muted: bool = False
        self._volume: int = self.MIN_VOLUME
        self._channel: int = self.MIN_CHANNEL  # Start at minimum channel
        self._previous_volume: int = self.MIN_VOLUME

    def power(self) -> None:
        """
        To Toggle Power Status of TV
        """
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
            self._channel = self.MIN_CHANNEL if self._channel == self.MAX_CHANNEL else self._channel + 1

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
        Returns a String that shows current Status of TV
        """
        return f"Power = {self._status}, Channel = {self._channel}, Volume = {self._volume}"













