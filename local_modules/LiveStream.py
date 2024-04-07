import webbrowser
from .Platform import Platform
from .Timer import Timer

class LiveStream:
    def __init__(self, streamer: str, timer: Timer, platform: Platform) -> None:
        self.__streamer = streamer
        self.__platform = platform(timer)

    @property
    def streamer(self) -> str:
        return self.__streamer

    def open_livestream(self) -> None:
        webbrowser.open(self.__platform.url(self.__streamer))

    def is_live(self) -> bool:
        return self.__platform.is_live(self.__platform.url(self.__streamer))