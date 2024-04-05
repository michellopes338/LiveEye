import requests
import webbrowser
from .Timer import Timer

class LiveStream:
    def __init__(self, streamer: str, timer: Timer) -> None:
        self.__streamer = streamer
        self.__total_trys = timer.to_trys()
    
    @property
    def url(self) -> str:
        return f'https://www.twitch.tv/{self.__streamer}'

    @property
    def streamer(self) -> str:
        return self.__streamer
    
    @property
    def total_trys(self):
        return self.__total_trys

    def open_livestream(self) -> None:
        webbrowser.open(self.url)

    def is_live(self) -> bool:
        htmlBody = requests.get(self.url, timeout=self.__total_trys).content.decode('utf-8')
        return 'isLiveBroadcast' in htmlBody