#ONLY_FINALCUT=True

import os
import sys
sys.path.append(os.getcwd())
sys.path.append(os.getcwd()+'/../')


#-----Variable Deinition-----#
from WPandCut2016 import *

cuts={}


if 'opt' in globals():
    configration_py=opt.cutsFile
else:
    configration_py=sys.argv[0]
print "configration_py=",configration_py


LepWPCut='(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'
LepCut="((Lepton_pt[0]>30) && (fabs(Lepton_eta[0]) < 2.5  ) && (  Alt$(Lepton_isLoose[1]*Lepton_pt[1],-1) < 10 )  )"
LepPtCut='(Lepton_pt[0] > ('+elePtCut+'*(abs(Lepton_pdgId[0])==11) + '+muPtCut+'*(abs(Lepton_pdgId[0])==13)) )'



#------End of Variable Definition-----#
#supercut = LepWPCut+'&&'+LepPtCut+'&&'+LepCut+'&&isFatJetEvent[0]'
#supercut = LepWPCut+'&&'+LepPtCut+'&&'+LepCut+' && ((isBoost_'+WTAG+'_nom && (lnJ_'+WTAG+'_nom_widx >=0)))'+'&&'+'('+METtype+'_nom_pt >'+METcutBst+')'
supercut = LepWPCut+'&&'+LepPtCut+'&&'+LepCut+' && ((isBoost_'+WTAG+'_nom && (lnJ_'+WTAG+'_nom_widx >=0)))'


##---Lepton Categorization---##



LepCats={}
if 'ele' in configration_py:
    LepCats['eleCH']='(Lepton_isTightElectron_'+eleWP+'[0]>0.5)'
if 'mu' in configration_py:
    LepCats['muCH']='(Lepton_isTightMuon_'+muWP+'[0]>0.5)'
if not ('mu' in configration_py) and not ('ele' in configration_py): ##for shape factory 
    LepCats={
        '_':'1',
        'eleCH':'(Lepton_isTightElectron_'+eleWP+'[0]>0.5)',
        'muCH':'(Lepton_isTightMuon_'+muWP+'[0]>0.5)',
    }
if ('ele' in configration_py) and ('mu' in configration_py): ##for plottin
    LepCats={
        '_':'1',
    }

LepCats={
    '_':'1',
}

##-----Basic categorization-----##



##---Boosted---##
##---common categorization -> GGF/VBF
PRODCUT={}
PRODCUT['BoostedALL']='(isBoost)'



##NBCUT
NBCUT={}
NBCUT['NB0'] ='(nBJetBoost_'+WTAG+'_nom  == 0)'
NBCUT['NBOver0'] ='(nBJetBoost_'+WTAG+'_nom  > 0)'
NBCUT['NRAWB0'] ='(raw_nbjet==0)'
# && (isBoostSR_'+WTAG+'_nom)'

##--HadronicW
WHADMASSCUT={}
WHADMASSCUT['WHADMASSON']='(isBoostSR_'+WTAG+'_nom)'
WHADMASSCUT['WHADMASSOFF']='(isBoostSB_'+WTAG+'_nom)'


METCUT={}
METCUT['MET'+METcutBst]='('+METtype+'_nom_pt >'+METcutBst+')'
METCUT['NoMET']='1'


PtOverMlnJCut= {}
PtOverMlnJCut['NoPtOverMcut']='1'
PtOverMlnJCut['PtOverM04']='(lnJ_'+WTAG+'_nom_minPtWOverM > 0.4)'
#PtOverMlnJCut['PtOverM04low']='(lnJ_'+WTAG+'_nom_minPtWOverM <= 0.4)'

    
MEKDCut={}
MEKDCut['NoMEKDCut']='1'


DPHLVICUT={
    'nocut':'1',
    '0.5':'dphi_lep_met<0.5'
}

##--FullSR
cuts['FullCutSR']=    '&&'.join([
    PRODCUT['BoostedALL'],
    NBCUT['NB0'],
    WHADMASSCUT['WHADMASSON'],
    METCUT['MET'+METcutBst],
    PtOverMlnJCut['PtOverM04']
])


##--NoNBJET
cuts['NONBJET']=    '&&'.join([
    PRODCUT['BoostedALL'],
    WHADMASSCUT['WHADMASSON'],
    METCUT['MET'+METcutBst],
    PtOverMlnJCut['PtOverM04']
])
##--NoWHADCUT
cuts['NOWHADMASS']=    '&&'.join([
    PRODCUT['BoostedALL'],
    NBCUT['NB0'],
    METCUT['MET'+METcutBst],
    PtOverMlnJCut['PtOverM04']
])
##--SBCR
cuts['SBCR']=    '&&'.join([
    PRODCUT['BoostedALL'],
    NBCUT['NB0'],
    WHADMASSCUT['WHADMASSOFF'],
    METCUT['MET'+METcutBst],
    PtOverMlnJCut['PtOverM04']
])

##--NoPTOVERM
cuts['NOPTOVERM']=    '&&'.join([
    PRODCUT['BoostedALL'],
    NBCUT['NB0'],
    WHADMASSCUT['WHADMASSON'],
    METCUT['MET'+METcutBst],
])

##--NoMET
cuts['NOMET']=    '&&'.join([
    PRODCUT['BoostedALL'],
    NBCUT['NB0'],
    WHADMASSCUT['WHADMASSON'],
    PtOverMlnJCut['PtOverM04']
])


##--TOPCR
cuts['TOPCR']=    '&&'.join([
    PRODCUT['BoostedALL'],
    WHADMASSCUT['WHADMASSON'],
    PtOverMlnJCut['PtOverM04'],
    METCUT['MET'+METcutBst],
    NBCUT['NBOver0'],

])



    
##---End of Boosted


print "Ncuts=",len(cuts)

for c in sorted(cuts):
    print c
