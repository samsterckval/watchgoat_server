from datetime import datetime


class Device:

    def __init__(self, ip):
        self.ip = ip
        self.last_checkin = datetime.now()