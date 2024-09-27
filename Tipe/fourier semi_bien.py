from numpy import linspace, mean
from scipy.fftpack import fft, fftfreq
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
import numpy as np
import math
##

def rev_binarisation(tab):
    l=len(tab)
    acc=0
    for i in range(l):
        acc=2*acc+l[i]
    return acc
    
def ste_to_mono(signal):
    #réduire le signal stéréo à un signal mono pour utiliser la transformation de fourier
    #on ne récupère que la composante à droite du son 
    a,b=np.shape(signal)
    signal2=[]
    for k in range(a):
        signal2.append(signal[k-1][0])
    return signal2
    
    
def fingerprint(nomfile):
    a,list=read(nomfile)     #lecture du fichier wav a=fréquence d'échantillonage
    list=np.array(ste_to_mono(list)) 
    list=list-mean(list)
    l=len(list)
    
    frameSize=round(a*0.37)
    frameAdvance=round(a*0.116)    
    c=math.ceil((l-frameSize)/frameAdvance)
    E = np.zeros((c,33))
    hamm=np.hamming(frameSize)
    Eind,start=0,0
     
    while  start+frameSize <= l:
        etude=(list[start:(start+frameSize)])*hamm
        freqdom = abs(fft(etude))
        meldom = freqdom#[111:740]
        for j in range(0,33):
            a=meldom[(j)*19:(j+1)*19+1]
            b=a.transpose()
            E[Eind][j] = np.dot(a,b)
        Eind,start=Eind+1 , start+frameAdvance
    
    F = np.zeros((c,32))
    for n in range(2,max(np.shape(E))+1):
        for m in range(1,33):
            if ((E[n][m]-E[n][m+1]) - (E[n-1][m]-E[n-1][m+1])) > 0 :
                F[n,m] = 1
            else:
                F[n,m] = 0
    return F
    
    FPs=[]
    for n in range(c):
        FPs.append(rev_binarisation(F[n]))