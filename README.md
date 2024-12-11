# Face Detection with OpenCV

This project demonstrates a simple face detection application using OpenCV. The program captures video from the webcam, detects faces in real-time, and highlights them with rectangles.

## Features

- Real-time face detection using OpenCV's Haar cascade.
- Simple and lightweight Python application.
- Customizable detection parameters (e.g., `scaleFactor`, `minNeighbors`).

## Prerequisites

- Python 3.6 or higher
- OpenCV library

## Installation

1. Clone the repository or download the project files:
   ```bash
   git clone https://github.com/yourusername/face-detection-opencv.git
   cd face-detection-opencv
   ```

2. Install the required Python packages:
   ```bash
   pip install opencv-python
   ```

3. Ensure you have the Haar cascade XML file (`face_ref.xml`) in the project directory. You can download it from the OpenCV GitHub repository:
   - [Haar Cascade for Face Detection](https://github.com/opencv/opencv/tree/master/data/haarcascades)

## Usage

1. Run the script:
   ```bash
   python face_detection.py
   ```

2. The program will open a webcam window and display real-time video with detected faces outlined in rectangles.

3. Press `q` to exit the application.

## File Structure

```
face-detection-opencv/
├── face_detection.py       # Main Python script
├── face_ref.xml            # Haar cascade file for face detection
├── README.md               # Project documentation
```

## Code Explanation

### Main Functions

1. **`face_detection(frame)`**:
   - Converts the frame to grayscale.
   - Detects faces using Haar cascade with specified parameters.

2. **`drawer_box(faces, frame)`**:
   - Draws rectangles around detected faces on the frame.

3. **`close_window()`**:
   - Releases the camera and closes all OpenCV windows.

### Workflow

- The program captures frames from the webcam.
- Faces are detected in each frame using the Haar cascade.
- Detected faces are highlighted with rectangles and displayed in real time.

## Requirements

- Python 3.6+
- OpenCV library (`opencv-python`)

## Troubleshooting

1. **`ModuleNotFoundError: No module named 'cv2'`**:
   - Ensure OpenCV is installed: `pip install opencv-python`.

2. **Webcam Not Opening**:
   - Check if another application is using the webcam.
   - Verify that your webcam is connected and enabled.

3. **Haar Cascade Missing**:
   - Download the `face_ref.xml` file and place it in the project directory.

## Customization

- Modify detection parameters in the `face_detection()` function to fine-tune face detection.
  ```python
  faces = face_ref.detectMultiScale(
      optimized_frame,
      scaleFactor=1.1,  # Adjust for image scaling
      minNeighbors=5,   # Adjust sensitivity
      minSize=(30, 30)  # Minimum face size
  )
  ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- OpenCV library for computer vision.
- Haar cascades provided by OpenCV.

---

Happy coding!
