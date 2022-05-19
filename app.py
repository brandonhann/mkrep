import csv
import os
import subprocess, sys
import pandas as pd
import numpy as np
import pdfkit
import time

csv_path='mkrep/bin/test.csv'
pdf_path='mkrep/Report.pdf'
header=pd.read_csv(r'mkrep/input/header.txt')
data_path=pd.read_csv(r'mkrep/input/data.txt')
html_path=csv_path[:-3]+'html'

def Convert():
    print('Creating Report...')
    wkhtmltopdf_path=r'/usr/bin/wkhtmltopdf'
    config=pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)

    df=pd.read_csv(csv_path,sep=',')
    df.to_html(html_path,index=False)

    pdfkit.from_file(html_path, pdf_path)
    print("Report Created")

def Open():
    opener='open' if sys.platform=='darwin' else 'xdg-open'
    subprocess.call([opener,csv_path])
    f=open(csv_path,'r')
    contents=f.read()

def Refresh():
    location='mkrep/bin/'
    if os.path.exists(pdf_path):
        print('Report Deleted')
        os.remove(pdf_path)
    for i in os.listdir(location):
        print(i + " Deleted")
        os.remove(os.path.join(location,i))

def Write():
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer=csv.writer(f)

        writer.writerow(header)
        writer.writerow(data_path)

Refresh()
Write()

if os.path.exists(csv_path):
    Open()
    Convert()