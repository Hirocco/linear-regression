import matplotlib.pyplot as plt
from data_normalization import normalized_x_data,normalized_y_data

def visualize(X,Y):
    # Create a scatter plot with black points
    plt.scatter(X, Y, color='black', s=5)

    # Add labels and title
    plt.xlabel('X Values')
    plt.ylabel('Y Values')
    plt.title('Data Visualization')

    # Show the plot
    plt.show()

visualize(normalized_x_data,normalized_y_data)