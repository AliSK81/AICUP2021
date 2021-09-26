import collections
from enum import Enum
from math import sqrt

import numpy as np


class Tile_State(Enum):
    deadzone = 0
    fire = 1
    box = 2
    wall = 3
    bomb = 4
    upgrade_range = 5
    upgrade_health = 6
    upgrade_trap = 7
    player = 8
    trap = 9
    box_broken = 10
    clear = 11
    target = 12


class Action(Enum):
    go_left = 0
    go_right = 1
    go_up = 2
    go_down = 3
    stay = 4
    place_bomb = 5
    place_trap_left = 6
    place_trap_right = 7
    place_trap_up = 8
    place_trap_down = 9
    init = 10
    no_action = 11


def has_state(_state_mask, _state_to_check):
    if _state_to_check == Tile_State.clear:
        if _state_mask & int(pow(2, Tile_State.fire.value)) or _state_mask & int(pow(2, Tile_State.deadzone.value)):
            return False
        elif not forbidden(_state_mask):
            return True
        else:
            return False
    else:
        return _state_mask & int(pow(2, _state_to_check.value))


def add_state(_state_mask, _state_to_add):
    return _state_mask | int(pow(2, _state_to_add.value))


def remove_state(_state_mask, _state_to_remove):
    return _state_mask & ~(int(pow(2, _state_to_remove.value)))


# Initiation stage

# Getting initiation message from engine
init_msg = input()
# Telling the engine that we received the initiation message
print("init confirm")
# Extracting info from initiation message
height, width, x, y, health, bombRange, trapCount, vision, \
bombDelay, maxBombRange, dzStart, dzDelay, maxStep = map(int, init_msg.split()[1:])

otherX = None
otherY = None
otherHealth = None
tiles = [[0 for _ in range(width)] for _ in range(height)]
center = (height // 2, width // 2)


def nearest_path(start, goal):
    queue = collections.deque([[start]])
    seen = {start}

    while queue:

        _path = queue.popleft()
        _x, _y = _path[-1]

        if has_state(tiles[_x][_y], goal):
            return _path
        for x2, y2 in dirs(_x, _y):

            if (x2, y2) not in seen and \
                    (not forbidden(tiles[x2][y2]) or has_state(tiles[x2][y2], goal)):
                queue.append(_path + [(x2, y2)])
                seen.add((x2, y2))


# sorting around directions (down\up\left\right)
# priority: closer to the center
def dirs(_x, _y):
    directs = [(_x + 1, _y), (_x, _y - 1), (_x - 1, _y), (_x, _y + 1)]
    directs.sort(key=lambda pos: distance(center, pos))
    return filter(lambda pos: 0 <= pos[0] < height and 0 <= pos[1] < width, directs)


def distance(pos1, pos2):
    return sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)


# check if a state exist in all tiles
def state_exist(state):
    for _x in tiles:
        for _y in _x[0:]:
            if has_state(_y, state):
                return True
    return False


# find a state position in tiles list
def positions_of(state):
    for _x in range(height):
        for _y in range(width):
            if has_state(tiles[_x][_y], state):
                yield _x, _y


# check if a tile is forbidden to move
forbidden_tiles = [Tile_State.wall, Tile_State.trap, Tile_State.bomb, Tile_State.box,
                   Tile_State.player, Tile_State.box_broken, Tile_State.deadzone]


def forbidden(tile):
    if has_state(tile, Tile_State.fire):
        if has_state(tiles[x][y], Tile_State.clear):
            return True
        for (_x, _y) in dirs(x, y):
            if has_state(tiles[_x][_y], Tile_State.clear):
                return True
        else:
            return False

    for state in forbidden_tiles:
        if has_state(tile, state):
            return True
    return False


