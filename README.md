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


## Pre-Trained Models

This repository uses pre-trained models from the [ILN repository](https://github.com/PinocchioYS/iln).

### Model Details
- **iln_1d_400.pth**: Pre-trained model for resolution-independent LiDAR super-resolution.
- **Copyright**: PinocchioYS, 2022.

For more information, refer to the original ILN repository: [https://github.com/PinocchioYS/iln](https://github.com/PinocchioYS/iln).
