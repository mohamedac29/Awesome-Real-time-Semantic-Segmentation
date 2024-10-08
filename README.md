# Real-time-Semantic-Segmentation
Semantic Segmentation for autonomous driving
# README

## Summary of Contents
his repo is used for recording, tracking several real-time semantic segmentation for autonmous driving
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
### FCN-like Network
 <table>
    <thead>
      <tr>
       <th>Method</th>
        <th>Year</th>
        <th>Venue</th>
        <th>Title</th>
        <th>Paper</th>
        <th>Code</th>
        <th>Dataset</th>
      </tr>
    </thead>
    <tbody>
    <tr>
        <td>ENet</td>
        <td>2016</td>
        <td>Arxiv</td>
        <td>ENet: A Deep Neural Network Architecture for Real-Time Semantic Segmentation</td>
        <td><a href="https://arxiv.org/pdf/1606.02147.pdf">Paper</a></td>
        <td><a href="https://github.com/TimoSaemann/ENet">Code</a></td>
        <td>Cityscapes, CamVid</td>
    </tr>
    <tr>
        <td>ERFNet</td>
        <td>2017</td>
        <td>T-ITS </td>
        <td>ERFNet: Efficient Residual Factorized ConvNet for Real-time Semantic Segmentation</td>
        <td><a href="https://ieeexplore.ieee.org/document/8063438">Paper</a></td>
        <td><a href="https://github.com/Eromera/erfnet">Code</a></td>
        <td>Cityscapes, Camvid</td>
    </tr>
    <tr>
        <td>DABNet</td>
        <td>2019</td>
        <td>BMVC</td>
        <td>DABNet: Depth-wise Asymmetric Bottleneck for Real-time Semantic Segmentation</td>
        <td><a href="https://arxiv.org/pdf/1907.11357.pdf">Paper</a></td>
        <td><a href="https://github.com/Reagan1311/DABNet">Code</a></td>
        <td>Cityscapes, CamVid</td>
    </tr>
    <tr>
        <td>LiteSeg</td>
        <td>2019</td>
        <td>DICTA</td>
        <td>LiteSeg: A Novel Lightweight ConvNet for Semantic Segmentation</td>
        <td><a href="https://ieeexplore.ieee.org/abstract/document/8945975">Paper</a></td>
        <td><a href="https://github.com/xiaoyufenfei/LEDNet">Code</a></td>
        <td>Cityscapes, CamVid</td>     
    </tr>
    </tbody>
    </table>

 ### Transformer-based Networks 
<table>
    <thead>
      <tr>
       <th>Method</th>
        <th>Year</th>
        <th>Venue</th>
        <th>Paper Title</th>
        <th>Code</th>
        <th>Dataset</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>SegFormer</td>
        <td>2021</td>
        <td>NeurIPS</td>
        <td>SegFormer: Simple and Efficient Design for Semantic Segmentation with Transformers</td>
        <td><a href="https://proceedings.neurips.cc/paper/2021/file/64f1f27bf1b4ec22924fd0acb550c235-Paper.pdf">Paper</a></td>
        <td><a href="https://github.com/NVlabs/SegFormer">Code</a></td>
        <td>Cityscapes, ADE20K</td>
    </tr>
    <tr>
        <td>AFFormer</td>
        <td>2023</td>
        <td>AAAI</td>
        <td>Head-Free Lightweight Semantic Segmentation with Linear Transformer</td>
        <td><a href="https://arxiv.org/pdf/2301.04648.pdf">Paper</a></td>
        <td><a href="https://github.com/dongbo811/AFFormer">Code</a></td>     
        <td>Cityscapes, ADE20K</td>     
    </tr>
     <tr>
        <td>SeaFormer</td>
        <td>2023</td>
        <td>ICLR</td>       
        <td>SEAFORMER: SQUEEZE-ENHANCED AXIAL TRANSFORMER FOR MOBILE SEMANTIC SEGMENTATION</td>
        <td><a href="https://arxiv.org/pdf/2301.13156">Paper</a></td>
        <td><a href="https://github.com/fudan-zvg/SeaFormer">Code</a></td>
        <td>Cityscapes, ADE20K, PascalContext, COCO-Stuff</td>         
    </tr>      
    </tbody>
    </table>


