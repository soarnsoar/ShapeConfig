NotUseTreeBase=False
#UseRegroupJES=False

    

import os
import sys
sys.path.insert(0, "SysBranch")
if 'opt' in globals():
    configration_py=opt.nuisancesFile
else:
    configration_py=sys.argv[0]


print "configration_py=",configration_py
from FatJet_Jet_SysBranches import * 
from WPandCut2016 import *

ForDatacard=False
if 'Datacard' in configration_py:
    ForDatacard=True

ForPlotting=False
if 'ForPlotting' in configration_py:
    ForPlotting=True

bst=''
if 'Boosted' in configration_py:
  bst='Boosted'
elif 'Resolved' in configration_py:
  bst='Resolved'

model_name = '_'+model.replace(".","")

SITE=os.uname()[1]


mc = [skey for skey in samples if (skey != 'DATA' and skey !='PseudoData')]
print mc


import sys
sys.path.insert(0, "MassPoints")
from List_MX import *
from List_MX_VBF import *



##---Luminosity---##
##--Ref: https://twiki.cern.ch/twiki/bin/view/CMS/TWikiLUM#LumiComb
if Year=='2016':
  nuisances['lumi_Uncorrelated'] = {
    'name': 'lumi_13TeV_2016',
    'type': 'lnN',
    'samples': dict((skey, '1.022') for skey in mc )
  }
  
  nuisances['lumi_XY'] = {
    'name': 'lumi_13TeV_XY',
    'type': 'lnN',
    'samples': dict((skey, '1.009') for skey in mc)
  }
  
  
  nuisances['lumi_BBD'] = {
    'name': 'lumi_13TeV_BBD',
    'type': 'lnN',
    'samples': dict((skey, '1.004') for skey in mc )
  }

  nuisances['lumi_DB'] = {
    'name': 'lumi_13TeV_DB',
    'type': 'lnN',
    'samples': dict((skey, '1.005') for skey in mc )
  }
  
  nuisances['lumi_GS'] = {
    'name': 'lumi_13TeV_GS',
    'type': 'lnN',
    'samples': dict((skey, '1.004') for skey in mc )
  }


  

if Year=='2017':
  nuisances['lumi_Uncorrelated'] = {
    'name': 'lumi_13TeV_2017',
    'type': 'lnN',
    'samples': dict((skey, '1.02') for skey in mc )
  }
  
  nuisances['lumi_XY'] = {
    'name': 'lumi_13TeV_XY',
    'type': 'lnN',
    'samples': dict((skey, '1.008') for skey in mc)
  }
  
  nuisances['lumi_LS'] = {
    'name': 'lumi_13TeV_LS',
    'type': 'lnN',
    'samples': dict((skey, '1.003') for skey in mc )
  }
  
  nuisances['lumi_BBD'] = {
    'name': 'lumi_13TeV_BBD',
    'type': 'lnN',
    'samples': dict((skey, '1.004') for skey in mc )
  }
  
  nuisances['lumi_DB'] = {
    'name': 'lumi_13TeV_DB',
    'type': 'lnN',
    'samples': dict((skey, '1.005') for skey in mc )
  }
  
  nuisances['lumi_BCC'] = {
    'name': 'lumi_13TeV_BCC',
    'type': 'lnN',
    'samples': dict((skey, '1.003') for skey in mc )
  }
  
  nuisances['lumi_GS'] = {
    'name': 'lumi_13TeV_GS',
    'type': 'lnN',
    'samples': dict((skey, '1.001') for skey in mc )
  }

if Year=='2018':
  nuisances['lumi_Uncorrelated'] = {
    'name': 'lumi_13TeV_2018',
    'type': 'lnN',
    'samples': dict((skey, '1.015') for skey in mc )
  }
  
  nuisances['lumi_XY'] = {
    'name': 'lumi_13TeV_XY',
    'type': 'lnN',
    'samples': dict((skey, '1.02') for skey in mc)
  }
  
  nuisances['lumi_LS'] = {
    'name': 'lumi_13TeV_LS',
    'type': 'lnN',
    'samples': dict((skey, '1.002') for skey in mc )
  }
  
  nuisances['lumi_BCC'] = {
    'name': 'lumi_13TeV_BCC',
    'type': 'lnN',
    'samples': dict((skey, '1.002') for skey in mc )
  }



