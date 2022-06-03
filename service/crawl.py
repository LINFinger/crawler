import requests

from constant import request
from dao import mysql


def crawl_message(req):
    for port_id, _ in request.PORTS_DICT.items():
        for index, message_url in enumerate(request.MESSAGE_URL_TUPLE):
            url = request.HEAD_URL + port_id + message_url
            res = requests.get(url, headers=req.headers)
            mysql.store_in_mysql(index, res.text)
