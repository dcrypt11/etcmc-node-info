# Etcmc Node Info
Extract info from running ETCMC node and exports it in a web accessible json.
It contains transactions count, balance, cpu and ram usage

## Before using
- Install [python](https://www.python.org/downloads/) on your device
- Install **web** and **screen-ocr** libraries with **pip**:<br>pip install web.py==0.61<br>pip install screen-ocr[winrt]
- Clone the repository

## How to use
- Make sure to have your pc resolution set to 1920x1080
- Make sure to have ETCMC Geth running in full screen
- Run the script from cmd with: **python node-info.py**
- Minimize the running script cmd window
- View your json node info by opening a browser and loading http://localhost:8080<br>You can also view the same info in your home network, usig the local IP of your device and port 8080 (for example http://192.168.0.101:8080)

## Additional options
- You can change the port on which the web client will be working. For example, if you want it on port **1234**, you must start the script with:<br>**python node-info.py 1234**