# add or remove fire of bombs before explosion to recognize safe tiles and escape
def update_fire_of_bombs():
    for _x in range(height):
        for _y in range(width):
            tiles[_x][_y] = remove_state(tiles[_x][_y], Tile_State.fire)

    for (xbomb, ybomb) in positions_of(Tile_State.bomb):

        for _y in range(ybomb + 1, width):
            if abs(_y - ybomb) <= bombRange:
                if forbidden(tiles[xbomb][_y]) \
                        and not has_state(tiles[xbomb][_y], Tile_State.player) \
                        and not has_state(tiles[xbomb][_y], Tile_State.fire):
                    break
                tiles[xbomb][_y] = add_state(tiles[xbomb][_y], Tile_State.fire)

        for _y in range(ybomb - 1, -1, -1):
            if abs(_y - ybomb) <= bombRange:
                if forbidden(tiles[xbomb][_y]) \
                        and not has_state(tiles[xbomb][_y], Tile_State.player) \
                        and not has_state(tiles[xbomb][_y], Tile_State.fire):
                    break
                tiles[xbomb][_y] = add_state(tiles[xbomb][_y], Tile_State.fire)

        for _x in range(xbomb + 1, height):
            if abs(_x - xbomb) <= bombRange:
                if forbidden(tiles[_x][ybomb]) \
                        and not has_state(tiles[_x][ybomb], Tile_State.player) \
                        and not has_state(tiles[_x][ybomb], Tile_State.fire):
                    break
                tiles[_x][ybomb] = add_state(tiles[_x][ybomb], Tile_State.fire)

        for _x in range(xbomb - 1, -1, -1):
            if abs(_x - xbomb) <= bombRange:
                if forbidden(tiles[_x][ybomb]) \
                        and not has_state(tiles[_x][ybomb], Tile_State.player) \
                        and not has_state(tiles[_x][ybomb], Tile_State.fire):
                    break
                tiles[_x][ybomb] = add_state(tiles[_x][ybomb], Tile_State.fire)


# move 1 step from x,y to dest_x, dest_y
def move(dest):
    _x, _y = dest
    if x == _x:
        return Action.go_right.value if y < _y else Action.go_left.value
    else:
        return Action.go_down.value if x < _x else Action.go_up.value


def update_traps():
    for (_x, _y) in traps:
        tiles[_x][_y] = add_state(tiles[_x][_y], Tile_State.trap)

    if isOtherPlayerInVision and (otherX, otherY) in traps:
        tiles[otherX][otherY] = remove_state(tiles[otherX][otherY], Tile_State.trap)
        traps.remove((otherX, otherY))


def path_to_other_player():
    tiles[x][y] = remove_state(tiles[x][y], Tile_State.player)
    _path = nearest_path((x, y), Tile_State.player)
    tiles[x][y] = add_state(tiles[x][y], Tile_State.player)
    return _path


def place_trap():
    if not isOtherPlayerInVision or trapCount == 0:
        return None

    # find path to second player
    _path = path_to_other_player()

    if _path is None:
        return None

    # trap_range = 1 if deadzone_risk() else 2
    trap_range = 1
    if reachable(_path, trap_range):
        traps.append(_path[1])
        _x, _y = _path[1]
        tiles[_x][_y] = add_state(tiles[_x][_y], Tile_State.trap)
        return 6 + move(_path[1])  # place trap
    else:
        return None


# check risk of bomb explosion fire in _x, _y
def bomb_risk(dest):
    _x, _y = dest
    return has_state(tiles[_x][_y], Tile_State.fire) or \
           has_state(tiles[_x][_y], Tile_State.bomb)


def trap_risk(dest):
    for _x, _y in dirs(dest[0], dest[1]):
        if (_x != x or _y != y) and has_state(tiles[_x][_y], Tile_State.player):
            return True

    return False


# check if the start and the end of path are reachable
# reachable if and only if:
# 1- direct path
# 2- max distance is _range
# 3- no forbidden tile in path
def reachable(_path, _range):
    if _path is None:
        return False

    _x, _y = _path[0]
    pos = _path[-1]
    return _x == pos[0] and abs(_y - pos[1]) == len(_path) - 1 <= _range or \
           _y == pos[1] and abs(_x - pos[0]) == len(_path) - 1 <= _range


