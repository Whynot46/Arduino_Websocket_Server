# Arduino_Websocket_Server
Сервер Websocket, развернутый на платформе Arduino, отправляет данные на сервер Fast API и отображает данные в виде графика.
<br>
Разрабатывалось для Arduino Uno R3 и Ethernet Shield на базе W5100.
![Иллюстрация к проекту](https://github.com/Whynot46/Arduino_Websocket_Server/blob/main/example.PNG)
## Содержание
- [Технологии](#технологии)
- [Использование](#использование)
- [Требования](#требования)
- [Команда проекта](#команда-проекта)
## Технологии
- [ArduinoWebsocketServer](https://github.com/ejeklint/ArduinoWebsocketServer)
- [FastAPI](https://fastapi.tiangolo.com/)
## Использование
Установите необходимые библиотеки с помощью команды:
<br>
<br>
For Windows:
```
pip install -r requirements.txt
```
For Linux/MacOS:
```
pip install -r requirements.txt
```
<br>
Скачайте библиотеку <a href="https://github.com/ejeklint/ArduinoWebsocketServer">ArduinoWebsocketServer</a> и установить её:
<br>
Откройте Arduino IDE и следуйте пути:

```
Скетч -> Подключить библиотеку -> Добавить .ZIP библиотеку
```
## Требования
- Arduino Uno (R3 and later)
- Arduino Ethernet Shield, Arduino Ethernet Shield 2, Leonardo Ethernet и любые другие устройства на базе W5100/W5200/W5500.
## Команда проекта
- [Алексей Пахалев](https://github.com/Whynot46)
