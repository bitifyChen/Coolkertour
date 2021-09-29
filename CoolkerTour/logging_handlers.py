import logging
import requests
from CoolkerTour.settings import LINE_NOTIFY_ACCESS_TOKEN, ALLOWED_HOSTS


class LineAdminHandler(logging.StreamHandler):
    def emit(self, record):
        requests.post('https://notify-api.line.me/api/notify', params={'message': get_full_url_message(record.message)},
                      headers={'Authorization': 'Bearer ' + LINE_NOTIFY_ACCESS_TOKEN,
                               'Content-Type': 'application/x-www-form-urlencoded'})


def get_full_url_message(message):
    part1, part2 = message.split(': ')
    return part1 + ' ' + ALLOWED_HOSTS[0] + part2
