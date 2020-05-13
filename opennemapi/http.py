"""
"""

import logging

import requests


def get_json(url, *args, **kwargs):
    """
    """
    try:
        r = requests.get(url, *args, **kwargs)                
        resp = r.json()
        if not resp:
            raise requests.exceptions.RequestException('data response is null')
        return resp
    except requests.exceptions.RequestException as e:
        logging.debug(f'get_json() error. {e} on {url}')
        raise(e)

