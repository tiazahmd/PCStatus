# PCStatus
My first GUI app. A small utility app that shows various data about your CPU, GPU, RAM and Storage. Linux only.
A very simple app that uses `Python3.6`, `PyQt5` and Python's `psutil` library to show various stats regarding your computer. This is tested on Ubuntu 18.04 only and some of the features are very Linux specific, so at this point, this app is not cross platform. 

### How to Run:
Requirements:
- Python3.6
- PyQt5 [GUI Framework]
- psutil [Python library]

Edit: Added requirements.txt so that it's easy to install from there.

```
$ gitclone https://github.com/tiazahmd/PCStatus
$ cd PCStatus
$ pip install -r requirements.txt
$ python3 main.py
```
### Screenshot:
![PCStatus Screenshot](https://raw.githubusercontent.com/tiazahmd/PCStatus/master/PCStatus-Screenshot.png)