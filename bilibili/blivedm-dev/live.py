import asyncio
import http.cookies
import random
from typing import *
import sys
import json
import aiohttp
import blivedm
from aiohttp import TCPConnector
import blivedm.models.web as web_models

room_id = 0
# 这里填一个已登录账号的cookie。不填cookie也可以连接，但是收到弹幕的用户名会打码，UID会变成0
SESSDATA = ''

session: Optional[aiohttp.ClientSession] = None


async def main():
    init_session()
    try:
        await run_single_client()
        # await run_multi_clients()
    finally:
        await session.close()

def save_json(file_name, json_data):
    with open(f'/opt/module/danmaku/bilibili-api-main/json/{file_name}.json', 'a', encoding='utf-8') as f:
        f.write(json_data + '\n')

def init_session():
    cookies = http.cookies.SimpleCookie()
    cookies['SESSDATA'] = SESSDATA
    cookies['SESSDATA']['domain'] = 'bilibili.com'

    global session
    session = aiohttp.ClientSession(connector=TCPConnector(ssl=False))
    session.cookie_jar.update_cookies(cookies)

async def run_multi_clients():
    """
    演示同时监听多个直播间
    """
    clients = [blivedm.BLiveClient(room_id, session=session)]
    handler = MyHandler()
    for client in clients:
        client.set_handler(handler)
        client.start()

    try:
        await asyncio.gather(*(
            client.join() for client in clients
        ))
    finally:
        await asyncio.gather(*(
            client.stop_and_close() for client in clients
        ))
async def run_single_client():
    """
    演示监听一个直播间
    """
    client = blivedm.BLiveClient(room_id, session=session)
    handler = MyHandler()
    client.set_handler(handler)

    client.start()
    try:
        await client.join()
    finally:
        await client.stop_and_close()

class MyHandler(blivedm.BaseHandler):
    def _on_danmaku(self, client: blivedm.BLiveClient, message: web_models.DanmakuMessage):
        danmaku_data = {
            "type": message.msg_type,
            "id_str": message.id_str,
            'timestamp': message.timestamp,
            'datatime_format': message.datatime_format,
            'time_format': message.time_format,
            'uid': message.uid,
            "color": message.color,
            "dm_type": message.dm_type,
            "font_size": message.font_size,
            "content": message.msg,
            "recommend_score": message.recommend_score,
        }
        json_data = json.dumps(danmaku_data, ensure_ascii=False)
        print(json_data)

        save_json('DANMU_MSG', json_data)



if __name__ == '__main__':
    if len(sys.argv) > 1:
        room_id = int(sys.argv[1])
        asyncio.run(main())
    else:
        print("请在命令行中输入room_id")
