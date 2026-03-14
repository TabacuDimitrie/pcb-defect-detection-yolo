from ultralytics import YOLO

def main():
    model = YOLO("yolov8n.pt")
    
    model.trai(
        data = "data/dataset.yaml",
        epochs = 100,
        batch = 16,
        imgsz = 640
    )

if __name__ == "__main__":
    main()