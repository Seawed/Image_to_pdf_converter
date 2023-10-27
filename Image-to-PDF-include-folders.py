import traceback
from os import listdir
from os.path import isfile, join
from fpdf import FPDF
import os

rootdir = 'C:/Users/avgal/Downloads/Naruto_Manga/Манга Наруто'
for it in os.scandir(rootdir):
    if it.is_dir():
        mypath = it.path
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and f.endswith('.jpg') or f.endswith('.png') or f.endswith('.jpeg') ]
        pdf = FPDF()
        # imagelist is the list with all image filenames

        try:

            for image in onlyfiles:
                pdf.add_page()
                pdf.image(name=it.path + "/" + str(image), x=5, y=5, w=200, h=270)
            pdf.output(it.path + "-naruto.pdf", "F")

        except:
            traceback.print_exc()
            print(it.path)
            continue