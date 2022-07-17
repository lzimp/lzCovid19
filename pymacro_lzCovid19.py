# macro for the data (xlsx) of Lanzhou Covid19 in July

import os, sys, platform, math
import datetime as dt
import pickle as pckl
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
#plt.style.use('classic')
#print(mpl.matplotlib_fname())

def datCovid():
    cvDat = pd.read_excel("/home/dxlin/jobs/covid19/lanzhou_covid-19_202207.xlsx", engine='openpyxl')
    cvDat.rename(columns = {'Unnamed: 0':'date', 'Unnamed: 1':'week-day', 'Unnamed: 3':'Lanzhou1', 'Unnamed: 5':'Chengguan1'}, inplace=True)
    #print(cvDat['date'][idt].date(), cvDat['Lanzhou'][idt])
    for idt in range(1, 28):
        cvDat['date'][idt] = cvDat['date'][idt].date()

    start, end = 3, 12
    fig, axs = plt.subplots(1, 1, constrained_layout=True)
    axs.plot(cvDat['date'][start:end], cvDat['Lanzhou'][start:end], '-or', label="Lanzhou Confirmed")
    axs.plot(cvDat['date'][start:end], cvDat['Lanzhou1'][start:end], '-.dr', label="Lanzhou Asympomatic")
    axs.plot(cvDat['date'][start:end], cvDat['Chengguan'][start:end], '-ob', label="Chengguan Confirmed")
    axs.plot(cvDat['date'][start:end], cvDat['Chengguan1'][start:end], '-.db', label="Chengguan Asympomatic")
    axs.tick_params(axis='x', labelrotation=45)
    axs.set_xlabel("Date", fontsize=16, horizontalalignment='right', x=1.0)
    axs.set_ylabel("Number of Cases", fontsize=16, horizontalalignment='right', y=1.0)


    plt.legend(loc='best', facecolor='whitesmoke', edgecolor='black', fontsize=12)
    plt.grid(axis='x', which='major', linestyle='--')
    plt.grid(axis='y', which='major', linestyle='--')
    
    #plt.show()
    plt.savefig("lanzhou_covid19_220715.png", dpi=200)
    

def main():

    datCovid()

if __name__ == '__main__':

    main()
