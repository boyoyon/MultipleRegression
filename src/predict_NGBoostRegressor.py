"""
最高気温、通行人数とアイスクリーム売上の関係を
NGBoostRegressorで曲面に当てはめる

"""
import pandas as pd
import numpy as np
from ngboost.ngboost import NGBoost
from ngboost.learners import default_tree_learner
from ngboost.distns import Normal, LogNormal
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import japanize_matplotlib
import joblib, os, sys

def main():
    
    argv = sys.argv
    argc = len(argv)

    print('%s predicts sales of ice cream using maximum temperature and number of pedestrians' % argv[0])
    print('[usage] python %s <maximum temperature> <number of pedestrians> [<model>]' % argv[0])

    if argc < 3:
        quit()

    temp = int(argv[1])
    street = int(argv[2])

    x = np.array([[temp, street]])

    filename_model = os.path.join(os.path.dirname(__file__), 'NGBoostRegressor.pkl')
    
    if argc > 3:
        filename_model = argv[3]

    ngb_rg = joblib.load(filename_model)

    p = ngb_rg.predict(x)

    print(p[0])

if __name__ == '__main__':
    main()
