import cv2
import numpy as np
import pyautogui
import threading
import time

class ScreenRecorder:
    def __init__(self, output_file, fps=10, zoom_factor=2, follow_duration=0.1):
        self.output_file = output_file
        self.fps = fps
        self.zoom_factor = zoom_factor
        self.follow_duration = follow_duration
        self.screen_size = pyautogui.size()
        self.recording = False
        self.out = None
        self.thread = None

    def _record(self):
        while self.recording:
            # Get the current screenshot
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Get the current text cursor position
            text_cursor_pos = pyautogui.position()  # This needs to be replaced with the actual text cursor position if available
            
            # Apply zoom and follow effect
            frame = self._zoom_and_follow_cursor(frame, text_cursor_pos)
            
            self.out.write(frame)
            time.sleep(1 / self.fps)

    def _zoom_and_follow_cursor(self, frame, cursor_pos):
        x, y = cursor_pos
        h, w, _ = frame.shape
        box_w, box_h = w // self.zoom_factor, h // self.zoom_factor

        x1, y1 = max(0, x - box_w // 2), max(0, y - box_h // 2)
        x2, y2 = min(w, x + box_w // 2), min(h, y + box_h // 2)

        cropped_frame = frame[y1:y2, x1:x2]

        # Resize the cropped frame back to the original size
        zoomed_frame = cv2.resize(cropped_frame, (w, h), interpolation=cv2.INTER_LINEAR)
        return zoomed_frame

    def start_recording(self):
        print("Starting recording")
        pyautogui.hotkey('ctrl', 'alt', '1', interval=0.5)

    def stop_recording(self):
        print("Stopping recording")
        pyautogui.hotkey('ctrl', 'alt', '2', interval=0.5)




