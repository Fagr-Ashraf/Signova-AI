import cv2
import numpy as np
from .config import WIDTH, HEIGHT, FPS, POSE_CONNECTIONS

# =========================
# COLORS
# =========================
WHITE = (255, 255, 255)

# #190124 in HEX
# RGB = (25, 1, 36)
# OpenCV uses BGR
BACKGROUND = (36, 1, 25)

# =========================
# HAND
# =========================
def draw_hand_stylish(img, hand_points, thickness=5):
    h, w = img.shape[:2]

    pts = [(int(x * w), int(y * h)) for x, y, _ in hand_points]

    fingers = {
        "thumb": [0, 1, 2, 3, 4],
        "index": [0, 5, 6, 7, 8],
        "middle": [0, 9, 10, 11, 12],
        "ring": [0, 13, 14, 15, 16],
        "pinky": [0, 17, 18, 19, 20]
    }

    for idxs in fingers.values():
        for i in range(len(idxs) - 1):
            x1, y1 = pts[idxs[i]]
            x2, y2 = pts[idxs[i + 1]]

            cv2.line(
                img,
                (x1, y1),
                (x2, y2),
                WHITE,
                thickness,
                cv2.LINE_AA
            )

# =========================
# POSE
# =========================
def draw_pose_lines(img, points, connections, thickness=4):
    h, w = img.shape[:2]

    pts = [(int(x * w), int(y * h)) for x, y, _ in points]

    for i, j in connections:
        if i < len(pts) and j < len(pts):
            cv2.line(
                img,
                pts[i],
                pts[j],
                WHITE,
                thickness,
                cv2.LINE_AA
            )

# =========================
# FACE LANDMARKS
# =========================
def draw_points_and_connections(img, points):
    h, w = img.shape[:2]

    pts = [(int(x * w), int(y * h)) for x, y, _ in points]

    for (x, y) in pts:
        if 0 <= x < w and 0 <= y < h:
            cv2.circle(
                img,
                (x, y),
                2,
                WHITE,
                -1
            )

# =========================
# MAIN DRAW
# =========================
def draw_skeleton(frame, img):
    # Pose
    draw_pose_lines(
        img,
        frame[42:75],
        POSE_CONNECTIONS,
        thickness=4
    )

    # Left hand
    draw_hand_stylish(
        img,
        frame[0:21],
        thickness=4
    )

    # Right hand
    draw_hand_stylish(
        img,
        frame[21:42],
        thickness=4
    )

    # Face
    draw_points_and_connections(
        img,
        frame[75:553]
    )

# =========================
# RENDER
# =========================
def render(frames, output="output.mp4"):
    writer = cv2.VideoWriter(
        output,
        cv2.VideoWriter_fourcc(*"mp4v"),
        FPS,
        (WIDTH, HEIGHT)
    )

    for frame in frames:
        # Create background using #190124
        img = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
        img[:] = BACKGROUND

        draw_skeleton(frame, img)
        writer.write(img)

    writer.release()
    return output