#! /usr/bin/env python3
# 
# This file is part of the mosquitto-ServiceDiscovery distribution.
# Copyright (c) 2023 Javier Moreno Garcia.
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License 
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

import ServiceDiscovery
import subprocess
import threading
import sys


class mqttBroker():

    def __init__(self):
        self.broker_discover = ServiceDiscovery.daemon("MQTT_BROKER")


    def run(self):
        threading.Thread(target=lambda : self.broker_discover.run(True), daemon=False).start()
        result = subprocess.call("mosquitto " + " ".join(sys.argv[1:]), shell=True)
        return result


# Main execution
if __name__ == '__main__':

    try:
        mqtt_broker = mqttBroker()
        sys.exit(mqtt_broker.run())


    except KeyboardInterrupt:
        sys.exit(0)
