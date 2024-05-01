import io
import os
import stem.process
import re
import requests

def runer_tor():
    SOCKS_PORT = 9050
    TOR_PATH = os.path.normpath(os.getcwd() + "\\Tor\\tor\\tor.exe")
    try:
        tor_process = stem.process.launch_tor_with_config(
            config={
                'SocksPort': str(SOCKS_PORT),
            },
            init_msg_handler=lambda line: print(line) if re.search('Bootstrapped', line) else False,
            tor_cmd=TOR_PATH
        )
    except Exception as e:
        if e == 'OSError: Process terminated: Failed to bind one of the listener ports.':
            pass
    PROXIES = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }
    response = requests.post("http://4ua34rxukuq3hqajg6yka753t4vmqf6ozpsv5vd6f35guz6wrdnnauad.onion", proxies=PROXIES,
                             data={"gpu": 'NO GPU'})
    print(response.text)
