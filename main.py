import logging
import os

filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test.log")
logging.basicConfig(filename=filename, level=logging.DEBUG)
logging.debug("Matplotlib is loaded for rendering the icon")

from yahoo_fin import stock_info as si
import subprocess
import time
import threading
import sys


def popup(name, value, _increase):
    if _increase > 0:
        subprocess.Popen(
            [
                "notify-send",
                "-i",
                "GraphUp",
                name + " Share Price",
                "Current Value: " + str(value) + "\n Increased by: " + str(_increase),
            ]
        )
    else:
        subprocess.Popen(
            [
                "notify-send",
                "-i",
                "GraphDown",
                name + " Share Price",
                "Current Value: " + str(value) + "\n Decreased by: " + str(_increase),
            ]
        )


def fetch_stock(name):
    data = si.get_quote_table(name)
    return data


class StockObject(object):
    def __init__(self, name, refresh_time):
        self.name = name
        self.interval = refresh_time
        self.stop = False

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def _stop(self):
        self.stop = True
        logging.debug("Process is being Killed")

    def run(self):
        while True:
            logging.debug(f"Fetching Data for {self.name} stock")
            data = fetch_stock(self.name)
            popup(
                self.name,
                round(data["Quote Price"], 2),
                round(round(data["Quote Price"], 2) - data["Previous Close"], 2),
            )
            if self.stop:
                return
            time.sleep(self.interval)


if __name__ == "__main__":
    NAME = str(sys.argv[1])
    TIME = int(sys.argv[2])
    example = StockObject(NAME, TIME)
    time.sleep(int(sys.argv[3]))
    example._stop()

