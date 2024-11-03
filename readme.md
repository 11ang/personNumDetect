Environment:
Python: 3.9.20
Running software: PyCharm
Running UI: PyQt
Computer graphics card: GPU
Virtual environment: Anaconda3
After installation, create a virtual environment:
conda create -n yolov8 python=3.9
Install PyTorch (GPU version):
pip install torch==2.0.0+cu118 torchvision==0.15.1+cu118 --extra-index-url https://download.pytorch.org/whl/cu118
Install ultralytics library:
pip install ultralytics
Download yolov8 source code:
https://github.com/ultralytics/ultralytics/
The yolov8m.pt model inside is needed.