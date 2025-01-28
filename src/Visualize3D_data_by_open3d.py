"""
pip install open3d

"""

import open3d as o3d
import numpy as np
import os
import pandas as pd

data=pd.read_csv(os.path.join(os.path.dirname(__file__), '../data/ice.csv'))

x = data['temp'].values
y = data['street'].values
z = data['ice'].values

minX = np.min(x)
maxX = np.max(x)
minY = np.min(y)
maxY = np.max(y)
minZ = np.min(z)
maxZ = np.max(z)

nrData = len(x)

points = []

for i in range(nrData):
    X = (x[i] - minX) / (maxX - minX)
    Y = (y[i] - minY) / (maxY - minY)
    Z = (z[i] - minZ) / (maxZ - minZ)
    points.append((X, Y, Z))
    #points.append((x, y, z))

# 点群オブジェクトを作成
point_cloud = o3d.geometry.PointCloud()
point_cloud.points = o3d.utility.Vector3dVector(points)

# ビジュアライザーを作成
vis = o3d.visualization.Visualizer()
vis.create_window()

# 点群を追加
vis.add_geometry(point_cloud)

# 点のサイズを設定
opt = vis.get_render_option()
opt.point_size = 30.0  # 点のサイズを30に設定

# 座標軸の作成 (デフォルトでサイズは0.5)
coordinate_frame = o3d.geometry.TriangleMesh.create_coordinate_frame(size=1)

# 座標軸をVisualizerに追加
vis.add_geometry(coordinate_frame)

# 表示
vis.run()
vis.destroy_window()