# simulate placing bomb and check if it's safe to escape
def can_escape_after_bomb():
    if bomb_risk((x, y)):
        return False
    #
    # dzStep = int((stepCount - dzStart) / dzDelay)
    # if bombDelay >= dzDelay and -2 < dzStep <= 0:
    #     return False

    if deadzone_risk():
        return False

    tiles[x][y] = add_state(tiles[x][y], Tile_State.bomb)
    update_fire_of_bombs()

    safe_path = nearest_path((x, y), Tile_State.clear)

    tiles[x][y] = remove_state(tiles[x][y], Tile_State.bomb)
    update_fire_of_bombs()

    if safe_path is None:
        return False

    for (_x, _y) in safe_path[1:]:
        if bomb_risk((_x, _y)) or has_state(tiles[_x][_y], Tile_State.player):
            return False

    if not reachable(safe_path, bombRange):
        if not bomb_risk(safe_path[1]):
            return True

    return False


def safe_to_move(_path):
    for tile in _path:
        if bomb_risk(tile):
            return False
    return True


def can_move_to_upgrade(upgrade_state):
    path1 = nearest_path((x, y), upgrade_state)

    if path1 is None:
        return False
    if len(path1) > vision and upgrade_state != Tile_State.upgrade_health:
        return False

    if bomb_risk(path1[1]):
        return False

    if not isOtherPlayerInVision:
        return True

    path2 = nearest_path((otherX, otherY), upgrade_state)
    if path2 is None:
        return True

    for (_x, _y) in dirs(path1[1][0], path1[1][1]):
        if (_x != x or _y != y) and has_state(tiles[_x][_y], Tile_State.player):
            return False

    return len(path1) - len(path2) <= 0


def deadzone_risk():
    dzStep = 1 + (stepCount - dzStart) / dzDelay

    if dzStep < -1.2:
        return False

    # if (x, y) in safe_zone(dzStep):
    #     return False
    #
    # if (x, y) in safe_tiles:
    #     return True

    return True


def single_box():
    _path = nearest_path((x, y), Tile_State.box)
    if _path is None:
        return None
    elif len(_path) == 2:
        return _path[0]
    elif reachable(_path, bombRange) and can_escape_after_bomb():
        return _path[0]
    elif len(_path) > vision and (stepCount - dzStart) / dzDelay > -3:
        return nearest_path_to_center((x, y))[1]
    else:
        return _path[1]


def best_box_path(start):
    n = len(boxes)

    if n < 2:
        return single_box()

    targets = []

    for n1 in range(n - 1):
        for n2 in range(n1 + 1, n):
            box1 = boxes[n1]
            box2 = boxes[n2]

            if distance(box1, box2) == 1:
                continue

            if box1[0] != box2[0] and box1[1] != box2[1]:

                x1, y1 = (box1[0], box2[1])
                x2, y2 = (box2[0], box1[1])

                if x1 < height and y1 < width and \
                        (not forbidden(tiles[x1][y1]) or (x1 == x and y1 == y)):
                    if reachable_box((x1, y1), box1) and reachable_box((x1, y1), box2):
                        targets.append((x1, y1))

                if x2 < height and y2 < width and \
                        (not forbidden(tiles[x2][y2]) or (x2 == x and y2 == y)):
                    if reachable_box((x2, y2), box1) and reachable_box((x2, y2), box2):
                        targets.append((x2, y2))

    targets.sort(key=lambda pos: distance(pos, (x, y)))

    queue = collections.deque([[start]])
    seen = {start}

    if len(targets) == 0:
        return single_box()

    if (x, y) in targets:
        if can_escape_after_bomb():
            return x, y
        else:
            return single_box()

    target = targets[0]

    while queue:

        _path = queue.popleft()
        _x, _y = _path[-1]

        if (_x, _y) == target:
            if _path is None:
                return single_box()
            elif len(_path) > vision:
                return single_box()
            elif len(_path) >= 2:
                return _path[1]
            else:
                return _path[0]
        for x2, y2 in [(_x + 1, _y), (_x, _y - 1), (_x - 1, _y), (_x, _y + 1)]:

            if 0 <= x2 < height and 0 <= y2 < width and (x2, y2) not in seen and \
                    (not forbidden(tiles[x2][y2]) or (x2, y2) == target):
                queue.append(_path + [(x2, y2)])
                seen.add((x2, y2))


