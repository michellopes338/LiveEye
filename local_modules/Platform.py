import requests
from .Timer import Timer

class Platform:
    def __init__(self, timer: Timer) -> None:
        self.__timer = timer

    @property
    def timer(self):
        return self.__timer

    @property
    def url(self):
        pass

    def is_live(self):
        pass


class Twitch(Platform):
    def __init__(self, timer: Timer) -> None:
        super().__init__(timer)

    def url(self, streamer) -> str:
        return f'https://www.twitch.tv/{streamer}'

    def is_live(self, stream_url):
        htmlBody = requests.get(stream_url, timeout=super().timer.cycles).content.decode('utf-8')
        return 'isLiveBroadcast' in htmlBody

class Youtube(Platform):
    def __init__(self, timer: Timer) -> None:
        super().__init__(timer)

    def url(self, streamer) -> str:
        return f'https://www.youtube.com/@{streamer}/live'

    def is_live(self, stream_url) -> bool: # not working
        htmlBody = requests.get(stream_url, timeout=super().timer.cycles).content.decode('utf-8')
        return '<div id="container" class="style-scope ytd-player">' in htmlBody

