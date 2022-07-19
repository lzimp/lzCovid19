# macro for the data (xlsx) of Lanzhou Covid19 in July
# 
# file requrie: lanzhou_covid-19_202207.xlsx
#
# Author: D.X.~Lin (Lanzhou)
# Date: July 16, 2022
#==============================================================

import os, sys, platform, math, time
import datetime as dt
import pickle as pckl
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
#plt.style.use('classic')
#print(mpl.matplotlib_fname())

def datCovid():
    cvDat = pd.read_excel("lanzhou_covid-19_202207.xlsx", engine='openpyxl')
    #cvDat.rename(columns = {'Unnamed: 0':'date', 'Unnamed: 1':'week-day', 'Unnamed: 3':'Lanzhou1', 'Unnamed: 5':'Chengguan1'}, inplace=True)
    #print(cvDat['date'][idt].date(), cvDat['Lanzhou'][idt])
    #print(cvDat)
    #cvDat = pd.read_csv('lanzhou_covid19_2207.dat', names=['date', 'lzcon', 'lzasy', 'cgcon', 'cgasy', 'cc1st', 'cc2nd'], header=1)
    print(cvDat)
    ndate = cvDat.shape[0]
    #for idt in range(ndate):
    #    cvDat['date'][idt] = cvDat['date'][idt].date()

    #start, end = 3, 14
    fig, axs = plt.subplots(1, 1, constrained_layout=True)
    axs.plot(cvDat['date'], cvDat['lzcon'], '-or', label="Lanzhou Confirmed")
    axs.plot(cvDat['date'], cvDat['lzasy'], '-.dr', label="Lanzhou Asympomatic")
    axs.plot(cvDat['date'], cvDat['cgcon'], '-ob', label="Chengguan Confirmed")
    axs.plot(cvDat['date'], cvDat['cgasy'], '-.db', label="Chengguan Asympomatic")
    axs.tick_params(axis='x', labelrotation=45)
    axs.set_xlabel("Date", fontsize=16, horizontalalignment='right', x=1.0)
    axs.set_ylabel("Number of Cases", fontsize=16, horizontalalignment='right', y=1.0)

    ax2 = axs.twinx()
    ax2.set_ylabel("Number of Close Contact", color='c', fontsize=16, horizontalalignment='right', y=1.0)
    ax2.plot(cvDat['date'], cvDat['cc1st'], '--pc', label="1st close contact")
    ax2.plot(cvDat['date'], cvDat['cc2nd'], '--sc', label="2nd close contact")


    axs.legend(loc='best', facecolor='whitesmoke', edgecolor='black', fontsize=10)
    ax2.legend(loc='center left', facecolor='whitesmoke', edgecolor='black', fontsize=10)
    plt.grid(axis='x', which='major', linestyle='--')
    plt.grid(axis='y', which='major', linestyle='--')
    
    plt.show()
    #plt.savefig("lanzhou_covid19_2207.png", dpi=200)
    #plt.clear()

    #cvDat['lzConAve'][start:end] = cvDat['Lanzhou'][start:end].rolling(7).mean()
    #print(cvDat)



def main():

    datCovid()

if __name__ == '__main__':

    main()
