# YOLO_Second_Largest_Seg_CCTV600_Benchmark

ทดสอบกลุ่ม **second_largest** บน CCTV 600 ภาพ ใช้ visible GT bbox ของคนด้านยาวตั้งแต่ 50 px และ common protocol เดียวกับทั้ง study

| Checkpoint |
| --- |
| `yolo26l-seg.pt` |
| `yolo11l-seg.pt` |
| `yolov9c-seg.pt` |
| `yolov8l-seg.pt` |

[สถานะ](STATUS.md) · [ผลคะแนนและความเร็ว](RESULTS_SUMMARY_TH.md) · [Protocol](EXPERIMENT_PROTOCOL.md) · [Master](https://github.com/folklazy/YOLO_Instance_Segmentation_CCTV600_Scaling_Study)

## การใช้งาน

Clone Master และ tier repositories ไว้ใน workspace เดียวกัน ใช้ shared models และ environment ที่ตรวจแล้ว

```bash
.venv/bin/python YOLO_Second_Largest_Seg_CCTV600_Benchmark/src/benchmark.py status
```

สถานะปิดรอบที่รวม timing continuation ให้อ่าน STATUS.md และ RESULTS_SUMMARY_TH.md ของ repo นี้ ส่วนคำสั่ง status ข้างต้นอ่าน original execution record ที่เก็บไว้ตามประวัติ

คำสั่ง launch จาก tier entry จำกัด scope ที่กลุ่มนี้ ส่วน Master entry เปิดคิวทั้ง study ตามลำดับขนาด ดูคำสั่ง prepare, launch และ reconcile ที่ Master README

Raw predictions, logs, per-image CSV และ fixed-sample gallery เก็บใน outputs ของ tier ส่วน metrics/RESULTS.json และ TIER_RESULTS.csv เป็นสถิติรวมสำหรับตรวจต่อ
