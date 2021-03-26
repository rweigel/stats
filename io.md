See also
* https://realpython.com/read-write-files-python/
* https://www.geeksforgeeks.org/reading-writing-text-files-python/

File Input (reading) and Output (writing)

# Writing Files

## One Line

Write one line to a file:

```Python
file = open("file1line.txt", "w")
file.write("Line 1")
file.close()
```

Look at the file size -- it should be 6 bytes. Each character requires one byte of storage.

The following does the same as above using a the "context manager" approach. The key differences are that the file does not need to be closed and if an error occurs when trying to open the file, the file is closed.

```Python
# Preferred method
with open("file1line.txt", "w") as file:
    file.write("Line 1")
```

## Multiple Lines

Write multiple lines to a file. The string `\n` is a special code that starts a new line.

```Python
file = open("file10lines.txt", "w")
for i in range(10):
    file.write("Line {0:d}\n".format(i))
file.close()
```

Same as above using a "context manager".

```Python
with open("file10lines.txt", "w") as file:
    for i in range(10):
        file.write("Line {0:d}\n".format(i))
```

## Multiple Files with Multiple Lines

```Python
for j in range(5):
    # Note the 02d used in the following line.
    fname = "multifile_{0:02d}.txt".format(j)
    print("Writing", fname)
    with open(fname, "w") as file:
        for i in range(10):
            file.write("Line {0:d}\n".format(i))
    print("Wrote", fname)
```

Here I have introduced the format code <code>02d</code> in place of <code>d</code>. 

The <code>02</code> means that the number should take up two spaces and any blank spaces should be replaced with zeros.

```Python
print("{0:02d}".format(9))  # 09
print("{0:02d}".format(10)) # 10
```

This is done so the files appear in order when listed by a file explorer.

## Multiple Figures

First attempt.

```Python
from matplotlib import pyplot as plt
import numpy as np

x = np.arange(0, 10)
y = x**2

for i in range(len(x)):
    plt.plot(x[0:i], y[0:i])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(['$y=x^2$'])
    plt.draw()
    fname = "animate_{0:02d}.png".format(i)
    print("Writing", fname)
    plt.savefig(fname, dpi=300)
    print("Wrote", fname)
```

In the first attempt, when `i=0`, nothing is plotted. This can be corrected by modifying the indices. In addition, the labels were rendered on every iteration, which can slow down an animation. 

```Python
from matplotlib import pyplot as plt
import numpy as np

x = np.arange(0, 10)
y = x**2

for i in range(len(x)-1):
    plt.plot(x[0:i+1], y[0:i+1], 'k-', marker='.')
    if i == 0:
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend(['$y=x^2$'])
        plt.xlim([0, 8])
        plt.ylim([0, 70])
        plt.grid()
    plt.draw()
    fname = "animate_{0:02d}.png".format(i)
    print("Writing", fname)
    plt.savefig(fname, dpi=300)
    print("Wrote", fname)
```

## The <code>csv</code> module

## <code>numpy.savetxt</code>

## <code>pandas.to_csv</code>


# Reading Files

* https://www.geeksforgeeks.org/reading-writing-text-files-python/
* https://janakiev.com/blog/csv-in-python/
* https://www.geeksforgeeks.org/working-csv-files-python/

## `read` and `seek`

The <code>read</code> method reads a given number of bytes from a file. By default, the bytes are assumed to be formatted as ASCII.

```Python
# Create file to read
with open("file.txt", "w") as file: file.write("Line 1\nLine 2")
    
with open("file.txt", "r") as file:
    a = file.read(1) # Read first byte
    b = file.read(1) # Read second byte
    c = file.read(2) # Read 3-4th byte

print(a) # L
print(b) # i
print(c) # ne
```

The <code>seek</code> method jumps a given number of bytes in a file so that the next read starts on the next byte.

This function is useful for extracting a small part from a large file - one does not need to read the entire file or loop through all rows in a file.

```Python
# Create file to read
with open("file.txt", "w") as file: file.write("Line 1\nLine 2")
    
with open("file.txt", "r") as file:
    file.seek(3) # Move to just after 4th byte
    a = file.read(1) # Read 4th byte
    b = file.read(2) # Read 5th and 6th byte
print(a) # e
print(b) #  1
```

