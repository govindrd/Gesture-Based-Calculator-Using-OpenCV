from flask import Flask, render_template, Response
import cv2
from calculator import Calculator
from button import Button
from hand_tracker import HandTracker

app = Flask(__name__)

# Initialize components
cap = cv2.VideoCapture(0)
calculator = Calculator()
hand_tracker = HandTracker()

# Define calculator layout
buttons = []
keys = [
    ['7', '8', '9', '+'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '*'],
    ['AC', '0', '=', '/']
]

for i in range(4):
    for j in range(4):
        buttons.append(Button((100 + j * 100, 150 + i * 100), (90, 90), keys[i][j]))

# State
delay_counter = 0
last_clicked_button = None

def gen_frames():
    global delay_counter, last_clicked_button

    while True:
        success, frame = cap.read()
        if not success:
            break
        frame = cv2.flip(frame, 1)

        # 1. Hand detection
        hand_landmarks, frame = hand_tracker.find_hand(frame)

        # 2. Draw calculator display bar
        cv2.rectangle(frame, (100, 50), (500, 120), (50, 50, 50), -1)
        cv2.putText(frame, calculator.get_equation(), (110, 110),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

        # 3. Draw buttons
        for button in buttons:
            if button == last_clicked_button and delay_counter > 0:
                button.draw(frame, color=(0, 255, 0))
            else:
                button.draw(frame)

        # 4. Hand tracking and pinch click
        if hand_landmarks:
            cursor = hand_tracker.get_cursor(hand_landmarks)

            if hand_tracker.is_pinch(hand_landmarks) and delay_counter == 0:
                for button in buttons:
                    if button.is_clicked(cursor):
                        if button.value == 'AC':
                            calculator.clear()
                        else:
                            calculator.add(button.value)
                        last_clicked_button = button
                        delay_counter = 15
                        break

            # Draw hand tracking point
            cv2.circle(frame, cursor, 10, (255, 0, 255), -1)

        # Delay handling
        if delay_counter > 0:
            delay_counter -= 1
            if delay_counter == 0:
                last_clicked_button = None

        # Encode to JPEG
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# Flask Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
