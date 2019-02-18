#!/usr/bin/env bash
rm -rf  /home/tuanho/Work/projects/software/toyota/dataset/bdd100k/labels/annotation_*

python anno_bdd1002voc.py --anno_file /home/tuanho/Work/projects/software/toyota/dataset/bdd100k/labels/bdd100k_labels_images_train.json \
                          --output_dir /home/tuanho/Work/projects/software/toyota/dataset/bdd100k/labels/annotation_train
python anno_bdd1002voc.py --anno_file /home/tuanho/Work/projects/software/toyota/dataset/bdd100k/labels/bdd100k_labels_images_val.json \
                          --output_dir /home/tuanho/Work/projects/software/toyota/dataset/bdd100k/labels/annotation_val
