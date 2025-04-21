import asyncio

RATIO = .01

def get_input():
    stops = []
    presents = []
    inp = map(int, input().split())
    while inp:
        stops.append(inp)
        inp = map(int, input().split())
    inp = input().split()
    while inp:
        name, time = inp[0], *map(int, inp[1:])
        presents.append((name, time))

    return stops, presents