# Arduino_Websocket_Server
Websocket сервер, развернутый на платформе Arduino, отправляет данные на сервер Fast API и отображает данные в виде графика.
<br>
Разрабатывалось для Arduino Uno R3 и Ethernet Shield на базе W5100.
![Иллюстрация к проекту](https://github.com/Whynot46/Arduino_Websocket_Server/blob/main/example.PNG)
## Содержание
- [Технологии](#технологии)
- [Использование](#использование)
- [Требования](#требования)
- [Ограничения](#ограничения)
- [Лицензия](#лицензия)
- [Команда проекта](#команда-проекта)
## Технологии
- [ArduinoWebsocketServer](https://github.com/ejeklint/ArduinoWebsocketServer)
- [FastAPI](https://fastapi.tiangolo.com/)
## Использование
Скачайте репозиторий:
<br>
<br>
For Windows:
```
git clone https://github.com/Whynot46/Arduino_Websocket_Server
```
For Linux:
```
sudo git clone https://github.com/Whynot46/Arduino_Websocket_Server
```
<hr>
Установите необходимые библиотеки с помощью команды:
<br>
<br>
For Windows:

```
pip install -r requirements.txt
```
For Linux:
```
pip3 install -r requirements.txt
```
<hr>
Скачайте библиотеку <a href="https://github.com/ejeklint/ArduinoWebsocketServer">ArduinoWebsocketServer</a> и установить её:
<br>
Откройте Arduino IDE и следуйте пути:
<br>
<br>

```
Скетч -> Подключить библиотеку -> Добавить .ZIP библиотеку
```
## Требования
- Arduino Uno (R3 and later)
- Arduino Ethernet Shield, Arduino Ethernet Shield 2, Leonardo Ethernet и любые другие устройства на базе W5100/W5200/W5500.
## Ограничения
- Количество одновременных подключений может быть ограничено оперативной памятью или аппаратным обеспечением (Каждое соединение занимает 16 байт ОЗУ, а шилд W5100 аппаратно ограничен четырьмя одновременными соединениями).
- Логика поддержания активности не реализована.
- Другие ограничения смотрите в репозитории библиотеки <a href="https://github.com/ejeklint/ArduinoWebsocketServer">ArduinoWebsocketServer</a>.
## Лицензия
Этот проект бесплатен для использования и не содержит какой-либо лицензии.
## Команда проекта
- [Алексей Пахалев](https://github.com/Whynot46)
