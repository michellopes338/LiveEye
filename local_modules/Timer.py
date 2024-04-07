import dateparser
from datetime import datetime

class Timer():
    def __init__(self, time: str, wait: int) -> None:
        self.__timedelta = datetime.now() - dateparser.parse(time)
        self.__wait = wait

    @property
    def cycles(self):
        return self.__timedelta.seconds // self.__wait

if __name__ == '__main__':
    timer = Timer('5min')

    print(timer.to_trys())
