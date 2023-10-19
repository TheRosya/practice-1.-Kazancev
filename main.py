import math
import matplotlib.pyplot as plt
from dataclasses import dataclass


@dataclass
class Channel:
    name: str
    freq: int
    diapason: str


G24 = {6: -87, 9: -86, 12: -85, 18: -83, 24: -80, 36: -76, 48: -71, 54: -66}

G5 = {15: -96, 30: -95, 45: -92, 60: -90, 90: -86, 120: -83, 135: -77, 150: -74}
SOM = 10

P = 10
Gt = 1
Gr = 1


chanel1 = Channel(name="7", freq=2442, diapason="2.4")
chanel2 = Channel(name="8", freq=2447, diapason="2.4")

chanel3 = Channel(name="100", freq=5500, diapason="5")
chanel4 = Channel(name="153", freq=5765, diapason="5")


def calc(chan: Channel, frequencies: dict[int, int]) -> list[str | list[int]]:
    mbits: list[int] = []
    metr: list[int] = []
    print(f"{chan.diapason}G канал {chan.name}, Частота: {chan.freq}")
    for key, val in frequencies.items():
        Ydb = P + Gt + Gr - val
        FSL = Ydb - SOM
        D = 10 ** (((FSL - 33) / 20) - math.log10(chan.freq))
        Dmetr = int(D * 1000)
        print(f"Mbit: {key}, Ydb: {Ydb}, FSL: {FSL}, D: {Dmetr}м")
        mbits.append(key)
        metr.append(Dmetr)
    return [mbits, metr, "ro", mbits, metr]


plt.plot(
    *calc(chan=chanel1, frequencies=G24),
    *calc(chan=chanel2, frequencies=G24),
    *calc(chan=chanel3, frequencies=G5),
    *calc(chan=chanel4, frequencies=G5),
)
plt.grid(True)
plt.show()
