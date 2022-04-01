import os
import sys
sys.path.append(os.getcwd())

##---Setting Flags
###--nuisance
StatOnly=True
UseRegroupJES=True

##--turn on only speific nuisances
LepMetOnly=False
JetMetOnly=False


###--MjjShape Study ->add slope shape
MjjShapeStudy=False
###--QCD norm study
QCDCR=False
###--Final without Optimization
NoOptimize=False
###--VBFCategory
VBFCat=True
VBFDNNCat=False
###--CUT && Variable ->
FORFINAL=True
N1CUT=False


##--Corretions
MjjShapeCorr=True
PowhegNorm=False
##--For QCD norm fitting
DIVIDEQCD=False
if QCDCR:
    DIVIDEQCD=True
if MjjShapeStudy:
    MjjShapeCorr=False
    N1CUT=True


##---shape submission
FilesPerJob=20
FilesPerJobMainBKG=1
FilesPerJobDATA=100
#FilesPerJobBuggy=1
FilesPerJobBuggy=FilesPerJob
if StatOnly:
    FilesPerJobDATA=2
    FilesPerJobBuggy=FilesPerJob



CombineMultiBoson=True ##Turn off when making shapes and combing multiv/ Turn on when mkRuncards, plotting
CombineWjets=False
CombineHTT=True

Wjets=['Wjets0j','Wjets1j','Wjets2j']
#MultiBoson=['WW','WZ','ZZ','WWW','WWZ','WZZ','ZZZ','ZHWWlnuqq_M125','WpHWWlnuqq_M125','WmHWWlnuqq_M125',]
MultiBoson=['WZ','ZZ','WWW','WWZ','WZZ','ZZZ']
#HTT=['ggHtautaulnuqq_M125','vbfHtautaulnuqq_M125','WmHtautaulnuqq_M125','WpHtautaulnuqq_M125','ZHtautaulnuqq_M125']


#H125=[   'ggH_hww125','ZHWWlnuqq_M125','WpHWWlnuqq_M125','WmHWWlnuqq_M125',] ##HWW
VH=[   'WpHWWlnuqq_M125','WmHWWlnuqq_M125','ZHWWlnuqq_M125'] ##HWW
#qqWWqq=['qqWWqq']
qqWWqq=['Wp2jWmln','WplvWm2j']
ggWW=['ggWW']



##---
#/cms/ldap_home/jhchoi/HWW_Analysis/slc7/ForShape/CMSSW_10_2_19/src/SNuAnalytics/Configurations/HWWSemiLepHighMass
configurations = '%s/src/SNuAnalytics/Configurations/HWWSemiLepHighMass/data/' % os.getenv('CMSSW_BASE')
xrootdPath = 'root://cms-xrdr.private.lo:2094'
treeBaseDir = "/xrootd/store/user/jhchoi/Latino/HWWNano/"
##--Set Campaign and Step--##
CAMPAIGN='Fall2017_102X_nAODv7_Full2017v7_HWW'
STEP="MCl1loose2017v7__MCCorr2017v7__HMSemilepSKIMv7_1__HMFull_V13_jhchoi_nom"

CAMPAIGN_DATA='Run2017_102X_nAODv7_Full2017v7'
STEP_DATA="DATAl1loose2017v7__HMSemilepSKIMv7_1_data__HMFull_V12_jhchoi_data"

directory=treeBaseDir+CAMPAIGN+'/'+STEP

##---Copy Wtagger Configuration--##
if not os.path.isfile('Wtagger_cfg.py'):
    os.system('cp '+configurations+'/Wtagger_cfg.py .')
if not os.path.isfile('Wjjtagger_cfg.py'):
    os.system('cp '+configurations+'/Wjjtagger_cfg.py .')

from Wtagger_cfg import WJID
from Wjjtagger_cfg import MYALGO,JETCUTS

##----WP
Year='2017'
eleWP='mvaFall17V1Iso_WP90'
muWP='cut_Tight_HWWW'
##---Btag
btagSFSource = '%s/src/PhysicsTools/NanoAODTools/data/btagSF/DeepCSV_94XSF_V2_B_F.csv' % os.getenv('CMSSW_BASE')
bAlgo='DeepB'
bWP='0.1522'


elePtCut='38'
muPtCut='30'

ALGO="dMchi2Resolution"
#WTAG="DeepAK8WP2p5"
WTAG="DeepAK8WP0p5"
#WTAG="HP45"

