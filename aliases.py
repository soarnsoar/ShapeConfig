import os
import copy
import inspect
import numpy as np

##---WP---##
from WPandCut2016 import *
_ALGO="_"+ALGO
_ALGO_="_"+ALGO+"_"
##-End WP--##

##--Get Boosted OR Resolved--##
if 'opt' in globals():
    configration_py=opt.aliasesFile
else:
    configration_py=sys.argv[0]

Boosted=False
Resolved=False
if 'Boosted' in configration_py:
    Boosted=True
if 'Resolved' in configration_py:
    Resolved=True
##End of 


#configurations = '%s/src/SNuAnalytics/Configurations/HWWSemiLepHighMass/' % os.getenv('CMSSW_BASE')
#print configurations

mc = [skey for skey in samples if skey not in ('Fake', 'DATA')]

###---Btag SF---###
aliases['Jet_btagSF_shapeFix'] = {
    'linesToAdd': [
        'gSystem->Load("libCondFormatsBTauObjects.so");',
        'gSystem->Load("libCondToolsBTau.so");',
        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_RELEASE_BASE'),
        '.L '+os.getcwd()+'/patches/btagsfpatch.cc+'
    ],
    'class': 'BtagSF',
    'args': (btagSFSource,),
    'samples': mc
}
aliases['btagSF'] = {
    'expr': 'TMath::Exp(Sum$(TMath::Log((Jet_pt_nom[CleanJet_jetIdx]>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shapeFix[CleanJet_jetIdx]+1*(Jet_pt_nom[CleanJet_jetIdx]<20 || abs(CleanJet_eta)>2.5))))',
    'samples': mc
}
for shift in ['jes', 'lf', 'hf', 'lfstats1', 'lfstats2', 'hfstats1', 'hfstats2', 'cferr1', 'cferr2']:
#for shift in ['lf', 'hf', 'lfstats1', 'lfstats2', 'hfstats1', 'hfstats2', 'cferr1', 'cferr2']:
    #aliases['Jet_btagSF_shapeFix_up_%s' % shift] = {                                                                                                         
    aliases['Jet_btagSF%sup_shapeFix' % shift] = {
        'class': 'BtagSF',
        'args': (btagSFSource, 'up_' + shift),
        'samples': mc
    }
    aliases['Jet_btagSF%sdown_shapeFix' % shift] = {
        'class': 'BtagSF',
        'args': (btagSFSource, 'down_' + shift),
        'samples': mc
    }
 
    aliases['btagSF%sup' % shift] = {
        'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'up'),
        'samples': mc
    }

    aliases['btagSF%sdown' % shift] = {
        'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'down'),
        'samples': mc
    }




puidSFSource = os.getcwd()+'/JetPUID/PUID_81XTraining_EffSFandUncties.root'

aliases['PUJetIdSF'] = {
    'linesToAdd': [
        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
        '.L '+os.getcwd()+'/JetPUID/pujetidsf_event_new.cc+'
    ],
    'class': 'PUJetIdEventSF',
    'args': (puidSFSource, Year, 'loose'),
    'samples': mc
}


##--VBF DNN
if Boosted:
    aliases['DNN_isVBF'] = {
        #'class': 'DNNprod',                                                                                                                                                                                
        'class': 'TMVA_DNN_prod_bst',
        'linesToAdd':[
            'gSystem->AddIncludePath("-I/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-numpy/1.14.1-gnimlf2/lib/python2.7/site-packages/numpy/core/include/")', ##for finding path                       
            'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
            '.L '+os.getcwd()+'/TMVA_jhchoi_bst/TMVA_DNN_prod_bst.cc+',
        ],
    }
if Resolved:
    aliases['DNN_isVBF'] = {
        'class': 'TMVA_DNN_prod_res',
        'linesToAdd':[
            'gSystem->AddIncludePath("-I/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-numpy/1.14.1-gnimlf2/lib/python2.7/site-packages/numpy/core/include/")', ##for finding path                       
            'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
            '.L '+os.getcwd()+'/TMVA_jhchoi_res/TMVA_DNN_prod_res.cc+',
        ],
    }
if Boosted:
    if Year=="2016":
        aliases['VBFDNNTag']={
            'expr':'DNN_isVBF>0.75'
        }
    elif Year=="2017":
        aliases['VBFDNNTag']={
            'expr':'DNN_isVBF>0.85'
        }
    elif Year=="2018":
        aliases['VBFDNNTag']={
            'expr':'DNN_isVBF>0.8'
        }
if Resolved:
    if Year=="2016":
        aliases['VBFDNNTag']={
            'expr':'DNN_isVBF>0.975'
        }
    elif Year=="2017":
        aliases['VBFDNNTag']={
            'expr':'DNN_isVBF>0.975'
        }
    elif Year=="2018":
        aliases['VBFDNNTag']={
            'expr':'DNN_isVBF>0.94'
        }






##--common variabls for Boosted/Resolved
aliases['isBoost']={
    'expr':'(isBoost_'+WTAG+'_nom && (lnJ_'+WTAG+'_nom_widx >=0))'
}

aliases['isBoostSR']={
    'expr':'(isBoost_'+WTAG+'_nom && (lnJ_'+WTAG+'_nom_widx >=0) && (isBoostSR_'+WTAG+'_nom))'
}
aliases['isFinalBoostSR']={
    'expr':'(isBoost_'+WTAG+'_nom && (lnJ_'+WTAG+'_nom_widx >=0) && (isBoostSR_'+WTAG+'_nom) && ((nBJetBoost_'+WTAG+'_nom ==0)))'
}


###--Wtagger ID eff. SF