The most basic pattern for reading a file in any programming language is

1. Loop through each byte
2. Accumulate bytes
3. If a pattern is found store accumulated bytes
4. Restart accumulation and then repeat steps 3. and 4. until the end of the file

The following program reads each byte in a file and appends it to <code>s</code>. It also displays <code>Found newline</code> when a newline character is found.

```Python
# Create file to read
with open("file.txt", "w") as file: file.write("Line 1\nLine 2")

s = "" # Will contain full string
with open("file.txt", "r") as file:
    tmp = file.read(1)      # Read 1st byte
    while tmp:              # Loop until end of file
        if tmp is "\n":     # Check byte contents
            print('Found newline')
        s = s + tmp         # Append byte to previous bytes
        tmp = file.read(1)  # Read next byte

print(s) 
# Line 1
# Line 2
```

```Python
# Create file to read
with open("file.txt", "w") as file: file.write("Line 1\nLine 2")

s = "" # Will contain full string
lines = []
with open("file.txt", "r") as file:
    tmp = file.read(1)      # Read 1st byte
    while tmp:              # Loop until end of file
        if tmp is "\n":     # Check byte contents
            lines.append(s) # If newline found put it in lines list
            s = ""          # Reset accumulator
        else:
            s = s + tmp     # Append byte to previous bytes
        tmp = file.read(1)  # Read next byte

# If the last character in the file is not a newline, then lines.append(s)
# will not be executed. This catches that case.
if tmp is not "\n":
    lines.append(s)

print(lines) # ['Line 1', 'Line 2']
```

## `readline`

Reading a file byte-by-byte is inefficient and requires many lines of code. The <code>readline</code> and <code>readlines</code> method are generally the first methods you should attempt to use when reading any text file.

In general, <code>readline</code> should be used when only a few lines of the file are to be read or when you want to do an operation on each line that is read.

The following program reads each line into a list named <code>lines</code>.

```Python
# Create file to read
with open("file.txt", "w") as file: file.write("Line 1\nLine 2")

lines = []
with open("file.txt", "r") as file:
    line = file.readline()      # Read one line
    while line:                 # Loop until end of file
        lines.append(line)      # Append line to lines list
        line = file.readline()  # Read next line
        
print(lines) # ['Line 1\n', 'Line 2']
```

As an example of operating on each line, the following program removes the newline character (if found) from each line read.

```Python
# Create file to read
with open("file.txt", "w") as file: file.write("Line 1\nLine 2")

lines = []
with open("file.txt", "r") as file:
    line = file.readline()      # Read one line
    while line:                 # Loop until end of file
        line = line.replace("\n", "") # Replace newline with nothing
        line = line.replace("L", "l") # Replace L with l
        lines.append(line)      # Append line to lines list
        line = file.readline()  # Read next line
        
print(lines) # ['line 1', 'line 2']
```

## <code>readlines</code>

In general, one wants to read the entire contents of a file into a list and then loop over the contents of a list and modify the elements in a list. This may be faster than doing the operation and file reading in the same loop.

The basic syntax is

```Python
# Create file to read
with open("file.txt", "w") as file: file.write("Line 1\nLine 2")

with open("file.txt", "r") as file:
    lines = file.readlines() # Read all lines into a list
        
print(lines) # ['Line 1\n', 'Line 2']
```

Next, consider a typical data file, in which the first line contains the names of the columns and the subsequent lines are data. The first step is to read the file and inspect the generated list.

```Python
# Create file to read
with open("file.txt", "w") as file: file.write("a b\n1 2\n3 4")

# Read file and inspect list
with open("file.txt", "r") as file:
    lines = file.readlines()
print(lines) # ['a b\n', '1  2\n', '3  4']
```

Next, we want to create a list for the contents of each column. First, we experiment with the first data line

