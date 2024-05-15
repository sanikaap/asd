import streamlit as st
import cv2
import threading
import numpy as np

# Global variables to manage the camera stream and threading
capture = None
stop_thread = False
frame_placeholder = None

def app():
    global capture, stop_thread, frame_placeholder

    def start_camera():
        global capture, stop_thread, frame_placeholder

        # Initialize the camera capture
        capture = cv2.VideoCapture(0)
        
        while not stop_thread:
            # Capture frame-by-frame
            ret, frame = capture.read()
            if ret:
                # Convert the frame to RGB (Streamlit uses RGB format)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # Update the frame placeholder with the new frame
                frame_placeholder.image(frame, channels="RGB")
    
        # Release the capture
        capture.release()

    def stop_camera():
        global capture, stop_thread

        # Stop the thread and release the capture
        stop_thread = True
        if capture is not None:
            capture.release()
        st.write("Camera stopped")

    # Streamlit UI
    st.title("Webcam Stream")

    # Buttons to start and stop the camera
    if st.button("Start Camera"):
        stop_thread = False
        frame_placeholder = st.empty()
        camera_thread = threading.Thread(target=start_camera)
        camera_thread.start()

    if st.button("Stop Camera"):
        stop_camera()
    st.divider()
    uploaded_file = st.file_uploader("Upload a file", type=['txt', 'csv', 'pdf'])

    if uploaded_file is not None:
    # Read and display the file
      file_contents = uploaded_file.read()
      st.write(file_contents)
      st.divider()
if __name__ == '__main__':
    app()