##---SF & Weight to use
SFweight='puWeight*trigWeight[0]*EMTFbug_veto*PrefireWeight*LepWPweight[0]*LepWPCut[0]*btagSF*PUJetIdSF'


#WtaggerSF=str(WJID['2017'][WTAG]['effSF']['nom']).replace('WtaggerFatjet_'+WTAG+'_nom_pt','Alt$(WtaggerFatjet_'+WTAG+'_nom_pt,0)')
WtaggerSF=str(WJID['2017'][WTAG]['effSF']['nom'])
#WtaggerSFup=str(WJID['2017'][WTAG]['effSF']['up']).replace('WtaggerFatjet_'+WTAG+'_nom_pt','Alt$(WtaggerFatjet_'+WTAG+'_nom_pt,0)')
WtaggerSFup=str(WJID['2017'][WTAG]['effSF']['up'])
#WtaggerSFdown=str(WJID['2017'][WTAG]['effSF']['down']).replace('WtaggerFatjet_'+WTAG+'_nom_pt','Alt$(WtaggerFatjet_'+WTAG+'_nom_pt,0)')
WtaggerSFdown=str(WJID['2017'][WTAG]['effSF']['down'])

jetptmin=str(JETCUTS['2017']['ptmin'])
jetetamax=str(JETCUTS['2017']['etamax'])


##---Mela WP----
MELA_MASS_BOOST=[400,900,1500]
MELA_MASS_BOOST=[900]
#MELA_C_BOOST=['1','0.1','0.01','0.001','0.0001','0.00001','0.000001','0.0000001','0.00000001']
MELA_C_BOOST=['0.2','0.004']
#MELA_C_BOOST=['0.001','0.003','0.006','0.01','0.03','0.06','0.1', '0.3', '0.6', '1.0']
MELA_MASS_BOOST_WP=900
MELA_C_BOOST_WP='0.2'
MELA_CUT_BOOST='0.35'

MELA_MASS_RESOL=[200,400]
MELA_MASS_RESOL=[200]
#MELA_C_RESOL=['1','0.1','0.01','0.001','0.0001','0.00001','0.000001','0.0000001','0.00000001']
MELA_C_RESOL=['0.0008']
#MELA_C_RESOL=['0.001','0.003','0.006','0.01','0.03','0.06','0.1', '0.3', '0.6', '1.0']
MELA_MASS_RESOL_WP=200
MELA_C_RESOL_WP='0.0008'
MELA_CUT_RESOL='0.75'

##--MET setup
METtype="PuppiMET"
METcutBst='40'
METcutRes='30'

##---MELA signal scenario
#model='cprime1.0BRnew0.0'
model='RelW0.02'
cbr_suffix='_c10brn00'



##--QCDlist                                                                                                                                                                                                 
QCD_MU=['QCD_Pt-15to20_MuEnrichedPt5',
        'QCD_Pt-20to30_MuEnrichedPt5',
        'QCD_Pt-30to50_MuEnrichedPt5',
        'QCD_Pt-50to80_MuEnrichedPt5',
        'QCD_Pt-80to120_MuEnrichedPt5',
        'QCD_Pt-120to170_MuEnrichedPt5',
        'QCD_Pt-170to300_MuEnrichedPt5',
        'QCD_Pt-300to470_MuEnrichedPt5',
        'QCD_Pt-470to600_MuEnrichedPt5',
        'QCD_Pt-600to800_MuEnrichedPt5',
        'QCD_Pt-800to1000_MuEnrichedPt5',
        'QCD_Pt-1000toInf_MuEnrichedPt5',
]
QCD_EM=[
  'QCD_Pt-20to30_EMEnriched',
  'QCD_Pt-30to50_EMEnriched',
  'QCD_Pt-50to80_EMEnriched',
  'QCD_Pt-80to120_EMEnriched',
  'QCD_Pt-120to170_EMEnriched',
  'QCD_Pt-170to300_EMEnriched',
  'QCD_Pt-300toInf_EMEnriched'
]
QCD_bcToE=[
  'QCD_Pt_20to30_bcToE',
  'QCD_Pt_30to80_bcToE',
  'QCD_Pt_80to170_bcToE',
  'QCD_Pt_170to250_bcToE',
  'QCD_Pt_250toInf_bcToE',
]


lumi=41.5

