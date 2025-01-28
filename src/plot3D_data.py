import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import japanize_matplotlib
import os

def main():
    data=pd.read_csv(os.path.join(os.path.dirname(__file__), '../data/ice.csv'))

    temp = data['temp'].values
    street = data['street'].values
    ice = data['ice'].values

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter3D(temp, street, ice)

    plt.title("アイスクリーム売り上げ")
    plt.xlabel("最高気温")
    plt.ylabel("通行人数")

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()