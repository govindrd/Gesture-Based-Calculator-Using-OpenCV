## Gesture-Based Calculator Using OpenCV

This project is a gesture-based calculator that uses computer vision to recognize hand gestures and allows users to perform basic arithmetic operations by interacting with a virtual calculator interface using their webcam. The application is built with Python, OpenCV, and Flask for the web interface.

---

### Features
- Real-time hand gesture recognition using OpenCV
- Virtual calculator interface with clickable buttons
- Web-based UI for easy access and demonstration
- Supports basic arithmetic operations: addition, subtraction, multiplication, division, clear, and evaluate

---

## Getting Started

### 1. Clone the Repository

Open your terminal or command prompt and run:

```sh
git clone https://github.com/your-username/gesture-based-calculator-opencv.git
```

Replace `your-username` with the actual GitHub username if you fork or host the project elsewhere.

### 2. Install Dependencies

Navigate to the project directory:

```sh
cd "Gesture-Based Calculator Using OpenCV"
```

Install the required Python packages:

```sh
pip install -r requirement.txt
```

### 3. Run the Application

Start the Flask server:

```sh
python main.py
```

The application will start running at `http://127.0.0.1:5000/` by default.

Open this URL in your web browser to access the calculator interface.

---
# Project Structure

gesture-calculator/\

├── templates/

│   └── index.html         # Frontend HTML

├── button.py              # Button rendering logic

├── calculator.py          # Calculator logic and expression evaluation

├── hand_tracker.py        # Hand detection and pinch gesture logic

├── main.py                # Flask backend and OpenCV integration

├── requirements.txt       # Python dependencies

└── README.md              # Project documentation


## How It Works (Step by Step)

1. **Webcam Initialization:**
   - The application accesses your webcam using OpenCV to capture real-time video frames.

2. **Hand Detection:**
   - The `HandTracker` module processes each frame to detect your hand and track its landmarks.

3. **Virtual Calculator Display:**
   - A virtual calculator interface is drawn on the video feed, including buttons for numbers and operations.

4. **Gesture Recognition:**
   - The system detects a "pinch" gesture (using thumb and index finger) to simulate a button click.

5. **Button Interaction:**
   - When a pinch is detected over a button, the corresponding value (number or operator) is added to the calculator's equation.
   - The 'AC' button clears the equation, and '=' evaluates the result.

6. **Display Update:**
   - The current equation or result is displayed on the calculator interface in real time.

7. **Web Streaming:**
   - The processed video stream is sent to the browser using Flask, updating the UI with each frame.

---

## Project Structure

- `main.py` - Flask app and main video processing loop
- `calculator.py` - Calculator logic (handling input, evaluation, clearing)
- `button.py` - Button class for the calculator interface
- `hand_tracker.py` - Hand detection and gesture recognition logic
- `templates/index.html` - Web UI template
- `requirement.txt` - List of required Python packages

---

## Notes
- Make sure your webcam is connected and accessible.
- For best results, use the calculator in a well-lit environment.
- The hand tracking logic may require a plain background for optimal accuracy.

---
<img width="1764" height="955" alt="image" src="https://github.com/user-attachments/assets/99379b2c-d060-41eb-a907-392524307f15" />
<img width="1647" height="854" alt="image" src="https://github.com/user-attachments/assets/8673f85e-ca65-425a-a964-a1f8506db5d7" />
<img width="1688" height="837" alt="image" src="https://github.com/user-attachments/assets/23010737-60f0-410e-ba7d-181d1f6b86eb" />
<img width="1544" height="946" alt="image" src="https://github.com/user-attachments/assets/38239696-d12d-4502-8290-c09664c22864" />
<img width="1371" height="822" alt="image" src="https://github.com/user-attachments/assets/76550488-0133-4619-81b9-3fbf59f259dc" />






