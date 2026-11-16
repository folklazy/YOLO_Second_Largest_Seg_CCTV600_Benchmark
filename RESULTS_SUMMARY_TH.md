# สรุปผล Second-largest (L/C) บน CCTV600

## สรุปใน 1 นาที

- ทดสอบ 4 pretrained checkpoints บน 600 ภาพชุดเดียวกันและ GT เข้าเกณฑ์ 769 คน
- Input 640×640, batch 1, FP32 บน Tesla T4 ไม่มี fine-tuning ใน benchmark รอบนี้
- คุณภาพครบ 600 IDs ต่อโมเดล และเวลาครบ 3 clean rounds ต่อโมเดล
- Box AP สูงสุดเป็น yolo26l-seg.pt ที่ 65.099%
- Adapter time ต่ำสุดเป็น yolo11l-seg.pt ที่ 58.082 ms/ภาพ
- Allocated VRAM ต่ำสุดเป็น yolov9c-seg.pt ที่ 506.215 MiB

## ผลลัพธ์หลัก

| Model | Box AP % | AP75 % | Recall % | Forward ms/ภาพ | Adapter ms/ภาพ | FPS | Allocated MiB |
| --- | --- | --- | --- | --- | --- | --- | --- |
| yolo26l-seg.pt | 65.099 | 74.179 | 78.544 | 32.419 | 59.770 | 16.731 | 671.182 |
| yolo11l-seg.pt | 63.696 | 72.222 | 78.674 | 31.570 | 58.082 | 17.217 | 727.638 |
| yolov9c-seg.pt | 62.788 | 71.876 | 75.553 | 33.930 | 60.060 | 16.650 | 506.215 |
| yolov8l-seg.pt | 62.978 | 72.434 | 76.723 | 39.798 | 72.958 | 13.707 | 686.878 |

Box AP/P/R/F1 แสดงเป็นเปอร์เซ็นต์ Forward และ adapter เป็น ms/ภาพ, FPS = 1000 / mean adapter ms และ VRAM เป็น peak allocated MiB

## ผู้ชนะของแต่ละด้าน

| ด้าน | โมเดล | ค่าที่วัด |
| --- | --- | --- |
| Box AP | yolo26l-seg.pt | 65.099 % |
| AP75 | yolo26l-seg.pt | 74.179 % |
| Recall | yolo11l-seg.pt | 78.674 % |
| Forward time | yolo11l-seg.pt | 31.570 ms/ภาพ |
| Adapter time | yolo11l-seg.pt | 58.082 ms/ภาพ |
| Adapter FPS | yolo11l-seg.pt | 17.217 ภาพ/วินาที |
| Allocated VRAM | yolov9c-seg.pt | 506.215 MiB |

## สิ่งที่ตัวเลขบอกเรา

- yolo26l-seg.pt มี AP สูงกว่า yolo11l-seg.pt 1.403 จุดเปอร์เซ็นต์
- ตัวนำ AP มี TP 604, FP 119 และ FN 165 ที่ confidence ≥0.25 / bbox IoU ≥0.50
- Adapter ของ yolo11l-seg.pt เร็วกว่าตัวนำ AP 1.687 ms/ภาพ
- ตัวนำ AP ใช้ allocated VRAM มากกว่าค่าต่ำสุด 164.966 MiB

## บทบาทของแต่ละโมเดล

| โมเดล | จุดเด่นที่วัดได้ | ข้อแลกเปลี่ยน | เงื่อนไขการเลือก |
| --- | --- | --- | --- |
| yolo26l-seg.pt | Box AP สูงสุดในกลุ่ม | Recall ห่างตัวนำ 0.130 pp, adapter เพิ่ม 1.687 ms, VRAM เพิ่ม 164.966 MiB | เน้น Box AP |
| yolo11l-seg.pt | Precision สูงสุด, Recall สูงสุด, forward เร็วสุดในกลุ่ม, adapter เร็วสุดในกลุ่ม | AP ห่างตัวนำ 1.403 pp, VRAM เพิ่ม 221.423 MiB | ลดสัดส่วนกรอบเกิน, เก็บคนให้ครบ, จำกัดเวลา adapter |
| yolov9c-seg.pt | allocated VRAM ต่ำสุดในกลุ่ม | AP ห่างตัวนำ 2.311 pp, Recall ห่างตัวนำ 3.121 pp, adapter เพิ่ม 1.978 ms | จำกัด allocated VRAM |
| yolov8l-seg.pt | AP 62.978% และ Recall 76.723% | AP ห่างตัวนำ 2.121 pp, Recall ห่างตัวนำ 1.951 pp, adapter เพิ่ม 14.875 ms | ใช้เป็นจุดอ้างอิงของ checkpoint ในกลุ่มนี้ |

## ข้อแลกเปลี่ยนหลัก

### คุณภาพกับความเร็ว

ตัวนำ AP มี AP 65.099% ส่วนตัว adapter เร็วสุดมี AP 63.696% ทั้งสองเป้าหมายอาจได้ checkpoint เดียวกัน ให้พิจารณา forward กับ adapter แยกกัน เพราะ native mask postprocessing มีต้นทุนอยู่หลัง model forward

### คุณภาพกับหน่วยความจำ

ตัว allocated VRAM ต่ำสุดมี AP 62.788% และใช้ 506.215 MiB ค่า allocator peak นี้ครอบคลุม resident model ใน benchmark หลัง warmup ส่วน memory รวมในระบบให้ตรวจ CUDA context และบริการที่รันร่วมด้วย

## ข้อควรระวังในการตีความ

GT ใช้ visible bbox ของคนด้านยาว ≥50 px รวม 769 คน การรับรอง person inventory อิงการตรวจรับของผู้จัดทำ dataset ยังไม่มี independent inventory review ครบชุด ขนาดโมเดลและข้อมูล pretraining ต่างกัน การเปรียบเทียบนี้ยังไม่แยกสาเหตุทาง architecture ไม่มี uncertainty analysis และ Person Mask AP ต้องมี GT silhouette เพิ่ม Adapter time ครอบคลุม preprocessing/H2D, forward และ postprocessing/native-mask transfer โดย input I/O, RLE, writing, model loading และ queue time มีขอบเขตแยก

## อ่านต่อ

[รายงานเทคนิค](REPORT.md) · [การวิเคราะห์ภาพและข้อผิดพลาด](PRESENTATION_SUMMARY_TH.md) · [ตารางเต็ม](metrics/TIER_RESULTS.csv) · [สูตรตัวชี้วัด](https://github.com/folklazy/YOLO_Instance_Segmentation_CCTV600_Scaling_Study/blob/main/METRIC_GUIDE_TH.md)
