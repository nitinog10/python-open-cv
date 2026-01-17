# Face Detection using OpenCV

This project demonstrates real-time face detection using OpenCV and a pre-trained Haar Cascade classifier.

## Project Files

- **face_detection.py** - Static image face detection (detects faces in a saved image file)
- **face_detection_camera.py** - Real-time face detection using your webcam
- **README.md** - This file with project documentation

## Requirements

- Python 3.13+
- OpenCV (`opencv-python`
-a proper working camera
## Installation

1. Install the required package:
```bash
pip install opencv-python==4.10.0.84
```

Or for Python 3.13 specifically:
```bash
python3.13.exe -m pip install opencv-python
```

## How to Use

### Real-Time Face Detection (Recommended)

Run the camera-based face detection:

```bash
python3.13.exe face_detection_camera.py
```

**Controls:**
- Press `q` - Quit the application
- Press `s` - Save a screenshot with detected faces

**What it does:**
- Opens your default webcam
- Detects faces in real-time using Haar Cascade
- Displays green rectangles around detected faces
- Shows the count of detected faces on the screen

### Static Image Face Detection

To detect faces in a saved image file:

```bash
python3.13.exe face_detection.py
```

Place your image file as `team.jpg` in the same directory, or modify the code to point to your image file.

## Features

✅ Real-time face detection from webcam  
✅ Face count display  
✅ Screenshot saving capability  
✅ Easy-to-use keyboard controls  
✅ Green bounding boxes around detected faces  

## Technical Details

- **Algorithm:** Haar Cascade Classifier (cascade of boosted classifiers working with HOG features)
- **Pre-trained Model:** haarcascade_frontalface_default.xml (included with OpenCV)
- **Color Space:** BGR (OpenCV default) for video, Grayscale for face detection

## Troubleshooting

**Issue:** `ModuleNotFoundError: No module named 'cv2'`
- **Solution:** Make sure you installed opencv-python for the correct Python interpreter:
  ```bash
  python3.13.exe -m pip install opencv-python
  ```

**Issue:** Camera not opening / "Cannot open camera"
- **Solution:** 
  - Check if another application is using your camera
  - Try restarting the script
  - Check camera permissions in your system settings

**Issue:** Faces not being detected
- **Solution:** 
  - Ensure good lighting
  - Keep your face clearly visible and not tilted too much
  - The algorithm works best with frontal face views

## Future Enhancements

- Add multiple face cascade classifiers (side faces, eyes, smiles)
- Implement facial recognition (identify specific people)
- Add recording functionality
- Use deep learning models (YOLO, SSD) for better accuracy
- Add face blurring for privacy

## References

- [OpenCV Documentation](https://docs.opencv.org/)
- [Haar Cascade Classifiers](https://docs.opencv.org/master/db/d28/tutorial_cascade_classifier.html)
- [OpenCV Tutorials](https://docs.opencv.org/master/d9/df8/tutorial_root.html)

## Author

Created for OpenCV learning project

## License

Open source - Feel free to modify and use as needed
