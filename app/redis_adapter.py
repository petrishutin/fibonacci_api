import redis
import json

from app.settings import config


class RedisAdapter(dict):
    """Dict-like class to store data in redis storage"""
    def __init__(self):
        self.r = redis.Redis(
            host=config.REDIS_HOST, port=config.REDIS_PORT, username=config.REDIS_USER, password=config.REDIS_PASSWORD
        )

    def __setitem__(self, key, item):
        item = json.dumps(item)
        self.r.mset({key: item})

    def __getitem__(self, key):
        item = self.r.get(key)
        return json.loads(item)

    def keys(self):
        r_keys = self.r.keys()
        if not r_keys:
            return ()
        return tuple(map(lambda x: int(x.decode('utf-8')), self.r.keys()))
