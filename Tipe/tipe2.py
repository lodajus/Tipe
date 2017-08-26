import numpy as np
from scipy import fftpack
from matplotlib import pyplot as plt

def image(n,tab):
    l=len(tab)
    k=0
    t_liste=[]
    t=1/n
   
    for i in range(l):
        t_liste.append(k)
        k+=t

    fe = 100
    T = t_liste[l-1]
    N = T*fe
    signal=tab
   # return shape(tab)
    signal = réduction_leaderprice(signal)
    signal = signal - mean(signal) # soustraction de la valeur moyenne du signal
                               # la fréquence nulle ne nous intéresse pas 
    signal_FFT = abs(fft(signal))
    # signal fréquentiel : on divise par la taille du vecteur pour normaliser la fft
    #fourier = fftpack.fft(tab)/l
    axe_f = np.fft.fftfreq(l,t)
    plt.figure()
    plt.subplot(121)
    plt.plot(t_liste,tab)
    plt.xlabel('axe temporel, en seconde')
    plt.subplot(122)
    plt.plot(axe_f,signal_FFT)
    plt.xlabel('axe frequentiels en Hertz')
    plt.show()

