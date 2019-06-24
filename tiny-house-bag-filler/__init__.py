import logging
import sys
import time

import gpiozero

RELAY_ONE = 'GPIO19' # 35
RELAY_TWO = 'GPIO16' # 36
RELAY_TWO = 'GPIO26' # 37
RELAY_TWO = 'GPIO20' # 38

LOG = logging.getLogger(__name__)

# [JN] Adapted from https://gist.github.com/johnwargo/ea5edc8516b24e0658784ae116628277

# Triggered by the output pin going low: active_high=False.
# Initially off: initial_value=False
relay_one = gpiozero.OutputDevice(RELAY_ONE, active_high=False, initial_value=False)


def set_relay(status):
    if status:
        LOG.info("Setting relay: ON")
        relay_one.on()
    else:
        LOG.info("Setting relay: OFF")
        relay_one.off()


def toggle_relay():
    LOG.info("toggling relay")
    relay_one.toggle()


def main_loop():
    logging.basicConfig(filename='bag-filler.log', level=logging.INFO)
    # start by turning the relay off
    set_relay(False)
    while 1:
        # then toggle the relay every second until the app closes
        toggle_relay()
        # wait a second
        time.sleep(1)


if __name__ == "__main__":
    try:
        main_loop()
    except KeyboardInterrupt:
        # turn the relay off
        set_relay(False)
        LOG.info("\nExiting application\n")
        # exit the application
        sys.exit(0)
