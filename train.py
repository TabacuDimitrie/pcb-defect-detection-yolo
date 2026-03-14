from ultralytics import YOLO

def main():

    
    model = YOLO("yolov8n.pt")

    model.train(
        data="data/dataset.yaml",
        epochs=30,
        imgsz=640,
        batch=16
    )

if __name__ == "__main__":
    main()
