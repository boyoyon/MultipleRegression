"""
最高気温、通行人数とアイスクリーム売上の関係を
CatBoostRegressorで曲面に当てはめる

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from catboost import CatBoostRegressor, FeaturesData, Pool
from mpl_toolkits.mplot3d import Axes3D
import japanize_matplotlib
import joblib, os

def main():
    data=pd.read_csv(os.path.join(os.path.dirname(__file__), '../data/ice.csv'))
    x=data[['temp','street']]
    y=data['ice']

    train_pool = Pool(data=x, label=y)
    test_pool = Pool(data=x)

    #model = CatBoostRegressor(iterations=200, learning_rate=0.05, depth=5)
    #model = CatBoostRegressor(iterations=2000, learning_rate=0.05, depth=10)
    model = CatBoostRegressor(iterations=2000, learning_rate=0.05, depth=10, langevin=True)
    model.fit(train_pool)

    joblib.dump(model, 'CatBoostRegressor.pkl')
    print('save CatBoostRegressor.pkl')

    range_temp = np.arange(x['temp'].min(), x['temp'].max())
    range_street = np.arange(x['street'].min(), x['street'].max())

    len_temp = len(range_temp)
    len_street = len(range_street)

    u, v = np.meshgrid(range_temp, range_street)
    x = np.c_[u.ravel(), v.ravel()]

    p=model.predict(x)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    temp = u.reshape((len_temp, len_street))
    street = v.reshape((len_temp, len_street))
    ice = p.reshape((len_temp, len_street))

    ax.plot_surface(temp, street, ice, cmap='summer')

    plt.title("アイスクリーム売り上げ")
    plt.xlabel("最高気温")
    plt.ylabel("通行人数")

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
