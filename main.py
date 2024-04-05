from time import sleep
from typing import Optional
from local_modules.LiveStram import LiveStream
from local_modules.Timer import Timer
from sys import argv as arguments

def args(argument: str, default: Optional[str]) -> str:
    try:
        argument_index = arguments.index(argument)
        return arguments[argument_index + 1]
    except ValueError:  # Argument not found in the list
        return default
    except IndexError:  # No next argument available
        return default

def main() -> None:
    timeout = args('--timeout', '10m')
    streamer = args('--streamer', 'rbiana')

    timer = Timer(timeout)
    livestream = LiveStream(streamer=streamer, timer=timer)
    
    for _ in range(livestream.total_trys):
        if livestream.is_live():
            print(f'A {streamer} abriu live 😃👍')
            livestream.open_livestream()
            return

        print(f'{streamer} ainda não abriu live 😔')
        sleep(5)
    
    print('Faz o L filho!! 🤡🫵')

if __name__ == '__main__':  
    main()
