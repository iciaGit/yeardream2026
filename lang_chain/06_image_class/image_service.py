import os

from transformers import pipeline

# window 경고메시지 지우기(선택사항)
os.environ["HF_HUB_DISABLE_SYMLINK_WARNING"] = "1"

# 이미지 분류
# uv pip install pillow torchvision
vision = pipeline(model="google/vit-base-patch16-224")
print(vision('upload/dog.png'))


