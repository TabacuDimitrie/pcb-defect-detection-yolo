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

## Technologies
-Python
-YOLOv8 (Ultralytics)
-Streamlit
-OpenCV

## Project Structure
pcb-defect-detection-yolo
│
├── prepare_dataset.py      # convert annotations to YOLO format
├── split_dataset.py        # train/validation split
├── remap_classes.py        # class id remapping
├── train.py                # YOLOv8 training script
├── detect.py               # inference script
├── streamlit_app.py        # Streamlit interface
├── dataset.yaml            # dataset configuration
├── requirements.txt
└── README.md

## How to RUN
Install dependencies:
```pip install -r requirements.txt```
Run detection:
```python detect.py```
Run Streamlit app:
```streamlit run streamlit_app.py```
