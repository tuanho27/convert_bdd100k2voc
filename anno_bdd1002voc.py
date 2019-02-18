import argparse, json
from lxml import etree, objectify
import os, re


def xml_base(anno):
    annotation = etree.Element("annotation")
    etree.SubElement(annotation, "folder").text = "bdd100k"
    etree.SubElement(annotation, "filename").text = anno['name']
    source = etree.SubElement(annotation, "source")
    etree.SubElement(source, "database").text = "Deep Drives"
    etree.SubElement(source, "annotation").text = "Deep Drives"
    etree.SubElement(source, "image").text = "Berkely"
    size = etree.SubElement(annotation, "size")
    etree.SubElement(size, "width").text = "1280"
    etree.SubElement(size, "height").text = "640"
    etree.SubElement(size, "depth").text = '3'
    etree.SubElement(annotation, "segmented").text = '0'
    return annotation


def xml_object(anno, xmltree):
    #xmin, ymin, xmax, ymax = anno['box2d']
    bbox = anno['box2d']
    attribute = anno['attributes']
    key_object = etree.SubElement(xmltree, "object")
    etree.SubElement(key_object, "name").text = anno['category']
    etree.SubElement(key_object, "pose").text = 'Unspecified'
    etree.SubElement(key_object, "difficult").text = '0'
    etree.SubElement(key_object, "truncated").text = str(attribute['truncated'])
    bndbox = etree.SubElement(key_object, "bndbox")
    etree.SubElement(bndbox, "xmin").text = str(bbox['x1'])
    etree.SubElement(bndbox, "ymin").text = str(bbox['y1'])
    etree.SubElement(bndbox, "xmax").text = str(bbox['x2'])
    etree.SubElement(bndbox, "ymax").text = str(bbox['y2'])
    return xmltree


def parse_info(content, outdir):
        for names in content:
            filename = os.path.join(outdir, names['name'].replace('jpg','xml'))
            print("@@@-----: ",filename)
            anno_tree = xml_base(names)
            for obj_labels in names['labels']:
                if str(obj_labels['category']) != "drivable area" and str(obj_labels['category']) != "lane":
                    doc = etree.ElementTree(anno_tree)
                    anno_tree = xml_object(obj_labels, anno_tree)
                doc.write(open(filename, "wb"), pretty_print=True)
        print("Formating xml file done!")


def main(args):
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
    content = json.load(open(args.anno_file, 'r'))
    print("Start convert json to xml!\n")
    parse_info(content, args.output_dir)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--anno_file", help="annotation file for object instance/keypoint")
    parser.add_argument("--output_dir", help="output directory for voc annotation xml file")
    args = parser.parse_args()
    main(args)
