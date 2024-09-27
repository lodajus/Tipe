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
        acc=2*acc+tab[i]
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
    sampling_freq,signal=read(nomfile)     #lecture du fichier wav a=fréquence d'échantillonage
    signal=np.array(ste_to_mono(signal)) #passage en mono
    signal=signal-mean(signal)  #suppression de la composante continue
    l=len(signal)
    
    
    frameSize=2048
    frameAdvance=round(frameSize/3)    
    c=math.ceil((l-frameSize)/frameAdvance)
    E = np.zeros((c,33))
    hamm=np.hamming(frameSize)
    start=0
    
    
    for i in range(c):
        etude=(signal[start:(start+frameSize)])*hamm
        freqdom = abs(fft(etude))[:1024] #ne prend que la moitié de l'analyse (l'autre est le symétrique) 
        for j in range(0,33): # 31 = 1024//33
            a=freqdom[(j)*31:(j+1)*31]
            E[i][j]=np.linalg.norm(a,ord=2)**2   #somme des termes entre (j)*31 et (j+1)*31 au carré
        start+=frameAdvance
    
    
    F = np.zeros((c,32))
    for n in range(1,c):
        for m in range(0,32):
            if ((E[n][m]-E[n][m+1]) - (E[n-1][m]-E[n-1][m+1])) > 0 :
                F[n,m] = 1
            else:
                F[n,m] = 0
    
    FPs=[]
    for n in range(c):
        FPs.append(rev_binarisation(F[n]))
    return FPs
    
    
    
    
    
    
    