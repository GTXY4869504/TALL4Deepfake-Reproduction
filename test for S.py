import torch
import einops
import timm
import cv2

print("=== 环境验证报告 ===")
print(f"1. PyTorch版本: {torch.__version__}")
print(f"2. PyTorch CUDA可用: {torch.cuda.is_available()} (应为False，这是CPU环境)")
print(f"3. timm版本: {timm.__version__}")
print(f"4. 所有关键库导入成功！")
print("====================")