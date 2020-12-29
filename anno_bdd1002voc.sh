#!/usr/bin/env bash

# Original json format 
#python anno_bdd1002voc.py --anno_file /data/bdd100k/coco_format/detection/annotations/bdd100k_det_train_cocoformat.json \
#                          --output_dir /data/bdd100k/voc_format/annotations/train
#python anno_bdd1002voc.py --anno_file /data/bdd100k/coco_format/detection/annotations/bdd100k_det_val_cocoformat.json \
#                          --output_dir /data/bdd100k/voc_format/annotations/val

# Json coco format
python anno_coco1002voc.py --anno_file /data/bdd100k/coco_format/detection/annotations/bdd100k_det_train_cocoformat.json \
                          --output_dir /data/bdd100k/voc_format/annotations/train
python anno_coco1002voc.py --anno_file /data/bdd100k/coco_format/detection/annotations/bdd100k_det_val_cocoformat.json \
                          --output_dir /data/bdd100k/voc_format/annotations/val
