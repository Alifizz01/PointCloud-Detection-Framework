# PointCloud-Detection-Framework

This project provides a pipeline for object detection using LiDAR point cloud data stored in a rosbag.

## Project Structure
- `rosbag_files/`: Folder to store rosbag files.
- `lidar_processing/`: Scripts for data extraction, conversion, and visualization.
- `models/`: Folder for pre-trained models.
- `data/`: Processed data (e.g., extracted point clouds).
- `output/`: Folder to store detection results.

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Alifizz01/PointCloud-Detection-Framework.git
   cd PointCloud-Detection-Framework
### **5. Add a Sample Rosbag File (Optional)**
If possible, include or link a small example rosbag file in the `rosbag_files/` folder to demonstrate the full pipeline.

---

### **6. Automate the Workflow**
Create a script to automate the entire pipeline (from rosbag extraction to visualization).

#### Script: `run_pipeline.py`
1. Create a new file named `run_pipeline.py`.
2. Add the following content:
   ```python
   import os

   def run_pipeline():
       # Step 1: Extract LiDAR from rosbag
       os.system("python lidar_processing/extract_lidar.py")

       # Step 2: Use ILN Model
       os.system("python lidar_processing/use_iln_model.py")

       # Step 3: Visualize Dense Point Cloud
       os.system("python lidar_processing/visualize_dense_pointcloud.py")

   if __name__ == "__main__":
       run_pipeline()



## Pre-Trained Models

This repository uses pre-trained models from the [ILN repository](https://github.com/PinocchioYS/iln).

### Model Details
- **iln_1d_400.pth**: Pre-trained model for resolution-independent LiDAR super-resolution.
- **Copyright**: PinocchioYS, 2022.

For more information, refer to the original ILN repository: [https://github.com/PinocchioYS/iln](https://github.com/PinocchioYS/iln).
