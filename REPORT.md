# Second-largest (L/C) YOLO Segmentation Benchmark — CCTV600

## 1. Experiment Status

COMPLETE for accuracy and dedicated clean timing. Each of 4 models has 600 accepted unique image packets. Evaluation includes 769 eligible person boxes. Dataset-quality and interpretation limitations remain documented below.

## 2. Models Tested

| Family | Checkpoint | Parameters | GFLOPs estimate | Weights MB |
| --- | --- | --- | --- | --- |
| YOLO26 | yolo26l-seg.pt | 31,515,528 | 151.304 | 63.700 |
| YOLO11 | yolo11l-seg.pt | 27,678,368 | 133.176 | 56.097 |
| YOLOv9 | yolov9c-seg.pt | 27,897,120 | 149.340 | 56.470 |
| YOLOv8 | yolov8l-seg.pt | 45,997,728 | 211.060 | 92.417 |

## 3. Protocol Compatibility

| Item | Status and evidence |
| --- | --- |
| Dataset | PASS · 600 exact IDs; dataset membership SHA in frozen config |
| Evaluator | PASS · GT-first bbox matching and shared ignore union |
| Preprocessing | PASS · frozen runtime source binding |
| Input size | 1×3×640×640, centered letterbox |
| Precision | FP32; no AMP/TF32/extra TTA |
| Thresholds | AP floor .001, fixed conf .25, match IoU .50, NMS IoU .70 |
| maxDet | Model 1000 / evaluator 200; cap parity PASS |
| Timing | 3×100 clean observations, warmup 10 each round; sample order verified |
| Environment | Python 3.12.3 / torch 2.14.0+cu130 / Ultralytics 8.4.160 / Tesla T4 |

Compatibility applies within this CCTV600 experiment. MOTS20 supplies the reporting structure and reused detector runtime. CCTV600 uses visible box GT, its ≥50 px eligibility and coarse rectangle-ignore policy. MOTS20 uses person silhouettes and mask matching.

## 4. Overall Results

| Model | Box AP % | AP75 % | Recall % | Forward ms/ภาพ | Adapter ms/ภาพ | FPS | Allocated MiB |
| --- | --- | --- | --- | --- | --- | --- | --- |
| yolo26l-seg.pt | 65.099 | 74.179 | 78.544 | 32.419 | 59.770 | 16.731 | 671.182 |
| yolo11l-seg.pt | 63.696 | 72.222 | 78.674 | 31.570 | 58.082 | 17.217 | 727.638 |
| yolov9c-seg.pt | 62.788 | 71.876 | 75.553 | 33.930 | 60.060 | 16.650 | 506.215 |
| yolov8l-seg.pt | 62.978 | 72.434 | 76.723 | 39.798 | 72.958 | 13.707 | 686.878 |

| Model | Precision % | Recall % | F1 % | TP | FP | FN | Ignored | TP-only box IoU |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| yolo26l-seg.pt | 83.541 | 78.544 | 80.965 | 604 | 119 | 165 | 22 | 0.881598 |
| yolo11l-seg.pt | 88.710 | 78.674 | 83.391 | 605 | 77 | 164 | 27 | 0.872591 |
| yolov9c-seg.pt | 85.947 | 75.553 | 80.415 | 581 | 95 | 188 | 21 | 0.870662 |
| yolov8l-seg.pt | 81.044 | 76.723 | 78.824 | 590 | 138 | 179 | 22 | 0.882126 |

AP/P/R/F1 columns use percentages. TP-only box IoU is a fraction. Counts use confidence ≥0.25 and box IoU ≥0.50. AP uses 10 IoU thresholds, 101 recall points and maxDet 200. Source-precision values remain in CSV.

## 5. Tier Winners

| ด้าน | โมเดล | ค่าที่วัด |
| --- | --- | --- |
| Box AP | yolo26l-seg.pt | 65.099 % |
| AP75 | yolo26l-seg.pt | 74.179 % |
| Recall | yolo11l-seg.pt | 78.674 % |
| Forward time | yolo11l-seg.pt | 31.570 ms/ภาพ |
| Adapter time | yolo11l-seg.pt | 58.082 ms/ภาพ |
| Adapter FPS | yolo11l-seg.pt | 17.217 ภาพ/วินาที |
| Allocated VRAM | yolov9c-seg.pt | 506.215 MiB |

## 6. Key Findings

The highest Box AP is yolo26l-seg.pt (65.099%), 1.403 percentage points above the runner-up. The shortest adapter mean belongs to yolo11l-seg.pt (58.082 ms/image). Differences are descriptive; no significance or architecture-causality claim is made.

