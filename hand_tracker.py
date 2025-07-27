import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(max_num_hands=1)
        self.mp_draw = mp.solutions.drawing_utils

    def find_hand(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb)
        hand_landmarks = None
        if results.multi_hand_landmarks:
            hand_landmarks = results.multi_hand_landmarks[0]
            self.mp_draw.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
        return hand_landmarks, frame

    def get_cursor(self, hand_landmarks):
        h, w = 480, 640  # default frame size
        index_tip = hand_landmarks.landmark[8]
        cx, cy = int(index_tip.x * w), int(index_tip.y * h)
        return (cx, cy)

    def is_pinch(self, hand_landmarks):
        # Distance between index finger tip and thumb tip
        index_tip = hand_landmarks.landmark[8]
        thumb_tip = hand_landmarks.landmark[4]

        dx = index_tip.x - thumb_tip.x
        dy = index_tip.y - thumb_tip.y
        distance = (dx**2 + dy**2)**0.5

        return distance < 0.05  # pinch threshold (tune if needed)
