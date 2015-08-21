# Project
This is a utility that records current internet speed and pushes it to a google form


# Setup
```
# From PyPi
pip install speedrecorder

# From GitHub
pip install git+git://github.com/rweyant/speedtest-cli
```

# Usage

From the command line

```
# Get Internet Speed
python examples/run_simple.py

# Get Internet Speed in a continuous loop
python examples/continuous.py

# Wait 10 minutes in between runs
python examples/continuous.py --delay 10
```

Within a python script

```
import speedrecorder
speedrecorder.speedtest()
speedrecorder.speedtest(quiet=False)
```
