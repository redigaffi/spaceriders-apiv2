from core.shared.ports import CacheServicePort
from dataclasses import dataclass
from emcache import Client
import time
import pickle


@dataclass
class MemCacheCacheServiceAdapter(CacheServicePort):
    client: Client

    async def set(self, key: str, value, expiry: int):
        data = pickle.dumps(value)

        await self.client.set(
            key.encode(),
            data,
            flags=4,
            # Expire in one hour
            exptime=int(time.time()) + expiry,
            # Do not ask for an explicit reply from Memcached
            noreply=True
        )

    async def get(self, key: str):
        item = await self.client.get(key.encode())

        if item is None:
            return None

        return pickle.loads(item.value)
