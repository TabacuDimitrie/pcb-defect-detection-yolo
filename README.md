# pcb-defect-detection-yolo
PCB defect detection using YOLOv8 and the DeepPCB dataset with a Streamlit interface
# PCB Defect Detection using YOLOv8

This project implements an end-to-end PCB defect detection pipeline using YOLOv8 and the DeepPCB dataset.

## Features

- Dataset preprocessing
- Annotation conversion to YOLO format
- YOLOv8 training
- Defect detection inference
- Streamlit interface for image upload


## Dataset

This project uses the **DeepPCB dataset**, a public dataset for PCB defect detection research.

The dataset is not included in this repository due to size.

## Training

```python train.py```

## Detection

```python detect.py```

## Streamlit App

```streamlit run streamlit_app.py```
##Technologies
-Python
-YOLOv8 (Ultralytics)
-Streamlit
-OpenCV
