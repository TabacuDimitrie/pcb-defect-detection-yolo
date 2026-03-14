import tempfile
from pathlib import Path

import streamlit as st
from PIL import Image
from ultralytics import YOLO


MODEL_PATH = "runs/detect/train4/weights/best.pt"


@st.cache_resource
def load_model():
    return YOLO(MODEL_PATH)


def main():
    st.set_page_config(page_title="PCB Defect Detection", layout="wide")
    st.title("PCB Defect Detection with YOLO")
    st.write("Încarcă o imagine PCB și modelul va încerca să detecteze defectele.")

    model = load_model()

    uploaded_file = st.file_uploader(
        "Alege o imagine",
        type=["jpg", "jpeg", "png", "bmp"]
    )

    conf = st.slider("Confidence threshold", 0.01, 1.0, 0.10, 0.01)

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Imagine originală")
            st.image(image, use_container_width=True)

        if st.button("Rulează detecția"):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
                temp_path = Path(tmp.name)
                image.save(temp_path)

            results = model.predict(
                source=str(temp_path),
                conf=conf,
                save=False
            )

            result = results[0]
            plotted = result.plot()

            with col2:
                st.subheader("Rezultat")
                st.image(plotted, use_container_width=True)

            boxes = result.boxes

            st.subheader("Detecții")
            if boxes is None or len(boxes) == 0:
                st.info("Nu a fost detectat niciun defect.")
            else:
                for box in boxes:
                    cls_id = int(box.cls[0].item())
                    score = float(box.conf[0].item())
                    class_name = model.names[cls_id]
                    st.write(f"- {class_name} — confidence: {score:.3f}")


if __name__ == "__main__":
    main()