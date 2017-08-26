import numpy as np
from scipy import fftpack
from matplotlib import pyplot as plt

def analyse(n,tab):
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
    # signal fréquentiel : on divise par la taille du vecteur pour normaliser la fft
    fourier = np.fft.fft(tab)/l
   # return fourier
    p = fourier.size//2
    
    freq = np.fft.fftfreq(p,t)
    long_freq=len(freq)
    long_four=len(fourier)
    return long_freq,long_four
   
   
    # fourier = fftpack.fft(tab)/l
    # axe_f=[]
    # for i in range(l):
    #     axe_f.append(i)
    # axe_f = np.array(axe_f)*fe/N
    plt.figure()
    plt.subplot(121)
    plt.plot(t_liste,tab)
    plt.xlabel('axe temporel, en seconde')
    plt.subplot(122)
    plt.plot(freq,fourier.real)
    plt.xlabel('axe frequentiels en Hertz')
    plt.show()



##
import numpy as np
import matplotlib.pyplot as plt

# definition du signal
dt = 0.1
T1 = 2
T2 = 5
t = np.arange(0, T1*T2, dt)
signal = 2*np.cos(2*np.pi/T1*t) + np.sin(2*np.pi/T2*t)

# affichage du signal
plt.subplot(211)
plt.plot(t,signal)

# calcul de la transformee de Fourier et des frequences
fourier = np.fft.fft(signal)
n = signal.size
freq = np.fft.fftfreq(n, d=dt)

# affichage de la transformee de Fourier
plt.subplot(212)
plt.plot(freq, fourier.real, label="real")
plt.plot(freq, fourier.imag, label="imag")
plt.legend()

plt.show()
##