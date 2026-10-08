import cv2
from ultralytics import YOLO

model = YOLO('yolo26n.pt')
print(f'open CV :{cv2.__version__}')
cap = cv2.VideoCapture('data/sample.mp4')

if not cap.isOpened():
    print('비디오에 이상이 있습니다.')
    exit()

while True:
    success,frame = cap.read()
    # print(success)
    if not success:
        print('프레임을 읽어올 수 없습니다.')
        break

    results = model.track( # track : 연속성이 있음(이전 프레임 기억)
        source=frame,
        persist=True, # 이전 프레임을 기억
        conf=0.5,
        imgsz=[480,640],# 해상도 조정(속도 향상)
        classes=[0,2],# 0번:사람,2번:자동차만 인식하도록 설정
        show=False, # 자체 팝업으로 보여주기
        verbose=False
    )

    # YOLO 가 탐지한 내용을 가져와서 그리기
    yolo_frame = results[0].plot()
    resize_frame = cv2.resize(yolo_frame,(480,640)) # 창 크기 줄이기
    cv2.imshow("YOLO 실시간 추적",resize_frame)

    # q 키 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()





