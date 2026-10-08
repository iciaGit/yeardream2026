from ultralytics import YOLO

model = YOLO('yolo26n.pt')

results = model.predict(
    source="data/sample.mp4",
    conf=0.5,
    show=True, # 별도의 창으로 화면 보여주기
    save=False, # 탐지내용 저장 여부
    imgsz = [480,640],# 사이즈 조정
    exist_ok=True,
    verbose=False,  # 프레임관련로그 출력 여부
)