#for shift in ['jes', 'lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
for shift in         ['lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
    btag_syst = ['(btagSF%sup)/(btagSF)<10 ? (btagSF%sup)/(btagSF) : 1.0' % (shift,shift), '(btagSF%sdown)/(btagSF) < 10 ? (btagSF%sdown)/(btagSF) : 1.0' % (shift,shift)]
    
    name = 'CMS_btag_%s' % shift
    if 'stats' in shift:
        name += '_'+Year

    nuisances['btag_shape_%s' % shift] = {
        'name': name,
        'kind': 'weight',
        'type': 'shape',
        #'samples': dict((skey, btag_syst) for skey in mc),
      'samples':{}
    }
    for skey in mc:
      nuisances['btag_shape_%s' % shift]['samples'][skey]=btag_syst



trig_syst=['mutrigWeight_up[0]*eletrigWeight_up','mutrigWeight_down[0]*eletrigWeight_down']
nuisances['trigg'] = {
    'name': 'CMS_eff_hwwtrigger_'+Year,
    'kind': 'weight',
    'type': 'shape',
    'samples': {},
}
for skey in mc:
  nuisances['trigg']['samples'][skey]=trig_syst


                                                         
#              dict((skey, trig_syst) for skey in mc),

prefire_syst = ['PrefireWeight_Up/PrefireWeight < 10 ? PrefireWeight_Up/PrefireWeight : 1', 'PrefireWeight_Down/PrefireWeight < 10 ? PrefireWeight_Down/PrefireWeight : 1']

if not Year=='2018':
  nuisances['prefire'] = {
    'name': 'CMS_eff_prefiring_'+Year,
    'kind': 'weight',
    'type': 'shape',
    #'samples': dict((skey, prefire_syst) for skey in mc),
    'samples':{}
  }
  for skey in mc:
    nuisances['prefire']['samples'][skey]=prefire_syst




#eff_e_syst = ['Lepton_tightElectron_'+eleWP+'_IdIsoSF_Up'+'[0]/Lepton_tightElectron_'+eleWP+'_IdIsoSF'+'[0]','Lepton_tightElectron_'+eleWP+'_IdIsoSF_Down'+'[0]/Lepton_tightElectron_'+eleWP+'_IdIsoSF'+'[0]']


eff_e_syst = ['Lepton_tightElectron_'+eleWP+'_TotSF_Up'+'[0]/Lepton_tightElectron_'+eleWP+'_TotSF'+'[0] < 10 ? Lepton_tightElectron_'+eleWP+'_TotSF_Up'+'[0]/Lepton_tightElectron_'+eleWP+'_TotSF'+'[0] : 1.0','Lepton_tightElectron_'+eleWP+'_TotSF_Down'+'[0]/Lepton_tightElectron_'+eleWP+'_TotSF'+'[0] < 10 ? Lepton_tightElectron_'+eleWP+'_TotSF_Down'+'[0]/Lepton_tightElectron_'+eleWP+'_TotSF'+'[0] : 1.0']

nuisances['eff_e'] = {
    'name': 'CMS_eff_e_'+Year,
    'kind': 'weight',
    'type': 'shape',
    #'samples': dict((skey, eff_e_syst) for skey in mc),
  'samples':{},
}
for skey in mc:
  nuisances['eff_e']['samples'][skey]=eff_e_syst



eff_m_syst = ['Lepton_tightMuon_'+muWP+'_TotSF_Up'+'[0]/Lepton_tightMuon_'+muWP+'_TotSF'+'[0] < 10 ? Lepton_tightMuon_'+muWP+'_TotSF_Up'+'[0]/Lepton_tightMuon_'+muWP+'_TotSF'+'[0] : 1.0','Lepton_tightMuon_'+muWP+'_TotSF_Down'+'[0]/Lepton_tightMuon_'+muWP+'_TotSF'+'[0] < 10 ? Lepton_tightMuon_'+muWP+'_TotSF_Down'+'[0]/Lepton_tightMuon_'+muWP+'_TotSF'+'[0] : 1.0']

nuisances['eff_m'] = {
    'name': 'CMS_eff_m_'+Year,
    'kind': 'weight',
    'type': 'shape',
    #'samples': dict((skey, eff_m_syst) for skey in mc),
  'samples':{}
}
for skey in mc:
  nuisances['eff_m']['samples'][skey]=eff_m_syst


#
eff_Wtag_syst = ['WtaggerSFup','WtaggerSFdown']
if 'Boosted' in configration_py: 
  nuisances['eff_Wtag'] = {
    
    'name': 'CMS_eff_Wtag_'+Year,
    'kind': 'weight',
    'type': 'shape',
    #'samples': dict((skey, eff_Wtag_syst) for skey in mc),
    'samples':{}
  }
  for skey in mc:
    nuisances['eff_Wtag']['samples'][skey]=eff_Wtag_syst

if not NotUseTreeBase:
    #for br in HMBoostBranches+WBranches:
    #  nuisances[s]['BrFromToUp'][br]=br.replace("nom",s.replace('fat','')+"up")
    #  #print nuisances[s]['BrFromToUp'][br]
    #  nuisances[s]['BrFromToDown'][br]=br.replace("nom",s.replace('fat','')+"down")
      
    nuisances['mupt'] = {
      'name': 'CMS_scale_m_'+Year,
      'kind': 'tree',
      'type': 'shape',
      'samples':{},
      'folderUp': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/'+STEP.replace('_nom','_nom_MupTup'),
      'folderDown': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/'+STEP.replace('_nom','_nom_MupTdo'),
    }
    for skey in mc:
      nuisances['mupt']['samples'][skey]=['1','1']


    nuisances['elept'] = {
      'name': 'CMS_scale_e_'+Year,
      'kind': 'tree',
      'type': 'shape',
      #'samples': dict((skey, ['1', '1']) for skey in mc),
      'samples':{},
      'folderUp': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/'+STEP.replace('_nom','_nom_ElepTup'),
      'folderDown': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/'+STEP.replace('_nom','_nom_ElepTdo'),
      
    }
    for skey in mc:
      nuisances['elept']['samples'][skey]=['1','1']


    nuisances['met'] = {
      'name': 'CMS_scale_met_'+Year,
      'kind': 'tree',
      'type': 'shape',
      #'samples': dict((skey, ['1', '1']) for skey in mc),
      'samples':{},
      'folderUp': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/'+STEP.replace('_nom','_nom_METup'),
      'folderDown': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/'+STEP.replace('_nom','_nom_METup'),

    }
    for skey in mc:
      nuisances['met']['samples'][skey]=['1','1']

    ##--HEM 15/16
    if Year=='2018':
        nuisances['hem1516'] = {
            'name': 'CMS_HEM1516_'+Year,
            'kind': 'tree',
            'type': 'shape',
            #'samples': dict((skey, ['1', '1']) for skey in mc),                                                                                                                                                  
            'samples':{},
            'folderUp': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/'+STEP.replace('_nom','_hemvar'),
            'folderDown': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/'+STEP,
            
        }
        for skey in mc:
            nuisances['hem1516']['samples'][skey]=['1','1']
##--PU--##
exec(open('PU/bkg_'+Year+'.py'))
exec(open('PU/sig_'+Year+'.py'))

nuisances['PU'] = {
    'name': 'CMS_PU_'+Year,
    'kind': 'weight',
    'type': 'shape',
    'samples':{},
}
for skey in mc:
    if skey in PU_bkg:
        upnorm=PU_bkg[skey]['upnorm']
        downnorm=PU_bkg[skey]['downnorm']
    elif skey in PU_sig:
        upnorm=PU_sig[skey]['upnorm']
        downnorm=PU_sig[skey]['downnorm']
    else :
        upnorm='1.'
        downnorm='1.'
    #print 'upnorm',upnorm
    #print 'downnorm',downnorm
    pu_sys_up='puWeightUp/puWeight*'+str(upnorm)
    pu_sys_down='puWeightDown/puWeight*'+str(downnorm)
    nuisances['PU']['samples'][skey]=[pu_sys_up,pu_sys_down]

##---QCDscale acceptance
handle=open('QCDscale/nuisanceinfo_QCDscale.py','r')
exec(handle)
handle.close()

#scalenuisances
scalenuisances_qqH={}
scalenuisances_ggH={}
scalenuisances_qq={}
scalenuisances_gg={}
scalenuisances_ttbar={}
scalenuisances_wjets={}#Wjets
scalenuisances_ZH={}
scalenuisances_WpH={}
scalenuisances_WmH={}
scalenuisances_WW={}


for s in scalenuisances:
    if 'ggH' in s:
        scalenuisances_ggH[s]=scalenuisances[s]
    elif 'vbfHWWlnuqq_M' in s or 'qqH' in s:
        scalenuisances_qqH[s]=scalenuisances[s]
        #elif 'top' in s or 'TT' in s or 'Top' in s:
    elif 'TT' in s or 'Top' in s:
        scalenuisances_ttbar[s]=scalenuisances[s]
    elif 'Wjets' in s:
        scalenuisances_wjets[s]=scalenuisances[s]
    elif 'ggWW' in s:
        scalenuisances_gg[s]=scalenuisances[s]
    elif 'qqWWqq' in s or 'Wp2jWmln' in s or 'WplvWm2j' in s:
        scalenuisances_qq[s]=scalenuisances[s]
    elif 'ZH' in s:
        scalenuisances_ZH[s]=scalenuisances[s]
    elif 'WpH' in s:
        scalenuisances_WpH[s]=scalenuisances[s]
    elif 'WmH' in s:
        scalenuisances_WmH[s]=scalenuisances[s]
    elif 'WW'==s:
        scalenuisances_WW[s]=scalenuisances[s]
nuisances['QCDscale_ggH_ACCEPT'] = {
  'name': 'QCDscale_ggH_ACCEPT',
  'kind': 'weight_envelope',
  'type': 'shape',
  'samples':scalenuisances_ggH,
}

nuisances['QCDscale_qqH_ACCEPT'] = {
  'name': 'QCDscale_qqH_ACCEPT',
  'kind': 'weight_envelope',
  'type': 'shape',
  'samples':scalenuisances_qqH,
}

nuisances['QCDscale_ttbar_ACCEPT'] = {
  'name': 'QCDscale_ttbar_ACCEPT',
  'kind': 'weight_envelope',
  'type': 'shape',
  'samples':scalenuisances_ttbar,
}

nuisances['QCDscale_wjets_ACCEPT'] = {
  'name': 'QCDscale_wjets_ACCEPT',
  'kind': 'weight_envelope',
  'type': 'shape',
  'samples':scalenuisances_wjets,
}

nuisances['QCDscale_gg_ACCEPT'] = {
  'name': 'QCDscale_gg_ACCEPT',
  'kind': 'weight_envelope',
  'type': 'shape',
  'samples':scalenuisances_gg,
}

nuisances['QCDscale_qq_ACCEPT'] = {
  'name': 'QCDscale_qq_ACCEPT',
  'kind': 'weight_envelope',
  'type': 'shape',
  'samples':scalenuisances_qq,
}

nuisances['QCDscale_ZH_ACCEPT'] = {
  'name': 'QCDscale_ZH_ACCEPT',
  'kind': 'weight_envelope',
  'type': 'shape',
  'samples':scalenuisances_ZH,
}

nuisances['QCDscale_WpH_ACCEPT'] = {
  'name': 'QCDscale_WpH_ACCEPT',
  'kind': 'weight_envelope',
  'type': 'shape',
  'samples':scalenuisances_WpH,
}

nuisances['QCDscale_WmH_ACCEPT'] = {
  'name': 'QCDscale_WmH_ACCEPT',
  'kind': 'weight_envelope',
  'type': 'shape',
  'samples':scalenuisances_WmH,
}
nuisances['QCDscale_WW_ACCEPT'] = {
  'name': 'QCDscale_WW_ACCEPT',
  'kind': 'weight_envelope',
  'type': 'shape',
  'samples':scalenuisances_WW,
}



##--PDF acceptance
#handle=open('PDF/nuisance_pdf.py','r')
handle=open('PDF/nuisanceinfo_pdf.py','r')
exec(handle)
handle.close()

pdfnuisances_ggH={}
pdfnuisances_qqH={}
pdfnuisances_gg={}
pdfnuisances_qq={}
pdfnuisances_ttbar={}
pdfnuisances_wjets={}
pdfnuisances_ZH={}
pdfnuisances_WmH={}
pdfnuisances_WpH={}
pdfnuisances_WW={}
for s in pdfnuisances:
    if 'ggH' in s:
        pdfnuisances_ggH[s]=pdfnuisances[s]
    elif 'vbfHWWlnuqq_M' in s or 'qqH' in s:
        pdfnuisances_qqH[s]=pdfnuisances[s]
        #elif 'top' in s or 'TT' in s or 'Top' in s:
    elif 'TT' in s or 'Top' in s:
        pdfnuisances_ttbar[s]=pdfnuisances[s]
    elif 'Wjets' in s:
        pdfnuisances_wjets[s]=pdfnuisances[s]
    elif 'ggWW' in s:
        pdfnuisances_gg[s]=pdfnuisances[s]
    elif 'qqWWqq' in s  or 'Wp2jWmln' in s or 'WplvWm2j' in s:
        pdfnuisances_qq[s]=pdfnuisances[s]
    elif 'ZH' in s:
        pdfnuisances_ZH[s]=pdfnuisances[s]
    elif 'WpH' in s:
        pdfnuisances_WpH[s]=pdfnuisances[s]
    elif 'WmH' in s:
        pdfnuisances_WmH[s]=pdfnuisances[s]
    elif 'WW'==s:
        pdfnuisances_WW[s]=pdfnuisances[s]
nuisances['pdf_Higgs_gg_ACCEPT'] = {
    'name': 'pdf_Higgs_gg_ACCEPT',
    'kind': 'weight_rms',
    'type': 'shape',
    'samples': pdfnuisances_ggH,
}

nuisances['pdf_Higgs_qqbar_ACCEPT'] = {
    'name': 'pdf_Higgs_qqbar_ACCEPT',
    'kind': 'weight_rms',
    'type': 'shape',
    'samples': pdfnuisances_qqH,
}

nuisances['pdf_gg_ACCEPT'] = {
    'name': 'pdf_gg_ACCEPT',
    'kind': 'weight_rms',
    'type': 'shape',
    'samples': pdfnuisances_gg,
}

nuisances['pdf_qqbar_ACCEPT'] = {
    'name': 'pdf_qqbar_ACCEPT',
    'kind': 'weight_rms',
    'type': 'shape',
    'samples': pdfnuisances_qq,
}

nuisances['pdf_ttbar_ACCEPT'] = {
    'name': 'pdf_ttbar_ACCEPT',
    'kind': 'weight_rms',
    'type': 'shape',
    'samples': pdfnuisances_ttbar,
}

nuisances['pdf_wjets_ACCEPT'] = {
    'name': 'pdf_wjets_ACCEPT',
    'kind': 'weight_rms',
    'type': 'shape',
    'samples': pdfnuisances_wjets,
}

nuisances['pdf_ZH_ACCEPT'] = {
    'name': 'pdf_ZH_ACCEPT',
    'kind': 'weight_rms',
    'type': 'shape',
    'samples': pdfnuisances_ZH,
}

nuisances['pdf_WpH_ACCEPT'] = {
    'name': 'pdf_WpH_ACCEPT',
    'kind': 'weight_rms',
    'type': 'shape',
    'samples': pdfnuisances_WpH,
}

nuisances['pdf_WmH_ACCEPT'] = {
    'name': 'pdf_WmH_ACCEPT',
    'kind': 'weight_rms',
    'type': 'shape',
    'samples': pdfnuisances_WmH,
}

nuisances['pdf_WW_ACCEPT'] = {
    'name': 'pdf_WW_ACCEPT',
    'kind': 'weight_rms',
    'type': 'shape',
    'samples': pdfnuisances_WW,
}


handle=open('PS/nuisanceinfo_PS.py','r')
exec(handle)
handle.close()

nuisances['UEPS_ISR']={
  'name': 'PS_ISR',
  'kind': 'weight',
  'type': 'shape',
  'samples':isrnuisances,
}

nuisances['UEPS_FSR']={
  'name': 'PS_FSR',
  'kind': 'weight',
  'type': 'shape',
  'samples':fsrnuisances,
}



##--Mjj shape
#MjjShape
if   bst=='Resolved' and MjjShapeCorr:
    nuisances['MjjReweight']={
        'name': 'mjjshape_'+Year,
        'kind': 'weight',
        'type': 'shape',
        'samples':{'Wjets':['1','1/MjjShape']},
    }
    if not CombineWjets:
        for wjet in Wjets:
            nuisances['MjjReweight']['samples'][wjet]=['1','1/MjjShape']
if not NotUseTreeBase:
  if UseRegroupJES :
    print "--UseRegroupJES--"

    ##--ak4--##
    for s in ['jesFlavorQCD','jesRelativeBal','jesHF','jesBBEC1','jesEC2','jesAbsolute']: ##year-correlated
      nuisances['ak4_'+s] = {
          #'name': 'CMS_ak4jet_'+s,
          'name': 'CMS_scale_'+s.replace('jes','JES'),
          'kind': 'branch_custom',
          'type': 'shape',
          #'samples': dict((skey, ['1', '1']) for skey in mc),
          'samples':{},
          #'folderUp': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_jetsysup_correlate',
          #'folderDown': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_jetsysdown_correlate',
          'folderUp': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/'+STEP.replace('_nom','_jetsysup_correlate'),
          'folderDown': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/'+STEP.replace('_nom','_jetsysdown_correlate'),
      }
      for skey in mc:
        nuisances['ak4_'+s]['samples'][skey]=['1','1']

      nuisances['ak4_'+s]['BrFromToUp']={}
      nuisances['ak4_'+s]['BrFromToDown']={}
      for br in JetBranches+WlepBranches+WjjBranches+HMBoostBranches+HMResolBranches:
        nuisances['ak4_'+s]['BrFromToUp'][br]=br.replace("nom",s+"Up")
        nuisances['ak4_'+s]['BrFromToDown'][br]=br.replace("nom",s+"Down")

    for s in ['jesAbsolute_'+Year,'jesHF_'+Year,'jesEC2_'+Year,'jesRelativeSample_'+Year,'jesBBEC1_'+Year,'jer']: ##year-uncorrelated
      nuisances['ak4_'+s] = {
          'name': 'CMS_scale_'+s.replace('jes','JES'),
        'kind': 'branch_custom',
        'type': 'shape',
        #'samples': dict((skey, ['1', '1']) for skey in mc),
        'samples':{},
        'folderUp': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/'+STEP.replace('_nom','_jetsysup_uncorrelate'),
        'folderDown': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/'+STEP.replace('_nom','_jetsysdown_uncorrelate'),
        #'folderUp': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_jetsysup_uncorrelate',
        #'folderDown': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_jetsysdown_uncorrelate',
      }
      for skey in mc:
        nuisances['ak4_'+s]['samples'][skey]=['1','1']

      if s=="jer": nuisances['ak4_'+s]['name']='CMS_res_j_'+Year
      nuisances['ak4_'+s]['BrFromToUp']={}
      nuisances['ak4_'+s]['BrFromToDown']={}
      for br in JetBranches+WlepBranches+WjjBranches+HMBoostBranches+HMResolBranches:
        nuisances['ak4_'+s]['BrFromToUp'][br]=br.replace("nom",s+"Up")
        nuisances['ak4_'+s]['BrFromToDown'][br]=br.replace("nom",s+"Down")


    ##--ak8jet00##
    for s in ['jesFlavorQCD','jesRelativeBal','jesHF','jesBBEC1','jesEC2','jesAbsolute']: ##year-correlated
      nuisances['ak8_'+s] = {
          'name': 'CMS_ak8jet_'+s.replace('jes','scale_JES'),
        'kind': 'branch_custom',
        'type': 'shape',
        #'samples': dict((skey, ['1', '1']) for skey in mc),
        'samples':{},
        'folderUp': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/'+STEP.replace('_nom','_fatjetsysup_correlate'),
        'folderDown': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/'+STEP.replace('_nom','_fatjetsysdown_correlate'),
      }
      for skey in mc:
        nuisances['ak8_'+s]['samples'][skey]=['1','1']

      nuisances['ak8_'+s]['BrFromToUp']={}
      nuisances['ak8_'+s]['BrFromToDown']={}
      for br in HMBoostBranches+WBranches:
        nuisances['ak8_'+s]['BrFromToUp'][br]=br.replace("nom",s+"Up")
        nuisances['ak8_'+s]['BrFromToDown'][br]=br.replace("nom",s+"Down")

    for s in ['jesAbsolute_'+Year,'jesHF_'+Year,'jesEC2_'+Year,'jesRelativeSample_'+Year,'jesBBEC1_'+Year,'jer','jmr','jms']: ##year-uncorrelated
      nuisances['ak8_'+s] = {
            'name': 'CMS_ak8jet_'+s.replace('jes','scale_JES').replace('jmr','JMR').replace('jms','JMS').replace('jer','res_j'),
           'kind': 'branch_custom',
           'type': 'shape',
           #'samples': dict((skey, ['1', '1']) for skey in mc),
           'samples':{},
           'folderUp': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/'+STEP.replace('_nom','_fatjetsysup_uncorrelate'),
           'folderDown': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/'+STEP.replace('_nom','_fatjetsysdown_uncorrelate'),
      }
      for skey in mc:
        nuisances['ak8_'+s]['samples'][skey]=['1','1']

      if not Year in s:
          nuisances['ak8_'+s]['name']+='_'+Year
      nuisances['ak8_'+s]['BrFromToUp']={}
      nuisances['ak8_'+s]['BrFromToDown']={}
      #for br in JetBranches+WlepBranches+WjjBranches+HMBoostBranches+HMResolBranches:
      for br in HMBoostBranches+WBranches:
        nuisances['ak8_'+s]['BrFromToUp'][br]=br.replace("nom",s+"Up")
        nuisances['ak8_'+s]['BrFromToDown'][br]=br.replace("nom",s+"Down")


    #for br in HMBoostBranches+WBranches:                                                                                                                                                                   
    #  nuisances[s]['BrFromToUp'][br]=br.replace("nom",s.replace('fat','')+"up")                                                                                                                            
    #  #print nuisances[s]['BrFromToUp'][br]                                                                                                                                                                
    #  nuisances[s]['BrFromToDown'][br]=br.replace("nom",s.replace('fat','')+"down")                                                                                                                        



  else:
    print "--Not UseRegroupJES--"
    ##--ak4--##
    nuisances['ak4_jesTotal'] = {
      #'name': 'CMS_jesTotal_'+Year,
      'name': 'CMS_ak4jet_jesTotal',
      'kind': 'branch_custom',
      'type': 'shape',
      #'samples': dict((skey, ['1', '1']) for skey in mc),
      'samples':{},
      'folderUp': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/'+STEP.replace('_nom','_jetsysup_correlate'),
      'folderDown': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/'+STEP.replace('_nom','_jetsysdown_correlate'),
      #'folderUp': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_jetsysup_correlate',
      #'folderDown': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_jetsysdown_correlate',
    }
    for skey in mc:
      nuisances['ak4_jesTotal']['samples'][skey]=['1','1']

    nuisances['ak4_jesTotal']['BrFromToUp']={}
    nuisances['ak4_jesTotal']['BrFromToDown']={}
    for br in JetBranches+WlepBranches+WjjBranches+HMBoostBranches+HMResolBranches:
      nuisances['ak4_jesTotal']['BrFromToUp'][br]=br.replace("nom","jesTotalUp")
      nuisances['ak4_jesTotal']['BrFromToDown'][br]=br.replace("nom","jesTotalDown")
      
    for s in ['jer']: ##year-uncorrelated
      nuisances['ak4_'+s] = {
        'name': 'CMS_ak4jet_'+s,
        'kind': 'branch_custom',
        'type': 'shape',
        #'samples': dict((skey, ['1', '1']) for skey in mc),
        'samples':{},
        'folderUp': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/'+STEP.replace('_nom','_jetsysup_uncorrelate'),
        'folderDown': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/'+STEP.replace('_nom','_jetsysdown_uncorrelate'),
        #'folderUp': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_jetsysup_uncorrelate',
        #'folderDown': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_jetsysdown_uncorrelate',
      }
      for skey in mc:
        nuisances['ak4_'+s]['samples'][skey]=['1','1']

      if not Year in s :
          nuisances['ak4_'+s]['name']+='_'+Year
      nuisances['ak4_'+s]['BrFromToUp']={}
      nuisances['ak4_'+s]['BrFromToDown']={}
      for br in JetBranches+WlepBranches+WjjBranches+HMBoostBranches+HMResolBranches:
        nuisances['ak4_'+s]['BrFromToUp'][br]=br.replace("nom",s+"Up")
        nuisances['ak4_'+s]['BrFromToDown'][br]=br.replace("nom",s+"Down")


    ##--ak8--#
    nuisances['ak8_jesTotal'] = {
      #'name': 'CMS_jesTotal_'+Year,
      'name': 'CMS_ak8jet_jesTotal',
      'kind': 'branch_custom',
      'type': 'shape',
      #'samples': dict((skey, ['1', '1']) for skey in mc),
      'samples':{},
      'folderUp': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/'+STEP.replace('_nom','_fatjetsysup_correlate'),
      'folderDown': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/'+STEP.replace('_nom','_fatjetsysdown_correlate'),
      #'folderUp': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_jetsysup_correlate',
      #'folderDown': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_jetsysdown_correlate',
    }
    for skey in mc:
      nuisances['ak8_jesTotal']['samples'][skey]=['1','1']

    nuisances['ak8_jesTotal']['BrFromToUp']={}
    nuisances['ak8_jesTotal']['BrFromToDown']={}
    for br in HMBoostBranches+WBranches:
      nuisances['ak8_jesTotal']['BrFromToUp'][br]=br.replace("nom","jesTotalUp")
      nuisances['ak8_jesTotal']['BrFromToDown'][br]=br.replace("nom","jesTotalDown")
      
    for s in ['jer','jms','jmr']: ##year-uncorrelated
      nuisances['ak8_'+s] = {
        'name': 'CMS_ak8jet_'+s,
        'kind': 'branch_custom',
        'type': 'shape',
        #'samples': dict((skey, ['1', '1']) for skey in mc),
        'samples':{},
        'folderUp': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/'+STEP.replace('_nom','_fatjetsysup_uncorrelate'),
        'folderDown': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/'+STEP.replace('_nom','_fatjetsysdown_uncorrelate'),
        #'folderUp': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_jetsysup_uncorrelate',
        #'folderDown': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_jetsysdown_uncorrelate',
      }
      for skey in mc:
        nuisances['ak8_'+s]['samples'][skey]=['1','1']

      if not Year in s :
          nuisances['ak8_'+s]['name']+='_'+Year
      nuisances['ak8_'+s]['BrFromToUp']={}
      nuisances['ak8_'+s]['BrFromToDown']={}
      for br in HMBoostBranches+WBranches:
        nuisances['ak8_'+s]['BrFromToUp'][br]=br.replace("nom",s+"Up")
        nuisances['ak8_'+s]['BrFromToDown'][br]=br.replace("nom",s+"Down")

## Use the following if you want to apply the automatic combine MC stat nuisances.




from LatinoAnalysis.Tools.HiggsXSection  import *
HiggsXS = HiggsXSection()


import sys
sys.path.insert(0, "MassPoints")
from List_MX import *
from List_MX_VBF import *


##--xsec of signals ##--->will be treated @ model workspace level
'''
nuisances['pdf_Higgs_gg']  = {
    'name'  : 'pdf_Higgs_gg',
    'samples' : {},
    'kind': 'weight',
    'type': 'shape',
    
}
nuisances['QCDscale_ggH']  = {
    'name'  : 'QCDscale_ggH',
    'kind': 'weight',
    'type': 'shape',
    'samples' : {},

}

for MX in List_MX:
    _pdf=HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggH',int(MX),'pdf','bsm')
    _temp=_pdf.split('/')
    up='1'
    down='1'
    if len(_temp)==1:
        up=_temp[0]
        down=str(2-float(_temp[0]))
    elif len(_temp)==2:
        up=_temp[1]
        down=_temp[0]
    #print up,down
    nuisances['pdf_Higgs_gg']['samples']['ggH_hww'+str(MX)+model_name]= [up,down]
    nuisances['pdf_Higgs_gg']['samples']['ggH_hww_SI'+str(MX)+model_name]= [up,down]

  
    _scale=HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggH',int(MX),'scale','bsm')
    _temp=_pdf.split('/')
    up='1'
    down='1'
    if len(_temp)==1:
        up=_temp[0]
        down=str(2-float(_temp[0]))
    elif len(_temp)==2:
        up=_temp[1]
        down=_temp[0]
    print "up,down=",up,down
    nuisances['QCDscale_ggH']['samples']['ggH_hww'+str(MX)+model_name]= [up,down]
    nuisances['QCDscale_ggH']['samples']['ggH_hww_SI'+str(MX)+model_name]= [up,down]
                                                    

nuisances['pdf_Higgs_qqbar']  = {
  'name'  : 'pdf_Higgs_qqbar',
    'kind': 'weight',
    'type': 'shape',
  'samples':{},
}
nuisances['QCDscale_qqH']  = {
    #'name'  : 'QCDscale_Higgs_qqbar',
    'name'  : 'QCDscale_qqH',
    'kind': 'weight',
    'type': 'shape',
    'samples':{},
}
for MX in List_MX_VBF:
    _pdf=HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH',int(MX),'pdf','bsm')
    _temp=_pdf.split('/')
    up='1'
    down='1'
    if len(_temp)==1:
        up=_temp[0]
        down=str(2-float(_temp[0]))
    elif len(_temp)==2:
        up=_temp[1]
        down=_temp[0]
    #print up,down           
    print "up,down=",up,down
    nuisances['pdf_Higgs_qqbar']['samples']['qqH_hww'+str(MX)+model_name]= [up,down]
    nuisances['pdf_Higgs_qqbar']['samples']['qqH_hww_SI'+str(MX)+model_name]= [up,down]


    _scale=HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH',int(MX),'scale','bsm')
    _temp=_pdf.split('/')
    up='1'
    down='1'
    if len(_temp)==1:
        up=_temp[0]
        down=str(2-float(_temp[0]))
    elif len(_temp)==2:
        up=_temp[1]
        down=_temp[0]
    print "up,down=",up,down
    nuisances['QCDscale_qqH']['samples']['qqH_hww'+str(MX)+model_name]= [up,down]
    nuisances['QCDscale_qqH']['samples']['qqH_hww_SI'+str(MX)+model_name]= [up,down]

'''

##---PS for 2016/2017

if Year=='2016' or Year=='2017':

    ##---PS for 
    handle=open('PsScript/PSunc_Semi_norm.py')
    exec(handle)
    handle.close()

    
    handle=open('PsScript/PSunc_Bkg_norm.py')
    exec(handle)
    handle.close()


    nuisances['UEPS_ISR_'+Year]={
        'name': 'PS_ISR',
        'kind': 'weight',
        'type': 'shape',
        'samples':{}
    }
    #print PSuncBkg
    ##--BKG--##
    for proc in sorted(PSuncBkg):
        if Year=='2017':
            if not proc in ['DY10to50','DY50','WZ','ZZ','WWW','WZZ','WWZ','ZZZ','ST_tch_antitop','ST_tch_top','Wjets0j','Wjets1j','Wjets2j','ZHWWlnuqq_M125','WpHWWlnuqq_M125','WmHWWlnuqq_M125','Wp2jWmln','WplvWm2j','tW_antitop','tW_top']: continue ## using genjet paramterization
        if Year=='2016':
            if proc in ['ST_tch_antitop', 'ggWW']:continue ##using PSbranch
            if 'qqH_hww3000' in proc :continue ##using PSbranch
        PSup = PSuncBkg[proc]['ISRup']
        PSdn = PSuncBkg[proc]['ISRdn']
        PSstring = [str(PSup['0j'])+'*(nCleanGenJet==0) + '+str(PSup['1j'])+'*(nCleanGenJet==1) + '+str(PSup['2j'])+'*(nCleanGenJet==2) + '+str(PSup['3j'])+'*(nCleanGenJet>=3)', str(PSdn['0j'])+'*(nCleanGenJet==0) + '+str(PSdn['1j'])+'*(nCleanGenJet==1) + '+str(PSdn['2j'])+'*(nCleanGenJet==2) + '+str(PSdn['3j'])+'*(nCleanGenJet>=3)']
        nuisances['UEPS_ISR_'+Year]['samples'][proc]=PSstring
        nuisances['UEPS_ISR_'+Year]['samples'][proc]=PSstring

    ##--Signal
    for MX in List_MX:
        if Year=='2017': continue
        PSup = PSunc['GGF'+str(MX)]['ISRup']
        PSdn = PSunc['GGF'+str(MX)]['ISRdn']
        PSstring = [str(PSup['0j'])+'*(nCleanGenJet==0) + '+str(PSup['1j'])+'*(nCleanGenJet==1) + '+str(PSup['2j'])+'*(nCleanGenJet==2) + '+str(PSup['3j'])+'*(nCleanGenJet>=3)', str(PSdn['0j'])+'*(nCleanGenJet==0) + '+str(PSdn['1j'])+'*(nCleanGenJet==1) + '+str(PSdn['2j'])+'*(nCleanGenJet==2) + '+str(PSdn['3j'])+'*(nCleanGenJet>=3)']

        nuisances['UEPS_ISR_'+Year]['samples']['ggH_hww'+str(MX)+model_name]=PSstring
        nuisances['UEPS_ISR_'+Year]['samples']['ggH_hww_SI'+str(MX)+model_name]=PSstring

    for MX in List_MX_VBF:
        if Year=='2017': continue
        PSup = PSunc['VBF'+str(MX)]['ISRup']
        PSdn = PSunc['VBF'+str(MX)]['ISRdn']
        PSstring = [str(PSup['0j'])+'*(nCleanGenJet==0) + '+str(PSup['1j'])+'*(nCleanGenJet==1) + '+str(PSup['2j'])+'*(nCleanGenJet==2) + '+str(PSup['3j'])+'*(nCleanGenJet>=3)', str(PSdn['0j'])+'*(nCleanGenJet==0) + '+str(PSdn['1j'])+'*(nCleanGenJet==1) + '+str(PSdn['2j'])+'*(nCleanGenJet==2) + '+str(PSdn['3j'])+'*(nCleanGenJet>=3)']

        nuisances['UEPS_ISR_'+Year]['samples']['qqH_hww'+str(MX)+model_name]=PSstring
        nuisances['UEPS_ISR_'+Year]['samples']['qqH_hww_SI'+str(MX)+model_name]=PSstring

    nuisances['UEPS_FSR_'+Year]={
        'name': 'PS_FSR',
        'kind': 'weight',
        'type': 'shape',
        'samples':{}
    }

    for proc in sorted(PSuncBkg):
        if Year=='2017':
            if not proc in ['DY10to50','DY50','WZ','ZZ','WWW','WZZ','WWZ','ZZZ','ST_tch_antitop','ST_tch_top','Wjets0j','Wjets1j','Wjets2j','ZHWWlnuqq_M125','WpHWWlnuqq_M125','WmHWWlnuqq_M125','Wp2jWmln','WplvWm2j','tW_antitop','tW_top']: continue
        if Year=='2016':
            if proc in ['ST_tch_antitop', 'ggWW']:continue ##using PSbranch
            if 'qqH_hww3000' in proc :continue ##using PSbranch
        PSup = PSuncBkg[proc]['FSRup']
        PSdn = PSuncBkg[proc]['FSRdn']
        PSstring = [str(PSup['0j'])+'*(nCleanGenJet==0) + '+str(PSup['1j'])+'*(nCleanGenJet==1) + '+str(PSup['2j'])+'*(nCleanGenJet==2) + '+str(PSup['3j'])+'*(nCleanGenJet>=3)', str(PSdn['0j'])+'*(nCleanGenJet==0) + '+str(PSdn['1j'])+'*(nCleanGenJet==1) + '+str(PSdn['2j'])+'*(nCleanGenJet==2) + '+str(PSdn['3j'])+'*(nCleanGenJet>=3)']
        nuisances['UEPS_FSR_'+Year]['samples'][proc]=PSstring                                                                                                                 
        nuisances['UEPS_FSR_'+Year]['samples'][proc]=PSstring


    for MX in List_MX:
        if Year=='2017': continue
        PSup = PSunc['GGF'+str(MX)]['FSRup']
        PSdn = PSunc['GGF'+str(MX)]['FSRdn']
        PSstring = [str(PSup['0j'])+'*(nCleanGenJet==0) + '+str(PSup['1j'])+'*(nCleanGenJet==1) + '+str(PSup['2j'])+'*(nCleanGenJet==2) + '+str(PSup['3j'])+'*(nCleanGenJet>=3)', str(PSdn['0j'])+'*(nCleanGenJet==0) + '+str(PSdn['1j'])+'*(nCleanGenJet==1) + '+str(PSdn['2j'])+'*(nCleanGenJet==2) + '+str(PSdn['3j'])+'*(nCleanGenJet>=3)']

        nuisances['UEPS_FSR_'+Year]['samples']['ggH_hww'+str(MX)+model_name]=PSstring
        nuisances['UEPS_FSR_'+Year]['samples']['ggH_hww_SI'+str(MX)+model_name]=PSstring

    for MX in List_MX_VBF:
        if Year=='2017': continue
        PSup = PSunc['VBF'+str(MX)]['FSRup']
        PSdn = PSunc['VBF'+str(MX)]['FSRdn']
        PSstring = [str(PSup['0j'])+'*(nCleanGenJet==0) + '+str(PSup['1j'])+'*(nCleanGenJet==1) + '+str(PSup['2j'])+'*(nCleanGenJet==2) + '+str(PSup['3j'])+'*(nCleanGenJet>=3)', str(PSdn['0j'])+'*(nCleanGenJet==0) + '+str(PSdn['1j'])+'*(nCleanGenJet==1) + '+str(PSdn['2j'])+'*(nCleanGenJet==2) + '+str(PSdn['3j'])+'*(nCleanGenJet>=3)']

        nuisances['UEPS_FSR_'+Year]['samples']['qqH_hww'+str(MX)+model_name]=PSstring
        nuisances['UEPS_FSR_'+Year]['samples']['qqH_hww_SI'+str(MX)+model_name]=PSstring

    


##--norm
nuisances['QCDnorm']={
    'name': 'QCDnorm'+Year,
    'type': 'lnN',
    'samples': {
      'QCD_MU':'1.40',
      'QCD_EM':'1.40',
      'QCD_bcToE':'1.40',
        'QCD':'1.40'
      }
}

'''
nuisances['CMS_hww_WWqscale']={
    'name': 'CMS_hww_WWqscale',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'WW'   : ['nllW_Qup/nllW', 'nllW_Qdown/nllW'],
      }
}

nuisances['CMS_hww_WWresum']={
    'name': 'CMS_hww_WWresum',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'WW'   : ['nllW_Qup/nllW', 'nllW_Qdown/nllW'],
      }
}
'''
#https://arxiv.org/pdf/1507.00020.pdf
nuisances['ggWWnorm']={
    'name': 'ggWWnorm',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'ggWW':['1.265','0.803'],
      }
}