aliases['WtaggerSFnom']={
    #'expr' : '('+WtaggerSF+')'+'*(isBoost_'+WTAG+'_nom) + 1*(!isBoost_'+WTAG+'_nom)',
    #'expr' : '(isBoost_'+WTAG+'_nom &&(lnJ_'+WTAG+'_nom_widx >=0)) ? ('+WtaggerSF+')'+' : 1',
    #'expr' : '(isBoost_'+WTAG+'_nom && (lnJ_'+WTAG+'_nom_widx >=0) && (WtaggerFatjet_'+WTAG+'_nom_mass[lnJ_'+WTAG+'_nom_widx] > 65) && (WtaggerFatjet_'+WTAG+'_nom_mass[lnJ_'+WTAG+'_nom_widx] < 105) && (Sum$(  (pow(WtaggerFatjet_'+WTAG+'_nom_eta[lnJ_'+WTAG+'_nom_widx]-GenPart_eta, 2 ) + pow(WtaggerFatjet_'+WTAG+'_nom_phi[lnJ_'+WTAG+'_nom_widx]-GenPart_phi, 2 ) < 0.36) && (abs(GenPart_pdgId)==24)  && (  (GenPart_statusFlags/(1<<13))%2 ==1 ) && (   (GenPart_statusFlags/(1<<8))%2 ==1   ) )>0)) ? ('+WtaggerSF+')'+' : 1',

    #'expr' : '(isBoost_'+WTAG+'_nom && (lnJ_'+WTAG+'_nom_widx >=0) && (Sum$(  (pow(WtaggerFatjet_'+WTAG+'_nom_eta[lnJ_'+WTAG+'_nom_widx]-GenPart_eta, 2 ) + pow(WtaggerFatjet_'+WTAG+'_nom_phi[lnJ_'+WTAG+'_nom_widx]-GenPart_phi, 2 ) < 0.36) && (abs(GenPart_pdgId)==24)  && (  (GenPart_statusFlags/(1<<13))%2 ==1 ) && (   (GenPart_statusFlags/(1<<8))%2 ==1   ) )>0)) ? ('+WtaggerSF+')'+' : 1',
    #'expr' : '(isBoost_'+WTAG+'_nom && (lnJ_'+WTAG+'_nom_widx >=0)) ? ('+WtaggerSF+')'+' : 1',
    'expr':"(isBoost_"+WTAG+"_nom && (lnJ_"+WTAG+"_nom_widx >=0) && (Sum$( (GenPart_genPartIdxMother>-1)&& (pow(WtaggerFatjet_"+WTAG+"_nom_eta[lnJ_"+WTAG+"_nom_widx]-GenPart_eta[GenPart_genPartIdxMother], 2 ) + pow(WtaggerFatjet_"+WTAG+"_nom_phi[lnJ_"+WTAG+"_nom_widx]-GenPart_phi[GenPart_genPartIdxMother], 2 ) < 0.36) && (abs(GenPart_pdgId[GenPart_genPartIdxMother])==24)  && (  (GenPart_statusFlags[GenPart_genPartIdxMother]/(1<<13))%2 ==1 ) && (   (GenPart_statusFlags[GenPart_genPartIdxMother]/(1<<8))%2 ==1   ) &&(abs(GenPart_pdgId)<6))>1)) ? ("+WtaggerSF+")"+" : 1",
    'samples' : mc
} ##1<<13 : lastcopy , 1<<8 : from hardprocess
aliases['WtaggerSFup']={
    #'expr' : 'isBoost_'+WTAG+'_nom ? ('+WtaggerSFup+')'+' : 1',
    #'expr' : '('+WtaggerSFup+')'+'*(isBoost_'+WTAG+'_nom) + 1*(!isBoost_'+WTAG+'_nom)',
    #'expr' : '(isBoost_'+WTAG+'_nom && (lnJ_'+WTAG+'_nom_widx >=0) &&(WtaggerFatjet_'+WTAG+'_nom_mass[lnJ_'+WTAG+'_nom_widx] > 65) &&(WtaggerFatjet_'+WTAG+'_nom_mass[lnJ_'+WTAG+'_nom_widx] < 105)) ? ('+WtaggerSFup+')'+' : 1',
    #'expr' : '(isBoost_'+WTAG+'_nom && (lnJ_'+WTAG+'_nom_widx >=0) && (WtaggerFatjet_'+WTAG+'_nom_mass[lnJ_'+WTAG+'_nom_widx] > 65) && (WtaggerFatjet_'+WTAG+'_nom_mass[lnJ_'+WTAG+'_nom_widx] < 105) && (Sum$(  (pow(WtaggerFatjet_'+WTAG+'_nom_eta[lnJ_'+WTAG+'_nom_widx]-GenPart_eta, 2 ) + pow(WtaggerFatjet_'+WTAG+'_nom_phi[lnJ_'+WTAG+'_nom_widx]-GenPart_phi, 2 ) < 0.36) && (abs(GenPart_pdgId)==24)  && (GenPart_statusFlags & 9)  )>0)) ? ('+WtaggerSFup+')'+' : 1',
    #'expr' : '(isBoost_'+WTAG+'_nom && (lnJ_'+WTAG+'_nom_widx >=0) && (WtaggerFatjet_'+WTAG+'_nom_mass[lnJ_'+WTAG+'_nom_widx] > 65) && (WtaggerFatjet_'+WTAG+'_nom_mass[lnJ_'+WTAG+'_nom_widx] < 105) && (Sum$(  (pow(WtaggerFatjet_'+WTAG+'_nom_eta[lnJ_'+WTAG+'_nom_widx]-GenPart_eta, 2 ) + pow(WtaggerFatjet_'+WTAG+'_nom_phi[lnJ_'+WTAG+'_nom_widx]-GenPart_phi, 2 ) < 0.36) && (abs(GenPart_pdgId)==24)  && (  (GenPart_statusFlags/(1<<13))%2 ==1 ) && (   (GenPart_statusFlags/(1<<8))%2 ==1   ) )>0)) ? (WtaggerSFnom*'+WtaggerSFup+')'+' : 1',
    #'expr' : '(isBoost_'+WTAG+'_nom && (lnJ_'+WTAG+'_nom_widx >=0) && (Sum$(  (pow(WtaggerFatjet_'+WTAG+'_nom_eta[lnJ_'+WTAG+'_nom_widx]-GenPart_eta, 2 ) + pow(WtaggerFatjet_'+WTAG+'_nom_phi[lnJ_'+WTAG+'_nom_widx]-GenPart_phi, 2 ) < 0.36) && (abs(GenPart_pdgId)==24)  && (  (GenPart_statusFlags/(1<<13))%2 ==1 ) && (   (GenPart_statusFlags/(1<<8))%2 ==1   ) )>0)) ? (WtaggerSFnom*'+WtaggerSFup+')'+' : 1',
    'expr':"(isBoost_"+WTAG+"_nom && (lnJ_"+WTAG+"_nom_widx >=0) && (Sum$( (GenPart_genPartIdxMother>-1)&& (pow(WtaggerFatjet_"+WTAG+"_nom_eta[lnJ_"+WTAG+"_nom_widx]-GenPart_eta[GenPart_genPartIdxMother], 2 ) + pow(WtaggerFatjet_"+WTAG+"_nom_phi[lnJ_"+WTAG+"_nom_widx]-GenPart_phi[GenPart_genPartIdxMother], 2 ) < 0.36) && (abs(GenPart_pdgId[GenPart_genPartIdxMother])==24)  && (  (GenPart_statusFlags[GenPart_genPartIdxMother]/(1<<13))%2 ==1 ) && (   (GenPart_statusFlags[GenPart_genPartIdxMother]/(1<<8))%2 ==1   ) &&(abs(GenPart_pdgId)<6))>1)) ? ("+WtaggerSFup+")"+" : 1",
    #'expr' : '(isBoost_'+WTAG+'_nom && (lnJ_'+WTAG+'_nom_widx >=0)) ? (WtaggerSFnom*'+WtaggerSFup+')'+' : 1',
    'samples' : mc
}
aliases['WtaggerSFdown']={
    #'expr' : 'isBoost_'+WTAG+'_nom ? ('+WtaggerSFdown+')'+' : 1',
    #'expr' : '('+WtaggerSFdown+')'+'*(isBoost_'+WTAG+'_nom) + 1*(!isBoost_'+WTAG+'_nom)',
    #'expr' : '(isBoost_'+WTAG+'_nom && (lnJ_'+WTAG+'_nom_widx >=0) && (WtaggerFatjet_'+WTAG+'_nom_mass[lnJ_'+WTAG+'_nom_widx] > 65) && (WtaggerFatjet_'+WTAG+'_nom_mass[lnJ_'+WTAG+'_nom_widx] < 105) ) ? ('+WtaggerSFdown+')'+' : 1',
    #'expr' : '(isBoost_'+WTAG+'_nom && (lnJ_'+WTAG+'_nom_widx >=0) && (WtaggerFatjet_'+WTAG+'_nom_mass[lnJ_'+WTAG+'_nom_widx] > 65) && (WtaggerFatjet_'+WTAG+'_nom_mass[lnJ_'+WTAG+'_nom_widx] < 105) && (Sum$(  (pow(WtaggerFatjet_'+WTAG+'_nom_eta[lnJ_'+WTAG+'_nom_widx]-GenPart_eta, 2 ) + pow(WtaggerFatjet_'+WTAG+'_nom_phi[lnJ_'+WTAG+'_nom_widx]-GenPart_phi, 2 ) < 0.36) && (abs(GenPart_pdgId)==24)  && (  (GenPart_statusFlags/(1<<13))%2 ==1 ) && (   (GenPart_statusFlags/(1<<8))%2 ==1   ) )>0)) ? (WtaggerSFnom*'+WtaggerSFdown+')'+' : 1',

    #'expr' : '(isBoost_'+WTAG+'_nom && (lnJ_'+WTAG+'_nom_widx >=0) && (Sum$(  (pow(WtaggerFatjet_'+WTAG+'_nom_eta[lnJ_'+WTAG+'_nom_widx]-GenPart_eta, 2 ) + pow(WtaggerFatjet_'+WTAG+'_nom_phi[lnJ_'+WTAG+'_nom_widx]-GenPart_phi, 2 ) < 0.36) && (abs(GenPart_pdgId)==24)  && (  (GenPart_statusFlags/(1<<13))%2 ==1 ) && (   (GenPart_statusFlags/(1<<8))%2 ==1   ) )>0)) ? (WtaggerSFnom*'+WtaggerSFdown+')'+' : 1',
    #'expr' : '(isBoost_'+WTAG+'_nom && (lnJ_'+WTAG+'_nom_widx >=0) ) ? (WtaggerSFnom*'+WtaggerSFdown+')'+' : 1',
    'expr':"(isBoost_"+WTAG+"_nom && (lnJ_"+WTAG+"_nom_widx >=0) && (Sum$( (GenPart_genPartIdxMother>-1)&& (pow(WtaggerFatjet_"+WTAG+"_nom_eta[lnJ_"+WTAG+"_nom_widx]-GenPart_eta[GenPart_genPartIdxMother], 2 ) + pow(WtaggerFatjet_"+WTAG+"_nom_phi[lnJ_"+WTAG+"_nom_widx]-GenPart_phi[GenPart_genPartIdxMother], 2 ) < 0.36) && (abs(GenPart_pdgId[GenPart_genPartIdxMother])==24)  && (  (GenPart_statusFlags[GenPart_genPartIdxMother]/(1<<13))%2 ==1 ) && (   (GenPart_statusFlags[GenPart_genPartIdxMother]/(1<<8))%2 ==1   ) &&(abs(GenPart_pdgId)<6))>1)) ? ("+WtaggerSFdown+")"+" : 1",

    #'expr' : '(isBoost_'+WTAG+'_nom && (lnJ_'+WTAG+'_nom_widx >=0) && (WtaggerFatjet_'+WTAG+'_nom_mass[lnJ_'+WTAG+'_nom_widx] > 65) && (WtaggerFatjet_'+WTAG+'_nom_mass[lnJ_'+WTAG+'_nom_widx] < 105) && (Sum$(  (pow(WtaggerFatjet_'+WTAG+'_nom_eta[lnJ_'+WTAG+'_nom_widx]-GenPart_eta, 2 ) + pow(WtaggerFatjet_'+WTAG+'_nom_phi[lnJ_'+WTAG+'_nom_widx]-GenPart_phi, 2 ) < 0.36) && (abs(GenPart_pdgId)==24)  && (GenPart_statusFlags & 9)  )>0)) ? ('+WtaggerSFdown+')'+' : 1',

    'samples' : mc
}




