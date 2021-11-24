import json
import building


class elevator(object):

    def __init__(self, id_: str = None, speed: int = 0, minFloor_e: str = 0, maxFloor_e: str = 0, closeTime: str = 0,
                 openTime: str = 0, startTime: str = 0, stopTime: str = 0, flag=0, pos={}):
        self.id_ = id_
        self.speed = speed
        self.minFloor_e = minFloor_e
        self.maxFloor_e = maxFloor_e
        self.closeTime = closeTime
        self.openTime = openTime
        self.startTime = startTime
        self.stopTime = stopTime
        self.flag = flag
        self.pos = pos
