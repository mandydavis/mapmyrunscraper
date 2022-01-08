import matplotlib.pyplot as plt
import pandas

# Read in data
runs_2020 = pandas.read_csv('runs_2020.csv')
# creates a new DF that holds the total count of runs on each data in 2020
count_runs_2020 = runs_2020.groupby(['Date']).count()
print(count_runs_2020)

# Create figure and plot space
fig, ax = plt.subplots(figsize=(10, 10))

# Add x-axis and y-axis
ax.scatter(count_runs_2020.index.values,
        count_runs_2020['Distance'],
        color='purple')

# Set title and labels for axes
ax.set(xlabel="Date",
       ylabel="Number of run activities",
       title="Daily Total Run Activities\nChicagoland area, 2020")

plt.show()