##--OTF EleTrigEff
ToBR={
    'up':'high',
    'down':'low'
}


if Year=='2017':
    ##--Weight
    #EleTrigEff/weightReaderWithEta.cc
    aliases['EleTrigWeight2017B'] = {
        'linesToAdd': [
            'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_RELEASE_BASE'),
            '.L '+os.getcwd()+'/EleTrigEff/weightReader.cc+'
        ],
        'class': 'WeightReader',
        'args': (os.getcwd()+'/EleTrigEff/EleTrigEffAndSF_latino.root','eff_2017Blatino'),
        'samples': mc

    }

    aliases['EleTrigWeight2017CDE'] = {
        'class': 'WeightReader',
        'args': (os.getcwd()+'/EleTrigEff/EleTrigEffAndSF_latino.root','eff_2017CDElatino'),
        'samples': mc
    }

    aliases['EleTrigWeight2017F'] = {
        'class': 'WeightReader',
        'args': (os.getcwd()+'/EleTrigEff/EleTrigEffAndSF_latino.root','eff_2017Flatino'),
        'samples': mc
    }

    aliases['EleTrigWeight']={
        'expr':'(run_period==1)*EleTrigWeight2017B + (run_period>1 && run_period<5)*EleTrigWeight2017CDE + (run_period==5)*EleTrigWeight2017F',
        'samples': mc
    }


    for var in ['up','down']:
        for period in ['B','CDE','F']:
            aliases['EleTrigWeight2017'+period+'_'+var] = {
                'class': 'WeightReader',
                'args': (os.getcwd()+'/EleTrigEff/EleTrigEffAndSF_latino.root','eff'+ToBR[var]+'_2017'+period+'latino_'+var),
                'samples': mc
            }
    for var in ['up','down']:
        aliases['EleTrigWeight_'+var]={
            'expr':'(run_period==1)*EleTrigWeight2017B_'+var+' + (run_period>1 && run_period<5)*EleTrigWeight2017CDE_'+var+' + (run_period==5)*EleTrigWeight2017F_'+var,
            'samples': mc
        }

    ##--decision
    aliases['passSingleElectronHLT']={
        'expr':'Sum$((TrigObj_id==11) && (TrigObj_filterBits & 1024) )'

    }

    

if Year=='2016':
    aliases['EleTrigWeight'] = {
        'linesToAdd': [
            'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_RELEASE_BASE'),
            '.L '+os.getcwd()+'/EleTrigEff/weightReader.cc+'
        ],
        'class': 'WeightReader',
        'args': (os.getcwd()+'/EleTrigEff/EleTrigEffAndSF_latino.root','eff_2016latino'),
        'samples': mc

    }

    for var in ['up','down']:
        
        period=''
        aliases['EleTrigWeight_'+var] = {
            'class': 'WeightReader',
            'args': (os.getcwd()+'/EleTrigEff/EleTrigEffAndSF_latino.root','eff'+ToBR[var]+'_2016'+period+'latino_'+var),
            'samples': mc
        }


    aliases['passSingleElectronHLT']={
        #'expr':'Trigger_sngEl'
        'expr':'Trigger_sngEl'

    }