```Python
# Create file to read
with open("file.txt", "w") as file: file.write("a b\n1 2\n3 4")

# Read file
with open("file.txt", "r") as file: lines = file.readlines()

a = []
b = []
print(lines[1]) 		# Print second line in file (first data line)
line = lines[1].split() # Split second line on whitespace 
print(line)
a.append(float(line[0])) # Store first column value in list a
b.append(float(line[1])) # Store second column value in list b
print(a) # [1.0]
print(b) # [1.0]
```

Finally, we loop through entire file contents.

```Python
# Create file to read
with open("file.txt", "w") as file: file.write("a b\n1 2\n3 4")

# Read file
with open("file.txt", "r") as file: lines = file.readlines()

# Loop through entire list returned by readlines
a = []
b = []
for i in range(1, len(lines)): # 
    print(lines[i])      # Display line for debugging
    l = lines[i].split() # Split on whitespace
    print(l)             # Display split line for debugging
    a.append(float(l[0])) # Store first element of l in list a
    b.append(float(l[1])) # Store second element of l in list a

h = lines[0].split() # Extract first line of file and split

print(h[0]) # Use header information to display first column's name
print(a)    # [1.0, 3.0]
print(h[1]) # Use header information to display second column's name
print(b)    # [2.0, 4.0]
```

## The <code>csv</code> module

In the previous example, we had to split each row on whitespace. The <code>csv</code> module can do this automatically (and much more).

```Python
# Create file to read
with open("file.txt", "w") as file: file.write("a b\n1 2\n3 4")

import csv
rows = []
with open("file.txt", 'r') as file:     
    csvreader = csv.reader(file, delimiter = ' ', skipinitialspace=True)
    for row in csvreader: 
        rows.append(row) 
print(rows) # [['a', 'b'], ['1', '2'], ['3', '4']]

a = []
b = []
for i in range(1, len(rows)):
    a.append(float(rows[i][0]))
    b.append(float(rows[i][1]))
print(a) # [1.0, 3.0]
print(b) # [2.0, 4.0]
```

Note that a more efficient way of extracting the columns is to use the <code>asarray</code> method from NumPy.

```Python
import numpy as np

# rows[1:] is all rows except first.
# dtype=np.float tells NumPy the type of data
# the elements should be converted to
A = np.asarray(rows[1:], dtype=np.float) 
print(A)
# A is now a NumPy array and we can slice on columns.
a = A[:,0] # Extract first column of A
b = A[:,1] # Extract second column of A
print(a) # [1. 3.]
print(b) # [2. 4.]
```

## <code>numpy.genfromtext</code>

## <code>pandas.read_csv</code>

# Problems

## Basic CSV File

Write a program that creates the following file named <code>HW8_1.csv</code> exactly

<pre>
t [s], x [m], y [m]
0,  1.0, 2.0
10, 2.0, 4.0
20, 3.0, 6.0
30, 4.0, 8.0
40, 5.0, 10.0
50, 6.0, 12.0
</pre>

Write a program that reads <code>HW8_1.csv</code> and plots on the same axes <code>x</code> vs. <code>t</code> and <code>y</code> vs. <code>t</code>. Include units on your axis labels.

<details>
  <summary><b>Answer</b></summary>

```Python
t = [0, 10, 20, 30, 40, 50]
x = [1, 2, 3, 4, 5, 6]
y = [2, 4, 6, 8, 10, 12]

with open('HW8_1.csv', "w") as file:
    file.write('t [s], x [m], y [m]\n')
    for i in range(len(t)):
    	# Extra space on first data line was not intentional.
    	# I accepted answer without extra space. Here is one
    	# way to insert it.
        pad = ''
        if i == 0:
            pad = ' '
        file.write('{0:d}, {1:s}{2:.1f}, {3:.1f}\n'
                   .format(t[i], pad, x[i], y[i]))

with open('HW8_1.csv', "r") as file:
    lines = file.readlines()

t = []
x = []
y = []    
for i in range(1, len(lines)):
    line = lines[i].split(',')
    t.append(int(line[0]))
    x.append(float(line[1]))
    y.append(float(line[2]))

from matplotlib import pyplot as plt

plt.plot(t, x)
plt.plot(t, y)
plt.xlabel('t [s]')
plt.legend(['x [m]', 'y [m]'])
plt.grid()
```
</details>


