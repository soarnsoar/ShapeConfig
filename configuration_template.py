
import os

import sys
sys.path.append(os.getcwd())
sys.path.append(os.getcwd()+'/../')


#-----Variable Deinition-----#                                                                                                                 
from WPandCut2016 import *

##Just set below things##

BOOST='__BST__'
#PROD='__PROD__'
REG='__REG__'


#tag=Year+'_SKIM10_'+BOOST+'_HMFull_V11_'+model+'_'+WTAG+'_'+ALGO+'_'+PROD+'_'+REG
tag=Year+'___TEST___'+BOOST+'_HMFull_V13_'+model+'_'+WTAG+'_'+ALGO+'_'+REG
print tag

variablesFile='variables_'+BOOST+'_'+REG+'.py' ##what variables to draw
cutsFile='cuts_'+BOOST+'_'+REG+'.py' ## event selection##region selection


samplesFile = 'samples_'+Year+'.py'

lumi=1.
if Year=='2016':
    lumi=35.9
if Year=='2017':
    lumi=41.5
if Year=='2018':
    lumi=59.7
if Year=='3yrs':
    lumi=137
#outputDirPlots='plots_'+tag+'Blined'
outputDirPlots='plots_'+tag
outputDir =           'rootFile_'+tag
treeName='Events'
aliasesFile='aliases_'+BOOST+'.py'
nuisancesFile = 'nuisances_'+BOOST+'.py'

maxLogCratio=100000
maxLogC=100000
