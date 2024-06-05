# LiveKeeper
A Python Library helps to keep your scripts alive on free hosting platforms.
Made within 5m by me. so if you got any issues please post it.

# Installation
After downloading the lib, unzip it. Then run the following command on the same dir:
```pip install .```

# Usage Example

```python
from LiveKeeper import LiveKeeper
from time import sleep

def example(): # example of a function you want to run on free hosting services
  while not sleep(2):
    print(1)


LiveKeeper.run() # and that's it!
```
