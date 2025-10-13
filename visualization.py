
import matplotlib.pyplot as plt
import pandas as pd

def visualize_data():
    df = pd.read_csv('crowd_data.csv')

    # Plotting the density of the crowd (X vs Y position)
    plt.hexbin(df['x'], df['y'], gridsize=50, cmap='Blues')
    plt.colorbar(label='Density')
    plt.title('Crowd Density Heatmap')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.show()

if __name__ == "__main__":
    visualize_data()
