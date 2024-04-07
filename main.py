from time import sleep
from typing import Optional
from local_modules.LiveStram import LiveStream
from local_modules.Timer import Timer
from sys import argv as arguments
from halo import Halo

def args(argument: str, default: Optional[str] = None) -> str:
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
    wait = args('--wait', '5')

    if wait.isdigit():
        wait = int(wait)

    timer = Timer(timeout)
    livestream = LiveStream(streamer=streamer, timer=timer)
    spinner = Halo(text=f'Esperando {streamer}', spinner='star', text_color='cyan')
    
    spinner.start()
    for _ in range(livestream.total_trys):
        if livestream.is_live():
            spinner.succeed(f'{streamer} abriu live 😃👍')
            livestream.open_livestream()
            return

        sleep(wait or 5)
    spinner.fail('Faz o L filho!! 🤡🫵')

if __name__ == '__main__':  
    main()