#assign 30%
nuisances['qqWWqqnorm']={
    'name': 'qqWWqqnorm',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'qqWWqq':['1.3','0.7'],
      }
}
for s in samples:
    if s=='qqWWqq' or 'Wp2jWmln'==s or 'WplvWm2j'==s:
        nuisances['qqWWqqnorm']['samples'][s]=['1.3','0.7']






CATS=['GGF0','GGF1','VBF',
      'GGFDNN0','GGFDNN1','VBFDNN']
##--wjets rateparam
for cat in CATS:
    #continue
    nuisances['Wjetsnorm_'+cat+'_'+bst]={
        'name': 'Wjetsnorm_'+bst+'_'+cat+'_'+Year,
        'type'  : 'rateParam',
        'samples': {
            'Wjets':'1.0',
        },
        
    }
    exec("nuisances['Wjetsnorm_'+"+"'"+cat+"'"+"+'_'+bst]['cuts']=cut_"+cat+"")
  
##--top rateparam ->currently only ttbar
for cat in CATS:
    #continue
    nuisances['Topnorm_'+cat+'_'+bst]={
        'name': 'topnorm_'+bst+'_'+cat+'_'+Year,
        'samples': {
            'Top':'1.0',
        },
        'type'  : 'rateParam',
    }
    exec("nuisances['Topnorm_'+"+"'"+cat+"'"+"+'_'+bst]['cuts']=cut_"+cat+"")
    
    
