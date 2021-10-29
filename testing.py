import requests
import json
import os

data = {'ip': {'eth0': "123.123.123.123"}}


def get_password() -> str:
    return "somepass"


def get_serial_apple() -> str:
    command = "ioreg -l | awk '/IOPlatformSerialNumber/ { print $4 }' | sed s/\\\"//g"
    serial = os.popen(command).read().replace("\n", "")
    return serial


if __name__ == "__main__":
    resp = requests.post("http://localhost:5000/goat", json=data, auth=(get_serial_apple(), get_password()))
    print(resp)
    print(resp.text)
