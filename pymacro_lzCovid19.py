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
from matplotlib.font_manager import FontProperties
font = FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc', size=10)

class covidData(object):
    def __init__(self, dtfile):
        self.file = dtfile

    def loadData(self):

        self.covidData = pd.read_excel(self.file, engine='openpyxl')



def datCovid(lzfile):

    lzCovid = covidData(lzfile)
    lzCovid.loadData()
    cvDat = lzCovid.covidData

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

    lzCovid = covidData(lzfile)
    lzCovid.loadData()
    cvDat = lzCovid.covidData
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

    #axs.bar(tsdate, lzpstv, label='每日新增阳性')
    axs.bar(tsdate, lzpstv, label='LZ daily pos')
    #axs.plot(tsdate, lzravg, '-or', label='七日平均阳性')
    axs.plot(tsdate, lzravg, '-or', label='LZ 7days avg')

    axs.tick_params(axis='x', labelrotation=45)
    axs.set_xlabel("Date", fontsize=16, horizontalalignment='right', x=1.0)
    axs.set_ylabel("Number of Cases", fontsize=16, horizontalalignment='right', y=1.0)

    axs.legend(loc='upper left', facecolor='whitesmoke', edgecolor='black', fontsize=10)
    plt.grid(axis='x', which='major', linestyle='--')
    plt.grid(axis='y', which='major', linestyle='--')

    #plt.show()     
    plt.savefig("lanzhou_pstvStats2207.png", dpi=200)

def cdDataStats(cdfile):

    cdCovid = covidData(cdfile)
    cdCovid.loadData()
    cvDat = cdCovid.covidData
    tsdate = cvDat['date']

    cvDat['cdpos22'] = cvDat['cdcon22'] + cvDat['cdasy22'] - cvDat['cdasytocon22']
    cdpstv22 = cvDat['cdpos22']
    cdrTot22 = cvDat['cdpos22'].cumsum()
    cdravg22 = cvDat['cdpos22'].rolling(window=7).mean()

    cvDat['cdpos15'] = cvDat['cdcon15'] + cvDat['cdasy15'] - cvDat['cdasytocon15']
    cdpstv15 = cvDat['cdpos15']
    cdrTot15 = cvDat['cdpos15'].cumsum()
    cdravg15 = cvDat['cdpos15'].rolling(window=7).mean()

    cvDat['cdpos15'] = cvDat['cdpos15'].fillna(0)
    cvDat['cdpos22'] = cvDat['cdpos22'].fillna(0)
    cvDat['cdpos'] = cvDat['cdpos15'] + cvDat['cdpos22']
    cdtwoavg = cvDat['cdpos'].rolling(window=7).mean()

    #print(lzravg, cgravg)
    print(cvDat)

    fig, axs = plt.subplots(1, 1, constrained_layout=True)
    tday = str(dt.date.today())
    axs.text(0.75, 0.95, 'by @lzimp (%s)'%(tday), transform=axs.transAxes, fontsize=8, color='gray', 
            alpha=0.25, ha='center', va='center', rotation='0')

    axs.bar(tsdate, cdpstv22, alpha=0.75, label='CD daily pos (0722)')
    axs.plot(tsdate, cdravg22, '-or', label='CD 7days avg (0722)')

    axs.bar(tsdate, cdpstv15, color='g', alpha=0.75, label='CD daily pos (0715)')
    axs.plot(tsdate, cdravg15, '-dm', label='CD 7days avg (0715)')
    axs.plot(tsdate, cdtwoavg, '-p', color='orange', label='CD 7days avg (total)')

    axs.tick_params(axis='x', labelrotation=45)
    axs.set_xlabel("Date", fontsize=16, horizontalalignment='right', x=1.0)
    axs.set_ylabel("Number of Cases", fontsize=16, horizontalalignment='right', y=1.0)

    axs.legend(loc='upper left', facecolor='whitesmoke', edgecolor='black', fontsize=10)
    plt.grid(axis='x', which='major', linestyle='--')
    plt.grid(axis='y', which='major', linestyle='--')

    #plt.show()     
    plt.savefig("chengdu_pstvStats2207.png", dpi=200)


def main():

    lzfile = "/home/dxlin/jobs/csLearn/lzCovid19/lanzhou_covid-19_202207.xlsx"
    datCovid(lzfile)
    lzDataStats(lzfile)
    cdfile = "/home/dxlin/jobs/csLearn/lzCovid19/chengdu_covid19.xlsx"
    cdDataStats(cdfile)

if __name__ == '__main__':

    main()
