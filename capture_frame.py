import cv2

def capture_frame(video_path, frame_number, output_image_path):
    cap = cv2.VideoCapture(video_path)
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

    ret, frame = cap.read()
    if ret:
        cv2.imwrite(output_image_path, frame)
    else:
        print("Não foi possível capturar o frame.")

    cap.release()

video_path = 'videos/video6.mp4'
frame_number = 1
output_image_path = 'images/imagem6.png'

capture_frame(video_path, frame_number, output_image_path)