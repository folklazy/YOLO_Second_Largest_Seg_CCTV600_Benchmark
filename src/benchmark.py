"""Tier entry point using the pinned common study implementation."""
from pathlib import Path
import sys

workspace = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(workspace / "YOLO_Instance_Segmentation_CCTV600_Scaling_Study" / "src"))
from cctv600.cli import main

if __name__ == "__main__":
    main(default_tier=Path(__file__).resolve().parents[1].name)
