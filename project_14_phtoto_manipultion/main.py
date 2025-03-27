import cv2
import numpy as np
import streamlit as st
from PIL import Image
import io

def process_image(image, filter_type, blur_size, low_threshold, high_threshold, edge_color):
    image_cv = np.array(image)
    image_cv = cv2.cvtColor(image_cv, cv2.COLOR_RGB2BGR)
    
    processed = image_cv.copy()
    
    if filter_type == "Grayscale":
        processed = cv2.cvtColor(processed, cv2.COLOR_BGR2GRAY)
        processed = cv2.cvtColor(processed, cv2.COLOR_GRAY2BGR)
    elif filter_type == "Sepia":
        kernel = np.array([[0.272, 0.534, 0.131],
                         [0.349, 0.686, 0.168],
                         [0.393, 0.769, 0.189]])
        processed = cv2.transform(processed, kernel)
    elif filter_type == "Negative":
        processed = cv2.bitwise_not(processed)
    
    if blur_size > 1:
        blur_size = blur_size if blur_size % 2 == 1 else blur_size + 1
        processed = cv2.GaussianBlur(processed, (blur_size, blur_size), 0)
    
    gray = cv2.cvtColor(processed, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, low_threshold, high_threshold)
    
    edge_mask = np.zeros_like(processed)
    edge_mask[edges != 0] = edge_color
    
    highlighted_edges = cv2.addWeighted(processed, 1, edge_mask, 0.7, 0)
    
    edges_only = np.ones_like(processed) * 255
    edges_only[edges != 0] = edge_color
    
    original_rgb = cv2.cvtColor(image_cv, cv2.COLOR_BGR2RGB)
    highlighted_edges = cv2.cvtColor(highlighted_edges, cv2.COLOR_BGR2RGB)
    edges_only = cv2.cvtColor(edges_only, cv2.COLOR_BGR2RGB)
    
    return original_rgb, highlighted_edges, edges_only

def main():
    st.title("Advanced Edge Detection")
    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        
        st.sidebar.header("Image Processing Parameters")
        
        filter_type = st.sidebar.selectbox(
            "Choose Filter",
            ["None", "Grayscale", "Sepia", "Negative"]
        )
        
        blur_size = st.sidebar.slider(
            "Blur Kernel Size",
            1, 21, 5, 2,
            help="Higher values increase blur (must be odd)"
        )
        
        low_threshold = st.sidebar.slider("Low Threshold", 0, 255, 60)
        high_threshold = st.sidebar.slider("High Threshold", 0, 255, 150)
        
        edge_color_rgb = st.sidebar.color_picker("Edge Color", "#00FF00")
        r = int(edge_color_rgb[1:3], 16)
        g = int(edge_color_rgb[3:5], 16)
        b = int(edge_color_rgb[5:7], 16)
        edge_color = (b, g, r)
        
        original, highlighted, edges_only = process_image(
            image, filter_type, blur_size, low_threshold, high_threshold, edge_color
        )
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.image(original, caption="Original Image", use_container_width=True)
        
        with col2:
            st.image(highlighted, caption="Highlighted Edges", use_container_width=True)
        
        with col3:
            st.image(edges_only, caption="Edges Only", use_container_width=True)
        
        result = np.hstack((original, highlighted, edges_only))
        result_pil = Image.fromarray(result)
        buf = io.BytesIO()
        result_pil.save(buf, format="PNG")
        byte_im = buf.getvalue()
        
        st.download_button(
            label="Download Result",
            data=byte_im,
            file_name="processed_image_result.png",
            mime="image/png"
        )
        


if __name__ == "__main__":
    main()