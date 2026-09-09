import matplotlib.pyplot as plt

# Define student groups and their numbers
groups = ['Freshman', 'Sophomore', 'Junior', 'Senior']
counts = [300, 250, 275, 225]

# Colors for each slice
colors = ['gold', 'lightcoral', 'lightskyblue', 'yellowgreen']

# Create the pie chart
plt.pie(counts, labels=groups, colors=colors, autopct='%.1f%%', startangle=90)

# Add a title
plt.title('Student Groups Distribution')

# Display the chart
plt.show()
