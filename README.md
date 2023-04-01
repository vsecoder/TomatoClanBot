# TomatoClanBot

[![wakatime](https://wakatime.com/badge/github/vsecoder/TomatoClanBot.svg)](https://wakatime.com/badge/github/vsecoder/TomatoClanBot)
![Telegram](https://img.shields.io/badge/Telegram-blue?style=flat&logo=telegram)
[![DeepSource](https://deepsource.io/gh/vsecoder/TomatoClanBot.svg/?label=active+issues&show_trend=true&token=tEWO-7pQW5lP2AsQq9tNLIK1)](https://deepsource.io/gh/vsecoder/TomatoClanBot/?ref=repository-badge)
[![CodeFactor](https://www.codefactor.io/repository/github/vsecoder/tomatoclanbot/badge)](https://www.codefactor.io/repository/github/vsecoder/tomatoclanbot)
![CodeStyle](https://img.shields.io/badge/code%20style-black-black)
![PythonVersions](https://img.shields.io/pypi/pyversions/aiogram)

## [bot](https://t.me/tomatoclanbot?start=1218845111)

## Features

* ![aiogram 3](https://img.shields.io/badge/dev--3.x-aiogram-blue) as a main library
* ![tortoise](https://img.shields.io/badge/last-tortoise-yellow) as ORM

## Run bot

### Dev

```bash
git clone https://github.com/vsecoder/TomatoClanBot.git
cd TomatoClanBot
python3 -m venv tomat
source tomat/bin/activate
pip install -r requirements.txt
cp example.toml config.toml
nano config.toml # <= edit config (token, admins, etc.)
python3 -m app
```

### Prod

```bash
git clone https://github.com/vsecoder/TomatoClanBot.git
cd TomatoClanBot
nano config.toml #  <= edit config (token, admins, etc.)
```

```bash
python3 -m venv tomat
source tomat/bin/activate
pip3 install -r requirements.txt

sudo nano /etc/systemd/system/tomato.service
```

Enter this:

```
Description=TomatoClanBot
[Service]
WorkingDirectory=/home/<USERNAME>/TomatoClanBot
nvironment=PYTHONPATH=/home/<USERNAME>/TomatoClanBot
ExecStart=/home/<USERNAME>/TomatoClanBot/tomat/bin/python3 -m app
Type=simple
Restart=always
RestartSec=1
User=<USERNAME>
[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl enable tomato
sudo systemctl start tomato # <= start bot
sudo systemctl status tomato # <= get status

sudo systemctl start tomato # <= stop bot
```