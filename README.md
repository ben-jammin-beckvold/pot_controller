# pot_controller
2-Step Raspberry Pi controller for a crock pot

This can be used to control anything that switches on/off at certain temperatures. This application is for a crock pot for making yogurt. Just change the temp if you want suvie.

#### Supplies
Raspberry Pi (any version)
[DS18B20 Temperature sensor](https://www.digikey.com/product-detail/en/dfrobot/DFR0198/1738-1311-ND/7597054)
[Power Relay](https://www.digikey.com/product-detail/en/adafruit-industries-llc/2935/1528-1777-ND/6227071)
resistor (anything between 4k-10k will be fine)
Crock pot

#### Software setup
You will need to download a few packages on the Pi. Your Pi probably has many of these already installed.

```sudo apt install python3 python3-pip```

```sudo pip install```


#### Acknowledgements and References
Big ups to [this site](https://electrosome.com/ds18b20-sensor-raspberry-pi-python/) for the temperature setup.