nuisances['dynorm']={
    'name': 'dynorm'+Year,
    'type': 'lnN',
    'samples': {
      'DY':'1.40',
    }
}


nuisances['MultiBosonnorm']={
    'name': 'MultiBosonnorm'+Year,
    'type': 'lnN',
    'samples': {
      #'MultiBoson':'1.1',
    }
}
if not CombineMultiBoson:
    for multiv in MultiBoson:
        nuisances['MultiBosonnorm']['samples'][multiv]='1.40'
else:
    nuisances['MultiBosonnorm']['samples']['MultiBoson']='1.40'

nuisances['stat'] = {
    'type': 'auto',
    'maxPoiss': '10',
    'includeSignal': '0',
    #  nuisance ['maxPoiss'] =  Number of threshold events for Poisson modelling
    #  nuisance ['includeSignal'] =  Include MC stat nuisances on signal processes (1=True, 0=False)
    'samples': {}
}
  
            

for n in nuisances.values():
    n['skipCMS'] = 1


#for n in sorted(nuisances): 
#  #USEONLY
#  if not n in USEONLY:
#    del nuisances[n]
print "nNuisances=",len(nuisances)



if StatOnly:

    #    'type': 'lnN',

    for nuis in sorted(nuisances):
        if 'type' in nuisances[nuis]:
            if 'lnN'==nuisances[nuis]['type']:continue
        if 'kind' in nuisances[nuis]:
            if 'type' in nuisances[nuis]:
                if 'weight'==nuisances[nuis]['kind'] and 'shape'==nuisances[nuis]['type']:continue
        del nuisances[nuis]



