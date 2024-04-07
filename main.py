from time import sleep
from typing import Optional
from local_modules.LiveStream import LiveStream
from local_modules.Timer import Timer
from local_modules.Platform import Twitch, Youtube
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
    timeout = args('--timeout', '24h')
    streamer = args('--streamer', 'rbiana')
    wait = args('--wait', '5') or 5
    platform = args('--platform', 'twitch')

    if wait.isdigit():
        wait = int(wait)

    platforms = {'twitch': Twitch, 'youtube': Youtube}
    timer = Timer(timeout, wait)
    livestream = LiveStream(streamer=streamer, timer=timer, platform=platforms[platform])
    spinner = Halo(text=f'Esperando {streamer}', spinner='star', text_color='cyan')
    
    spinner.start()
    for _ in range(timer.cycles):
        if livestream.is_live():
            spinner.succeed(f'{streamer} abriu live 😃👍')
            livestream.open_livestream()
            return

        sleep(wait)
    spinner.fail('Faz o L filho!! 🤡🫵')

if __name__ == '__main__':  
    main()
