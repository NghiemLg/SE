import yt_dlp
import cv2
from ultralytics import YOLO

# Load the pre-trained YOLO model
model = YOLO('yolov8n.pt')  # Bạn có thể thay thế bằng mô hình YOLO khác như 'yolov8s.pt'

# URL của video YouTube
video_url = 'https://www.youtube.com/watch?v=DjdUEyjx8GM&list=LL&index=4'  # Thay bằng URL video thực tế

# Lấy liên kết phát trực tiếp từ YouTube
ydl_opts = {'format': 'best'}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(video_url, download=False)
    stream_url = info_dict.get('url', None)

# Mở video stream
cap = cv2.VideoCapture(stream_url)

if not cap.isOpened():
    print("❌ Error: Unable to open video stream.")
else:
    print("✅ Video stream opened successfully!")

# Đọc và phát hiện từng frame
while True:
    ret, frame = cap.read()
    if not ret:
        print("⚠️ Error: Cannot read frame from video stream.")
        break

    # Chạy YOLO để phát hiện đối tượng
    results = model(frame)

    # Hiển thị kết quả
    annotated_frame = results[0].plot()  # Vẽ bounding boxes lên frame

    cv2.imshow("YOLO Video Detection", annotated_frame)

    # Thoát khi nhấn phím 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

   
# Giải phóng tài nguyên
cap.release()
cv2.destroyAllWindows()
