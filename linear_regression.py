from data_normalization import normalized_x_data,normalized_y_data
import matplotlib.pyplot as plt

def Linear_Regression(X,Y): # szuka alfy [a] i bety [b]  g(x)=a*x+b
    n=len(X)
    Exy=0
    Ex=0
    Ey=0
    Ex_2=0
    # E-suma, Ex_2- suma x do kwadratu
    for i in range(n):
        Exy=Exy+X[i]*Y[i]
        Ex =Ex+ X[i]
        Ey=Ey +Y[i]
        Ex_2=Ex_2+X[i]*X[i]
    a=(Exy-Ex*Ey)/(Ex_2-Ex*Ex)
    b=(1/n)*Ey-a*(1/n)*Ex
    # takie smieszne wzorki na wyliczenie alfe i bete
    return (a,b)


def plot_linear_regression(a, b, normalizedX, normalizedY):
    # Create the plot
    plt.scatter(normalizedX, normalizedY, color='black', label='Data Points')

    # Generate x values in the range [min(normalizedX), max(normalizedX)]
    x_values = [min(normalizedX), max(normalizedX)]

    # Calculate y values using the linear function y = ax + b
    y_values = [a * x + b for x in x_values]

    # Plot the linear regression line
    plt.plot(x_values, y_values, color='y', label='Linear Regression')

    # Add labels and title
    plt.xlabel('Normalized X')
    plt.ylabel('Normalized Y')
    plt.title('Linear Regression')

    # Add a legend
    plt.legend()

    # Show the plot
    plt.grid(True)
    plt.show()

alfa,beta = Linear_Regression(normalized_x_data,normalized_y_data)
plot_linear_regression(alfa,beta,normalized_x_data,normalized_y_data)

