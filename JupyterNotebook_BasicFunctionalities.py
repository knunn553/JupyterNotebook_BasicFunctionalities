# %%
print('Hello People!')

# %%
import time
time.sleep(3)

# %%
def say_hello(recipient):
    return 'Hello, {}!'.format(recipient)

say_hello('Kyle')

# %%


# %%
# A green outline means the cell is in edit mode and a blue outline means the cell is in command mode.
# We press either A or B to insert new cell above or below an active cell. Must do this in command mode, though.
# M will transform the active cell to a markdown cell.
# Y will set the active cell to a code cell.
# D + D will delete the active cell but it has to be in command mode (blue).
# Z will undo cell deletion

# %%
# Ctrl + Shift + - will split the active cell at the cursor
# Hold Shift + Up/Down arrow to select multiple cells at once. Shift + M with merge you selection 


# %%
# Behind every notebook runs a kernel.
import numpy as np
def square(x):
    return x * x

# %%


# %%
x = np.random.randint(1,10)
y = square(x)
print('%d squared is %d' % (x,y))

# %%
print('Is %d Squared %d?' % (x,y))

# %%
y = 10
print('Is %d Squared %d?' % (x,y))

# %%
# Import pandas() to work with our data, matplotlib() to create charts, Seaborn() to make our charts prettier.
# Its also common to import Numpy(), but in this case pandas() imports it for us.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")


# %%
# Need to set the working directory to import the data set.
!pwd
!ls # This helps to see where your files are located! Big help.
!ls * .csv

# %%
pwd

# %%
!cd /Users/kylenunn/Desktop

# %%
!pwd