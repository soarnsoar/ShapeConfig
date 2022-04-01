#ONLY_FINALCUT=True
import os
import sys
sys.path.append(os.getcwd())
sys.path.append(os.getcwd()+'/../')

#-----Variable Deinition-----#
from WPandCut2016 import *

_ALGO="_"+ALGO
_ALGO_="_"+ALGO+"_"


cuts={}
#opt.cutsFile=''

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
supercut = LepWPCut+'&&'+LepPtCut+'&&'+LepCut
METtype="PuppiMET"
#met>30
#supercut +='&&(!isFinalBoostSR) &&(isResol'+_ALGO_+'nom)'+'&&'+'('+METtype+'_nom_pt >'+METcutRes+')'
supercut +='&&(!isBoost) &&(isResol'+_ALGO_+'nom)'

##---Lepton Categorization---##



LepCats={}
if 'ele' in configration_py:
    LepCats['eleCH']='(Lepton_isTightElectron_'+eleWP+'[0]>0.5)'
if 'mu' in configration_py:
    LepCats['muCH']='(Lepton_isTightMuon_'+muWP+'[0]>0.5)'
if not ('mu' in configration_py) and not ('ele' in configration_py):
    LepCats={
        '_':'1',
        'eleCH':'(Lepton_isTightElectron_'+eleWP+'[0]>0.5)',
        'muCH':'(Lepton_isTightMuon_'+muWP+'[0]>0.5)',
    }
if ('ele' in configration_py) and ('mu' in configration_py): ##for plotting
    LepCats={
        '_':'1',
    }
##-----Basic categorization-----##

PRODCUT={}
PRODCUT['ResolvedALL']='(isResol'+_ALGO_+'nom)'


NBJETCUT={}
NBJETCUT['NB0']='(nBJetResol'+_ALGO_+'nom == 0)'
NBJETCUT['NBOver0']='(nBJetResol'+_ALGO_+'nom > 0)'

WHADMASSCUT={}
WHADMASSCUT['WHADMASSON']='isResolSR'+_ALGO_+'nom'
WHADMASSCUT['WHADMASSOFF']='isResolSB'+_ALGO_+'nom'

METCUT={}
METCUT['MET'+METcutRes]='('+METtype+'_nom_pt >'+METcutRes+')'

PtOverMCut = {}
PtOverMCut['PtOverM035'] = '(lnjj'+_ALGO_+'nom_minPtWOverM>0.35)'

WlepMtCut = {}
WlepMtCut['WlepMtOver50'] = '(Wlep_nom_Mt > 50)'

WWMtCut = {}
WWMtCut['WWMtOver60']='(lnjj'+_ALGO_+'nom_Mt > 60)'
##--fullSR
cuts['FullCutSR']='&&'.join([
    PRODCUT['ResolvedALL'],
    NBJETCUT['NB0'],
    WHADMASSCUT['WHADMASSON'],
    METCUT['MET'+METcutRes],
    PtOverMCut['PtOverM035'],
    WlepMtCut['WlepMtOver50'],
    WWMtCut['WWMtOver60']
])
##--SB
cuts['SBCR']='&&'.join([
    PRODCUT['ResolvedALL'],
    NBJETCUT['NB0'],
    WHADMASSCUT['WHADMASSOFF'],
    METCUT['MET'+METcutRes],
    PtOverMCut['PtOverM035'],
    WlepMtCut['WlepMtOver50'],
    WWMtCut['WWMtOver60']
])

cuts['TOPCR']='&&'.join([
    PRODCUT['ResolvedALL'],
    NBJETCUT['NBOver0'],
    WHADMASSCUT['WHADMASSON'],
    METCUT['MET'+METcutRes],
    PtOverMCut['PtOverM035'],
    WlepMtCut['WlepMtOver50'],
    WWMtCut['WWMtOver60']
])
##--NoNBJET
cuts['NONBJET']='&&'.join([
    PRODCUT['ResolvedALL'],
    
    WHADMASSCUT['WHADMASSON'],
    METCUT['MET'+METcutRes],
    PtOverMCut['PtOverM035'],
    WlepMtCut['WlepMtOver50'],
    WWMtCut['WWMtOver60']
])
##--NoWHADMASS
cuts['NOWHADMASS']='&&'.join([
    PRODCUT['ResolvedALL'],
    NBJETCUT['NB0'],
    
    METCUT['MET'+METcutRes],
    PtOverMCut['PtOverM035'],
    WlepMtCut['WlepMtOver50'],
    WWMtCut['WWMtOver60']
])

##--NOPTOVERM
cuts['NOPTOVERM']='&&'.join([
    PRODCUT['ResolvedALL'],
    NBJETCUT['NB0'],
    WHADMASSCUT['WHADMASSON'],
    METCUT['MET'+METcutRes],
    WlepMtCut['WlepMtOver50'],
    WWMtCut['WWMtOver60']
])
##--NOMET
cuts['NOMET']='&&'.join([
    PRODCUT['ResolvedALL'],
    NBJETCUT['NB0'],
    WHADMASSCUT['WHADMASSON'],
    PtOverMCut['PtOverM035'],
    WlepMtCut['WlepMtOver50'],
    WWMtCut['WWMtOver60']

])
##--WLEPMT
cuts['NOWMT']='&&'.join([
    PRODCUT['ResolvedALL'],
    NBJETCUT['NB0'],
    WHADMASSCUT['WHADMASSON'],
    METCUT['MET'+METcutRes],
    PtOverMCut['PtOverM035'],
    WWMtCut['WWMtOver60']
])
##--WWMT
cuts['NOWWMT']='&&'.join([
    PRODCUT['ResolvedALL'],
    NBJETCUT['NB0'],
    WHADMASSCUT['WHADMASSON'],
    METCUT['MET'+METcutRes],
    PtOverMCut['PtOverM035'],
    WlepMtCut['WlepMtOver50'],

])
##--WWMT
#cuts['isVBF']='isVBF'
print "Ncuts=",len(cuts)
for c in cuts:
    print c
