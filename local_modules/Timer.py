import dateparser
from datetime import datetime

class Timer():
    def __init__(self, time: str) -> None:
        self.timedelta = datetime.now() - dateparser.parse(time)
    
    def to_trys(self):
        return self.timedelta.seconds // 5

if __name__ == '__main__':
    timer = Timer('5min')

    print(timer.to_trys())
