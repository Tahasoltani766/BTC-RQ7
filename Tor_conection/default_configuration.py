import io
import os
import stem.process
import re
import requests
import json
from datetime import datetime


def runer_tor():
    SOCKS_PORT = 9050
    TOR_PATH = os.path.normpath(os.getcwd() + "\\Tor\\tor\\tor.exe")
    tor_process = stem.process.launch_tor_with_config(
        config={
            'SocksPort': str(SOCKS_PORT),
        },
        init_msg_handler=lambda line: print(line) if re.search('Bootstrapped', line) else False,
        tor_cmd=TOR_PATH
    )
    PROXIES = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }
    response = requests.get("http://4ua34rxukuq3hqajg6yka753t4vmqf6ozpsv5vd6f35guz6wrdnnauad.onion", proxies=PROXIES)
    # result = json.loads(response.text)
    # print('TOR IP [%s]: %s %s' % (datetime.now().strftime("%d-%m-%Y %H:%M:%S"), result["query"], result["country"]))
    print(response.text)