import os
from torchvision import datasets
from ultralytics import YOLO

class_names = ["T-shirt", "Trouser", "Pullover", "Dress", "Coat",
               "Sandal", "Shirt", "Sneaker", "Bag", "Ankle-boot"]

# 1. fation-mnist 를 받는다.
def download_image(split='train'):
    is_train = True if split == 'train' else False # 학습용, 시험용 데이터 여부
    # data 폴더에 원본을 다운로드 받는다.(학습데이터 여부)
    dataset = datasets.FashionMNIST(root="./data",train=is_train, download=True)

    # tqdm() : 반복문 처리시 처리 진행율을 보여주는 함수
    for idx in range(len(dataset)):
        img,label = dataset[idx] # 데이터로 부터 이미지 객체, 정답 라벨(숫자) 추출
        label_name = class_names[label] # 해당 번호의 분류 명을 추출
        # 이미지를 받아서 fashion_mnist/train/T-shirts/0.jpg 저장
        # 분류모델 학습시 반드시 [라벨이름] 이 되어야 한다.
        save_dir = f'fashion_mnist/{split}/{label_name}' # 저장경로 생성
        os.makedirs(save_dir,exist_ok=True)
        img.save(f'{save_dir}/{idx}.jpg') # idx 를 통해서 0.jpg 형태로 파일 저장
    print(f'{split} 이미지 저장')

# download_image('train')
# download_image('test')

# 2. 모델을 불러와서 인식
if __name__ == '__main__':
    model = YOLO('yolo26n-cls.pt')
    model.train(
        data = 'fashion_mnist', # 학습데이터 폴더 경로
        exist_ok=True, # 덮어쓰기여부
        epochs=5, # 전체 데이터 학습 횟수
        imgsz=28, # 이미지크기 지정(28*28)
        batch=64, # 한번에 처리할 수
        workers=1, # 데이터 로딩에 사용할 스레드 수
    )
    print('모델 학습 완료')











