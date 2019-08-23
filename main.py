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
        try:
            subprocess.Popen(
                [
                    "notify-send",
                    "-i",
                    "GraphUp",
                    name + " Share Price",
                    "Current Value: "
                    + str(value)
                    + "\n Increased by: "
                    + str(_increase),
                ]
            )
        except:
            subprocess.Popen(
                [
                    "notify-send",
                    name + " Share Price",
                    "Current Value: "
                    + str(value)
                    + "\n Increased by: "
                    + str(_increase),
                ]
            )

    else:
        try:
            subprocess.Popen(
                [
                    "notify-send",
                    "-i",
                    "GraphDown",
                    name + " Share Price",
                    "Current Value: "
                    + str(value)
                    + "\n Decreased by: "
                    + str(_increase),
                ]
            )
        except:
            subprocess.Popen(
                [
                    "notify-send",
                    name + " Share Price",
                    "Current Value: "
                    + str(value)
                    + "\n Decreased by: "
                    + str(_increase),
                ]
            )


def fetch_stock(name):
    try:
        data = si.get_quote_table(name)
        return data
    except ValueError:
        print("Invalid stock name. Check and try again.")
        logging.debug("Invalid stock name.")
        return None


class IntervalStockObject(object):
    def __init__(self, name, refresh_time):
        self.name = name
        self.interval = refresh_time
        self.stop = False

        self.thread = threading.Thread(target=self.run, args=())
        self.thread.daemon = True
        self.thread.start()

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
    if len(sys.argv) == 3 or len(sys.argv) == 4:
        NAME = str(sys.argv[1])
        if fetch_stock(NAME) != None:
            TIME = int(sys.argv[2])
            example = IntervalStockObject(NAME, TIME)
            if len(sys.argv) == 3:
                example.thread.join()
            elif len(sys.argv) == 4:
                time.sleep(int(sys.argv[3]))
                example._stop()

    else:
        print("Invalid parameters")
        logging.debug("Invalid parameters")

