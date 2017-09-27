# progressBar
A tiny class for simulating task progress in a bar graph on terminal output


## Synopsis
I figured sometimes we need a distraction while waiting for large processes to complete. The progressBar class provides minimal simulation of an actual progressbar in the terminal output.

## Requirements
* Python 2.7 or above

## Installation
* `git clone https://github.com/codexceed/progressBar/`

## Usage Example
``` from progress import ProgressBar as pb
x = [1,2,3,4,5,6,79898,8,9,10,123,1314,1241241412,12412412] # list of iterables to show progress of

prog = pb(x, 'printing ') # pb object takes in 2 arguments, the iterable list and the progress status message (optional)

for i in x:
    prog.updateBar() # call the updateBar() function on the start of every task in the list
    time.sleep(2)
prog.endBar # call the endBar() function to mark the end of the list
```
