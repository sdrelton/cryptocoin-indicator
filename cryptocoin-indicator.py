# Author: Samuel D. Relton
# Email: samuel.relton@manchester.ac.uk
# Website: www.samrelton.com
# BTC Tips: 1N1cN6V4AwcibwzSXC2fywB6NorSwRAEpd

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import GObject as gobject
import signal
import os
import urllib
import json

APPINDICATOR_ID = "cryptocoin-indicator"

# Notes: Change icon dynamically with indicator.set_icon()

# Global variable for function to collect updated prices
# Default to BTCUSD on BitFinex
global currentupdate

# Quit indicator
def quit(source):
    gtk.main_quit()

##############################
# Update Prices
##############################

###############
# BitFinex
###############
# Update BTC with BitFinex
def update_btcusd_bitfinex():
    url = r"https://api.bitfinex.com/v1/ticker/btcusd"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    price = data["last_price"]
    price = str(round(float(price), 3))
    mystring = "BTCUSD: " + price
    return mystring

def set_update_btcusd_bitfinex(source):
    global currentupdate
    currentupdate = update_btcusd_bitfinex

# Update ETH with BitFinex
def update_ethbtc_bitfinex():
    url = r"https://api.bitfinex.com/v1/ticker/ethbtc"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    price = data["last_price"]
    price = str(round(float(price), 7))
    mystring = "ETHBTC: " + price
    return mystring

def set_update_ethbtc_bitfinex(source):
    global currentupdate
    currentupdate = update_ethbtc_bitfinex

def update_ltcusd_bitfinex():
    url = r"https://api.bitfinex.com/v1/ticker/ltcusd"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    price = data["last_price"]
    price = str(round(float(price), 4))
    mystring = "LTCUSD: " + price
    return mystring

def set_update_ltcusd_bitfinex(source):
    global currentupdate
    currentupdate = update_ltcusd_bitfinex

###############
# BTC-e
###############
def update_btcusd_btce():
    url = r"https://btc-e.com/api/3/ticker/btc_usd"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    price = data["btc_usd"]["last"]
    price = str(round(float(price), 3))
    mystring = "BTCUSD: " + price
    return mystring

def set_update_btcusd_btce(source):
    global currentupdate
    currentupdate = update_btcusd_btce

def update_ethbtc_btce():
    url = r"https://btc-e.com/api/3/ticker/eth_btc"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    price = data["eth_btc"]["last"]
    price = str(round(float(price), 7))
    mystring = "ETHBTC: " + price
    return mystring

def set_update_ethbtc_btce(source):
    global currentupdate
    currentupdate = update_ethbtc_btce

def update_ltcusd_btce():
    url = r"https://btc-e.com/api/3/ticker/ltc_usd"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    price = data["ltc_usd"]["last"]
    price = str(round(float(price), 4))
    mystring = "LTCUSD: " + price
    return mystring

def set_update_ltcusd_btce(source):
    global currentupdate
    currentupdate = update_ltcusd_btce

###############
# Bitinka
###############
# Update BTC with BitFinex
def update_btcars_bitinka():
    url = r"https://www.bitinka.com.ar/api/apinka/ticker?format=json"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    price = data["ARS"]["ask"]
    price = str(round(float(price), 3))
    mystring = "BTCARS: " + price
    return mystring

def set_update_btcars_bitinka(source):
    global currentupdate
    currentupdate = update_btcars_bitinka

###############
# Ripio
###############
# Update BTC with BitFinex
def update_btcars_ripio():
    url = r"https://www.ripio.com/api/v1/rates/"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    price = data["rates"]["ARS_BUY"]
    price = str(round(float(price), 2))
    mystring = "BTCARS: " + price
    return mystring

def set_update_btcars_ripio(source):
    global currentupdate
    currentupdate = update_btcars_ripio

###############
# SatoshiTango
###############
# Update BTC with BitFinex
def update_btcars_satoshitango():
    url = r"https://api.satoshitango.com/v2/ticker"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    price = data["data"]["compra"]["arsbtc"]
    price = str(round(float(price), 3))
    mystring = "BTCARS: " + price
    return mystring

def set_update_btcars_satoshitango(source):
    global currentupdate
    currentupdate = update_btcars_satoshitango

##############################
# Initialization
##############################
# Default to BTCUSD from BitFinex
currentupdate = update_btcusd_bitfinex

# Update prices
def update_price(indicator):
    curprice = currentupdate()
    indicator.set_label(curprice, "BTCUSDX: 1000.32112")
    return True

##############################
# Create menu
##############################
def build_menu():
    menu = gtk.Menu()

    # Which price to display
    btcusd_bitfinex = gtk.MenuItem("BTCUSD: BitFinex")
    btcusd_bitfinex.connect("activate", set_update_btcusd_bitfinex)
    menu.append(btcusd_bitfinex)

    ethbtc_bitfinex = gtk.MenuItem("ETHBTC: BitFinex")
    ethbtc_bitfinex.connect("activate", set_update_ethbtc_bitfinex)
    menu.append(ethbtc_bitfinex)

    ltcusd_bitfinex = gtk.MenuItem("LTCUSD: BitFinex")
    ltcusd_bitfinex.connect("activate", set_update_ltcusd_bitfinex)
    menu.append(ltcusd_bitfinex)

    # Separator
    menu.append(gtk.SeparatorMenuItem())

    btcusd_btce = gtk.MenuItem("BTCUSD: BTC-e")
    btcusd_btce.connect("activate", set_update_btcusd_btce)
    menu.append(btcusd_btce)

    ethbtc_btce = gtk.MenuItem("ETHBTC: BTC-e")
    ethbtc_btce.connect("activate", set_update_ethbtc_btce)
    menu.append(ethbtc_btce)

    ltcusd_btce = gtk.MenuItem("LTCUSD: BTC-e")
    ltcusd_btce.connect("activate", set_update_ltcusd_btce)
    menu.append(ltcusd_btce)

    # Separator
    menu.append(gtk.SeparatorMenuItem())

    btcars_bitinka = gtk.MenuItem("BTCARS: Bitinka")
    btcars_bitinka.connect("activate", set_update_btcars_bitinka)
    menu.append(btcars_bitinka)

    btcars_ripio = gtk.MenuItem("BTCARS: Ripio")
    btcars_ripio.connect("activate", set_update_btcars_ripio)
    menu.append(btcars_ripio)

    btcars_satoshitango = gtk.MenuItem("BTCARS: SatoshiTango")
    btcars_satoshitango.connect("activate", set_update_btcars_satoshitango)
    menu.append(btcars_satoshitango)

    # Separator
    menu.append(gtk.SeparatorMenuItem())

    # Quit
    item_quit = gtk.MenuItem("Quit")
    item_quit.connect("activate", quit)
    menu.append(item_quit)
    menu.show_all()
    return menu

##############################
# Main function
##############################
def main():
    # Set up indicator

    indicator = appindicator.Indicator.new(APPINDICATOR_ID,
                                       os.path.abspath('cryptocoin-indicator.svg'),
                                       appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())

    indicator.set_label("BTCUSD: ...", "BTCUSD: 1000.32")

    # Allow stop signal
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    # Update prices every 2 seconds
    updatetimer = gobject.timeout_add(20000, update_price, indicator)

    # Start main loop
    gtk.main()


if __name__ == "__main__":
    main()
