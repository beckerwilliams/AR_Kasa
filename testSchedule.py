import json
import asyncio
from kasa import SmartPlug

from schedule import on_schedule, off_schedule
from json import load
from pathlib import PosixPath as Path

with Path("schedules/on_schedule.json").open() as ofj:
    on_sched = json.load(ofj)

with Path("schedules/off_schedule.json").open() as ofj:
    off_sched = json.load(ofj)

plug = SmartPlug("192.168.1.3")
asyncio.run(plug.update())
schedule = plug.modules.get("schedule")
print(schedule.__getattribute__("name"))
# schedule: dict = off_schedule
# print(schedule)
#
#
# p.__setattr__("schedule", schedule)
# await p.update()

# print(p.__getattribute__("schedule"))
