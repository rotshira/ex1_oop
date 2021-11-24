import json


class building(object):
    def __init__(self, maxFloor: int = 0, minFloor: int = 0, elevator: list = [], *args, **kwargs):
        self.maxFloor = maxFloor
        self.minFloor = minFloor
        self.elevator = elevator

    def init_from_file(self, file_name: str) -> None:
        json_file = open('B1.json', encoding="utf-8")
        buildings = json.load(json_file)
        json_file.close()
        return buildings

    def __str__(self):
        return f"building: maxFloor:{self.maxFloor}, minFloor:{self.minFloor}, elevator:{self.elevator}"
