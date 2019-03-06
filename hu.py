# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 18:15:42 2019

@author: Mehmet YEŞİLKAYA
"""

from PIL import Image
import numpy
import math

image = Image.open("kızKulesi.jpg")
np_im = numpy.array(image,dtype=numpy.int64)
imageWidth,imageHeight = image.size
imageArray =numpy.zeros((imageHeight,imageWidth),dtype=numpy.float64)
normalizeHuMoments = numpy.arange(7,dtype = numpy.float64)       

def griyeCevir(imageHeight,imageWidth,np_im,imageArray):
    for i in range(imageHeight):
        for j in range(imageWidth):
            grayValue = int(0.299*np_im[i][j][0] + 0.587*np_im[i][j][1] + 0.114*np_im[i][j][2])
            imageArray[i][j]= grayValue
    return imageArray      

def moment(p,q):
    momentpq=0
    for x in range(1,imageWidth + 1):
        for y in range(1,imageHeight + 1):
            momentpq=pow(x,p)*pow(y,q)*imageArray[y-1][x-1]+momentpq
           
    return momentpq
  
def degismezMoment(p,q):
    degismezMomentVar = 0
    moment10=moment(1,0)
    moment00=moment(0,0)
    moment01=moment(0,1)  

    kütleMerkeziX=moment10//moment00
    kütleMerkeziY=moment01//moment00 
   
    for x in range (imageWidth):
        for y in range(imageHeight):
                degismezMomentVar = pow(x-kütleMerkeziX,p)*pow(y-kütleMerkeziY,q)*imageArray[y][x] + degismezMomentVar

    return degismezMomentVar

def nMoment(p,q):
    y=((p+q)/2)+1
    normalizeMomentVar = degismezMoment(p,q)/(pow(degismezMoment(0,0),y))
    return normalizeMomentVar

def huMoments():
    griyeCevir(imageHeight,imageWidth,np_im,imageArray)
    nMoment02 = nMoment(0,2)
    nMoment03 = nMoment(0,3)
    nMoment11 = nMoment(1,1)
    nMoment12 = nMoment(1,2)
    nMoment20 = nMoment(2,0)
    nMoment21 = nMoment(2,1)
    nMoment30 = nMoment(3,0)
    m1 = (nMoment20 + nMoment02)
    m2 = pow(nMoment20 - nMoment02,2) + 4*pow(nMoment11,2)
    m3 = pow(nMoment30 - 3*nMoment12,2) + pow(3*nMoment21 - nMoment03,2)
    m4 = pow(nMoment30 + nMoment12,2) + pow(nMoment21 + nMoment03,2)
    m5 = (nMoment30-3*nMoment12)*(nMoment30+nMoment12)*(pow((nMoment30 + nMoment12),2)-3*(pow((nMoment21+nMoment03),2)))+(3*nMoment21-nMoment03)*(nMoment21+nMoment03)*(3*(pow(nMoment30+nMoment12,2))-pow((nMoment21+nMoment03),2))
    m6 = (nMoment20-nMoment02)*(pow(nMoment30+nMoment12,2)-pow(nMoment21+nMoment03,2))+4*nMoment11*(nMoment30+nMoment12)*(nMoment21+nMoment03)
    m7 = (3*nMoment21-nMoment03)*(nMoment30+nMoment12)*(pow(nMoment30+nMoment12,2)-3*(pow(nMoment21+nMoment03,2)))-(nMoment30-3*nMoment12)*(nMoment21+nMoment03)*(3*pow(nMoment30+nMoment12,2)-pow(nMoment21+nMoment03,2))
#    log Transform
    normalizeHuMoments[0] = abs(-numpy.copysign(1.0,m1)*numpy.log10(numpy.abs(m1)))
    normalizeHuMoments[1] = abs(-numpy.copysign(1.0,m2)*numpy.log10(numpy.abs(m2)))
    normalizeHuMoments[2] = abs(-numpy.copysign(1.0,m3)*numpy.log10(numpy.abs(m3)))
    normalizeHuMoments[3] = abs(-numpy.copysign(1.0,m4)*numpy.log10(numpy.abs(m4)))
    normalizeHuMoments[4] = abs(-numpy.copysign(1.0,m5)*numpy.log10(numpy.abs(m5)))
    normalizeHuMoments[5] = abs(-numpy.copysign(1.0,m6)*numpy.log10(numpy.abs(m6)))
    normalizeHuMoments[6] = abs(-numpy.copysign(1.0,m7)*numpy.log10(numpy.abs(m7)))
    
    print("Hu Moment Değerleri:")    
    print("m1:",+normalizeHuMoments[0])
    print("m2:",+normalizeHuMoments[1])
    print("m3:",+normalizeHuMoments[2])
    print("m4:",+normalizeHuMoments[3])
    print("m5:",+normalizeHuMoments[4])
    print("m6:",+normalizeHuMoments[5])
    print("m7:",+normalizeHuMoments[6])
    
    