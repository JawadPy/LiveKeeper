# LiveKeeper
A Python Library helps to keep your scripts alive on free hosting platforms.
Tested on replit.

Made within 5m by me, so if you got any issues please post it.

# Installation
After downloading the zip file, unzip it, then enter the new folder and run the following command:
```pip install .```

# Usage Example
Ex1:
```python
from LiveKeeper import LiveKeeper
from time import sleep

def example(): # example of a function you want to run on free hosting services
  while not sleep(2):
    print(1)


LiveKeeper.run() # and that's it!
```

Ex2:
```python
from LiveKeeper import LiveKeeper
LiveKeeper.run()
print(1)
```

Ex3:
```python
from LiveKeeper import LiveKeeper
print(1)
LiveKeeper.run()
```
