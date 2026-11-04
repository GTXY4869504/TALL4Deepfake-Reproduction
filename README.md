# TALL4Deepfake 复现

> 本科「科学与社会」研讨课 · 人脸篡改检测课题：对 ICCV 2023 / IJCV 2024 的 TALL、TALL++ 工作进行复现与实验。
> 原始实现见下方官方说明，本地改动见文末「关于本仓库」。

---

# Official implementation for TALL and TALL++

## [**[ICCV-2023] Thumbnail Layout for Deepfake Video Detection**](https://openaccess.thecvf.com/content/ICCV2023/papers/Xu_TALL_Thumbnail_Layout_for_Deepfake_Video_Detection_ICCV_2023_paper.pdf)

## [**[IJCV-2024] Learning Spatiotemporal Inconsistency via Thumbnail Layout for Face Deepfake Detection**](https://arxiv.org/pdf/2403.10261.pdf)


* 2024.3.8  :tada:The improved version TALL++ has been accepted by IJCV2024!
* 2024.3.7  Updated the basic data preparation code, which is sourced from [FaceForensic](https://github.com/ondyari/FaceForensics/blob/master/classification/detect_from_video.py).
* 2024.2.18 There is a small error in the version released by ICCV about appendix. We have added the appendix to the text. A revised version of the paper can be found on [arXiv](https://arxiv.org/pdf/2307.07494.pdf).

## Attention: The code for our improved IJCV extension (TALL++, https://arxiv.org/pdf/2403.10261.pdf ) will be made available in this repository.

Our implementation is based on [Swin-Transformer](https://github.com/microsoft/Swin-Transformer).

# Requirements
 - einops
 - fvcore
 - timm==0.4.12
 - torch==1.13.1
 - torchaudio==0.13.1
 - torchvision==0.14.1

# Data Preparation
Please refer to [FaceForensic](https://github.com/ondyari/FaceForensics/blob/master/classification/detect_from_video.py) for how to prepare deepfake datasets such as FF++, Celeb-DF, and DFDC.

The data loader can load image sequences stored in txt files in the following format:
```
#example for train.txt
# path  |  start frame | end frame | label
original_faces_c23/928 1 300 0
original_faces_c23/712 1 300 0
original_faces_c23/582 1 300 0
original_faces_c23/602 1 300 0
deepfakes_faces_c23/143_140 1 300 1
deepfakes_faces_c23/408_424 1 300 1
deepfakes_faces_c23/766_761 1 300 1
deepfakes_faces_c23/964_174 1 300 1
```

# Training:

[IMPORTANT] Edit main.py and change the default arg-parser values according to your convenience (especially the config paths)

```
CUDA_VISIBLE_DEVICES=0 python main.py --dataset ffpp \
 --input-size 112 --num_clips 8 --output_dir [your_output_dir] --opt adamw --lr 1.5e-5 --warmup-lr 1.5e-8 --min-lr 1.5e-7 \
 --epochs 60 --sched cosine --duration 4 --batch-size 4 --thumbnail_rows 2 --disable_scaleup --cutout True \
 --pretrained --warmup-epochs 10 --no-amp --model TALL_SWIN \
 --hpe_to_token 2>&1 | tee ./output/train_ffpp_`date +'%m_%d-%H_%M'`.log
```

# Evaluation:

```
CUDA_VISIBLE_DEVICES=0 python test.py  --dataset ffpp \
 --input_size 112 --opt adamw --lr 1e-4 --epochs 30 --sched cosine --duration 4 --batch-size 4 --thumbnail_rows 2 --disable_scaleup \
 --pretrained --warmup-epochs 5 --no-amp --model TALL_SWIN  \
 --hpe_to_token --initial_checkpoint [model_checkpoint] --eval --num_crops 1 --num_clips 8 \
 2>&1 | tee ./output/test_ffpp_`date +'%m_%d-%H_%M'`.log
```
# Citation

```
@inproceedings{xu2023tall,
  title={TALL: Thumbnail Layout for Deepfake Video Detection},
  author={Xu, Yuting and Liang, Jian and Jia, Gengyun and Yang, Ziming and Zhang, Yanhao and He, Ran},
  booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision},
  pages={22658--22668},
  year={2023}
}
```
# Contact

- [xuyuting@iie.ia.ac](mailto:xuyuting@iie.ia.ac)

---

# 关于本仓库（About this fork）

本仓库是 TALL / TALL++ 官方实现（MIT License，见 `LICENSE`）的**课程复现版本**，
用于本科生“科学与社会”研讨课的人脸篡改检测课题。原始代码与论文版权归上列作者所有，
本仓库仅保留原许可协议并注明出处。

在原始代码基础上的本地改动：

| 文件 | 说明 |
| --- | --- |
| `my_models/tall_swin.py`、`my_models/__init__.py` | 本地新增的模型定义与封装 |
| `video_dataset_config.py` | 数据集配置（ffpp 单数据集） |
| `test for S.py` | 运行环境自检脚本（torch / timm / cuda 可用性） |
| `.gitignore`、`.gitattributes` | 忽略缓存与 IDE 文件、统一换行符 |