if Year=='2018':
    aliases['EleTrigWeight'] = {
        'linesToAdd': [
            'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_RELEASE_BASE'),
            '.L '+os.getcwd()+'/EleTrigEff/weightReader.cc+'
        ],
        'class': 'WeightReader',
        'args': (os.getcwd()+'/EleTrigEff/EleTrigEffAndSF_latino.root','eff_2018latino'),
        'samples': mc

    }


    period =''
    for var in ['up','down']:
        aliases['EleTrigWeight_'+var] = {
            'class': 'WeightReader',
            'args': (os.getcwd()+'/EleTrigEff/EleTrigEffAndSF_latino.root','eff'+ToBR[var]+'_2018'+period+'latino_'+var),
            'samples': mc
        }
    

    aliases['passSingleElectronHLT']={
        'expr':'Trigger_sngEl'

    }






##---Trig eff
aliases['trigWeight']={
    'expr' : '(Lepton_isTightElectron_'+eleWP+'[0]>0.5)&&(Lepton_isTightMuon_'+muWP+'[0]<0.5) ?  EleTrigWeight : TriggerEffWeight_1l*'+'(Lepton_isTightMuon_'+muWP+'[0]>0.5)', ##eletron trig_eff_SF isnot valid yet
    #'expr' : '1',
    'samples':mc

}
mutrig_syst = ['((Lepton_isTightMuon_'+muWP+'[0]>0.5)&&(TriggerEffWeight_1l_u/TriggerEffWeight_1l < 10)) ? (TriggerEffWeight_1l_u/TriggerEffWeight_1l)*(TriggerEffWeight_1l>0.02)+(TriggerEffWeight_1l<=0.02) : 1.0',
               '((Lepton_isTightMuon_'+muWP+'[0]>0.5)&&(TriggerEffWeight_1l_u/TriggerEffWeight_1l < 10)) ? (TriggerEffWeight_1l_d/TriggerEffWeight_1l)*(TriggerEffWeight_1l>0.02)+(TriggerEffWeight_1l<=0.02) : 1.0']

eletrig_syst = ['((Lepton_isTightElectron_'+eleWP+'[0]>0.5)&&(EleTrigWeight_up/EleTrigWeight < 10)) ? (EleTrigWeight_up/EleTrigWeight) : 1.0',
                '((Lepton_isTightElectron_'+eleWP+'[0]>0.5)&&(EleTrigWeight_down/EleTrigWeight < 10)) ? (EleTrigWeight_down/EleTrigWeight) : 1.0']

aliases['eletrigWeight_up']={
    'expr':eletrig_syst[0],
    'samples':mc
}


aliases['eletrigWeight_down']={
    'expr':eletrig_syst[1],
    'samples':mc
}


aliases['mutrigWeight_up']={
    'expr':mutrig_syst[0],
    'samples':mc
}


aliases['mutrigWeight_down']={
    'expr':mutrig_syst[1],
    'samples':mc
}


##--Lepton ISO/ID/RECO
aliases['LepWPweight']={
    'expr':' Lepton_promptgenmatched[0] ? (((Lepton_isTightElectron_'+eleWP+'[0]>0.5)*(Lepton_tightElectron_'+eleWP+'_TotSF'+'[0]'+')) + ((Lepton_isTightMuon_'+muWP+'[0]>0.5)*(Lepton_tightMuon_'+muWP+'_TotSF'+'[0]'+'))) : 1',
    'samples':mc
}

aliases['LepWPCut']={
    'expr':'(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'
}

aliases['SFweight']={
    'expr':SFweight,
    'samples':mc
}



aliases['nJetPassBKin']={
    'expr':'Sum$(Jet_pt_nom[CleanJet_jetIdx]>20 && abs(CleanJet_eta)<2.5)'
}

aliases['JetMultplicity']={
    'expr':'Sum$(Jet_pt_nom[CleanJet_jetIdx]>'+jetptmin+' && abs(CleanJet_eta)<'+jetetamax+')'
}

aliases['JetMultplicity_eta4p7']={
    'expr':'Sum$(Jet_pt_nom[CleanJet_jetIdx]>'+jetptmin+' && abs(CleanJet_eta)<4.7)'
}


for M_MELA in MELA_MASS_BOOST:
    for C in MELA_C_BOOST:
        M=str(M_MELA)
        C=str(C)
        P_S='meP'+M+'_Bst_ggf_S_'+WTAG+'_nom'
        P_B='meP'+M+'_Bst_ggf_B_'+WTAG+'_nom'
        P_B_S=P_B+'/'+P_S
        aliases['MEKD_Bst_C_'+C+'_M'+str(M)]={
            'expr':P_S+'>0 ? '+'1/(1+'+C+'*'+P_B_S+')'+':-1'
        }


for M_MELA in MELA_MASS_RESOL:
    for C in MELA_C_RESOL:
        M=str(M_MELA)
        C=str(C)
        P_S='meP'+M+'_Res_ggf_S_'+ALGO+'_nom'
        P_B='meP'+M+'_Res_ggf_B_'+ALGO+'_nom'
        P_B_S=P_B+'/'+P_S
        aliases['MEKD_Res_C_'+C+'_M'+str(M)]={
            'expr':P_S+'>0 ? '+'1/(1+'+C+'*'+P_B_S+')'+':-1'
        }



##--some missing branch
#PuppiMET_nom_pt
#aliases['PuppiMET_nom_pt']={
#    'expr':'sqrt(PuppiMET_nom_px*PuppiMET_nom_px+PuppiMET_nom_py*PuppiMET_nom_py)'
#}

if Year=='2018':
    lastcopy = (1 << 13)
    aliases['topGenPtOTF'] = {
        'expr': 'Sum$((GenPart_pdgId == 6 && TMath::Odd(GenPart_statusFlags / %d)) * GenPart_pt)' % lastcopy,
        'samples': ['tW','TT','SingleTop','TTsemilep','TTleptonic',]
    }

    aliases['antitopGenPtOTF'] = {
        'expr': 'Sum$((GenPart_pdgId == -6 && TMath::Odd(GenPart_statusFlags / %d)) * GenPart_pt)' % lastcopy,
        'samples': ['tW','TT','SingleTop','TTsemilep','TTleptonic']
    }

    aliases['Top_pTrw'] = {
        'expr': '(topGenPtOTF * antitopGenPtOTF > 0.) * (TMath::Sqrt((0.103*TMath::Exp(-0.0118*topGenPtOTF) - 0.000134*topGenPtOTF + 0.973) * (0.103*TMath::Exp(-0.0118*antitopGenPtOTF) - 0.000134*antitopGenPtOTF + 0.973))) + (topGenPtOTF * antitopGenPtOTF <= 0.)',
        #    'expr': '(topGenPt * antitopGenPt > 0.) * (TMath::Sqrt((0.103*TMath::Exp(-0.0118*topGenPt) - 0.000134*topGenPt + 0.973) * (0.103*TMath::Exp(-0.0118*antitopGenPt) - 0.000134*antitopGenPt + 0.973))) + (topGenPt * antitopGenPt <= 0.)',
        #'expr':'1',
        'samples': ['tW','TT','SingleTop','TTsemilep','TTleptonic',]
    }

    #aliases['Top_pTrw'] = {
    #    'expr': '(topGenPt * antitopGenPt > 0.) * (TMath::Sqrt((0.103*TMath::Exp(-0.0118*topGenPt) - 0.000134*topGenPt + 0.973) * (0.103*TMath::Exp(-0.0118*antitopGenPt) - 0.000134*antitopGenPt + 0.973))) + (topGenPt * antitopGenPt <= 0.)',
    #    'samples': ['tW','TT','SingleTop']
    #}

