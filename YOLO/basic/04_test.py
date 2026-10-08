from pathlib import Path

from ultralytics import YOLO

# 1. 모델 불러오기
model = YOLO('data/best.pt')
# 2. 테스트할 파일 경로
test_image = 'fashion_mnist/test/Shirt/4.jpg'
# 3. 예측
curr_dir = Path(__file__).resolve().parent

results = model.predict(
    source=test_image,
    save=True,
    project=f'{curr_dir}/runs/predict',
    name="test_result",
    exist_ok=True
)
print('예측 성공')
result = results[0]
print(f'확률이 가장 높은 class idx : {result.probs.top1}')
print(f'1등인 idx 의 확률 : {result.probs.top1conf}')
print(f'1~5 위 까지의 class idx : {result.probs.top5}')
print(f'1~5 위 까지의 확률 : {result.probs.top5conf.tolist()}')
print(f'이미지경로 : {result.path}')
print(f'클래스이름들 : {result.names}')
print(f'원본데이터 배열 : {result.orig_img.shape}')

import matplotlib.pyplot as plt
plt.title(result.names[result.probs.top1])
plt.imshow(result.orig_img)
plt.axis('off')
plt.show()
