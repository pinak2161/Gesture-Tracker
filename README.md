
# Gesture-Tracker
This repository contains code for a gesture tracking project that utilizes computer vision techniques to detect and analyze gestures in video streams. The project includes modules for gesture detection, annotation, and video processing, providing a comprehensive solution for tracking gestures in real-time or recorded videos.

## Features
- Detects predefined gestures in video streams.
- Annotates detected gestures in real-time or recorded videos.
- Adjustable threshold for gesture detection.
- Supports various input gesture representations (images).
- Provides customizable options for video output.

## Requirements
- Python 3.x
- OpenCV
- NumPy

## Installation
1. Clone this repository:
   ```
   (https://github.com/pinak2161/Gesture-Tracker/tree/main)
   ```
2. Install the required dependencies:
   ```bash
   pip install opencv-python numpy
   ```

## Usage
1. Place your input gesture image in the `src` directory.
2. Prepare your test video and place it in the `src` directory.
3. Update the `input_gesture_path` and `test_video_path` variables in the `main()` function of `main.py` with the appropriate file paths.
4. Optionally adjust the threshold value in `main.py` for gesture detection.
5. Run the main script:
   ```bash
   python main.py
   ```

## Video Demonstration


https://github.com/pinak2161/Gesture-Tracker/assets/130877143/2b781cf2-4252-4304-9471-ddbc5c0496cc



## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request for any improvements or bug fixes.

