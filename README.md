# Flask Telegram Logger
A simple flask api that updates (logs) to user with a given user ID.
### Installation
#### With Docker
- pull docker image `adarshbaderia/flask-telegram-logger`
- run with command `docker run -d -p 8353:8353 -e TELEGRAM_TOKEN={YOUR_BOT_TOKEN_GOES_HERE} -e USER_ID={YOUR_TELEGRAM_USER_ID_GOES_HERE} adarshbadera/flask-telegram/logger`
#### Running Script
- Add `TELEGRAM_TOKEN` and `USER_ID` to your env variables.
- run the script.

### Usage
- Depending on how you configure this, call the API `http://{YOUR_LAN_IP}:8353/update  with message in request body to send the request body to the user.

### But... Why?
I needed a quick app that updates my about locally running server. I have multiple scripts running which, being the great coder that I am, might break due to any number of reasons. I needed a simple way to update me whenever something broke and this seemed like the most user friendly.

### Future plans
- Adding support for custom messages, log, warning, info, error among other things.
- Adding support for multiple users.

### Error & Bugs
- If you issue a PR fixing any vulnerability or bug, I will definitely approve it.
- If you report a bug, I will get to it when I get to it.
