# -*- coding: utf-8 -*-
# programme AnalSpectrale02
# tracé du spectre d'un signal réel tiré d'un fichier .wav
# Dominique Lefebvre pour TangenteX.com
# 14 décembre 2014

# importation des librairies
from numpy import linspace, mean
from scipy.fftpack import fft, fftfreq
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
import numpy as np

##


def ste_to_mono(signal):
    a,b=np.shape(signal)
    signal2=[]
    for k in range(a):
        signal2.append(signal[k-1][0])
    return signal2
    
def reduc(rate,signal):
    l=len(signal)
    tab=[]
    for x in range(0,l-4,4):
        tab.append(np.mean(signal[x:x+4] ))
    rate= rate//4
    return (rate,tab)
  
  ##  
    
#nomfile = 'C:/Users/ludovic/Documents/prépa/68448__pinkyfinger__piano-g.wav'
def fourier(nomfile):    

   
    rate,signal = read(nomfile)
    
    # définition du vecteur temps
    dt = 1./rate
    FFT_size = 2**18
    NbEch = signal.shape[0]
    
    # t = linspace(0,(NbEch-1)*dt,NbEch)
    # t = t[0:FFT_size]
    
    # calcul de la TFD par l'algo de FFT
    signal = signal[0:FFT_size]
    signal = ste_to_mono(signal)
    signal = signal - mean(signal) # soustraction de la valeur moyenne du signal
                                # la fréquence nulle ne nous intéresse pas 
    signal_FFT = abs(fft(signal))  # on ne récupère que les composantes réelles
    
    
    # récupération du domaine fréquentiel en passant la période d'échantillonnage
    signal_freq = fftfreq(signal.size, dt)
    
    # extraction des valeurs réelles de la FFT et du domaine fréquentiel
    signal_FFT = signal_FFT[0:len(signal_FFT)//2]
    signal_freq = signal_freq[0:len(signal_freq)//2]
    return (signal_freq,signal_FFT)

def graph_fourier(nomfile):
      
    signal_freq,signal_FFT = fourier(nomfile)  
    
    #affichage du signal
    plt.subplot(211)
    plt.title('Signal reel et son spectre')
    plt.plot(t,signal)
    plt.xlabel('Temps (s)'); plt.ylabel('Amplitude')
    
    #affichage du spectre du signal
    plt.subplot(212)
    plt.xlabel('Frequence (Hz)'); plt.ylabel('Amplitude')
  
    #Fmin = 0
    #Fmax = 4000    
    #plt.xlim(Fmin,Fmax)
    #plt.ylim(125,200)
    plt.plot(signal_freq,signal_FFT)
    
    plt.show()

##

def fenetre(longueur,rate,t):
    temps=np.zeros(longueur)
    window=np.hamming(rate/10)
    for x in range(len(window)):
        temps[x+t]=window[x]
    return temps
    
def clef_fourier(nomfile):
    rate,signal = read(nomfile)
    signal=ste_to_mono(signal)
    rate,signal=reduc(rate,signal)
    signal = signal - mean(signal)
    a=len(signal)
    tab =[]
    for x in range(rate):
        temps=fenetre(a,rate,x) # fenêtre analysée
        signal_FFT = abs(fft(signal*temps))
        tab.append(signal_FFT)
    dt=1/rate
    signal_freq = fftfreq(len(signal), dt)
    signal_freq = signal_freq[0:len(signal_freq)//2]
    return (tab,signal_freq)
    
    
 
##
def selection(tab_fft,tab_freq):
    
    l_30=l_40=l_80=l_120=l_180=l_300=0
    for x in range(len(tab_freq)):
        if tab_freq[x]>=30:
            l_30=i
        elif tab_freq[x]>=40:
            l_40=i
        elif tab_freq[x]>=80:
            l_80=i
        elif tab_freq[x]>=120:
            l_120=i
        elif tab_freq[x]>=180:
            l_180=i
        elif tab_freq[x]>=300:
            l_300=i
            break
    m_1=np.amax(tab_fft[l_30:l_40+1])
    m_2=np.amax(tab_fft[l_40:l_80+1])
    m_3=np.amax(tab_fft[l_80:l_120+1])
    m_4=np.amax(tab_fft[l_120:l_180+1])
    m_5=np.amax(tab_fft[l_180:l_300+1])
    return ([m_1,m_2,m_3,m_4,m_5])
    
##
def shazamization(nomfile):
    tab,signal_freq = clef_fourier(nomfile)
    return tab
    
    
   # 
