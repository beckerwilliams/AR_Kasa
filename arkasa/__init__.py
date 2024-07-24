import asyncio
from json import dumps

from kasa import (Discover, SmartPlug)
from kasa.exceptions import SmartDeviceException
from kasa.exceptions import TimeoutException


# Smart Plug Interface

async def discover(timeout=10):
    try:
        return await Discover.discover(timeout=timeout)

    except SmartDeviceException as e:
        print("Timeout error: {}".format(e))


async def hosts():
    devices = await Discover.discover(timeout=10)
    hosts = [host for host in devices]
    return hosts


async def get(host, timeout=10):
    try:
        return await Discover.discover_single(host, timeout=timeout)

    except SmartDeviceException as e:
        print("Host: {}, Timeout error: {}".format(host, e))


async def turn_on(host):
    p = SmartPlug(host)
    await p.update()
    await p.turn_on()


async def turn_off(host):
    p = SmartPlug(host)
    await p.update()
    await p.turn_off()
