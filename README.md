# Stock-Notifications

Simple utility to track stock prices using popups in python3 written over one unwell schoolnight.

## Tested on:
- Elementary OS Juno

## Running
Start from command line using the commmand if you want it to run till set time: 
```
python3 StockPopUp.py [STOCKNAME] [REFRESH-TIME] [LIVE-TIME] &
OR
python StockPopUp.py [STOCKNAME] [REFRESH-TIME] [LIVE-TIME] &
```
Start from command line using the commmand if you want it to run till forever:
```
python3 StockPopUp.py [STOCKNAME] [REFRESH-TIME]&
OR
python StockPopUp.py [STOCKNAME] [REFRESH-TIME]&
```

## Example Output: 
![Example Output](https://github.com/ParadoxicalNerd/Stock-Notifications/blob/master/example-output.png)

## Notes:
- All time is in seconds
- To get the image in the popup, add the GraphUp.png and GraphDown.png to ~/.local/share/icons
