# TomatoClanBot

[![wakatime](https://wakatime.com/badge/user/17993a3c-e23b-43ce-a9c6-84b6248d1411/project/1017f65b-9711-47c2-8bc2-b8568b9852c2.svg)](https://wakatime.com/badge/user/17993a3c-e23b-43ce-a9c6-84b6248d1411/project/1017f65b-9711-47c2-8bc2-b8568b9852c2)
![Telegram](https://img.shields.io/badge/Telegram-blue?style=flat&logo=telegram)
[![DeepSource](https://deepsource.io/gh/vsecoder/TomatoClanBot.svg/?label=active+issues&show_trend=true&token=tEWO-7pQW5lP2AsQq9tNLIK1)](https://deepsource.io/gh/vsecoder/TomatoClanBot/?ref=repository-badge)
[![CodeFactor](https://www.codefactor.io/repository/github/vsecoder/tomatoclanbot/badge)](https://www.codefactor.io/repository/github/vsecoder/tomatoclanbot)
![CodeStyle](https://img.shields.io/badge/code%20style-black-black)
![PythonVersions](https://img.shields.io/pypi/pyversions/aiogram)

## [bot](https://t.me/tomatoclanbot)

## Features

* ![aiogram 3](https://img.shields.io/badge/dev--3.x-aiogram-blue) as a main library
* ![tortoise](https://img.shields.io/badge/last-tortoise-yellow) as ORM

## Start bot

```bash
git clone https://github.com/vsecoder/TomatoClanBot.git
cd TomatoClanBot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp example.toml config.toml
nano config.toml # <= edit config (token, admins, etc.)
python3 -m app
```