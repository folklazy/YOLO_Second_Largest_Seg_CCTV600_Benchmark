# ผลประเมิน YOLO กลุ่ม second_largest บน CCTV600

Run `cctv600-20261116T073208561699Z` · ตรวจปิดรอบเมื่อ 2026-11-16T16:13:20+07:00 (เวลาไทย)

คุณภาพครบ 4/4 โมเดล ตัวละ 600 ภาพ GT เข้าเกณฑ์ 769 คน คะแนน Box AP สูงสุดในกลุ่มคือ **yolo26l-seg.pt 65.099%**

## คุณภาพกรอบบุคคล

| Model | AP % | AP50 % | AP75 % | P % | R % | F1 % | TP | FP | FN |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| yolo26l-seg.pt | 65.099 | 83.971 | 74.179 | 83.541 | 78.544 | 80.965 | 604 | 119 | 165 |
| yolo11l-seg.pt | 63.696 | 84.760 | 72.222 | 88.710 | 78.674 | 83.391 | 605 | 77 | 164 |
| yolov9c-seg.pt | 62.788 | 84.033 | 71.876 | 85.947 | 75.553 | 80.415 | 581 | 95 | 188 |
| yolov8l-seg.pt | 62.978 | 82.235 | 72.434 | 81.044 | 76.723 | 78.824 | 590 | 138 | 179 |

AP ใช้ IoU 0.50–0.95, 101 recall points และ maxDet 200 P/R/F1 ใช้ confidence ≥0.25 และ IoU ≥0.50 จับ valid GT ก่อนพิจารณา ignore union

## ความเร็ว

| Model | Clean rounds | Forward ms/ภาพ | Adapter ms/ภาพ | FPS | Allocated MiB |
| --- | --- | --- | --- | --- | --- |
| yolo26l-seg.pt | 3/3 | 32.419 | 59.770 | 16.731 | 671.182 |
| yolo11l-seg.pt | 3/3 | 31.570 | 58.082 | 17.217 | 727.638 |
| yolov9c-seg.pt | 3/3 | 33.930 | 60.060 | 16.650 | 506.215 |
| yolov8l-seg.pt | 3/3 | 39.798 | 72.958 | 13.707 | 686.878 |

เวลาหลักมาจาก 100 ภาพเดิม × 3 clean rounds หลัง warmup 10 calls ต่อรอบ Adapter รวม preprocess/H2D + forward + postprocess/native-mask transfer ส่วน input read/decode, RLE และเขียนไฟล์วัดแยก FPS = 1000 / mean adapter ms

## กราฟและภาพตัวอย่าง

![PR curve](https://raw.githubusercontent.com/folklazy/YOLO_Instance_Segmentation_CCTV600_Scaling_Study/main/metrics/plots/second_largest_pr_curve.png)

![F1-confidence curve](https://raw.githubusercontent.com/folklazy/YOLO_Instance_Segmentation_CCTV600_Scaling_Study/main/metrics/plots/second_largest_f1_curve.png)

เส้น F1 แสดงผลของ threshold ต่อ trade-off โดย main threshold คง 0.25 ภาพเปรียบเทียบ 16 ภาพเดิมเปิดในเครื่องที่ `outputs/cctv600-20261116T073208561699Z/gallery/index.html` ของ repo นี้

## แหล่งผลและข้อจำกัด

[ตารางกลุ่ม](metrics/TIER_RESULTS.csv) และ [canonical summary](metrics/RESULTS.json) มาจาก saved packets ที่ตรวจรับแล้ว Source/scientific bindings คงเดิม อ่าน [รายงานรวม](https://github.com/folklazy/YOLO_Instance_Segmentation_CCTV600_Scaling_Study/blob/main/MASTER_RESULTS.md), [สูตรตัวชี้วัด](https://github.com/folklazy/YOLO_Instance_Segmentation_CCTV600_Scaling_Study/blob/main/METRIC_GUIDE_TH.md) และ [ผลตรวจปิดรอบ](https://github.com/folklazy/YOLO_Instance_Segmentation_CCTV600_Scaling_Study/blob/main/metrics/CLOSEOUT.json)

งานนี้วัด visible bbox บน CCTV600 ของ pretrained segmentation checkpoints ส่วน native masks เก็บเป็น output diagnostics ยังไม่มี GT silhouette สำหรับ Person Mask AP ไม่มี human parsing/color/tracking score และยังไม่มี uncertainty analysis