## 7. Per-group Observations

| Model | Day AP % | Night AP % | R 50–99 px % | R 100–199 px % | R ≥200 px % |
| --- | --- | --- | --- | --- | --- |
| yolo26l-seg.pt | 59.651 | 69.628 | 54.494 | 82.456 | 90.361 |
| yolo11l-seg.pt | 57.962 | 68.283 | 54.494 | 83.041 | 89.960 |
| yolov9c-seg.pt | 54.252 | 69.406 | 45.506 | 80.409 | 90.361 |
| yolov8l-seg.pt | 55.732 | 68.569 | 46.629 | 82.164 | 90.763 |

Day/night use existing metadata and contain different scenes and people. Pooled AP is read directly from the canonical full-population result. Size-band recall conditions on GT size and the original matching; precision/AP by size were not computed under a new policy.

## 8. Efficiency and Resource Observations

| Model | Pre mean ms | Post mean ms | Adapter P50 ms | Adapter P95 ms | Adapter std ms | Reserved MiB |
| --- | --- | --- | --- | --- | --- | --- |
| yolo26l-seg.pt | 1.835 | 25.515 | 52.419 | 105.924 | 23.022 | 1296.000 |
| yolo11l-seg.pt | 1.876 | 24.636 | 50.077 | 108.010 | 21.926 | 1236.000 |
| yolov9c-seg.pt | 1.897 | 24.233 | 53.830 | 95.997 | 19.065 | 960.000 |
| yolov8l-seg.pt | 2.037 | 31.123 | 65.687 | 118.441 | 22.959 | 1026.000 |

Means, median, P95 and population standard deviation use all 300 accepted observations. Adapter FPS excludes disk/decode, RLE, packet writing and load/warmup. Native postprocessing substage timers are inclusive subsets. Allocated/reserved peaks include the resident model and take the maximum across the three accepted rounds.

## 9. Warnings and Anomalies

The original study ended with incomplete Nano timing. A linked segment supplied four accepted clean rounds, retaining the original contaminated YOLO11n round and original completion unchanged. Accuracy was not rerun. Detailed accepted round paths and hashes are in the common result index. The owned web worker was restored after authorized temporary suspension.

## 10. Limitations

GT inventory relies on the dataset creator's 600-image acceptance. Independent all-person inventory adjudication remains unavailable. No full-person silhouette GT, mask AP, tracking or parsing/color score is reported here. TP-only IoU excludes missed people. Different pretrained capacities and training histories confound architecture attribution. Related frames and absent uncertainty analysis limit generalization.

## 11. Reproducibility and Source Artifacts

[Canonical tier table](metrics/TIER_RESULTS.csv), [timing statistics](metrics/TIMING_SUMMARY.csv), [shared source/protocol/checkpoint bindings](https://github.com/folklazy/YOLO_Instance_Segmentation_CCTV600_Scaling_Study/blob/main/metrics/RESULT_INDEX.json), [closed-run checks](https://github.com/folklazy/YOLO_Instance_Segmentation_CCTV600_Scaling_Study/blob/main/metrics/CLOSEOUT.json), [metric definitions](https://github.com/folklazy/YOLO_Instance_Segmentation_CCTV600_Scaling_Study/blob/main/METRIC_GUIDE_TH.md) and [presentation revision evidence](https://github.com/folklazy/YOLO_Instance_Segmentation_CCTV600_Scaling_Study/blob/main/metrics/PRESENTATION_REVISION.json).

## 12. Relation to Full Scaling Study

[Largest (X/E)](https://github.com/folklazy/YOLO_Large_Seg_CCTV600_Benchmark) · [Second-largest (L/C)](https://github.com/folklazy/YOLO_Second_Largest_Seg_CCTV600_Benchmark) · [Medium (M)](https://github.com/folklazy/YOLO_Medium_Seg_CCTV600_Benchmark) · [Small (S)](https://github.com/folklazy/YOLO_Small_Seg_CCTV600_Benchmark) · [Nano (N)](https://github.com/folklazy/YOLO_Nano_Seg_CCTV600_Benchmark) · [Master](https://github.com/folklazy/YOLO_Instance_Segmentation_CCTV600_Scaling_Study)

## Qualitative Analysis

[PRESENTATION_SUMMARY_TH.md](PRESENTATION_SUMMARY_TH.md) discusses four diagnostic cases from the original fixed16. Full frames, identical ROIs and per-GT matching are retained in the private local gallery. Only aggregate charts and de-identified qualitative observations are published.
