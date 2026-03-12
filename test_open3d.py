import numpy as np
import open3d as o3d

if __name__ == "__main__":
    for t in range(1, 10):
        pcd = o3d.io.read_triangle_mesh(f"datadump/pcd_frame{t}.ply")
        # print(np.array(pcd.points))
        o3d.visualization.draw(pcd)

        pcd = o3d.io.read_triangle_mesh(f"datadump/pcd_frame{t}_base_coords.ply")
        # print(np.array(pcd.points))
        o3d.visualization.draw(pcd)

        pcd = o3d.io.read_triangle_mesh(f"datadump/pcd_frame{t}_map_coords.ply")
        # print(np.array(pcd.points))
        o3d.visualization.draw(pcd)