def reachable_box(start, end):
    xbomb, ybomb = start
    xbox, ybox = end

    if distance((x, y), start) > vision and visibleBoxesCount > 0:
        return False

    if xbox == xbomb:
        if abs(ybox - ybomb) > bombRange:
            return False
        for _y in range(min(ybomb, ybox) + 1, max(ybomb, ybox)):
            if forbidden(tiles[xbomb][_y]) and not has_state(tiles[xbomb][_y], Tile_State.player):
                return False

    if ybox == ybomb:
        if abs(xbox - xbomb) > bombRange:
            return False
        for _x in range(min(xbomb, xbox) + 1, max(xbomb, xbox)):
            if forbidden(tiles[_x][ybomb]) and not has_state(tiles[_x][ybomb], Tile_State.player):
                return False

    tiles[xbomb][ybomb] = add_state(tiles[xbomb][ybomb], Tile_State.target)
    _path = nearest_path((x, y), Tile_State.target)
    tiles[xbomb][ybomb] = remove_state(tiles[xbomb][ybomb], Tile_State.target)

    return _path is not None


def nearest_path_to_center(start):
    queue = collections.deque([[start]])
    seen = {start}

    temp_safe = []
    for (_x, _y) in safe_tiles:
        if not forbidden(tiles[_x][_y]):
            temp_safe.append((_x, _y))

    min_dist = 0
    if len(temp_safe) == 0:
        min_dist = max(width, height)
        for _x in range(height):
            for _y in range(width):
                dist = distance((_x, _y), center)
                if dist < min_dist and has_state(tiles[_x][_y], Tile_State.clear):
                    min_dist = dist

    while queue:

        _path = queue.popleft()
        _x, _y = _path[-1]

        if (_x, _y) in temp_safe or (len(temp_safe) == 0 and distance(center, (_x, _y)) <= min_dist):
            return _path if _path is not None else nearest_path(start, Tile_State.clear)
        for x2, y2 in dirs(_x, _y):

            if (x2, y2) not in seen and \
                    has_state(tiles[x2][y2], Tile_State.clear):
                queue.append(_path + [(x2, y2)])
                seen.add((x2, y2))


def final_standing():
    if not deadzone_risk():
        return False

    return (x, y) in safe_tiles


traps = []
boxes = []
upgrades = []


def safe_zone(*step):
    h = height
    w = width

    stp = -1
    if step != ():
        stp = step[0]

    zone = np.zeros((h, w), dtype=tuple)
    for _x in range(h):
        for _y in range(w):
            zone[_x][_y] = (_x, _y)

    k = 0
    while zone.shape[0] > 2 and zone.shape[1] > 2:
        zone = np.delete(zone, 0, 0)
        zone = np.delete(zone, h - 2 - k, 0)
        zone = np.delete(zone, 0, 1)
        zone = np.delete(zone, w - 2 - k, 1)
        k += 2
        if stp != -1:
            stp -= 1
            if stp == 0:
                result = []
                for k, value in np.ndenumerate(zone):
                    if not forbidden(tiles[value[0]][value[1]]):
                        result.append(value)
                return result

    result = []
    for k, value in np.ndenumerate(zone):
        if not forbidden(tiles[value[0]][value[1]]):
            result.append(value)
    return result


safe_tiles = []

