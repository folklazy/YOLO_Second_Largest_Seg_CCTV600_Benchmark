# ผลประเมิน YOLO บน CCTV600

Run `cctv600-20261116T073208561699Z`

คะแนนหลักเป็น Person Box AP ของ segmentation checkpoints บน visible GT bbox เกณฑ์คนด้านยาว ≥50 px

| Model | Complete | Box AP % | AP50 % | AP75 % | P % | R % | F1 % |
| --- | --- | --- | --- | --- | --- | --- | --- |
| yolo26l-seg.pt | 0/600 | — | — | — | — | — | — |
| yolo11l-seg.pt | 0/600 | — | — | — | — | — | — |
| yolov9c-seg.pt | 0/600 | — | — | — | — | — | — |
| yolov8l-seg.pt | 0/600 | — | — | — | — | — | — |

| Model | Clean rounds | Forward ms/image | Adapter ms/image | FPS | Allocated MiB |
| --- | --- | --- | --- | --- | --- |
| yolo26l-seg.pt | 0/3 | — | — | — | — |
| yolo11l-seg.pt | 0/3 | — | — | — | — |
| yolov9c-seg.pt | 0/3 | — | — | — | — |
| yolov8l-seg.pt | 0/3 | — | — | — | — |

Adapter time รวม preprocessing/H2D, forward, NMS/native masks และ compact transfer ส่วน input I/O, RLE และ output writing เก็บแยก

P/R/F1 ใช้confidence≥0.25 และbboxIoU≥0.50 ส่วนAPใช้IoU0.50:0.05:0.95 และmaxDet200 โดยเก็บpredictionsเหนือconfidencefloor0.001

Timing หลักแสดงเมื่อมีสาม clean rounds ครบ งาน GPU อื่นทำให้รอบเวลาเป็น diagnostics

GT person inventory อ้างคำยืนยันตรวจ600ภาพตามกติกาทุกคน≥50px ข้อมูลบางส่วนเคยใช้พัฒนาannotation helper ส่วนผู้เข้าสอบใช้pretrained checkpointที่ตรึง

ภาพจริงและ per-image diagnostics เก็บ private ใน outputs ของ tier ส่วน results JSON/CSV เก็บสถิติรวม

ผลนี้เป็น checkpoint+application configuration comparison ของกรอบคน และยังไม่มีผล Person Mask AP หรือ tracking
