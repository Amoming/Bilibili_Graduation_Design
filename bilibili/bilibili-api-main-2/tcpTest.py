import asyncio
import time

import json
from bilibili_api import live, sync

room_id = 25746936
room = live.LiveDanmaku(room_id)


async def send_data(data):
    reader, writer = await asyncio.open_connection('hadoop102', 9000)
    writer.write(data.encode())
    await writer.drain()
    writer.close()
    await writer.wait_closed()


# 收到弹幕
@room.on('DANMU_MSG')
async def on_danmaku(event):
    # timestamp = int(time.time())

    flag = 1
    if flag == 0:
        print(event)
    if flag == 1:
        # 是一个字符串
        extra_str: str = event['data']['info'][0][15]['extra']
        extra_list = extra_str.split(',')
        data_str = ','.join(extra_list)
        extra_data = json.loads(data_str)
        uid = event['data']['info'][2][0]
        ts = event['data']['info'][9]['ts']
        datatime_format = time.strftime('%Y-%m-%d', time.localtime(ts))
        # print(time_format)

        danmaku_data = {
            "type": event['type'],
            'room_display_id': event['room_display_id'],
            "id_str": extra_data["id_str"],
            'timestamp': ts,
            'datatime_format': datatime_format,
            'uid': uid,
            "color": extra_data["color"],
            "dm_type": extra_data["dm_type"],
            "font_size": extra_data["font_size"],
            "content": extra_data["content"],
            "recommend_score": extra_data["recommend_score"],
        }

        json_data = json.dumps(danmaku_data, ensure_ascii=False)
        # json_data = json.dumps(danmaku_data)
        print(json_data)
        await send_data(json_data)


sync(room.connect())
try:
    # 您的代码
    sync(room.connect())
except KeyboardInterrupt:
    print('程序已停止')
