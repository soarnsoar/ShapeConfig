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
###--QCD norm Study
QCDCR=False
###--Final without Optimization
NoOptimize=False
##--VBF Category
VBFCat=True
VBFDNNCat=False
###--CUT && Variable ->
FORFINAL=True  ####--For final result -> final category and final variable only
N1CUT=False  ####--For AN plots



##--Corrections
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


Wjets=['Wjets0j','Wjets1j','Wjets2j']
#MultiBoson=['WW','WZ','ZZ','WWW','WWZ','WZZ','ZZZ']
MultiBoson=['WZ','ZZ','WWW','WWZ','WZZ','ZZZ']
#HTT=['ggHtautaulnuqq_M125','vbfHtautaulnuqq_M125','WmHtautaulnuqq_M125','WpHtautaulnuqq_M125','ZHtautaulnuqq_M125']


#H125=[      'qqH_hww125','ggH_hww125','ZHWWlnuqq_M125','WpHWWlnuqq_M125','WmHWWlnuqq_M125'] ##HWW
VH=[     'ZHWWlnuqq_M125','WpHWWlnuqq_M125','WmHWWlnuqq_M125'] ##HWW

qqWWqq=['Wp2jWmln','WplvWm2j']
ggWW=['ggWW']




##---
#/cms/ldap_home/jhchoi/HWW_Analysis/slc7/ForShape/CMSSW_10_2_19/src/SNuAnalytics/Configurations/HWWSemiLepHighMass
configurations = '%s/src/SNuAnalytics/Configurations/HWWSemiLepHighMass/data/' % os.getenv('CMSSW_BASE')
xrootdPath = 'root://cms-xrdr.private.lo:2094'
treeBaseDir = "/xrootd/store/user/jhchoi/Latino/HWWNano/"
##--Set Campaign and Step--##

CAMPAIGN='Summer16_102X_nAODv7_Full2016v7_HWW'
STEP="MCl1loose2016v7__MCCorr2016v7__HMSemilepSKIMv7_1__HMFull_V13_jhchoi_nom"

CAMPAIGN_DATA='Run2016_102X_nAODv7_Full2016v7'
STEP_DATA="DATAl1loose2016v7__HMSemilepSKIMv7_1_data__HMFull_V12_jhchoi_data"


directory=treeBaseDir+CAMPAIGN+'/'+STEP

##---Copy Wtagger Configuration--##
if not os.path.isfile('Wtagger_cfg.py'):
    os.system('cp '+configurations+'/Wtagger_cfg.py .')
if not os.path.isfile('Wjjtagger_cfg.py'):
    os.system('cp '+configurations+'/Wjjtagger_cfg.py .')

from Wtagger_cfg import WJID
from Wjjtagger_cfg import MYALGO,JETCUTS

##----WP
Year='2016'
eleWP='mva_90p_Iso2016'
muWP='cut_Tight80x'
##---Btag
btagSFSource = '%s/src/PhysicsTools/NanoAODTools/data/btagSF/DeepCSV_2016LegacySF_V1.csv' % os.getenv('CMSSW_BASE')
bAlgo='DeepB'
bWP='0.2217'


elePtCut='30'
muPtCut='30'

ALGO="dMchi2Resolution"
#WTAG="HP40"
#WTAG="DeepAK8WP5"
WTAG="DeepAK8WP0p5"

##---SF & Weight to use
SFweight='puWeight*EMTFbug_veto*PrefireWeight*trigWeight[0]*LepWPweight[0]*LepWPCut[0]*btagSF*PUJetIdSF'


#WtaggerSF=str(WJID['2016'][WTAG]['effSF']['nom']).replace('WtaggerFatjet_'+WTAG+'_nom_pt','Alt$(WtaggerFatjet_'+WTAG+'_nom_pt,0)')
WtaggerSF=str(WJID['2016'][WTAG]['effSF']['nom'])
#WtaggerSFup=str(WJID['2016'][WTAG]['effSF']['up']).replace('WtaggerFatjet_'+WTAG+'_nom_pt','Alt$(WtaggerFatjet_'+WTAG+'_nom_pt,0)')
WtaggerSFup=str(WJID['2016'][WTAG]['effSF']['up'])
#WtaggerSFdown=str(WJID['2016'][WTAG]['effSF']['down']).replace('WtaggerFatjet_'+WTAG+'_nom_pt','Alt$(WtaggerFatjet_'+WTAG+'_nom_pt,0)')
WtaggerSFdown=str(WJID['2016'][WTAG]['effSF']['down'])