if Year=='2017':

    aliases['Top_pTrw'] = {
        'expr': '(topGenPt * antitopGenPt > 0.) * (TMath::Sqrt((0.103*TMath::Exp(-0.0118*topGenPt) - 0.000134*topGenPt + 0.973) * (0.103*TMath::Exp(-0.0118*antitopGenPt) - 0.000134*antitopGenPt + 0.973))) + (topGenPt * antitopGenPt <= 0.)',
        'samples': ['tW','TT','SingleTop','TTsemilep','TTleptonic',]
    }

    #aliases['Top_pTrw'] = {
    #    'expr':'1',
    #    'samples': ['tW','TT','SingleTop']
    #}


if Year=='2016':
    aliases['Top_pTrw']={

        'expr':'(topGenPt * antitopGenPt > 0.) * (TMath::Sqrt((0.103*TMath::Exp(-0.0118*topGenPt) - 0.000134*topGenPt + 0.973) * (0.103*TMath::Exp(-0.0118*antitopGenPt) - 0.000134*antitopGenPt + 0.973))) * (TMath::Sqrt(TMath::Exp(1.61468e-03 + 3.46659e-06*topGenPt - 8.90557e-08*topGenPt*topGenPt) * TMath::Exp(1.61468e-03 + 3.46659e-06*antitopGenPt - 8.90557e-08*antitopGenPt*antitopGenPt))) + (topGenPt * antitopGenPt <= 0.)', # Same Reweighting as other years, but with additional fix for tune CUET -> CP5                                                                                     
        'samples':['tW','TT','SingleTop','TTsemilep','TTleptonic']
    }
    #aliases['Top_pTrw'] = {
    #    'expr':'1',
    #    'samples': ['tW','TT','SingleTop']
    #}


aliases['LHEPartWlepPt'] = {
    #'linesToAdd': ['.L %s/HWWSemiLepHighMass/Full2017/LHEPartWlepPt.cc+' % configurations],
    'linesToAdd':['.L '+os.getcwd()+'/W_EWKNLO/LHEPartWlepPt.cc+'],
    'class': 'LHEPartWlepPt',
    'samples': ['Wjets0j', 'Wjets1j','Wjets2j']
}
data = np.genfromtxt(os.getenv('CMSSW_BASE')+'/src/LatinoAnalysis/Gardener/python/data/ewk/kewk_w.dat', skip_header=2, skip_footer=7)
weight_string = "("
uncert_string = "("
for row in data:
    low  = row[0]
    high = row[1]
    weight = (1+row[2])
    ucert = row[3]

    weight_string+="({}<LHEPartWlepPt[0] && LHEPartWlepPt[0]<={})*{}+".format(low, high, weight)
    uncert_string+="({}<LHEPartWlepPt[0] && LHEPartWlepPt[0]<={})*{}+".format(low, high, weight)
# remove trailing + sign and close parentheses
weight_string=weight_string[:-1]+")"
uncert_string=uncert_string[:-1]+")"

aliases['EWK_W_correction'] = {
    'expr': weight_string,
    'samples': ['Wjets0j', 'Wjets1j','Wjets2j']
}
aliases['EWK_W_correction_uncert'] = {
    'expr': uncert_string,
    # 'samples': 'Wjets'
    'samples': ['Wjets0j', 'Wjets1j','Wjets2j']
}


aliases['dphi_lep_met']={
    'expr':'fabs(Lepton_phi-'+METtype+'_phi)<TMath::Pi() ? fabs(Lepton_phi-'+METtype+'_phi) : 2*TMath::Pi()-fabs(Lepton_phi-'+METtype+'_phi)'
}

#aliases['dPhi_WW_boosted']={
    #'expr':' ((isBoost_'+WTAG+'_nom)&&(lnJ_'+WTAG+'_nom_widx >=0)) ? (WtaggerFatjet_'+WTAG+'_nom_phi[lnJ_'+WTAG+'_nom_widx]-Wlep_nom_phi)-2*3.1415927*(  (WtaggerFatjet_'+WTAG+'_nom_phi[lnJ_'+WTAG+'_nom_widx]-Wlep_nom_phi) > 3.1415927) + 2*3.1415927*((WtaggerFatjet_'+WTAG+'_nom_phi[lnJ_'+WTAG+'_nom_widx]-Wlep_nom_phi) < 3.1415927) : -100.'
#    'expr':' ('+aliases['isBoost']['expr']+') ? (WtaggerFatjet_'+WTAG+'_nom_phi[lnJ_'+WTAG+'_nom_widx]-Wlep_nom_phi)-2*3.1415927*(  (WtaggerFatjet_'+WTAG+'_nom_phi[lnJ_'+WTAG+'_nom_widx]-Wlep_nom_phi) > 3.1415927) + 2*3.1415927*((WtaggerFatjet_'+WTAG+'_nom_phi[lnJ_'+WTAG+'_nom_widx]-Wlep_nom_phi) < 3.1415927) : -100.'
#}


#aliases['dPhi_WW_resolved']={
#    'expr':'(Whad'+_ALGO_+'nom_phi-Wlep_nom_phi)-2*3.1415927*(  (Whad'+_ALGO_+'nom_phi-Wlep_nom_phi) > 3.1415927) + 2*3.1415927*((Whad'+_ALGO_+'nom_phi-Wlep_nom_phi) < 3.1415927)'
#}


aliases['nCleanGenJet'] = {
    'linesToAdd': ['.L '+os.getcwd()+'/PsScript/ngenjet.cc+'
    ],
    'class': 'CountGenJet',
    'samples': mc

}

#aliases['GenJet_HT'] = {
#    'expr':'Sum$(GenJet_pt)',
#    'samples':mc
#}

##---python name
import sys
sys.path.insert(0, "MjjShapeWeight")
from MjjShapeWeight import DICT_MjjShapeW

if 'opt' in globals():
    configration_py=opt.aliasesFile
else:
    configration_py=sys.argv[0]

##---MjjShapeSys --configuration
if Boosted:
    #WmassVariable=' ((isBoost_'+WTAG+'_nom && (lnJ_'+WTAG+'_nom_widx >=0)) ? WtaggerFatjet_'+WTAG+'_nom_mass[lnJ_'+WTAG+'_nom_widx] : -1)'
    WmassVariable=' (('+aliases['isBoost']['expr']+') ? WtaggerFatjet_'+WTAG+'_nom_mass[lnJ_'+WTAG+'_nom_widx] : -1)'
    bst='Boosted'
if Resolved:
    WmassVariable='Whad'+_ALGO_+'nom_mass'
    bst='Resolved'
