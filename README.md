# Brain Tumor Detection with YOLOv11
_Brain tumor detection with Computer Vision YOLOv11 model. This model identifies a box that indicate tumor locations in MRI (Magnetic Resonance Imaging)._


On the first part, i did the read_img_label.py to load the images and show that with cv2 with polygon that indicate the tumor location.

## Dataset
The data comes ready to train, with yaml, the labels and images.

The dataset live in ```data/```, (I'll put it in a gitignore), I download this dataset in [kaggle](https://www.kaggle.com/datasets/pkdarabi/medical-image-dataset-brain-tumor-detection/data).

The dataset comes with train/DEV/valid split:
```
data/train -> /labels or /images
data/test -> /labels or /images
data/valid -> /labels or /images
```
In ```configs/``` you can find ```data.yaml``` 

## The run code of show_all_img.py
![print segmentation instance](docs\exemple_segIns_with_class.png)
Obs: pra fechar antes de acabar todos os caminhos você precisa dar ctrl+c no terminal e fechar a aba.