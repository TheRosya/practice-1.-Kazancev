import math
import matplotlib.pyplot as plt
from dataclasses import dataclass, field

freq_equality_for_5GG = {
    36: 5180,
    40: 5200,
    44: 5220,
    48: 5240,
    52: 5260,
    56: 5280,
    60: 5300,
    64: 5320,
    100: 5500,
    104: 5520,
    108: 5540,
    112: 5560,
    116: 5580,
    120: 5600,
    124: 5620,
    128: 5640,
    132: 5660,
    136: 5680,
    140: 5700,
    149: 5745,
    153: 5765,
    157: 5785,
    161: 5805,
}

freq_equality_for_2_4GG = {
    1: 2412,
    2: 2417,
    3: 2422,
    4: 2427,
    5: 2432,
    6: 2437,
    7: 2442,
    8: 2447,
    9: 2452,
    10: 2457,
    11: 2462,
    12: 2467,
    13: 2472,
    14: 2484,
}


@dataclass
class Channel:
    chanell_number: int
    diapason: str
    freq: int = field(init=False)

    def __post_init__(self):
        self.freq = (
            freq_equality_for_5GG[self.chanell_number]
            if self.diapason == "5"
            else freq_equality_for_2_4GG[self.chanell_number]
        )


GG = {
    "2.4": {6: -87, 9: -86, 12: -85, 18: -83, 24: -80, 36: -76, 48: -71, 54: -66},
    "5": {15: -96, 30: -95, 45: -92, 60: -90, 90: -86, 120: -83, 135: -77, 150: -74},
}


SOM = 10

P: int = ...
Gt: int = ...
Gr: int = ...


chanel1 = Channel(chanell_number=..., diapason="2.4")
chanel2 = Channel(chanell_number=..., diapason="2.4")

chanel3 = Channel(chanell_number=..., diapason="5")
chanel4 = Channel(chanell_number=..., diapason="5")


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