print "[WmassVariable]",WmassVariable

##----reweight

##---[END]MjjShapeSys--##


##--dphi module
#aliases['Setup_dPhiVBF'] = {
#    'linesToAdd': [        
#        '.L '+os.getcwd()+'/OTFtemplate/dPhiVBF.cc+'
#    ],
#    'expr':'1',
#}
#dPhiVBF



##--Simple Expression for plotting--##
##--common variabls for Boosted/Resolved

aliases['nAK4Jet']={
    'expr':'Sum$(Jet_pt_nom[CleanJet_jetIdx]>'+jetptmin+' && abs(CleanJet_eta)<'+jetetamax+')'
}
aliases['nAK4Jet_eta4p7']={
    'expr':'Sum$(Jet_pt_nom[CleanJet_jetIdx]>'+jetptmin+' && abs(CleanJet_eta)<4.7)'
}

aliases['LeadingJet_BtagScore']={
    'expr':'Jet_btagDeepB[CleanJet_jetIdx[0]]'
}
aliases['LeadingJet_pt']={
    'expr':'Jet_pt_nom[CleanJet_jetIdx[0]]'
}
aliases['LeadingJet_eta']={
    'expr':'Jet_eta[CleanJet_jetIdx[0]]'
}

aliases['SubLeadingJet_BtagScore']={
    'expr':'Jet_btagDeepB[CleanJet_jetIdx[1]]'
}
aliases['SubLeadingJet_pt']={
    'expr':'Jet_pt_nom[CleanJet_jetIdx[1]]'
}
aliases['SubLeadingJet_eta']={
    'expr':'Jet_eta[CleanJet_jetIdx[1]]'
}
 


##--BJet--##
if Boosted:
    aliases['nBJet']={
        'expr':'nBJetBoost_'+WTAG+'_nom'
    }
if Resolved:
    aliases['nBJet']={
        'expr':'nBJetResol_'+ALGO+'_nom'
    }


##--addjet--##
if Boosted:
    aliases['AddJet_BtagScore']={
        'expr':'Jet_btagDeepB[CleanJet_jetIdx[AddJetBoost_'+WTAG+'_nom_cjidx]]'
    }
    aliases['nAddJet']={
        'expr':'Sum$(AddJetBoost_'+WTAG+'_nom_cjidx>=0)'
    }
    aliases['AddJet_eta']={
        'expr':'AddJetBoost_'+WTAG+'_nom_eta'
    }
    aliases['AddJet_pt']={
        'expr':'AddJetBoost_'+WTAG+'_nom_pt'
    }

    aliases['LeadingAddJet_BtagScore']={
        'expr':'Jet_btagDeepB[CleanJet_jetIdx[AddJetBoost_'+WTAG+'_nom_cjidx[0]]]'
    }
    aliases['LeadingAddJet_eta']={
        'expr':'AddJetBoost_'+WTAG+'_nom_eta[0]'
    }
    aliases['LeadingAddJet_pt']={
        'expr':'AddJetBoost_'+WTAG+'_nom_pt[0]'
    }


    aliases['SubLeadingAddJet_BtagScore']={
        'expr':'Jet_btagDeepB[CleanJet_jetIdx[AddJetBoost_'+WTAG+'_nom_cjidx[1]]]'
    }
    aliases['SubLeadingAddJet_eta']={
        'expr':'AddJetBoost_'+WTAG+'_nom_eta[1]'
    }
    aliases['SubLeadingAddJet_pt']={
        'expr':'AddJetBoost_'+WTAG+'_nom_pt[1]'
    }


if Resolved:
    aliases['AddJet_BtagScore']={
        'expr':'Jet_btagDeepB[CleanJet_jetIdx[AddJetResol_'+ALGO+'_nom_cjidx]]'
    }
    aliases['nAddJet']={
        'expr':"Sum$(AddJetResol_dMchi2Resolution_nom_cjidx>=0)"
    }
    aliases['AddJet_eta']={
        'expr':'AddJetResol_'+ALGO+'_nom_eta'
    }
    aliases['AddJet_pt']={
        'expr':'AddJetResol_'+ALGO+'_nom_pt'
    }

    aliases['LeadingAddJet_BtagScore']={
        'expr':'Jet_btagDeepB[CleanJet_jetIdx[AddJetResol_'+ALGO+'_nom_cjidx[0]]]'
    }
    aliases['LeadingAddJet_eta']={
        'expr':'AddJetResol_'+ALGO+'_nom_eta[0]'
    }
    aliases['LeadingAddJet_pt']={
        'expr':'AddJetResol_'+ALGO+'_nom_pt[0]'
    }


    aliases['SubLeadingAddJet_BtagScore']={
        'expr':'Jet_btagDeepB[CleanJet_jetIdx[AddJetResol_'+ALGO+'_nom_cjidx[1]]]'
    }
    aliases['SubLeadingAddJet_eta']={
        'expr':'AddJetResol_'+ALGO+'_nom_eta[1]'
    }
    aliases['SubLeadingAddJet_pt']={
        'expr':'AddJetResol_'+ALGO+'_nom_pt[1]'
    }


##--Hadronic W--##

if Boosted:
    ##--Hadronic W--##
    aliases['HadronicW_mass']={
        'expr':'WtaggerFatjet_'+WTAG+'_nom_mass[lnJ_'+WTAG+'_nom_widx]'
    }
    aliases['HadronicW_pt']={
        'expr':'WtaggerFatjet_'+WTAG+'_nom_pt[lnJ_'+WTAG+'_nom_widx]'
    }
    aliases['HadronicW_Score']={}
    if 'HP' in WTAG:
        aliases['HadronicW_Score']['expr']='WtaggerFatjet_'+WTAG+'_nom_tau21ddt[lnJ_'+WTAG+'_nom_widx]'
    if 'DeepAK8' in WTAG:
        if not 'MD' in WTAG:
            aliases['HadronicW_Score']['expr']='WtaggerFatjet_'+WTAG+'_nom_deepTag[lnJ_'+WTAG+'_nom_widx]'
        else:
            aliases['HadronicW_Score']['expr']='WtaggerFatjet_'+WTAG+'_nom_deepTagMD[lnJ_'+WTAG+'_nom_widx]'

if Resolved:
    aliases['HadronicW_mass']={
        'expr':'Whad'+_ALGO_+'nom_mass'
    }
    aliases['HadronicW_pt']={
        'expr':'Whad'+_ALGO_+'nom_pt'
    }
    aliases['HadronicW_Score']={}
    aliases['HadronicW_Score']['expr']='Whad'+_ALGO_+'nom_ScoreToLeast'

##---PTSUM
if Boosted:
    aliases['CandSumPt']={
        'expr':'Boost_CandSumPt_'+WTAG+'_nom'
    }
if Resolved:
    aliases['CandSumPt']={
        'expr':'Resol_CandSumPt_'+ALGO+'_nom'
    }
