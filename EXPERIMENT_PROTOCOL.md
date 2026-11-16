# Protocol ของ YOLO_Second_Largest_Seg_CCTV600_Benchmark

ใช้ [common study protocol](https://github.com/folklazy/YOLO_Instance_Segmentation_CCTV600_Scaling_Study/blob/main/EXPERIMENT_PROTOCOL.md) รุ่น 1.0.0 พร้อม [config ของกลุ่มนี้](configs/benchmark.json)

มี 4 checkpoints ตาม roster ที่ประกาศ ทุกกลุ่มใช้ source เดียวกันสำหรับ preprocessing, packet export, bbox scoring, timing และ reporting โดยกำหนด model membership แยกใน config

Primary คือ Person Box AP@[.50:.95] ภายใต้ GT-first matching, coarse-ignore union และ maxDet 200 ส่วน fixed Precision/Recall/F1 ใช้ confidence 0.25 และ bbox IoU 0.50

ใช้ population 600 ภาพและ bindings เดียวกัน ผลไม่ครบให้ primary เป็น null CPU acceptance และ preflight ต้องผ่านก่อน full run โดยใช้ FP32, batch 1 และ input 640

Dedicated timing ใช้ 100 ภาพสาม clean rounds และ warmup 10 calls ต่อรอบ แยก input I/O, RLE และ output writing จาก adapter pipeline รอบที่ GPU ปนเปื้อนเก็บเป็น diagnostics

Person inventory อ้างคำยืนยันตรวจ 600 ภาพตามกติกาทุกคน ≥50 px และคง source annotations เดิม รายละเอียด resource guards, recovery และข้อจำกัดให้ยึด common protocol
