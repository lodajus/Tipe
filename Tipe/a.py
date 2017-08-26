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

    fe = n
    T = t_liste[l-1]
    N = T*fe
    # signal fréquentiel : on divise par la taille du vecteur pour normaliser la fft
    fourier =np.fft.rfft(tab)
    
    axe_f = np.fft.fftfreq(l,t)
    # axe_f=[]
    # for i in range(l):
    #     axe_f.append(i)
    # axe_f = np.array(axe_f)*fe/N
    plt.figure()
    plt.subplot(311)
    plt.plot(t_liste,tab)
    plt.xlabel('axe temporel, en seconde')
    # plt.subplot(122)
    plt.subplot(312)
    plt.plot(axe_f,fourier.real,'b')
    plt.ylabel("partie reelle")
    
    plt.subplot(313)
    plt.plot(axe_f,abs(fourier),'r')
    plt.ylabel("partie imaginaire")  

    
    
    
#    plt.plot(axe_f,fourier.real,b)

    plt.xlabel('axe frequentiels en Hertz')
    plt.show()

