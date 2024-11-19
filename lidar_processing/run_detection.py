import os

def run_detection(kitti_dir, model_cfg, ckpt, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    command = f"""
    python tools/demo.py \
        --cfg_file {model_cfg} \
        --ckpt {ckpt} \
        --data_path {kitti_dir} \
        --save_to {output_dir}
    """
    os.system(command)

if __name__ == "__main__":
    kitti_dir = "output/kitti_format"       # KITTI-format point clouds
    model_cfg = "cfgs/kitti_models/second.yaml"  # Model config file
    ckpt = "checkpoints/second_pytorch.pth" # Path to pre-trained model
    output_dir = "output/detections"        # Output directory for detections

    run_detection(kitti_dir, model_cfg, ckpt, output_dir)
