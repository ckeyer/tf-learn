#!/usr/bin/python3
 
import numpy as np
import sklearn
import pandas as pd
import os
import sys
import time
import tensorflow as tf

from tensorflow import keras

print(sys.version_info)
for module in  np, pd, sklearn, tf, keras:
    print(module.__name__, module.__version__)


