# Etcmc Node Info
Extract info from running ETCMC node and exports it in a web accessible json.
It contains transactions count, balance, cpu and ram usage.<br>
The script extracts the information using OCR (Optical Character Recognition), so the ETCMC Geth needs to be opened in the foreground

## Before using
- Install [python](https://www.python.org/downloads/) on your device
- Install **web** and **screen-ocr** libraries with **pip**:<br>pip install web.py==0.61<br>pip install screen-ocr[winrt]
- Clone the repository or download the **node-info.py** script

## How to use
- Make sure to have your pc resolution set to 1920x1080
- Make sure to have ETCMC Geth running in full screen in the foreground
- Run the script just by doble-clicking on **node-info.py** or from cmd with: **python node-info.py**
- Minimize the running script cmd window
- Leave the ETCMC Geth running in the foreground
- View your json node info by opening a browser and loading http://localhost:8080<br>You can also view the same info in your home network, using the local IP of your device and port 8080 (for example http://192.168.0.101:8080)

## Additional options
- You can change the port on which the web client will be working. For example, if you want it on port **1234**, you must start the script from cmd with:<br>**python node-info.py 1234**