else:
    if LepMetOnly:
        USEONLY=['eletrigg','mutrigg','eff_e','eff_m','elept','mupt','met','MjjReweight']
        for n in sorted(nuisances):
            #USEONLY
            if not n in USEONLY:
                del nuisances[n]
    if JetMetOnly:
        USEONLY=[]
        USEONLY.append('MjjReweight')
        ##--btag
        for shift in ['lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
            USEONLY.append('btag_shape_%s' % shift)
        ##--jet
        for s in ['jesFlavorQCD','jesRelativeBal','jesHF','jesBBEC1','jesEC2','jesAbsolute']+['jesAbsolute_'+Year,'jesHF_'+Year,'jesEC2_'+Year,'jesRelativeSample_'+Year,'jesBBEC1_'+Year,'jer','jesTotal']:
            USEONLY.append('ak4_'+s)
            USEONLY.append('ak8_'+s)
        for s in ['jmr','jms']:
            USEONLY.append('ak8_'+s)
        

        for n in sorted(nuisances):
            #USEONLY
            if not n in USEONLY:
                del nuisances[n]
    

##------Add SBI's nuisance 
if ForDatacard or ForPlotting:
    ggH_sbi_list = [skey for skey in samples if ('SBI' in skey) and ('ggH_hww' in skey) ]
    qqH_sbi_list = [skey for skey in samples if ('SBI' in skey) and ('qqH_hww' in skey) ]
    for n in nuisances:
      for s in sorted(nuisances[n]['samples']):
        if 'ggH_hww' in s and 'ggH_hww'!=s:
          sbi=s.replace('ggH_hww','ggH_hww_SBI')
          nuisances[n]['samples'][sbi]=nuisances[n]['samples'][s]
        elif 'ggWW'==s:
          #sbi=s.replace('ggH_hww',ggH_hww'_SBI')
          for sbi in ggH_sbi_list:
           if not sbi in nuisances[n]['samples'] : nuisances[n]['samples'][sbi]=nuisances[n]['samples'][s]
        elif 'ggH_hww'==s:
          #sbi=s.replace('ggH_hww',ggH_hww'_SBI')
          for sbi in ggH_sbi_list:
           if not sbi in nuisances[n]['samples'] : nuisances[n]['samples'][sbi]=nuisances[n]['samples'][s]
        if 'qqH_hww' in s and 'qqH_hww'!=s:
          sbi=s.replace('qqH_hww','qqH_hww_SBI')
          nuisances[n]['samples'][sbi]=nuisances[n]['samples'][s]
        elif 'qqWWqq'==s:
          for sbi in qqH_sbi_list:
           if not sbi in nuisances[n]['samples'] : nuisances[n]['samples'][sbi]=nuisances[n]['samples'][s]
        elif 'qqH_hww'==s:
          for sbi in qqH_sbi_list:
           if not sbi in nuisances[n]['samples'] : nuisances[n]['samples'][sbi]=nuisances[n]['samples'][s]
  
    ##---Combined VH
    vh_list = ['WmHWWlnuqq_M125','WpHWWlnuqq_M125','ZHWWlnuqq_M125']
    for n in nuisances:
        for s in sorted(nuisances[n]['samples']):
            if s in vh_list:
                nuisances[n]['samples']['VH']=nuisances[n]['samples'][s]
    ##---Combined Wjets
    wjet_list = ['Wjets0j','Wjets1j','Wjets2j']
    for n in nuisances:
        for s in sorted(nuisances[n]['samples']):
            if s in wjet_list:
                nuisances[n]['samples']['Wjets']=nuisances[n]['samples'][s]

    ##---Combined Top
    top_list = ['SingleTop','TT','tW','TTsemilep','TTleptonic','tW_antitop','tW_top','ST_sch','ST_tch_antitop','ST_tch_top']
    for n in nuisances:
        for s in sorted(nuisances[n]['samples']):
            if s in top_list:
                nuisances[n]['samples']['Top']=nuisances[n]['samples'][s]


    ##---Combined DY
    dy_list = ['DY10to50','DY50']
    for n in nuisances:
        for s in sorted(nuisances[n]['samples']):
            if s in dy_list:
                nuisances[n]['samples']['DY']=nuisances[n]['samples'][s]
    ##---Combined qqWWqq
    qqwwqq_list = ['Wp2jWmln','WplvWm2j']
    for n in nuisances:
        for s in sorted(nuisances[n]['samples']):
            if s in qqwwqq_list:
                nuisances[n]['samples']['qqWWqq']=nuisances[n]['samples'][s]

    ##---Combined Multiboson
    multiboson_list = ['WZ','ZZ','WWW','WZZ','ZZZ','WWZ']
    for n in nuisances:
        for s in sorted(nuisances[n]['samples']):
            if s in multiboson_list:
                nuisances[n]['samples']['MultiBoson']=nuisances[n]['samples'][s]

    ##---Combined Qcd
    #qcd_list = ['WZ','ZZ','WWW','WZZ','ZZZ','WWZ']
    for n in nuisances:
        for s in sorted(nuisances[n]['samples']):
            if 'QCD' in s:
                nuisances[n]['samples']['QCD']=nuisances[n]['samples'][s]





###---bin by bin of sbi,s,b
if ForDatacard:
    for cut in cuts:
        #continue
        ##--ggH signal
        for binidx in range(1,int('<NBINS>')+1):
            nuiName='CMS_hww_'+str(Year)+'_'+cut+'_'+'<VARIABLE>'+'_'+'ggH_hww<MASS>'+model_name+'_bin'+str(binidx)+'_stat'
            nuisances[nuiName]={
                'name': nuiName,
                'kind': 'weight',
                'type': 'shape',
                'samples': {
                    'ggH_hww<MASS>'+model_name   : ['1','1'],
                    'ggH_hww_SBI<MASS>'+model_name   : ['1','1']
                },
                'cuts':[cut]
            }
            ##--ggH h125
            nuiName='CMS_hww_'+str(Year)+'_'+cut+'_'+'<VARIABLE>'+'_'+'ggH_hww_bin'+str(binidx)+'_stat'
            nuisances[nuiName]={
                'name': nuiName,
                'kind': 'weight',
                'type': 'shape',
                'samples': {
                    'ggH_hww'   : ['1','1'],
                    'ggH_hww_SBI<MASS>'+model_name   : ['1','1']
                },
                'cuts':[cut],
            }
            
            ##--ggWW
            nuiName='CMS_hww_'+str(Year)+'_'+cut+'_'+'<VARIABLE>'+'_'+'ggWW_bin'+str(binidx)+'_stat'
            nuisances[nuiName]={
                'name': nuiName,
                'kind': 'weight',
                'type': 'shape',
                'samples': {
                    'ggWW'   : ['1','1'],
                    'ggH_hww_SBI<MASS>'+model_name   : ['1','1']
                },
                'cuts':[cut]
            }
            
            ##--qqH signal
            nuiName='CMS_hww_'+str(Year)+'_'+cut+'_'+'<VARIABLE>'+'_'+'qqH_hww<MASS>'+model_name+'_bin'+str(binidx)+'_stat'
            nuisances[nuiName]={
                'name': nuiName,
                'kind': 'weight',
                'type': 'shape',
                'samples': {
                    'qqH_hww<MASS>'+model_name   : ['1','1'],
                    'qqH_hww_SBI<MASS>'+model_name   : ['1','1']
                },
                'cuts':[cut]
            }
            ##--qqH h125
        nuiName='CMS_hww_'+str(Year)+'_'+cut+'_'+'<VARIABLE>'+'_'+'qqH_hww_bin'+str(binidx)+'_stat'
        nuisances[nuiName]={
            'name': nuiName,
            'kind': 'weight',
            'type': 'shape',
            'samples': {
                'qqH_hww'   : ['1','1'],
                'qqH_hww_SBI<MASS>'+model_name   : ['1','1']
            },
            'cuts':[cut]
        }
        
        ##--qqWWqq
        nuiName='CMS_hww_'+str(Year)+'_'+cut+'_'+'<VARIABLE>'+'_'+'qqWWqq_bin'+str(binidx)+'_stat'
        nuisances[nuiName]={
            'name': nuiName,
            'kind': 'weight',
            'type': 'shape',
            'samples': {
                'qqWWqq'   : ['1','1'],
                'qqH_hww_SBI<MASS>'+model_name   : ['1','1']
            },
            'cuts':[cut]
        }


for n in nuisances.values():
    n['skipCMS'] = 1
#for n in sorted(nuisances):
#    #if 'kind' in nuisances[n]:
#    #    if 'weight' in nuisances[n]['kind']:continue
#    #if 'type' in nuisances[n]:
#    #    if 'rateParam'==nuisances[n]['type']:continue
#    #if n=='stat':continue
#    #if '_stat' in n : continue
#    #del nuisances[n]
print sorted(nuisances)
#del nuisances
#nuisances={}
    
#nuisances['stat'] = {
#    'type': 'auto',
#    'maxPoiss': '10',
#    'includeSignal': '0',
#    'samples': {}
#}


print "nNuisances=",len(nuisances)
