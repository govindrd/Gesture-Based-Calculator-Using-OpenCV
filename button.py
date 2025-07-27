import cv2

class Button:
    def __init__(self, pos, size, value):
        self.pos = pos
        self.size = size
        self.value = value

    def draw(self, img, color=(100, 100, 100)):  # Accept color
        x, y = self.pos
        w, h = self.size
        cv2.rectangle(img, (x, y), (x + w, y + h), color, -1)
        cv2.putText(img, self.value, (x + 20, y + 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)

    def is_clicked(self, cursor):
        x, y = self.pos
        w, h = self.size
        cx, cy = cursor
        return x < cx < x + w and y < cy < y + h
