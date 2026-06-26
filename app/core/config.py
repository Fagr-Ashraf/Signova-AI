import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

I3D_WEIGHTS = os.path.join(
    BASE_DIR,
   # "assets/I3D_300Weights/FINAL_nslt_300_iters2997_top156.14_top579.94_top1086.98.pt"
   "assets/I3D_300Weights/FINAL_nslt_100_iters=896_top1=65.89_top5=84.11_top10=89.92 (1).pt"
)

CLASS_LIST = os.path.join(
    BASE_DIR,
    "assets/I3D_modelfiles/wlasl_class_list.txt"
)