jetptmin=str(JETCUTS['2016']['ptmin'])
jetetamax=str(JETCUTS['2016']['etamax'])


##---Mela WP----
MELA_MASS_BOOST=[400,900,1500]
MELA_MASS_BOOST=[1500]
#MELA_C_BOOST=['10','1.1','1','0.1','0.01','0.001','0.0001','0.00001','0.000001','0.0000001','0.00000001']
#MELA_C_BOOST=['10','1.1','1','0.1','0.01','0.001','0.0001','0.00001','0.000001','0.0000001','0.00000001']
#MELA_C_BOOST=['0.001','0.003','0.006','0.01','0.03','0.06','0.1', '0.3', '0.6', '1.0']
MELA_C_BOOST=['0.05','0.001']
MELA_MASS_BOOST_WP=1500
MELA_C_BOOST_WP='0.05'
MELA_CUT_BOOST='0.5'

MELA_MASS_RESOL=[200,400]
MELA_MASS_RESOL=[200]
#MELA_C_RESOL=['10','1.1','1','0.1','0.01','0.001','0.0001','0.00001','0.000001','0.0000001','0.00000001']
MELA_C_RESOL=['0.0008']
#MELA_C_RESOL=['0.001','0.003','0.006','0.01','0.03','0.06','0.1', '0.3', '0.6', '1.0']
MELA_MASS_RESOL_WP=200
MELA_C_RESOL_WP='0.0008'
MELA_CUT_RESOL='0.25'

##--MET setup
METtype="PuppiMET"
METcutBst='40'
METcutRes='30'

##---MELA signal scenario
#model='cprime1.0BRnew0.0'
model='RelW0.02'
cbr_suffix='_c10brn00'


##--QCD list
#QCD_MU=['QCD_Pt-15to20_MuEnrichedPt5','QCD_Pt-20toInf_MuEnrichedPt15']
QCD_MU=[
    'QCD_Pt-15to20_MuEnrichedPt5',
    'QCD_Pt-20to30_MuEnrichedPt5',
    'QCD_Pt-20to30_MuEnrichedPt5',
    'QCD_Pt-30to50_MuEnrichedPt5',
    'QCD_Pt-30to50_MuEnrichedPt5',
    'QCD_Pt-50to80_MuEnrichedPt5',
    'QCD_Pt-80to120_MuEnrichedPt5_ext1',
    'QCD_Pt-120to170_MuEnrichedPt5',
    'QCD_Pt-170to300_MuEnrichedPt5_ext1',
    'QCD_Pt-300to470_MuEnrichedPt5_ext2',
    'QCD_Pt-470to600_MuEnrichedPt5_ext2',
    'QCD_Pt-600to800_MuEnrichedPt5_ext1',
    'QCD_Pt-800to1000_MuEnrichedPt5_ext2',
    'QCD_Pt-1000toInf_MuEnrichedPt5_ext1',
]
QCD_EM=[
  'QCD_Pt-20to30_EMEnriched',
  'QCD_Pt-30to50_EMEnriched_ext1',
  'QCD_Pt-50to80_EMEnriched_ext1',
  'QCD_Pt-80to120_EMEnriched_ext1',
  'QCD_Pt-120to170_EMEnriched_ext1',
  'QCD_Pt-170to300_EMEnriched',
  'QCD_Pt-300toInf_EMEnriched'
]
QCD_bcToE=[
  'QCD_Pt_15to20_bcToE',
  'QCD_Pt_20to30_bcToE',
  'QCD_Pt_30to80_bcToE',
  'QCD_Pt_80to170_bcToE',
  'QCD_Pt_170to250_bcToE',
  'QCD_Pt_250toInf_bcToE',
]



lumi=35.9

