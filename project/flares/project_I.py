import pandas as pd
import matplotlib.pyplot as plt

# Read a file created by data/download.py into a DataFrame
infile = 'data/download.2000.csv'
print(f"Reading {infile}")
df = pd.read_csv(infile)

# Display the first few rows of the DataFrame
print(df.head())

# Extract only rows where the 4th column starts with "M" (r = reduced)
dfr = df[df.iloc[:, 3].astype(str).str.startswith('M')].copy()

# Remove the "X" from the start of the 4th column
dfr.loc[:, dfr.columns[3]] = dfr.iloc[:, 3].str.lstrip('M')

# Get unique values in the 4th column
unique_labels = pd.to_numeric(dfr.iloc[:, 3].unique())

# Convert the 4th column to numbers
dfr.loc[:, dfr.columns[3]] = pd.to_numeric(dfr.iloc[:, 3])

# Convert the second column to datetime
dfr.loc[:, dfr.columns[1]] = pd.to_datetime(dfr.iloc[:, 1])

# Display the first few rows of reduced data frame
print(dfr.head())

# Plot the 4th column vs the second column (timestamp)
plt.figure(figsize=(8.5, 11))
plt.plot(dfr.iloc[:, 1], dfr.iloc[:, 3], 'k.')
plt.yticks(unique_labels, fontsize=8)
plt.xlabel(r'Time of Peak [UTC] (event_peaktime)')
plt.ylabel('Classification')
plt.grid()
plt.title('GOES Event List M-Class Flares')
plt.savefig('project_I.png', dpi=300, bbox_inches='tight')

