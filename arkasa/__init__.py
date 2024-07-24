import asyncio
import tracemalloc
from pathlib import PosixPath as Path
from json import load

from kasa import (Discover, SmartPlug)
from kasa.exceptions import KasaException


# Smart Plug Interface

async def discover(timeout=10):
    try:
        return await Discover.discover(timeout=timeout)

    except KasaException as e:
        print("Timeout error: {}".format(e))


async def hosts():
    devices = await Discover.discover(timeout=10)
    hosts = [host for host in devices]
    return hosts


async def get(host, timeout=10):
    try:
        return await Discover.discover_single(host, timeout=timeout)

    except KasaException as e:
        print("Host: {}, Timeout error: {}".format(host, e))


async def turn_on(host):
    p = SmartPlug(host)
    await p.update()
    await p.turn_on()
    return (await get(host)).is_on


async def turn_off(host):
    p = SmartPlug(host)
    await p.update()
    await p.turn_off()
    return (await get(host)).is_off


async def set_schedule(host="192.168.1.3"):
    # Load Schedules
    with Path("schedules/off_schedule.json").open() as ons:
        off_schedule = load(ons)
    with Path("schedules/on_schedule.json").open() as ons:
        on_schedule = load(ons)

    p = SmartPlug(host)
    await p.update()

    p.__setattr__("schedule", off_schedule)
    await p.update()
    # print(p.__getattribute__("schedule"))

    p.__setattr__("schedule", on_schedule)
    await p.update()
    # print(p.__getattribute__("schedule"))

    p = SmartPlug(host)
    await p.update()
    sched = p.modules.get("schedule")
    print(sched.data)


if __name__ == "__main__":
    asyncio.run(set_schedule())