##--WW--##
if Boosted:
    aliases['WW_mass']={
        'expr':'lnJ_'+WTAG+'_nom_mass'
    }
    aliases['WW_pt']={
        'expr':'lnJ_'+WTAG+'_nom_pt'
    }
    aliases['WW_pt_over_mass']={
        'expr':'lnJ_'+WTAG+'_nom_minPtWOverM'
    }
    aliases['WW_maxpt_over_mass']={
        'expr':'lnJ_'+WTAG+'_nom_maxPtWOverM'
    }
    aliases['WW_MET_over_mass']={
        'expr':METtype+'_nom_pt/lnJ_'+WTAG+'_nom_mass'
    }

    aliases['WW_Whadpt_over_mass']={
        'expr':'WtaggerFatjet_'+WTAG+'_nom_pt[lnJ_'+WTAG+'_nom_widx]/lnJ_'+WTAG+'_nom_mass'
    }
    aliases['WW_Wleppt_over_mass']={
        'expr':'Wlep_nom_pt/lnJ_'+WTAG+'_nom_mass'
    }
    aliases['WW_dPhi']={
        #'expr':' ((isBoost_'+WTAG+'_nom)&&(lnJ_'+WTAG+'_nom_widx >=0)) ? (WtaggerFatjet_'+WTAG+'_nom_phi[lnJ_'+WTAG+'_nom_widx]-Wlep_nom_phi)-2*3.1415927*(  (WtaggerFatjet_'+WTAG+'_nom_phi[lnJ_'+WTAG+'_nom_widx]-Wlep_nom_phi) > 3.1415927) + 2*3.1415927*((WtaggerFatjet_'+WTAG+'_nom_phi[lnJ_'+WTAG+'_nom_widx]-Wlep_nom_phi) < 3.1415927) : -100.'                                                                                                                                  
        #'expr':' ((isBoost_'+WTAG+'_nom)&&(lnJ_'+WTAG+'_nom_widx >=0)) ? \
        #dPhiVBF(   WtaggerFatjet_'+WTAG+'_nom_pt[lnJ_'+WTAG+'_nom_widx] , WtaggerFatjet_'+WTAG+'_nom_eta[lnJ_'+WTAG+'_nom_widx], WtaggerFatjet_'+WTAG+'_nom_phi[lnJ_'+WTAG+'_nom_widx], WtaggerFatjet_'+WTAG+'_nom_mass[lnJ_'+WTAG+'_nom_widx],\
        #Wlep_nom_pt, Wlep_nom_eta, Wlep_nom_phi, Wlep_nom_mass,\
        #0,0,0,0,\
        #0,0,0,0)\
        #: -999.'
        'expr':' ((isBoost_'+WTAG+'_nom)&&(lnJ_'+WTAG+'_nom_widx >=0)) ? \
        fabs(WtaggerFatjet_'+WTAG+'_nom_phi[lnJ_'+WTAG+'_nom_widx]-Wlep_nom_phi)*( fabs(WtaggerFatjet_'+WTAG+'_nom_phi[lnJ_'+WTAG+'_nom_widx]-Wlep_nom_phi) < TMath::Pi()   )\
        +(2*TMath::Pi() - fabs(WtaggerFatjet_'+WTAG+'_nom_phi[lnJ_'+WTAG+'_nom_widx]-Wlep_nom_phi))*(fabs(WtaggerFatjet_'+WTAG+'_nom_phi[lnJ_'+WTAG+'_nom_widx]-Wlep_nom_phi)>=TMath::Pi())\
         : -999'
    }#dPhiVBF


    #aliases['WW_dPhi_VBF']={
        #'expr':' ((isBoost_'+WTAG+'_nom)&&(lnJ_'+WTAG+'_nom_widx >=0)) ? (WtaggerFatjet_'+WTAG+'_nom_phi[lnJ_'+WTAG+'_nom_widx]-Wlep_nom_phi)-2*3.1415927*(  (WtaggerFatjet_'+WTAG+'_nom_phi[lnJ_'+WTAG+'_nom_widx]-Wlep_nom_phi) > 3.1415927) + 2*3.1415927*((WtaggerFatjet_'+WTAG+'_nom_phi[lnJ_'+WTAG+'_nom_widx]-Wlep_nom_phi) < 3.1415927) : -100.'                                                                                                                                  
       # 'expr':' ((isBoost_'+WTAG+'_nom)&&(lnJ_'+WTAG+'_nom_widx >=0)&&(isVBF_Boost_'+WTAG+'_nom)&&(VBFjjBoost_cjidx1_'+WTAG+'_nom >= 0 )&&(VBFjjBoost_cjidx2_'+WTAG+'_nom>=0)) ? \
       # dPhiVBF(   WtaggerFatjet_'+WTAG+'_nom_pt[lnJ_'+WTAG+'_nom_widx] , WtaggerFatjet_'+WTAG+'_nom_eta[lnJ_'+WTAG+'_nom_widx], WtaggerFatjet_'+WTAG+'_nom_phi[lnJ_'+WTAG+'_nom_widx], WtaggerFatjet_'+WTAG+'_nom_mass[lnJ_'+WTAG+'_nom_widx],\
       # Wlep_nom_pt, Wlep_nom_eta, Wlep_nom_phi, Wlep_nom_mass,\
       # Jet_pt_nom[CleanJet_jetIdx[VBFjjBoost_cjidx1_'+WTAG+'_nom]],Jet_eta[CleanJet_jetIdx[VBFjjBoost_cjidx1_'+WTAG+'_nom]],Jet_phi[CleanJet_jetIdx[VBFjjBoost_cjidx1_'+WTAG+'_nom]],Jet_mass[CleanJet_jetIdx[VBFjjBoost_cjidx1_'+WTAG+'_nom]],\
       # Jet_pt_nom[CleanJet_jetIdx[VBFjjBoost_cjidx2_'+WTAG+'_nom]],Jet_eta[CleanJet_jetIdx[VBFjjBoost_cjidx2_'+WTAG+'_nom]],Jet_phi[CleanJet_jetIdx[VBFjjBoost_cjidx2_'+WTAG+'_nom]],Jet_mass[CleanJet_jetIdx[VBFjjBoost_cjidx2_'+WTAG+'_nom]])\
       # : -999.'
    #}#dPhiVBF
#VBFjjBoost_cjidx1_'+WTAG+'_nom

