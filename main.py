import math
import matplotlib.pyplot as plt
from dataclasses import dataclass


@dataclass
class Channel:
    name: str
    freq: int
    diapason: str


P = 11
Gt = 2
Gr = 3

G24 = {6: -87, 9: -86, 12: -85, 18: -83, 24: -80, 36: -76, 48: -71, 54: -66}

G5 = {15: -96, 30: -95, 45: -92, 60: -90, 90: -86, 120: -83, 135: -77, 150: -74}

chanel1 = Channel(name="1", freq=2412, diapason="2.4")
chanel2 = Channel(name="9", freq=2452, diapason="2.4")

chanel3 = Channel(name="112", freq=5560, diapason="5")
chanel4 = Channel(name="157", freq=5785, diapason="5")


def calc(chan: Channel, huiny: dict[int, int]) -> list[str | list[int]]:
    mbits: list[int] = []
    metr: list[int] = []
    print(f"{chan.diapason}G канал {chan.name}, Частота: {chan.freq}")
    for key, val in huiny.items():
        Ydb = P + Gt + Gr - val
        FSL = Ydb - 10
        D = 10 ** (((FSL - 33) / 20) - math.log10(chan.freq))
        Dmetr = int(D * 1000)
        print(f"Mbit: {key}, Ydb: {Ydb}, FSL: {FSL}, D: {Dmetr}м")
        mbits.append(key)
        metr.append(Dmetr)
    return [mbits, metr, "ro", mbits, metr]


plt.plot(
    *calc(chan=chanel1, huiny=G24),
    *calc(chan=chanel2, huiny=G24),
    *calc(chan=chanel3, huiny=G5),
    *calc(chan=chanel4, huiny=G5),
)
plt.grid(True)
plt.show()
