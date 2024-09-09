#!/usr/bin/python3

# This file is part of TorBox, an easy to use anonymizing router based on Raspberry Pi.
# Copyright (C) 2024 Patrick Truffer
# Contact: anonym@torbox.ch
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it is useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# DESCRIPTION
# This file fetches THREE new bridges. The return values are:
# obfs4 <IP address>:<Port> <Fingerprint> <Certificate> <iat-mode>
# or -1 if fetching the bridge fails over tor and clearnet.
#
# IMPORTANT
# The bridge database delivers only 1-3 bridges approximately every 24 hours,
# of which we pick one. With the bridges already delivered this should be sufficient.
#
# SYNTAX
# Usage: bridges_get.py [OPTIONS]
#
# Options:
#   -n, --network TEXT  Force to get bridges over specific network
#   -c, --country TEXT  Circumvention country setting - <TEXT> has to be in lowercase
#   --snowflake         Get snowflake bridges instead of obfs4 (circumvention
#                       country need to be set)
#   --help              Show this message and exit.
#
# ERROR CODES:
# -1: Network error
# -2: Bridges not found


import click
import sys
import base64
import requests


def get_proxy(network=''):
    # Tor Socks Proxy
    proxy = {
        "http": "socks5h://127.0.0.1:9050",
        "https": "socks5h://127.0.0.1:9050",
    }

    if not network:
        # Check if Tor proxy is up, otherwise set inet network
        try:
            r = requests.get("https://torproject.org", proxies=proxy, timeout=5)
        except:  # noqa
            network = 'inet'

    if network == "inet":
        proxy = {
            "http": "",
            "https": "",
        }
    return proxy



def get_bridges(network):
    bridges = False
    return bridges


def get_circumvention_bridges(country, network, snowflake):
    return False

def main(network, country, snowflake):
    # If country is set get circumvention bridges
    if country:
        bridges = get_circumvention_bridges(country=country, network=network, snowflake=snowflake)
    # BridgeDB obfs4 bridges
    else:
        bridges = get_bridges(network)

    print("\n".join(bridges))


if __name__ == '__main__':
    main()
