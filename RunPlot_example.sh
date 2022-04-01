inputdir="/xrootd_user/jhchoi/xrootd/Histos/"

name="lqq_Boosted_NOMET"
mkPlot.py --pycfg=configuration_Boosted_Combine.py --inputFile=/xrootd_user/jhchoi/xrootd/Histos/${name}.root --samplesFile=samples_3yrs.py --plotFile=plot.py --cutsFile=CutAndNuisances/cuts_${name}.py --outputDirPlots=plots_3yrs_Boosted_Combine --nuisancesFile=CutAndNuisances/nuisances_Boosted_Combine.py
