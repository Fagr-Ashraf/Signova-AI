import cv2
hands = None
HAND_LOWER_THRESHOLD = 0.85 
def get_hands():
    global hands

    if hands is None:
        import mediapipe as mp

        print("Loading MediaPipe...")
        hands = mp.solutions.hands.Hands(
            static_image_mode=False,
            max_num_hands=2
        )

    return hands

def extract_hand_status(frame):

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = get_hands().process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand in results.multi_hand_landmarks:
            for lm in hand.landmark:
                if lm.y < HAND_LOWER_THRESHOLD:
                    return False

    return True