### Two-branch Network
<table>
    <thead>
      <tr>
       <th>Method</th>
        <th>Year</th>
        <th>Venue</th>
        <th>Title</th>
        <th>Paper</th>
        <th>Code</th>
        <th>Dataset</th>
      </tr>
    </thead>
    <tbody>
    <tr>
        <td>BiSeNet</td>
        <td>2018</td>
        <td>ECCV</td>
        <td>BiSeNet: Bilateral Segmentation Network for Real-time Semantic Segmentation</td>
        <td><a href="https://openaccess.thecvf.com/content_ECCV_2018/papers/Changqian_Yu_BiSeNet_Bilateral_Segmentation_ECCV_2018_paper.pdf">Paper</a></td>
        <td><a href="https://github.com/ycszen/BiSeNet">Code</a></td>
        <td>Cityscapes, CamVid, COCO-Stuff</td>  
    </tr>
    <tr>
        <td>Fast-SCNN</td>
        <td>2019</td>
        <td>BMVC</td>
        <td>Fast-SCNN: Fast Semantic Segmentation Network</td>
        <td><a href="https://bmvc2019.org/wp-content/uploads/papers/0959-paper.pdf">Paper</a></td>
        <td><a href="https://github.com/Tramac/Fast-SCNN-pytorch">Code</a></td>
        <td>Cityscapes</td>  
    </tr>
    <tr>
        <td>BiSeNetV2</td>
        <td>2021</td>
        <td>IJCV</td>
        <td>BiSeNet V2: Bilateral Network with Guided Aggregation for Real-time Semantic Segmentation</td>
        <td><a href="https://arxiv.org/pdf/2004.02147.pdf">Paper</a></td>
        <td><a href="https://github.com/ycszen/BiSeNet">Code</a></td>        
        <td>Cityscapes, CamVid, COCO-Stuff</td>  
    </tr>
    <tr>
        <td>STDC</td>
        <td>2021</td>
        <td>CVPR</td>
        <td>Rethinking BiSeNet For Real-time Semantic Segmentation</td>
        <td><a href="https://openaccess.thecvf.com/content/CVPR2021/papers/Fan_Rethinking_BiSeNet_for_Real-Time_Semantic_Segmentation_CVPR_2021_paper.pdf">Paper</a></td>
        <td><a href="https://github.com/MichaelFan01/STDC-Seg">Code</a></td>
        <td>Cityscapes, CamVid</td>  
    </tr>
    <tr>
        <td>DSANet</td>
        <td>2021</td>
        <td>ESWA</td>        
        <td>DSANet: Dilated spatial attention for real-time semantic segmentation in urban street scenes</td>
        <td><a href="https://www.sciencedirect.com/science/article/abs/pii/S0957417421005315">Paper</a></td>
        <td><a href="https://github.com/mohamedac29/DSANet">Code</a></td>
        <td>Cityscapes, CamVid</td>   
    </tr>
    <tr>
        <td>DDRNet</td>
        <td>2022</td>
        <td>T-ITS</td>
        <td>Deep Dual-resolution Networks for Real-time and Accurate Semantic Segmentation of Traffic Scenes</td>
        <td><a href="https://arxiv.org/pdf/2101.06085.pdf">Paper</a></td>
        <td><a href="https://github.com/ydhongHIT/DDRNet">Code</a></td>
        <td>Cityscapes, CamVid, COCO-Stuff</td>  
    </tr>
    </tbody>
    </table>

### Multi Branch Networks

<table>
    <thead>
      <tr>
       <th>Method</th>
        <th>Year</th>
        <th>Venue</th>
        <th>Title</th>
        <th>Paper</th>
        <th>Code</th>
        <th>Dataset</th>
      </tr>
    </thead>
    <tbody>
    <tr>
        <td>ICNet</td>
        <td>2018</td>
        <td>ECCV</td>
        <td>ICNet for Real-Time Semantic Segmentation on High-Resolution Images</td>
        <td><a href="https://openaccess.thecvf.com/content_ECCV_2018/papers/Hengshuang_Zhao_ICNet_for_Real-Time_ECCV_2018_paper.pdf">Paper</a></td>
        <td><a href="https://github.com/hszhao/ICNet">Code</a></td>
        <td>Cityscapes, CamVid</td>  
    </tr>
    <tr>
        <td>ESPNet</td>
        <td>2018</td>
        <td>ECCV</td>
        <td>ESPNet: Efficient Spatial Pyramid of Dilated Convolutions for Semantic Segmentation</td>
        <td><a href="https://openaccess.thecvf.com/content_ECCV_2018/papers/Sachin_Mehta_ESPNet_Efficient_Spatial_ECCV_2018_paper.pdf">Paper</a></td>
        <td><a href="https://sacmehta.github.io/ESPNet/">Code</a></td>
        <td>Cityscapes, PascalVOC</td>  
    </tr>
    <tr>
        <td>DFANet</td>
        <td>2019</td>
        <td>CVPR</td>
        <td>DFANet: Deep Feature Aggregation for Real-Time Semantic Segmentation</td>
        <td><a href="https://openaccess.thecvf.com/content_CVPR_2019/papers/Li_DFANet_Deep_Feature_Aggregation_for_Real-Time_Semantic_Segmentation_CVPR_2019_paper.pdf">Paper</a></td>
        <td><a href="https://github.com/huaifeng1993/DFANet">Code</a></td>
        <td>Cityscapes, CamVid</td> 
    </tr>
    <tr>
        <td>PIDNet</td>
        <td>2023</td>
        <td>CVPR</td>
        <td>PIDNet: A Real-time Semantic Segmentation Network Inspired by PID Controllers</td>
        <td><a href="https://openaccess.thecvf.com/content/CVPR2023/papers/Xu_PIDNet_A_Real-Time_Semantic_Segmentation_Network_Inspired_by_PID_Controllers_CVPR_2023_paper.pdf">Paper</a></td>
        <td><a href="https://github.com/XuJiacong/PIDNet">Code</a></td>
        <td>Cityscapes, CamVid,PASCAL Context</td>
    </tr>
    </tbody>
    </table>
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
 <!-- ICNet https://github.com/hszhao/ICNet Officialcode
 Template-Based-NAS-arch1 https://github.com/drsleep/nas-segm-pytorch Officialcode
 LiteSeg https://github.com/tahaemara/LiteSeg Officialcode
 Template-Based-NAS-arch0 https://github.com/drsleep/nas-segm-pytorch Officialcode
 ENet https://github.com/iArunava/ENet-Real-Time-Semantic-Segmentation Third-partycode
 ENet+Lovász-Softmax https://github.com/bermanmaxim/LovaszSoftmax Officialcode
 SegNet https://github.com/alexgkendall/caffe-segnet Third-partycode
 EDANet https://github.com/shaoyuanlo/EDANet Officialcode -->