## Write Many Log Files

Write a program that creates files with dates as names according to

```
 20191023.csv
 20191024.csv
 ...
 20191121.csv
 ```

Each file should have the timestamp for all minutes in a day as the first column and the minute of the day as the second column. 

For example, the first file <code>20191024.csv</code> should have 1440 lines

```
 2019-10-23T00:00, 0
 2019-10-23T00:01, 1
 ...
 2019-10-23T23:59, 1439
```

The last file  <code>20191121.csv</code> should have

```
 2019-11-21T00:00, 0
 2019-11-21T00:01, 1
 ...
 2019-11-21T23:59, 1439
```

Save your program as <code>HW8_2.py</code> and upload it to Bitbucket. When executed, I should see the requested files generated.

<details>
  <summary><b>Answer</b></summary>

```Python
for d in range(23, 32):
    fname = "201910{0:02d}.csv".format(d)
    with open(fname, "w") as file:
        i = 0
        for h in range(0, 24):
            for m in range(0, 60):
                file.write("2019-10-{0:02d}T{1:02d}:{2:02d}, {3:d}\n"
                           .format(d, h, m, i))
                i = i + 1

for d in range(1, 22):
    fname = "201911{0:02d}.csv".format(d)
    with open(fname, "w") as file:
        i = 0
        for h in range(0, 24):
            for m in range(0, 60):
                file.write("2019-10-{0:02d}T{1:02d}:{2:02d}, {3:d}\n"
                           .format(d, h, m, i))
                i = i + 1
```
</details>

## Read SSN File Using <code>readlines</code>

