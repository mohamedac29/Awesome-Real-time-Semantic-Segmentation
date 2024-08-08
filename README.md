# Awesome-Real-time-Semantic-Segmentation
Semantic Segmentation for autonomous driving
# README

## Summary of Contents

- [Methods: A Survey](#methods-a-survey)
  <!-- - [Meta-Architecture](#meta-architecture)
  - [Strong Representation](#strong-representation)
  - [Interaction Design in Decoder](#interaction-design-in-decoder)
  - [Optimizing Object Query](#optimizing-object-query)
  - [Using Query For Association](#using-query-for-association)
  - [Conditional Query Generation](#conditional-query-generation)
<!-- - [Related Domains and Beyond](#related-domains-and-beyond)
  - [Point Cloud Segmentation](#point-cloud-segmentation)
  - [Tuning Foundation Models](#tuning-foundation-models)
  - [Domain-aware Segmentation](#domain-aware-segmentation)
  - [Label and Model Efficient Segmentation](#label-and-model-efficient-segmentation)
  - [Class Agnostic Segmentation and Tracking](#class-agnostic-segmentation-and-tracking)
  - [Medical Image Segmentation](#medical-image-segmentation) --> -->

## Methods: A Survey

### Meta-Architecture

| Year | Venue | Acronym | Paper Title | Code/Project | Dataset(s)|
|------|-------|---------|-------------|--------------|--------------|
| 2021 | T-ITS  | DDRNet | [Deep Dual-resolution Networks for Real-time and Accurate Semantic Segmentation of Road Scenes](https://arxiv.org/abs/2101.06085) | [Code]( https://github.com/ydhongHIT/DDRNet) | Cityscapes, CamVid| 
| 2021 | CVPR  |  STDC-Seg | [Rethinking BiSeNet For Real-time Semantic Segmentation](https://arxiv.org/abs/2104.13188) | [Code](https://github.com/MichaelFan01/STDC-Seg) | Cityscapes, CamVid|

| 2021 | CVPR  |  ENet | [Rethinking BiSeNet For Real-time Semantic Segmentation](https://arxiv.org/abs/2104.13188) | [Code](https://github.com/iArunava/ENet-Real-Time-Semantic-Segmentation) | Cityscapes, CamVid|
| 202 7| T-ITS  |  ERFNet | [ERFNet: Efficient Residual Factorized ConvNet for Real-time Semantic Segmentation](https://ieeexplore.ieee.org/document/8063438) | [Code](https://github.com/Eromera/erfnet) | Cityscapes, CamVid|
| 2018 | CVPR  |  ICNet | [ICNet for Real-Time Semantic Segmentation on High-Resolution Images](https://arxiv.org/abs/1704.08545) | [Code](https://github.com/hszhao/ICNet) | Cityscapes, CamVid|
| 2017 | T-PAMI |  SegNet | [SegNet: A Deep Convolutional Encoder-Decoder Architecture for Image Segmentation](https://ieeexplore.ieee.org/abstract/document/7803544) | [Code](https://github.com/alexgkendall/caffe-segnet) | Cityscapes, CamVid|
| 2019 | ICIp  |  LEDNet | [Lednet: A Lightweight Encoder-Decoder Network for Real-Time Semantic Segmentation](https://ieeexplore.ieee.org/abstract/document/8803154) | [Code](https://github.com/xiaoyufenfei/LEDNet) | Cityscapes, CamVid|
| 2018 | CVPR  |  BiSeNet | [BiSeNet: Bilateral Segmentation Network for Real-time Semantic Segmentation](https://arxiv.org/abs/2104.13188) | [Code](https://github.com/MichaelFan01/STDC-Seg) | Cityscapes, CamVid|
| 2021 | IJCV  |  BiSeNetV2 | [BiSeNet V2: Bilateral Network with Guided Aggregation for Real-Time Semantic Segmentation](https://link.springer.com/article/10.1007/s11263-021-01515-2) | [Code](https://github.com/CoinCheung/BiSeNet) | Cityscapes, CamVid|
| 2019 | CVPR  |  LiteSeg | [LiteSeg: A Novel Lightweight ConvNet for Semantic Segmentation](https://ieeexplore.ieee.org/abstract/document/8945975) | [Code](https://github.com/xiaoyufenfei/LEDNet) | Cityscapes, CamVid|



<!-- | 2021 | NeurIPS | MaskFormer | [MaskFormer: Per-Pixel Classification is Not All You Need for Semantic Segmentation](https://arxiv.org/abs/2107.06278) | [Code](https://github.com/facebookresearch/MaskFormer) | -->
<!-- | 2023 | CVPR  | PIDNet| [PIDNet: A Real-time Semantic Segmentation Network Inspired by PID Controllers
](https://arxiv.org/abs/2206.02066) | [Code](https://github.com/XuJiacong/PIDNet) | -->

<!-- 
 HyperSeg https://github.com/YuvalNirkin/hyperseg Officialcode
 STDC1-50 https://github.com/MichaelFan01/STDC-Seg Officialcode
 SegBlocks https://github.com/thomasverelst/segblocks-Segmentation-pytorch Officialcode
 SQ https://github.com/klickmal/speeding_up_semantic_Segmentation Third-partycode
 ERFNet https://github.com/Eromera/erfnet Officialcode
 LinkNet https://github.com/e-lab/LinkNet Third-partycode
 ContextNet https://github.com/klickmal/ContextNet Third-partycode
 DSNet https://github.com/s7ev3n/DSNet Third-partycode
 ESPNetv2 https://github.com/sacmehta/ESPNetv2 Officialcode
 LWRF https://github.com/DrSleep/light-weight-refinenet Third-partycode
 DABNet https://github.com/Reagan1311/DABNet Officialcode
 DFANet https://github.com/huaifeng1993/DFANet Third-partycode
 Fast-SCNN https://github.com/Tramac/Fast-SCNN-pytorch Third-partycode
 ShuffleSeg https://github.com/MSiam/TFSegmentation Officialcode
 U-HarDNet-70 https://github.com/PingoLH/Pytorch-HarDNet Officialcode
 SwiftNetRN-18 https://github.com/orsic/swiftnet Officialcode
 TD4-BISE18 https://github.com/feinanshan/TDNet Officialcode
 ShelfNet18 https://github.com/juntang-zhuang/ShelfNet Officialcode
 BiSeNet https://github.com/osmr/imgclsmob Third-partycode
 BiSeNetV2 https://github.com/CoinCheung/BiSeNet Third-partycode
 FasterSeg https://github.com/VITA-Group/FasterSeg Officialcode
 ESNet https://github.com/osmr/imgclsmob Third-partycode
 LEDNet https://github.com/xiaoyufenfei/LEDNet Third-partycode -->
 ICNet https://github.com/hszhao/ICNet Officialcode
 Template-Based-NAS-arch1 https://github.com/drsleep/nas-segm-pytorch Officialcode
 LiteSeg https://github.com/tahaemara/LiteSeg Officialcode
 Template-Based-NAS-arch0 https://github.com/drsleep/nas-segm-pytorch Officialcode
 ENet https://github.com/iArunava/ENet-Real-Time-Semantic-Segmentation Third-partycode
 ENet+Lovász-Softmax https://github.com/bermanmaxim/LovaszSoftmax Officialcode
 SegNet https://github.com/alexgkendall/caffe-segnet Third-partycode
 EDANet https://github.com/shaoyuanlo/EDANet Officialcode
