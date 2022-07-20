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


class lzCovidData(object):
    def __init__(self, dtfile):
        self.file = dtfile

    def loadData(self):

        self.lzCovidData = pd.read_excel(self.file, engine='openpyxl')



def datCovid(lzfile):

    lzCovid = lzCovidData(lzfile)
    lzCovid.loadData()
    cvDat = lzCovid.lzCovidData

    print(cvDat)
    ndate = cvDat.shape[0]
    #for idt in range(ndate):
    #    cvDat['date'][idt] = cvDat['date'][idt].date()

    #start, end = 3, 14
    fig, axs = plt.subplots(1, 1, constrained_layout=True)
    tday = str(dt.date.today())
    axs.text(0.75, 0.95, 'by @lzimp (%s)'%(tday), transform=axs.transAxes, fontsize=8, color='gray', 
            alpha=0.25, ha='center', va='center', rotation='0')

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
    
    #plt.show()
    plt.savefig("lanzhou_cvdCases2207.png", dpi=200)
    #plt.clear()

    #cvDat['lzConAve'][start:end] = cvDat['Lanzhou'][start:end].rolling(7).mean()
    #print(cvDat)

def lzDataStats(lzfile):

    lzCovid = lzCovidData(lzfile)
    lzCovid.loadData()
    cvDat = lzCovid.lzCovidData
    tsdate = cvDat['date']

    cvDat['lzpos'] = cvDat['lzcon'] + cvDat['lzasy'] - cvDat['lzasytocon']
    lzpstv = cvDat['lzpos']
    cvDat['cgpos'] = cvDat['cgcon'] + cvDat['cgasy'] - cvDat['cgasytocon']
    cgpstv = cvDat['cgpos']
    lzrTot = cvDat['lzpos'].cumsum()
    cgrTot = cvDat['cgpos'].cumsum()

    lzravg = cvDat['lzpos'].rolling(window=7).mean()
    cgravg = cvDat['cgpos'].rolling(window=7).mean()
    #print(lzravg, cgravg)

    fig, axs = plt.subplots(1, 1, constrained_layout=True)
    tday = str(dt.date.today())
    axs.text(0.75, 0.95, 'by @lzimp (%s)'%(tday), transform=axs.transAxes, fontsize=8, color='gray', 
            alpha=0.25, ha='center', va='center', rotation='0')

    axs.bar(tsdate, lzpstv, label='LZ new pos')
    axs.plot(tsdate, lzravg, '-or', label='LZ 7ds avg')

    axs.tick_params(axis='x', labelrotation=45)
    axs.set_xlabel("Date", fontsize=16, horizontalalignment='right', x=1.0)
    axs.set_ylabel("Number of Cases", fontsize=16, horizontalalignment='right', y=1.0)

    axs.legend(loc='best', facecolor='whitesmoke', edgecolor='black', fontsize=10)
    plt.grid(axis='x', which='major', linestyle='--')
    plt.grid(axis='y', which='major', linestyle='--')

    #plt.show()     
    plt.savefig("lanzhou_pstvStats2207.png", dpi=200)


def main():

    lzfile = "/home/dxlin/jobs/csLearn/lzCovid19/lanzhou_covid-19_202207.xlsx"
    datCovid(lzfile)
    lzDataStats(lzfile)

if __name__ == '__main__':

    main()
