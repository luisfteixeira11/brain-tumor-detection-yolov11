# Brain Tumor Detection with YOLOv11
_Brain tumor detection with Computer Vision YOLOv11 model. This model identifies bouding boxes that indicate tumor locations in MRI (Magnetic Resonance Imaging)._

## Dataset
The data comes ready to train, with yaml, the labels and images (with data augmentation, i think, because have rotations and zoons on it, but i can't prove that).

The dataset live in ```data/```, (I had to put it in a gitignore), I download this dataset in [kaggle](https://www.kaggle.com/datasets/pkdarabi/medical-image-dataset-brain-tumor-detection/data).

The dataset comes with train/DEV/valid split:
```
data/train -> /labels or /images
data/test -> /labels or /images
data/valid -> /labels or /images
```