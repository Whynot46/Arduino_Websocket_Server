import websockets
import asyncio
import json
import logging
import sys
from datetime import datetime
from typing import Iterator
from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import Response
import uvicorn


server_ip = "192.168.1.10"


logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)


application = FastAPI()
templates = Jinja2Templates(directory="templates")


@application.get("/", response_class=HTMLResponse)
async def index(request: Request) -> Response:
    return templates.TemplateResponse("index.html", {"request": request})


async def generate_random_data(request: Request) -> Iterator[str]:
    client_ip = request.client.host
    logger.info("Client %s connected", client_ip)

    async with websockets.connect(f"ws://{server_ip}", ping_interval=None) as websocket:

        while True:
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            value = await websocket.recv()
            json_data = json.dumps(
                {
                    "time": date,
                    "value": value,
                }
            )
            yield f"data:{json_data}\n\n"

            await asyncio.sleep(0.0005)


@application.get("/chart-data")
async def chart_data(request: Request) -> StreamingResponse:
    response = StreamingResponse(generate_random_data(request), media_type="text/event-stream")
    response.headers["Cache-Control"] = "no-cache"
    response.headers["X-Accel-Buffering"] = "no"
    return response

if __name__=="__main__":
    uvicorn.run("webclient:application", port=80)