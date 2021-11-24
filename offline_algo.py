import csv
import json
import random
import building
import elevator
from building import building
from elevator import elevator
call_list = []
list_pos = []
build = building()


def init_from_json(file_name:str):
    with open(file_name, 'r') as file:
        reader = json.load(file)
        return reader


d = init_from_json("B1.json")
num_of_elevator = len(d["_elevators"])
for i in range(0, num_of_elevator):
    list_pos.append(0)


def init_from_file(file_name:str):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        list = []
        for row in reader:
            list.append(row)
    return list


def dist(src, dest, i):
    elev = elevator(id_= d["_elevators"][i]["_id"],speed=d["_elevators"][i]["_speed"]
                    , minFloor_e=d["_elevators"][i]["_minFloor"],
                    maxFloor_e=d["_elevators"][i]["_maxFloor"],
                    closeTime=d["_elevators"][i]["_closeTime"],openTime=d["_elevators"][i]["_openTime"],
                    startTime=d["_elevators"][i]["_startTime"],stopTime=d["_elevators"][i]["_stopTime"])
    return (abs(int(src) - int(dest)) / int(elev.speed)) + int(elev.closeTime) + int(elev.openTime) + int(elev.stopTime) + int(elev.startTime)


def allocate(filename: str):
    call_list = init_from_file(filename)
    state = []
    limit_elev = []
    for i in range(0, num_of_elevator):
        state.append(0)
        limit_elev.append(0)
    for i in range(0, num_of_elevator):
        c_src = call_list[i][2]
        c_dest = call_list[i][3]
        list_pos[i] = c_dest
        if c_dest > c_src:
            state[i] = 1
            call_list[i][5] = i
            limit_elev[i] = limit_elev[i] + 1
        else:
            state[i] = -1
            call_list[i][5] = i
            limit_elev[i] = limit_elev[i] + 1
    for i in range(num_of_elevator, len(call_list)):
        c_src = call_list[i][2]
        c_dest = call_list[i][3]
        ans = 0
        if num_of_elevator == 1:
            list_pos[ans] = c_dest
            call_list[i][5] = ans
        else:
            for j in range(1, num_of_elevator):
                if (state[j] == 1 and int(c_dest) > int(c_src)) or (state[j] == -1 and int(c_dest) < int(c_src) ):
                    if dist(c_src, c_dest, ans) > dist(c_src, c_dest, j):
                            ans = j
                            if limit_elev[ans] < len(call_list)/num_of_elevator:
                                list_pos[ans] = int(c_dest)
                                call_list[i][5] = j
                                limit_elev[j] = limit_elev[j]+1
                    else:
                        call_list[i][5] = ans
                        limit_elev[ans] = limit_elev[ans] + 1
                        if limit_elev[ans] > len(call_list)/num_of_elevator:
                            ans = ((ans + 1) % num_of_elevator)

                elif limit_elev[ans] < (len(call_list) / num_of_elevator):
                        call_list[i][5] = ans
                        limit_elev[ans] = limit_elev[ans] + 1
                else:
                    ans = random.randint(0, num_of_elevator-1)
                    call_list[i][5] = ans

    with open('out.csv', 'w', newline="") as file:
        csvwrite = csv.writer(file)
        csvwrite.writerows(call_list)
    return csvwrite


if __name__ == '__main__':
    b = allocate("Calls_c.csv")
    print(b)