Download the file [http://www.sidc.be/silso/DATA/SN_d_tot_V2.0.txt SN_d_tot_V2.0.txt] from [http://www.sidc.be/silso/datafiles]. Information about the contents of the file is given at http://www.sidc.be/silso/datafiles and http://www.sidc.be/silso/infosndtot.

1. Use the <code>readlines</code> method to read the decimal day-of-year and sunspot number columns (columns 4 and 5) into lists named <code>ddy</code> and <code>ssn</code>

2. Plot <code>ssn</code> versus <code>ddy</code>.
3. Compute the mean and std of <code>ssn</code> excluding invalid values (indicated by <code>ssn=-1</code> as per the documentation).

Save your program as <code>HW8_3.py</code> and upload it to Bitbucket. When executed, I should see the requested plot and a print statement of the form

 SSN mean = X, SSN std = Y, Number of valid values = Z

Where <code>X</code> and <code>Y</code> are printed with one significant figure and <code>Z</code> is printed as an integer.

<details>
  <summary><b>Answer</b></summary>

```Python
from os import path
import urllib.request
from matplotlib import pyplot as plt
import numpy as np


# Download and save file from web if not found
file = 'SN_d_tot_V2.0.txt'
if not path.exists(file):
    url = 'http://www.sidc.be/silso/DATA/SN_d_tot_V2.0.txt'
    urllib.request.urlretrieve(url, file)

# Read as CSV file
with open(file, "r") as file:
    lines = file.readlines() # Read all lines into a list

ddy = []
ssn = []
for i in range(1, len(lines)): # 
    #print(lines[i])      # Display line for debugging
    l = lines[i].split() # Split on whitespace
    # print(l)             # Display split line for debugging
    # If ssn (5th column) is not -1, store it
    if float(l[5]) != -1:
        ddy.append(float(l[3])) # Store 4th column
        ssn.append(float(l[4])) # Store 5th column

Nr = len(lines)-len(ssn)
print('Number removed: {0:d}; Fraction removed: {1:.2f}'
      .format(Nr, Nr/len(lines)))

# Convert to numpy ndarray. Could also do calculation in loop w/o NumPy
# Problem statement said one significant figure, but should have said one
# decimal place. Both answers accepted.
ssn = np.asarray(ssn)
print('SSN mean = {0:.1e}, SSN std = {1:.1e}, Number of valid values = {2:d}'
      .format(np.mean(ssn), np.std(ssn), len(ssn)))
# Problem statement should have asked for two decimal places ...
print('SSN mean = {0:.2f}, SSN std = {1:.2f}, Number of valid values = {2:d}'
      .format(np.mean(ssn), np.std(ssn), len(ssn)))      
# SSN mean = 82.95, SSN std = 77.25, Number of valid values = 70471
plt.plot(ddy, ssn)
```
</details>

## Read SSN File Using CSV Module

Use the <code>csv</code> module to read the decimal day-of-year and sunspot number columns and then plot <code>ssn</code> vs. <code>ddy</code>. Save your program as <code>HW8_4.py</code> and upload it to Bitbucket. When executed, I should see the requested plot.

<details>
  <summary><b>Answer</b></summary>

```Python
import csv
import urllib.request
from matplotlib import pyplot as plt

# Download and save file from web
url = 'http://www.sidc.be/silso/DATA/SN_d_tot_V2.0.txt'
urllib.request.urlretrieve(url, 'SN_d_tot_V2.0.txt')

# Method #1: Read file contents into list then loop through list
# and populate ddn and ssn lists.
rows = []
with open("SN_d_tot_V2.0.txt", 'r') as file:
    csvreader = csv.reader(file, delimiter= ' ', skipinitialspace = True)   
    for row in csvreader: 
        rows.append(row) 

ssn = []
ddn = []
for i in range(len(rows)):
    ddn.append(float(rows[i][3]))
    ssn.append(float(rows[i][4]))

plt.plot(ddn, ssn)
plt.xlabel('Year')
plt.ylabel('SSN')
plt.grid()


# Method #2 read each row and populate ddn and ssn lists as each row is read
rows = []
ssn = []
ddn = []
with open("SN_d_tot_V2.0.txt", 'r') as file:
    csvreader = csv.reader(file, delimiter= ' ', skipinitialspace = True)   
    for row in csvreader: 
        ddn.append(float(row[3]))
        ssn.append(float(row[4]))
    
from matplotlib import pyplot as plt

plt.plot(ddn, ssn)
plt.xlabel('Year')
plt.ylabel('SSN')
plt.grid()
```
</details>

## Read SSN File using `datetime` Objects

For background information on <code>datetime</code> objects, see [[Notes#datetimes|datetimes]].

In the previous problem, you plotted the ssn versus the fractional day-of-year. In this problem, use the first three columns to create a list named <code>t</code> containing <code>datetime</code> objects. Then plot <code>ssn</code> versus <code>t</code>.

If done correctly, printing the first two values of <code>t</code> using <code>print(t[0:2])</code> should result in

    [datetime.datetime(1818, 1, 1, 0, 0), datetime.datetime(1818, 1, 2, 0, 0)]

which shows that the list <code>t</code> contains datetime objects.

Save your program as <code>HW8_5.py</code> and upload it to Bitbucket. When executed, I should see the requested plot.

<details>
  <summary><b>Answer</b></summary>

```Python
from os import path
import csv
import urllib.request
from datetime import datetime
from matplotlib import pyplot as plt

# Download and save file from web if not found
file = 'SN_d_tot_V2.0.txt'
if not path.exists(file):
    url = 'http://www.sidc.be/silso/DATA/SN_d_tot_V2.0.txt'
    urllib.request.urlretrieve(url, file)

# Read as CSV file
rows = []
with open("SN_d_tot_V2.0.txt", 'r') as file:
    csvreader = csv.reader(file, delimiter= ' ', skipinitialspace = True)   
    for row in csvreader: 
        rows.append(row) 

ssn = []
t = []
for i in range(len(rows)):
    y = int(rows[i][0])
    m = int(rows[i][1])
    d = int(rows[i][2])
    t.append(datetime(y, m, d))
    ssn.append(float(rows[i][4]))
    
# Notice that when you zoom in at the month level, the date values
# on the x-axis are correct. Compare this with the previous case where
# only ddn was plotted.    
plt.plot(t, ssn)
plt.xlabel('Year')
plt.ylabel('SSN')
plt.grid()
```
</details>

## Extra Credit I

Re-do the problem of creating many log files using the <code>datetime</code> module. However,

1. Do not use a format statement to generate the timestamps and
2. Have at most one <code>for</code> or <code>while</code> loop

<details>
  <summary><b>Answer</b></summary>

```Python
from datetime import datetime, timedelta

def genlines(d):
    t = np.arange(d, d+dt, dtype='datetime64[m]')
    x = np.arange(1440)
    ts = np.datetime_as_string(t, unit='m')
    dtype = [('Time', (np.str_, 16)), ('x', np.int32)]
    data = np.zeros(ts.size, dtype=dtype)
    data['Time'] = ts
    data['x'] = x
    return data

t1 = datetime(2019, 10, 23)
t2 = datetime(2019, 11, 22)

dt = t2 - t1
n = dt.days
dt = timedelta(days=1)
    
import numpy as np
for i in range(n):
    d = t1 + i*dt
    ds = d.isoformat()
    fname = ds[0:10].replace("-", "") + ".csv"
    lines = genlines(d)
    np.savetxt(fname, lines, fmt='%s, %d', delimiter=',')
```
</details>

<details>
  <summary><b>Answer</b></summary>

```Python
minutes_per_day= 1440

from datetime import datetime, timedelta
 
ti = datetime(2020, 10, 23, hour=0, minute=0)
tf = datetime(2020, 11, 22, hour=0, minute=0)

t_current = ti
#print(t_current)

dt_minutes = timedelta(days=0, hours=0, minutes=1)

counter_time = 0
num_of_days = 0

while ( (counter_time <= minutes_per_day) and (t_current < tf) ):        
    if (counter_time == 0):
        fname = t_current.strftime('%Y%m%d.csv')
        print(fname)
        file = open(fname, "w")        
        print("Writing #1",t_current.isoformat())
        file.write(t_current.isoformat())
        file.write(',')
        file.write(str(counter_time))
        file.write('\n')
        counter_time = counter_time + 1            
    if (counter_time > 0):        
        t_current = t_current + dt_minutes
        file.write(t_current.isoformat())
        file.write(',')
        file.write(str(counter_time))
        file.write('\n')
        counter_time = counter_time + 1            
    if (counter_time == minutes_per_day):
        counter_time = 0        
        num_of_days = num_of_days + 1
        t_current = t_current + dt_minutes
        file.close()    
</details>

<details>
  <summary><b>Answer</b></summary>

```Python
from datetime import datetime, timedelta, timezone
t1 = datetime(2019, 10, 23, 
              hour=0, minute=0, second=0, 
              microsecond=0, tzinfo=timezone.utc)
t2 = datetime(2019, 11, 21, 
              hour=23, minute=59, second=0, 
              microsecond=0, tzinfo=timezone.utc)
dt = timedelta(minutes=1, seconds=0, microseconds=0)
mins=0
while t1<=t2:
      filename=t1.strftime('%Y%m%d.csv')#filename
      with open(filename, "a") as file:
           ts=t1.strftime('%Y-%m-%dT%H:%M, ')+str(mins)+'\n' 
           file.write(ts)
           t1=t1+dt
           if t1.hour==0 and t1.minute==0:
              mins=0
           else:
              mins=mins+1
```
</details>

## Extra Credit II

Write a program to read and plot the content of the files generated in the previous problem. Then plot the contents using only one <code>plot</code> statement. When executed, I should see a plot similar to the one shown below.

<img src="https://raw.githubusercontent.com/rweigel/513/master/Hw1.1_RungeKatta54.png">

[[Image:HW8_ECII.png|500px]]

<details>
  <summary><b>Answer</b></summary>

```Python
from datetime import datetime, timedelta
import numpy as np
from matplotlib import pyplot as plt

t1 = datetime(2019, 10, 23)
t2 = datetime(2019, 11, 22)

dt = t2 - t1
n = dt.days
dt = timedelta(days=1)
dtype = [('Time', (np.str_, 16)), ('x', np.int32)]

x = []
t = []
for i in range(n):
    d = t1 + i*dt
    ds = d.isoformat()
    fname = ds[0:10].replace("-", "") + ".csv"
    data = np.genfromtxt(fname, dtype=dtype, delimiter=',')
    t.append(np.array(data['Time'], dtype='datetime64'))
    x.append(data['x'])
    
plt.plot(np.array(t).flatten(), np.array(x).flatten())
```
</details>

<details>
  <summary><b>Answer</b></summary>

```Python
import matplotlib.pyplot as plt
import csv
from datetime import datetime, timedelta, timezone
t = []
ssn = []
dat =[]
t1 = datetime(2019, 10, 23, 
              hour=0, minute=0, second=0, 
              microsecond=0)
t2 = datetime(2019, 11, 21, 
              hour=23, minute=59, second=0, 
              microsecond=0)
dt = timedelta(days=1)
mins=0
while t1<=t2:
    filename=t1.strftime('%Y%m%d.csv')#filenamewith open("20191024.csv", 'r') as file:     
    with open(filename, 'r') as file:
        csvreader = csv.reader(file, delimiter = ',', skipinitialspace=True)
        for row in csvreader: 
             dat=[] 
             dat2=[] 
             dat3=[]
             dat=row[0].split("-",3)
             dat2=dat[2].split("T", 1)
             dat3=dat2[1].split(":",1)
             t1=datetime(int(dat[0]), int(dat[1]), int(dat2[0]), int(dat3[0]), int(dat3[1]))
             t.append(t1)
             ssn.append(float(row[1]))
        t1=t1+dt
plt.plot(t, ssn, '-', linewidth=1)
plt.xlabel('Date')
plt.ylabel('Number of Seconds')
plt.grid()
plt.title('Seconds per day')
```
</details>


## Write One File

Write a program that creates the following file named <code>a.csv</code> _exactly_

```
0, 1.0
1, 2.0
2, 3.0
4, 4.0
5, 5.0
6, 6.0
```

Before checking the file size, predict what it will be.

----

Write a program that creates the following file named <code>b.csv</code> _exactly_

```
t, x, y
0, 1.0, 11.00
1, 2.0, 12.00
2, 3.0, 13.00
4, 4.0, 14.00
5, 5.0, 15.00
6, 6.0, 16.00
```

## Write Many Log Files

Write a program that creates files with dates as names according to

```
 20191023.csv
 20191024.csv
 ...
 20191121.csv
```

Each file should have the timestamp for all minutes in a day as the first column and the minute of the day as the second column. 

For example, the first file <code>20191024.csv</code> should have 1440 lines

```Python
 2019-10-23T00:00, 0
 2019-10-23T00:01, 1
 ...
 2019-10-23T23:59, 1439
```

The last file  <code>20191121.csv</code> should have

```Python
 2019-11-21T00:00, 0
 2019-11-21T00:01, 1
 ...
 2019-11-21T23:59, 1439
```

## Write Many Images

Write a program that creates an animation of a sine wave over one period. There should be a total of 24 frames and each frame should have a new point.

## <code>read</code> and <code>seek</code>

The following program creates 10 files. Write a program that reads the 9th byte of each file and stores them in a list named <code>L</code>.

```Python
for i in range(10):
    with open("{0:d}.txt".format(i), "w") as file: 
        file.write("12345678" + str(i))
```

Do this using only the <code>read</code> (and optionally <code>seek</code>) function (e.g., not <code>readline</code> or <code>readlines</code>, etc.)

The last line of your program should be <code>print(L)</code> and should result in the display

```
 ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
```

## `readlines`

Download the file [http://www.sidc.be/silso/DATA/SN_d_tot_V2.0.txt SN_d_tot_V2.0.txt] from [http://www.sidc.be/silso/datafiles]. Information about the contents of the file is given at http://www.sidc.be/silso/datafiles and http://www.sidc.be/silso/infosndtot.

1. Use the <code>readlines</code> method to read the decimal day-of-year and sunspot number columns (columns 4 and 5) into lists named <code>ddy</code> and <code>ssn</code>
2. Use the <code>csv</code> module to read the decimal day-of-year and sunspot number columns (columns 4 and 5).

Plot <code>ssn</code> versus <code>ddy</code>.

Optional: Do this using [https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.genfromtxt.html <code>genfromtxt</code>]. Do not hand-edit the data file.