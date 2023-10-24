'''
_______________________________________________________________________________#

 File    : xbee_sender.py
 Author  : Badr Bacem KAABIA
 Version : 0.3
 Date    : 29 August 2020
 Brief   : Xbee simple sender example : Sending "Hello Xbee" message periodically
 from Xbee node to another.
_______________________________________________________________________________

 Copyright 2021, badrbacekaabia@gmail.com.

 Permission to use, copy, modify, and/or distribute this software for any
 purpose with or without fee is hereby granted, provided that the above
 copyright notice and this permission notice appear in all copies.

 THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
 WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
 MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
 ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
 WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
 ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
 OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
_______________________________________________________________________________#
'''

# Imports
# --------------------- #
from __future__ import absolute_import
import argparse
from time import sleep
import sys
import logging
from digi.xbee.devices import RemoteXBeeDevice, XBeeDevice, XBee64BitAddress
from digi.xbee.exception import TimeoutException, TransmitException, InvalidOperatingModeException, XBeeException
from serial.serialutil import SerialException


# Defines
# --------------------- #
COM_PORT = "/dev/pts/8"
COM_SPEED = 9600
LOOP_PERIOD_S = 2

logging.basicConfig(format='[%(asctime)s] - %(levelname)s : %(lineno)d - %(message)s', \
                    level = logging.DEBUG, datefmt='%m-%d-%Y %I:%M:%S')

def wait_s(period_sec):
    """Do loading

    Args:
        period_sec (int): delay in seconds
    """
    for i in range(period_sec, 0, -1):
        sleep(1)
        sys.stdout.write("\u001b[1000D" + "Waiting " + str(i - 1) + " seconds")
        sys.stdout.flush()
    print("")


def main():
    """
    Main function
    """
    print("""
    +----------------------------------------------+
    |       Xbee Data Sender Receiver Example      |
    +----------------------------------------------+
    """)

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", help="COM port", default=COM_PORT)
    parser.add_argument("-s", help="COM speed", default=COM_SPEED)
    parser.add_argument("-r", help="Remote Xbee MAC address", default="0013A20041723B63")
    parser.add_argument("-t", help="period in seconds", default=LOOP_PERIOD_S)
    parser.add_argument("-b", help="broadcast", default=False)
    args = parser.parse_args()
    # Create non-remote generic XBee device
    device = XBeeDevice(args.c, args.s)

    try:
        logging.info("Starting Xbee device...")
        # Open device
        device.open()
    except SerialException as err:
        logging.error(repr(err))
        sys.exit(0)

    # Instantiate a remote XBee device object.
    remote_device = RemoteXBeeDevice(device, XBee64BitAddress.from_hex_string(args.r))
    while True:
        try:
            msg = bytearray("Hello Xbee".encode())
            logging.info("Sending data to %s >> %s", remote_device.get_64bit_addr(), list(msg))
            device.send_data(remote_device, msg)
            wait_s(int(args.t))
        except (TimeoutException, TransmitException, InvalidOperatingModeException, XBeeException) as err:
            logging.error(repr(err))
        finally:
            if device is not None and device.is_open():
                device.close()

# run tests if called from command-line
if __name__ == "__main__":
    main()