while True:
    # Getting input from engine
    raw_inp = input()

    boxes.clear()
    visibleBoxesCount = 0

    if len(safe_tiles) == 0:
        safe_tiles = safe_zone()

    for i in range(height):
        for j in range(width):
            if has_state(tiles[i][j], Tile_State.player) and (i != x or j != y):
                tiles[i][j] = remove_state(tiles[i][j], Tile_State.player)

            if has_state(tiles[i][j], Tile_State.bomb) and not bomb_risk((x, y)):
                tiles[i][j] = remove_state(tiles[i][j], Tile_State.bomb)

    # Termination stage
    if 'term' in raw_inp:
        break

    # Extracting info from loop message
    inp = list(map(int, raw_inp.split()[:-1]))

    stepCount, lastAction, x, y, health, healthUpgradeCount, bombRange, trapCount, isOtherPlayerInVision = inp[:9]

    tilesBaseIndex = 9
    if isOtherPlayerInVision:
        otherX = inp[9]
        otherY = inp[10]
        otherHealth = inp[11]
        tilesBaseIndex += 3

    visibleBombsCount = 0
    visibleUpgradesCount = 0

    for i in range(inp[tilesBaseIndex]):
        tileX = inp[tilesBaseIndex + (3 * i) + 1]
        tileY = inp[tilesBaseIndex + (3 * i) + 2]
        tileState = inp[tilesBaseIndex + (3 * i) + 3]
        tiles[tileX][tileY] = tileState

        # Count the number visible boxes
        if has_state(tileState, Tile_State.box):
            visibleBoxesCount += 1
            boxes.append((tileX, tileY))

        if has_state(tileState, Tile_State.bomb):
            visibleBombsCount += 1

        if has_state(tileState, Tile_State.upgrade_health) \
                or has_state(tileState, Tile_State.upgrade_trap):
            visibleUpgradesCount += 1
            upgrades.append((tileX, tileY))

    # Deciding our next move...

    response = None
    path = None

    try:

        update_fire_of_bombs()
        update_traps()

        response = place_trap()
        if response is not None:
            print(response)
            continue

        elif isOtherPlayerInVision and not bomb_risk((x, y)) and visibleUpgradesCount == 0:
            path = path_to_other_player()
            if path is not None:
                if reachable(path, bombRange) and can_escape_after_bomb():
                    response = Action.place_bomb.value
                    print(response)
                    continue

        if deadzone_risk():

            if bomb_risk((x, y)):
                path = nearest_path((x, y), Tile_State.clear)
                if path is not None:
                    response = move(path[1])
                    print(response)
                    continue

            if final_standing():
                response = Action.stay.value
                print(response)
                continue

            path = nearest_path_to_center((x, y))
            if path is None:
                response = Action.stay.value
            elif len(path) == 1:
                response = Action.stay.value
            elif bomb_risk(path[1]):
                response = Action.stay.value
            else:
                response = move(path[1])

        elif can_move_to_upgrade(Tile_State.upgrade_health):
            path = nearest_path((x, y), Tile_State.upgrade_health)
            response = move(path[1])


        elif can_move_to_upgrade(Tile_State.upgrade_trap):
            path = nearest_path((x, y), Tile_State.upgrade_trap)
            response = move(path[1])


        elif can_move_to_upgrade(Tile_State.upgrade_range) and bombRange < maxBombRange:
            path = nearest_path((x, y), Tile_State.upgrade_range)
            response = move(path[1])

        elif bomb_risk((x, y)):
            path = nearest_path((x, y), Tile_State.clear)
            if path is None:
                response = Action.stay.value
            else:
                response = move(path[1])


        elif visibleBombsCount > 1 and visibleBoxesCount > 1 \
                or visibleBombsCount > 1 and visibleUpgradesCount > 1:
            response = Action.stay.value

        elif state_exist(Tile_State.box):
            next_move = best_box_path((x, y))

            if next_move is None:
                response = Action.stay.value
            elif (x, y) == next_move:
                if (visibleBoxesCount != 1 or visibleBombsCount != 1) and can_escape_after_bomb():
                    response = Action.place_bomb.value
                else:
                    response = Action.stay.value

            elif not bomb_risk(next_move) and not trap_risk(next_move):
                response = move(next_move)
            else:
                response = Action.stay.value


        else:
            if state_exist(Tile_State.bomb):
                response = Action.stay.value
            else:
                path = nearest_path_to_center((x, y))
                if path is None:
                    path = nearest_path((x, y), Tile_State.clear)
                response = move(path[1])

    except Exception as ex:
        response = Action.stay.value

    print(f'{response}')
