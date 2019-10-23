# sudo pip3 install opencv-python==4.1.1.26
import os
import cv2
import argparse

def compress(dirname):
    for filename in os.listdir(dirname):
        img=cv2.imread(dirname+'/'+filename,1)
        cv2.imwrite(dirname+'/'+filename,img,[cv2.IMWRITE_JPEG_QUALITY,20])

def print_gallery_statements(dirname, gallery_name):
    for filename in os.listdir(dirname):
        print("{{% gallery /img/gallery/{}/{} {} %}}".format(gallery_name,filename,dirname))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Compress the images and then print gallery statements')

    parser.add_argument(
        '-d', '--dirname',
        type=str,
        help="the directory name including the images you want to compress")
    parser.add_argument(
    '-g', '--galleryname',
    type=str,
    help="the gallery name including the images you want to post")

    args = parser.parse_args()
    compress(args.dirname)
    print_gallery_statements(args.dirname, args.galleryname)
