import math
import matplotlib.pyplot as plt
from dataclasses import dataclass


@dataclass
class Channel:
    chanell_number: int
    freq: int
    diapason: str


GG = {
    "2.4": {6: -87, 9: -86, 12: -85, 18: -83, 24: -80, 36: -76, 48: -71, 54: -66},
    "5": {15: -96, 30: -95, 45: -92, 60: -90, 90: -86, 120: -83, 135: -77, 150: -74},
}

SOM = 10

P: int = ...
Gt: int = ...
Gr: int = ...


chanel1 = Channel(chanell_number=..., freq=..., diapason="2.4")
chanel2 = Channel(chanell_number=..., freq=..., diapason="2.4")

chanel3 = Channel(chanell_number=..., freq=..., diapason="5")
chanel4 = Channel(chanell_number=..., freq=..., diapason="5")


def calc(chan: Channel) -> list[str | list[int]]:
    mbits: list[int] = []
    metr: list[int] = []
    frequencies = GG[chan.diapason]
    print(f"{chan.diapason}ГГц канал {chan.chanell_number}, Частота: {chan.freq}")
    for speed, dB in frequencies.items():
        Ydb = P + Gt + Gr - dB
        FSL = Ydb - SOM
        D = 10 ** (((FSL - 33) / 20) - math.log10(chan.freq))
        Dmetr = int(D * 1000)
        print(f"Mbit: {speed}, Ydb: {Ydb}, FSL: {FSL}, D: {Dmetr}м")
        mbits.append(speed)
        metr.append(Dmetr)
    return [mbits, metr, "ro", mbits, metr]


plt.plot(
    *calc(chanel1),
    *calc(chanel2),
    *calc(chanel3),
    *calc(chanel4),
)
plt.xlabel("Мбит/сек")
plt.ylabel("Метры")
plt.grid(True)
plt.show()