if Resolved:
    aliases['WW_mass']={
        'expr':'lnjj_'+ALGO+'_nom_mass'
    }
    aliases['WW_pt']={
        'expr':'lnjj_'+ALGO+'_nom_pt'
    }
    aliases['WW_pt_over_mass']={
        'expr':'lnjj_'+ALGO+'_nom_minPtWOverM'
    }
    aliases['WW_maxpt_over_mass']={
        'expr':'lnjj_'+ALGO+'_nom_maxPtWOverM'
    }
    aliases['WW_Mt']={
        'expr':'lnjj'+_ALGO_+'nom_Mt'
    }
    aliases['WW_MET_over_mass']={
        'expr':METtype+'_nom_pt/lnjj_'+ALGO+'_nom_mass'
    }

    aliases['WW_Whadpt_over_mass']={
        'expr':'Whad'+_ALGO_+'nom_pt/lnjj_'+ALGO+'_nom_mass'
    }
    aliases['WW_Wleppt_over_mass']={
        'expr':'Wlep_nom_pt/lnjj_'+ALGO+'_nom_mass'
    }
    #aliases['WW_dPhi_VBF']={
        #'expr':' ((isBoost_'+WTAG+'_nom)&&(lnJ_'+WTAG+'_nom_widx >=0)) ? (WtaggerFatjet_'+WTAG+'_nom_phi[lnJ_'+WTAG+'_nom_widx]-Wlep_nom_phi)-2*3.1415927*(  (WtaggerFatjet_'+WTAG+'_nom_phi[lnJ_'+WTAG+'_nom_widx]-Wlep_nom_phi) > 3.1415927) + 2*3.1415927*((WtaggerFatjet_'+WTAG+'_nom_phi[lnJ_'+WTAG+'_nom_widx]-Wlep_nom_phi) < 3.1415927) : -100.'                                                                                                                                  
        #'expr':' (VBFjjResol_cjidx1_'+ALGO+'_nom >=0 && VBFjjResol_cjidx2_'+ALGO+'_nom >=0 && isVBF_Resol'+_ALGO_+'nom)  ?\
        #dPhiVBF(   Whad'+_ALGO_+'nom_pt, Whad'+_ALGO_+'nom_eta,Whad'+_ALGO_+'nom_phi,Whad'+_ALGO_+'nom_mass,\
        #Wlep_nom_pt, Wlep_nom_eta, Wlep_nom_phi, Wlep_nom_mass,\
        #Jet_pt_nom[CleanJet_jetIdx[VBFjjResol_cjidx1_'+ALGO+'_nom]],Jet_eta[CleanJet_jetIdx[VBFjjResol_cjidx1_'+ALGO+'_nom]],Jet_phi[CleanJet_jetIdx[VBFjjResol_cjidx1_'+ALGO+'_nom]],Jet_mass[CleanJet_jetIdx[VBFjjResol_cjidx1_'+ALGO+'_nom]],\
        #Jet_pt_nom[CleanJet_jetIdx[VBFjjResol_cjidx2_'+ALGO+'_nom]],Jet_eta[CleanJet_jetIdx[VBFjjResol_cjidx2_'+ALGO+'_nom]],Jet_phi[CleanJet_jetIdx[VBFjjResol_cjidx2_'+ALGO+'_nom]],Jet_mass[CleanJet_jetIdx[VBFjjResol_cjidx2_'+ALGO+'_nom]]) : -999'
    #}

    aliases['WW_dPhi']={
        #'expr':' ((isBoost_'+WTAG+'_nom)&&(lnJ_'+WTAG+'_nom_widx >=0)) ? (WtaggerFatjet_'+WTAG+'_nom_phi[lnJ_'+WTAG+'_nom_widx]-Wlep_nom_phi)-2*3.1415927*(  (WtaggerFatjet_'+WTAG+'_nom_phi[lnJ_'+WTAG+'_nom_widx]-Wlep_nom_phi) > 3.1415927) + 2*3.1415927*((WtaggerFatjet_'+WTAG+'_nom_phi[lnJ_'+WTAG+'_nom_widx]-Wlep_nom_phi) < 3.1415927) : -100.'                                                                                                                                  
        #'expr':' dPhiVBF(   Whad'+_ALGO_+'nom_pt,Whad'+_ALGO_+'nom_eta,Whad'+_ALGO_+'nom_phi,Whad'+_ALGO_+'nom_mass,\
        #Wlep_nom_pt, Wlep_nom_eta, Wlep_nom_phi, Wlep_nom_mass,\
        #0,0,0,0,\
        #0,0,0,0)'
        'expr':'fabs(Whad'+_ALGO_+'nom_phi - Wlep_nom_phi)*( fabs(Whad'+_ALGO_+'nom_phi - Wlep_nom_phi) < TMath::Pi()  )\
        +(2*TMath::Pi()-fabs(Whad'+_ALGO_+'nom_phi - Wlep_nom_phi))*(fabs(Whad'+_ALGO_+'nom_phi - Wlep_nom_phi) >= TMath::Pi())\
        '

    }

aliases['raw_nbjet']={
    'expr':'Sum$(Jet_pt_nom[CleanJet_jetIdx]>20 && abs(CleanJet_eta)<2.5 && Jet_btagDeepB[CleanJet_jetIdx]>'+bWP+')'
}

##--VBF--
if Boosted:
    aliases['maxmjj_mass_jj_VBF']={
        'expr':'max_mjj_Boost_'+WTAG+'_nom'
    }
    aliases['maxmjj_dEta_jj_VBF']={
        'expr':'dEta_of_max_mjj_Boost_'+WTAG+'_nom'
    }




    aliases['mass_jj_VBF']={
        'expr':'VBFjjBoost_mjj_'+WTAG+'_nom'
    }

    aliases['dEta_jj_VBF']={
        'expr':'VBFjjBoost_dEta_'+WTAG+'_nom'
    }

    aliases['VBFj1_eta']={
        'expr':'VBFjjBoost_cjidx1_'+WTAG+'_nom >= 0 ? CleanJet_eta[VBFjjBoost_cjidx1_'+WTAG+'_nom] : -100'
    }    

    aliases['VBFj2_eta']={
        'expr':'VBFjjBoost_cjidx2_'+WTAG+'_nom >= 0 ? CleanJet_eta[VBFjjBoost_cjidx2_'+WTAG+'_nom] : -100'
    }    



if Resolved:
    aliases['maxmjj_mass_jj_VBF']={
        'expr':'max_mjj_Resol_'+ALGO+'_nom'
    }
    aliases['maxmjj_dEta_jj_VBF']={
        'expr':'dEta_of_max_mjj_Resol_'+ALGO+'_nom'
    }

    aliases['mass_jj_VBF']={
        'expr':'VBFjjResol_mjj_'+ALGO+'_nom'
    }
    aliases['dEta_jj_VBF']={
        'expr':'VBFjjResol_dEta_'+ALGO+'_nom'
    }

    aliases['VBFj1_eta']={
        'expr':'VBFjjResol_cjidx1_'+ALGO+'_nom >= 0 ? CleanJet_eta[VBFjjResol_cjidx1_'+ALGO+'_nom] : -100'
    }    
    aliases['VBFj2_eta']={
        'expr':'VBFjjResol_cjidx2_'+ALGO+'_nom >= 0 ? CleanJet_eta[VBFjjResol_cjidx2_'+ALGO+'_nom] : -100'
    }    



##----reweight
if Resolved:
    slope=DICT_MjjShapeW[Year]['Resolved']['slope']
    intercept=DICT_MjjShapeW[Year]['Resolved']['intercept']
    aliases['MjjShape']={
        'expr':'HadronicW_mass > 0 ? '+str(intercept)+'+'+str(slope)+'*HadronicW_mass : 0'
    }
if Boosted:
    aliases['MjjShape']={
        'expr':'1'
    }

#aliases['MjjShapeMin']={ ##normalize factor
#    'expr':'wmass > 0 ? '+intercept+' : 0'
#}
##----if not reweight (if you don't want it or to measure fitting param)
if not MjjShapeCorr:
    aliases['MjjShape']={
        'expr':'1'
    }
