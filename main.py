import math
import matplotlib.pyplot as plt
from dataclasses import dataclass, field
from config import *
from constants import *
from typing import Union


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


chanel1 = Channel(chanell_number=channel, diapason="2.4")
chanel2 = Channel(chanell_number=channel2, diapason="2.4")

chanel3 = Channel(chanell_number=channel3, diapason="5")
chanel4 = Channel(chanell_number=channel4, diapason="5")


def calc(chan: Channel) -> list[Union[str, list[int]]]:
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


plt.plot(  # type: ignore
    *calc(chanel1),
    *calc(chanel2),
    *calc(chanel3),
    *calc(chanel4),
)
plt.xlabel("Мбит/сек")  # type: ignore
plt.ylabel("Метры")  # type: ignore
plt.grid(True)  # type: ignore
plt.show()  # type: ignore
