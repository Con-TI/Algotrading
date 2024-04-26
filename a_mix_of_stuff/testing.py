import matplotlib.pyplot as plt

# Create a figure
fig = plt.figure(figsize=(10, 8))

# Add subplots manually using add_subplot
ax1 = fig.add_subplot(321)
ax2 = fig.add_subplot(322, sharex=ax1)
ax3 = fig.add_subplot(323)
ax4 = fig.add_subplot(324, sharex=ax3)
ax5 = fig.add_subplot(325)
ax6 = fig.add_subplot(326, sharex=ax5)

# Example data for plotting
x = [1, 2, 3, 4, 5]
y1 = [10, 15, 20, 25, 30]
y2 = [5, 10, 15, 20, 25]

# Plotting on each subplot
ax1.plot(x, y1, label='Line 1')
ax2.plot(x, y2, label='Line 2')
ax3.plot(x, y1, label='Line 1')
ax4.plot(x, y2, label='Line 2')
ax5.plot(x, y1, label='Line 1')
ax6.plot(x, y2, label='Line 2')

# Adding legends and labels
for ax in [ax1, ax2, ax3, ax4, ax5, ax6]:
    ax.legend()
    ax.set_xlabel('X-axis Label')
    ax.set_ylabel('Y-axis Label')

# Adjust layout and display the plot
plt.tight_layout()
plt.show()