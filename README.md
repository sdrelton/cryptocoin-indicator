# cryptocoin-indicator
Ubuntu indicator for cryptocoin price fluctuations.

Tips (BTC): 1N1cN6V4AwcibwzSXC2fywB6NorSwRAEpd

## About the Project
This Python script places the current price of a currency pair in the indicator panel (near the time and date etc.)
at the top of your screen.
The price updates every 2 seconds to reflect changes in the market.

The following currency pairs and exchanges are currently supported.

|  Exchange  |  Currency Pair |
| ---------- | -------------- |
|  BitFinex  |     BTCUSD     |
|            |     ETHBTC     |
|            |     LTCUSD     |
|   BTC-e    |     BTCUSD     |
|            |     ETHBTC     |
|            |     LTCUSD     |
|   RIPIO    |     BTCARS     |
|SatoshiTango|     BTCARS     |

It is very simple to add new currency pairs, which need not involve a cryptocurrency.

## Installing
The project needs the following Python libraries (which should be pre-installed on your system):
- gi (for Gtk 3.0, AppIndicator3 0.1, and GObject)
- signal
- os
- urllib
- json

Once you have cloned the repository you can start the indicator by opening a terminal,
navigating to the git repository, and typing `python cryptocoin-indicator.py`.
You might also consider adding this to your list of startup applications to run it automatically when logging in.

## Usage
To change currency pairs, simply click on the logo to open the menu and select which pair you would like to track.

Selecting 'Quit' from this menu will terminate the indicator.

## Things to do
There are a number of things which could be improved in the indicator. 
For example:
- adding new currency pairs.
- displaying multiple currency pairs simultaneously.
- getting a better logo.
- adding the ability to change the interval between updates.
