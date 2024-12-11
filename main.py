import cv2

face_ref = cv2.CascadeClassifier("face_ref.xml")
if face_ref.empty():
    print("Error: Could not load face_ref.xml.")
    exit()

camera = cv2.VideoCapture(0)
if not camera.isOpened():
    print("Error: Could not open camera.")
    exit()

def face_detection(frame):
    optimized_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_ref.detectMultiScale(optimized_frame, scaleFactor=1.1, minSize=(100, 100))
    return faces

def drawer_box(faces, frame):
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 4)
    return frame

def close_window():
    camera.release()
    cv2.destroyAllWindows()

def main():
    while True:
        ret, frame = camera.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        faces = face_detection(frame)
        frame = drawer_box(faces, frame)

        cv2.imshow("Face Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    close_window()

if __name__ == "__main__":
    main()
