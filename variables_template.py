
if not 'cuts' in vars():
    cuts={}
variables={}


#ListNotDraw=['SubLeadingJet_pt','SubLeadingJet_BtagScore','SubLeadingJet_eta','SubLeadingAddJet_BtagScore','SubLeadingAddJet_pt','SubLeadingAddJet_eta']
ListNotDraw=[]






import os
import sys
sys.path.append(os.getcwd())


#-----Variable Deinition-----#
from WPandCut2016 import *



if 'opt' in globals():
    configration_py=opt.variablesFile
else:
    configration_py=sys.argv[0]
print "configration_py=",configration_py

cut_GGF=[] ##--not use mela
cut_GGF0=[]
cut_GGF1=[]
cut_VBF=[] ##--no use mela
cut_VBF0=[]
cut_VBF1=[]


cut_GGFDNN=[] ##--not use mela
cut_GGFDNN0=[]
cut_GGFDNN1=[]
cut_VBFDNN=[] ##--no use mela
cut_VBFDNN0=[]
cut_VBFDNN1=[]
cut_Others=[]


for c in cuts:
    if 'DNN' in c:
        if 'GGF' in c:
            if 'MEKDTAG' in c:
                cut_GGFDNN0.append(c)
            elif 'UNTAGGED' in c:
                cut_GGFDNN1.append(c)
            elif 'NoMEKDCut' in c:
                cut_GGFDNN.append(c)
            else:
                cut_Others.append(c)
        elif 'VBF' in c:
            if 'MEKDTAG' in c:
                cut_VBFDNN0.append(c)
            elif 'UNTAGGED' in c:
                cut_VBFDNN1.append(c)
            elif 'NoMEKDCut' in c:
                cut_VBFDNN.append(c)
            else:
                cut_Others.append(c)
        else:
            cut_Others.append(c)
    else:
        if 'GGF' in c:
            if 'MEKDTAG' in c:
                cut_GGF0.append(c)
            elif 'UNTAGGED' in c:
                cut_GGF1.append(c)
            elif 'NoMEKDCut' in c:
                cut_GGF.append(c)
            else:
                cut_Others.append(c)
        elif 'VBF' in c:
            if 'MEKDTAG' in c:
                cut_VBF0.append(c)
            elif 'UNTAGGED' in c:
                cut_VBF1.append(c)
            elif 'NoMEKDCut' in c:
                cut_VBF.append(c)
            else:
                cut_Others.append(c)
        else:
            cut_Others.append(c)


Boosted=False
Resolved=False
ForDatacard=False
if 'Datacard' in configration_py:
    ForDatacard=True
if 'Boosted' in configration_py:
    Boosted=True
if 'Resolved' in configration_py:
    Resolved=True
#scriptname=opt.variablesFile

#------End of Variable Definition-----#
#variables={}

#variables['lnJ_DeepAK8WP0p5_nom_widx'] = {
#    'name' : 'lnJ_DeepAK8WP0p5_nom_widx',
#    'range':(3,0,3),
#    'xaxis':'lnJ_DeepAK8WP0p5_nom_widx',
#    'fold': 3,
#}


variables['Event'] = {
    'name' : '1',
    'range':(1,0,2),
    'xaxis':'1',
    'fold': 3,
}


variables['DeepAKScore'] = {
    'name' : '"TMath::Max(0,Max$(FatJet_deepTag_WvsQCD))"',
    'range':(100,0,1),
    'xaxis':'DeepAK8 Score',
    'fold': 3,
}
##Wtagger kin##

variables['HadronicW_pt']={
    'name':'HadronicW_pt',
    #'range':(100,0,1000),
    'range':([0,200,230,260,290,320,350,380,600,800,1000],),
    'xaxis':'P_{T}(Hadronic W boson) [GeV]',
    'divideByBinWidth':1,
    'fold': 3,

}
if Resolved:
    variables['HadronicW_pt']['range']=([0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,230,260,290,320,350,380,410,500,700,1000],)

variables['HadronicW_mass']={
    'name':'HadronicW_mass',
    'range':([40,45,50,55,65,70,75,80,85,90,95,100,105,110,115,120,125,130,150,170,200,250],),
    'divideByBinWidth':1,
    'xaxis':'M(Hadronic W boson) [GeV]',
    'fold': 3,
}

variables['HadronicW_mass_zoom']={
    'name':'HadronicW_mass',
    'range':(8,65,105) ,

    'xaxis':'M(Hadronic W boson) [GeV]',
    'fold': 3,
}

##Change range of Wmass -> SR/TOP : Wmass 65-105
#if ('TOP' in configration_py) or ('SR' in configration_py) :
#    variables['HadronicW_mass']['range']=(8,65,105)



variables['HadronicW_Score']={
    'name':'HadronicW_Score',
    'range':(20,0,1),
    'xaxis':'HadronicW_Score',
    'fold': 3,
    
}
if Boosted:
    if 'HP' in WTAG:
        variables['HadronicW_Score']['xaxis']='#tau_{21}'
    if 'DDT' in WTAG:
        variables['HadronicW_Score']['xaxis']+='(DDT)'
    if 'DeepAK8' in WTAG:
        variables['HadronicW_Score']['xaxis']='deepTagAK8'
            
if Resolved:
    variables['HadronicW_Score']['xaxis']='#chi^{2}'
    if 'chi2' in ALGO :
        variables['HadronicW_Score']['range']=(40,0,200)
    else:
        variables['HadronicW_Score']['range']=(40,0,40)
##--nBjet

variables['nBJet']={
    'name':'nBJet',
    'range':(5,0,5),
    'xaxis':'number of btagged AK4 Jet, out of Whad',
    'fold':3,
}
#raw_nbjet
variables['nBJet_raw']={
    'name':'raw_nbjet',
    'range':(5,0,5),
    'xaxis':'number of btagged AK4 Jet',
    'fold':3,
}



##--ak4jet
#variables['nAK4Jet']={
#    'name':'nAK4Jet',
#    'range':(10,0,10),
#    'xaxis':'number of AK4 Jet',
#    'fold':3,
#}
#variables['nAK4Jet_eta4p7']={
#    'name':'nAK4Jet_eta4p7',
#    'range':(10,0,10),
#    'xaxis':'number of AK4 Jet',
#    'fold':3,
#}
##--leading ak4jet
'''
variables['LeadingJet_pt']={
    'name':'LeadingJet_pt',
    'range':(100,25,300),
    'xaxis':'P_{T}(Leading AK4 Jet) [GeV]',
    'fold':3,
}
variables['LeadingJet_eta']={
    'name':'LeadingJet_eta',
    'range':(30,-5,5),
    'xaxis':'#eta(Leading AK4 Jet)',
    'fold':3,
}
variables['LeadingJet_BtagScore']={
    'name':'LeadingJet_BtagScore',
    'range':(20,0,1),
    'xaxis':bAlgo+'(Leading AK4 Jet)',
    'fold':3,
}
##--subleading ak4jets
variables['SubLeadingJet_pt']={
    'name':'SubLeadingJet_pt',
    'range':(100,25,300),
    'xaxis':'P_{T}(SubLeading AK4 Jet) [GeV]',
    'fold':3,
}
variables['SubLeadingJet_eta']={
    'name':'SubLeadingJet_eta',
    'range':(30,-5,5),
    'xaxis':'#eta(SubLeading AK4 Jet)',
    'fold':3,
}
variables['SubLeadingJet_BtagScore']={
    'name':'SubLeadingJet_BtagScore',
    'range':(20,0,1),
    'xaxis':bAlgo+'(SubLeading AK4 Jet)',
    'fold':3,
}


##---ak4jet not in Wtag
variables['nAddJet']={
    'name':'nAddJet',
    'range':(10,0,10),
    'xaxis':'number of AK4 Jet Not Wtagged',
    'fold':3,
}
'''
variables['AddJet_pt']={
    'name':'AddJet_pt',
    'range':(100,20,300),
    'xaxis':'P_{T}(AK4 Jet Not Wtagged) [GeV]',
    'fold':3,
}
variables['AddJet_eta']={
    'name':'AddJet_eta',
    'range':(30,-5,5),
    'xaxis':'#eta(AK4 Jet Not Wtagged)',
    'fold':3,
}
'''
variables['AddJet_BtagScore']={
    'name':'AddJet_BtagScore',
    'range':(20,0,1),
    'xaxis':bAlgo+'(AK4 Jet Not Wtagged)',
    'fold':3,
}

##--Leading addjet
variables['LeadingAddJet_pt']={
    'name':'LeadingAddJet_pt',
    'range':(100,20,300),
    'xaxis':'P_{T}(1st AK4 Jet Not Wtagged) [GeV]',
    'fold':3,
}
variables['LeadingAddJet_eta']={
    'name':'LeadingAddJet_eta',
    'range':(30,-5,5),
    'xaxis':'#eta(1st AK4 Jet Not Wtagged)',
    'fold':3,
}
variables['LeadingAddJet_BtagScore']={
    'name':'LeadingAddJet_BtagScore',
    'range':(20,0,1),
    'xaxis':bAlgo+'(1stAK4 Jet Not Wtagged)',
    'fold':3,
}
##--Subleading addjet
variables['SubLeadingAddJet_pt']={
    'name':'SubLeadingAddJet_pt',
    'range':(100,20,600),
    'xaxis':'P_{T}(2nd AK4 Jet Not Wtagged) [GeV]',
    'fold':3,
}
variables['SubLeadingAddJet_eta']={
    'name':'SubLeadingAddJet_eta',
    'range':(30,-5,5),
    'xaxis':'#eta(2nd AK4 Jet Not Wtagged)',
    'fold':3,
}
variables['SubLeadingAddJet_BtagScore']={
    'name':'SubLeadingAddJet_BtagScore',
    'range':(20,0,1),
    'xaxis':bAlgo+'(2nd AK4 Jet Not Wtagged)',
    'fold':3,
}
'''

##--Lepton
variables['Lepton_pt[0]']={
    'name' : 'Lepton_pt[0]',
    'range':(20,25,600),
    'xaxis':'P_{T}(Lepton) [GeV]',
    'fold':3

}
variables['Lepton_eta[0]']={
    'name' : 'Lepton_eta[0]',
    'range':(30,-5,5),
    'xaxis':'#eta(Lepton)',
    'fold':3
}




##--MET


variables[METtype]={
    'name' : METtype+'_nom_pt',
    'range':(30,0,600),
    'xaxis':METtype+' [GeV]',
    'fold':3
}


##--Leptonic W
variables['Wlep_Mt']={
    'name' : 'Wlep_nom_Mt',
    'range':(20,0,200),
    'xaxis':'M_{T}(LeptonicW) [GeV]',
    'fold':3
}

variables['Wlep_nom_pt']={
    'name' : 'Wlep_nom_pt',
    'range':(47,30,500),
    'xaxis':'P_{T}(LeptonicW) [GeV]',
    'fold':3
}

variables['Wlep_nom_mass']={
    'name' : 'Wlep_nom_mass',
    'range':(10,70,90),
    'xaxis':'M(LeptonicW) [GeV]',
    'fold':3
}

##-nPV
variables ['PV_npvs']={
    'name' : 'PV_npvs',
    'range' : (80,0,80),
    'xaxis' : 'PV_npvs',
    'fold':0
}

##--WW
variables['WW_pt_over_mass']={
    'name':'WW_pt_over_mass',
    'range':(40,0,1),
    'xaxis':'min(P_{T}(W)/M(WW))',
    'fold':0
}
variables['WW_pt']={
    'name':'WW_pt',
    'range':(80,0,800),
    'xaxis':'P_${T}(WW))',
    'fold':0
}
'''
variables['WW_maxpt_over_mass']={
    'name':'WW_maxpt_over_mass',
    'range':(80,0,2),
    'xaxis':'max(P_{T}(W)/M(WW))',
    'fold':0
}
'''


variables['WW_mass']={
    'name': 'WW_mass',

    'range':(
        [0,300,
         400,
         500,
         600,
         700,
         800,
         900,
         1000,
         1100,
         1200,
         1400,
         2000,
         4000,
     ],),
    
    'divideByBinWidth':1,
    

    'xaxis': 'M(WW) [GeV]',
    'fold':3
}
if Boosted:
    ##--cutbased
    variables['WW_mass_GGF0']={
        'name': 'WW_mass',
        'range':([0.0, 820.0, 910.0, 920.0, 970.0, 1020.0, 1120.0, 1210.0, 1260.0, 1400.0, 1530.0, 1560.0, 1760.0, 1860.0, 4000.0]
                 ,),
        'divideByBinWidth':1,
        'xaxis': 'M(WW) [GeV]',
        'fold':3,
        'cuts':cut_GGF0,
    }
    if Year=='2017': variables['WW_mass_GGF0']['range']=([0.0, 750.0, 800.0, 920.0, 980.0, 1110.0, 1180.0, 1290.0, 1320.0, 1440.0, 1740.0, 1810.0, 1940.0, 2090.0, 2290.0, 4000.0],)
    if Year=='2018': variables['WW_mass_GGF0']['range']=([0.0, 700.0, 740.0, 760.0, 910.0, 920.0, 930.0, 940.0, 950.0, 960.0, 1000.0, 1060.0, 1070.0, 1080.0, 1120.0, 1180.0, 1190.0, 1200.0, 1290.0, 1350.0, 1360.0, 1390.0, 1410.0, 1420.0, 1580.0, 1590.0, 1920.0, 1990.0, 4000.0],)



    variables['WW_mass_VBF']={
        'name': 'WW_mass',
        'range':([0.0, 240.0, 270.0, 320.0, 350.0, 360.0, 410.0, 440.0, 480.0, 500.0, 520.0, 550.0, 570.0, 590.0, 600.0, 620.0, 660.0, 710.0, 740.0, 770.0, 860.0, 1020.0, 1080.0, 2630.0, 4000.0]
                 ,),
        'divideByBinWidth':1,
        'xaxis': 'M(WW) [GeV]',
        'fold':3,
        'cuts':cut_VBF,
    }
    if Year=='2017': variables['WW_mass_VBF']['range']=([0.0, 210.0, 220.0, 230.0, 280.0, 290.0, 310.0, 370.0, 380.0, 390.0, 400.0, 420.0, 430.0, 440.0, 460.0, 490.0, 520.0, 530.0, 550.0, 560.0, 570.0, 590.0, 600.0, 620.0, 630.0, 640.0, 650.0, 670.0, 740.0, 820.0, 870.0, 900.0, 1330.0, 1510.0, 4000.0],)
    if Year=='2018': variables['WW_mass_VBF']['range']=([0.0, 210.0, 220.0, 230.0, 240.0, 290.0, 300.0, 310.0, 340.0, 350.0, 390.0, 400.0, 420.0, 430.0, 460.0, 480.0, 500.0, 510.0, 530.0, 540.0, 550.0, 580.0, 590.0, 600.0, 610.0, 620.0, 630.0, 640.0, 650.0, 660.0, 670.0, 700.0, 710.0, 770.0, 780.0, 870.0, 890.0, 1190.0, 1230.0, 1420.0, 1910.0, 4000.0],)



    variables['WW_mass_GGF1']={
        'name': 'WW_mass',
        'range':([0.0, 210.0, 250.0, 260.0, 280.0, 300.0, 320.0, 330.0, 340.0, 370.0, 390.0, 400.0, 410.0, 420.0, 430.0, 440.0, 450.0, 460.0, 470.0, 480.0, 490.0, 500.0, 510.0, 520.0, 530.0, 540.0, 550.0, 560.0, 570.0, 580.0, 590.0, 600.0, 610.0, 620.0, 630.0, 640.0, 650.0, 660.0, 670.0, 680.0, 690.0, 700.0, 710.0, 720.0, 730.0, 740.0, 750.0, 760.0, 770.0, 780.0, 790.0, 800.0, 810.0, 820.0, 830.0, 840.0, 850.0, 860.0, 870.0, 880.0, 890.0, 900.0, 910.0, 920.0, 930.0, 950.0, 970.0, 990.0, 1020.0, 1030.0, 1040.0, 1060.0, 1110.0, 1150.0, 1290.0, 1320.0, 4000.0]
        ,),
    'divideByBinWidth':1,
    'xaxis': 'M(WW) [GeV]',
    'fold':3,
    'cuts':cut_GGF1,
    }
    if Year=='2017': variables['WW_mass_GGF1']['range']=([0.0, 200.0, 220.0, 240.0, 260.0, 280.0, 300.0, 320.0, 340.0, 360.0, 380.0, 390.0, 400.0, 410.0, 420.0, 430.0, 440.0, 450.0, 460.0, 470.0, 480.0, 490.0, 500.0, 510.0, 520.0, 530.0, 540.0, 550.0, 560.0, 570.0, 580.0, 590.0, 600.0, 610.0, 620.0, 630.0, 640.0, 650.0, 660.0, 670.0, 680.0, 690.0, 700.0, 710.0, 720.0, 730.0, 740.0, 750.0, 760.0, 770.0, 780.0, 790.0, 800.0, 810.0, 820.0, 830.0, 840.0, 850.0, 860.0, 870.0, 880.0, 890.0, 900.0, 920.0, 940.0, 960.0, 970.0, 980.0, 1000.0, 1030.0, 1070.0, 1080.0, 1100.0, 1110.0, 1170.0, 1180.0, 1300.0, 1400.0, 4000.0],)
    if Year=='2018': variables['WW_mass_GGF1']['range']=([0.0, 200.0, 220.0, 230.0, 240.0, 250.0, 260.0, 270.0, 280.0, 290.0, 300.0, 310.0, 320.0, 330.0, 340.0, 350.0, 360.0, 370.0, 380.0, 390.0, 400.0, 410.0, 420.0, 430.0, 440.0, 450.0, 460.0, 470.0, 480.0, 490.0, 500.0, 510.0, 520.0, 530.0, 540.0, 550.0, 560.0, 570.0, 580.0, 590.0, 600.0, 610.0, 620.0, 630.0, 640.0, 650.0, 660.0, 670.0, 680.0, 690.0, 700.0, 710.0, 720.0, 730.0, 740.0, 750.0, 760.0, 770.0, 780.0, 790.0, 800.0, 810.0, 820.0, 830.0, 840.0, 850.0, 860.0, 870.0, 880.0, 890.0, 900.0, 910.0, 920.0, 930.0, 940.0, 950.0, 960.0, 970.0, 990.0, 1010.0, 1030.0, 1040.0, 1080.0, 1100.0, 1160.0, 1170.0, 1180.0, 1240.0, 1260.0, 1470.0, 1580.0, 1840.0, 2770.0, 4000.0],)

    ##--dnn
    variables['WW_mass_GGFDNN0']={
        'name': 'WW_mass',
        'range':([0.0, 820.0, 920.0, 970.0, 1020.0, 1120.0, 1210.0, 1260.0, 1380.0, 1400.0, 1590.0, 1860.0, 4000.0]
                 ,),
        'divideByBinWidth':1,
        'xaxis': 'M(WW) [GeV]',
        'fold':3,
        'cuts':cut_GGFDNN0,
    }
    if Year=='2017': variables['WW_mass_GGFDNN0']['range']=([0.0, 750.0, 800.0, 890.0, 970.0, 1090.0, 1190.0, 1270.0, 1290.0, 1320.0, 1430.0, 1670.0, 1740.0, 1810.0, 1950.0, 2150.0, 2520.0, 4000.0],)
    if Year=='2018': variables['WW_mass_GGF1']['range']=([0.0, 700.0, 740.0, 760.0, 900.0, 910.0, 920.0, 930.0, 940.0, 950.0, 960.0, 1000.0, 1060.0, 1070.0, 1080.0, 1120.0, 1180.0, 1190.0, 1200.0, 1290.0, 1340.0, 1350.0, 1360.0, 1390.0, 1410.0, 1420.0, 1580.0, 1590.0, 1930.0, 1990.0, 4000.0],)


    variables['WW_mass_VBFDNN']={
        'name': 'WW_mass',
        'range':([0.0, 280.0, 400.0, 520.0, 550.0, 580.0, 590.0, 620.0, 660.0, 770.0, 950.0, 4000.0]
                 ,),
        'divideByBinWidth':1,
        'xaxis': 'M(WW) [GeV]',
        'fold':3,
        'cuts':cut_VBFDNN,
    }
    if Year=='2017': variables['WW_mass_VBFDNN']['range']=([0.0, 290.0, 320.0, 430.0, 490.0, 520.0, 530.0, 540.0, 570.0, 610.0, 620.0, 670.0, 840.0, 880.0, 4000.0],)
    if Year=='2018': variables['WW_mass_VBFDNN']['range']=([0.0, 200.0, 310.0, 390.0, 400.0, 470.0, 500.0, 530.0, 540.0, 550.0, 560.0, 590.0, 630.0, 640.0, 650.0, 660.0, 670.0, 760.0, 780.0, 1020.0, 1070.0, 1150.0, 1260.0, 1360.0, 1500.0, 1880.0, 2420.0, 4000.0],)


    variables['WW_mass_GGFDNN1']={
        'name': 'WW_mass',
        'range':([0.0, 200.0, 220.0, 250.0, 260.0, 270.0, 290.0, 310.0, 330.0, 340.0, 370.0, 390.0, 400.0, 410.0, 420.0, 430.0, 440.0, 450.0, 460.0, 470.0, 480.0, 490.0, 500.0, 510.0, 520.0, 530.0, 540.0, 550.0, 560.0, 570.0, 580.0, 590.0, 600.0, 610.0, 620.0, 630.0, 640.0, 650.0, 660.0, 670.0, 680.0, 690.0, 700.0, 710.0, 720.0, 730.0, 740.0, 750.0, 760.0, 770.0, 780.0, 790.0, 800.0, 810.0, 820.0, 830.0, 840.0, 850.0, 860.0, 870.0, 880.0, 890.0, 900.0, 910.0, 920.0, 930.0, 950.0, 970.0, 990.0, 1020.0, 1030.0, 1040.0, 1060.0, 1100.0, 1140.0, 1270.0, 1320.0, 4000.0]
        ,),
    'divideByBinWidth':1,
    'xaxis': 'M(WW) [GeV]',
    'fold':3,
    'cuts':cut_GGFDNN1,
    }
    if Year=='2017': variables['WW_mass_GGFDNN1']['range']=([0.0, 200.0, 220.0, 240.0, 260.0, 270.0, 280.0, 300.0, 320.0, 330.0, 340.0, 360.0, 380.0, 390.0, 400.0, 410.0, 420.0, 430.0, 440.0, 450.0, 460.0, 470.0, 480.0, 490.0, 500.0, 510.0, 520.0, 530.0, 540.0, 550.0, 560.0, 570.0, 580.0, 590.0, 600.0, 610.0, 620.0, 630.0, 640.0, 650.0, 660.0, 670.0, 680.0, 690.0, 700.0, 710.0, 720.0, 730.0, 740.0, 750.0, 760.0, 770.0, 780.0, 790.0, 800.0, 810.0, 820.0, 830.0, 840.0, 850.0, 860.0, 870.0, 880.0, 890.0, 900.0, 920.0, 940.0, 950.0, 970.0, 980.0, 1000.0, 1030.0, 1070.0, 1080.0, 1100.0, 1110.0, 1180.0, 1300.0, 1330.0, 4000.0],)
    if Year=='2018': variables['WW_mass_GGFDNN1']['range']=([0.0, 170.0, 190.0, 210.0, 220.0, 230.0, 240.0, 250.0, 260.0, 270.0, 280.0, 290.0, 300.0, 310.0, 320.0, 330.0, 340.0, 350.0, 360.0, 370.0, 380.0, 390.0, 400.0, 410.0, 420.0, 430.0, 440.0, 450.0, 460.0, 470.0, 480.0, 490.0, 500.0, 510.0, 520.0, 530.0, 540.0, 550.0, 560.0, 570.0, 580.0, 590.0, 600.0, 610.0, 620.0, 630.0, 640.0, 650.0, 660.0, 670.0, 680.0, 690.0, 700.0, 710.0, 720.0, 730.0, 740.0, 750.0, 760.0, 770.0, 780.0, 790.0, 800.0, 810.0, 820.0, 830.0, 840.0, 850.0, 860.0, 870.0, 880.0, 890.0, 900.0, 910.0, 920.0, 930.0, 940.0, 950.0, 960.0, 970.0, 990.0, 1010.0, 1030.0, 1040.0, 1080.0, 1100.0, 1160.0, 1170.0, 1180.0, 1240.0, 1260.0, 1450.0, 1530.0, 1720.0, 2020.0, 4000.0],)


if Resolved:
    ##--cutbased
    variables['WW_mass_GGF0']={
        'name': 'WW_mass',
        'range':([0.0, 310.0, 320.0, 340.0, 350.0, 360.0, 370.0, 380.0, 390.0, 400.0, 410.0, 420.0, 430.0, 440.0, 450.0, 460.0, 470.0, 480.0, 490.0, 500.0, 510.0, 520.0, 530.0, 540.0, 550.0, 560.0, 570.0, 580.0, 590.0, 600.0, 610.0, 620.0, 630.0, 640.0, 650.0, 660.0, 670.0, 680.0, 690.0, 700.0, 710.0, 720.0, 740.0, 750.0, 760.0, 770.0, 800.0, 810.0, 830.0, 850.0, 860.0, 870.0, 880.0, 930.0, 940.0, 970.0, 990.0, 1020.0, 1040.0, 1090.0, 1220.0, 3000.0]
                 ,),
        'divideByBinWidth':1,
        'xaxis': 'M(WW) [GeV]',
        'fold':3,
        'cuts':cut_GGF0,
    }
    if Year=='2017': variables['WW_mass_GGF0']['range']=([0.0, 310.0, 320.0, 330.0, 340.0, 350.0, 360.0, 370.0, 380.0, 390.0, 400.0, 410.0, 420.0, 430.0, 440.0, 450.0, 460.0, 470.0, 480.0, 490.0, 500.0, 510.0, 520.0, 530.0, 540.0, 550.0, 560.0, 570.0, 580.0, 590.0, 600.0, 610.0, 620.0, 630.0, 640.0, 650.0, 660.0, 670.0, 680.0, 690.0, 700.0, 710.0, 720.0, 730.0, 740.0, 750.0, 760.0, 770.0, 780.0, 790.0, 800.0, 810.0, 820.0, 830.0, 840.0, 850.0, 860.0, 870.0, 880.0, 900.0, 920.0, 940.0, 970.0, 1000.0, 1040.0, 1090.0, 1290.0, 3000.0],)
    if Year=='2018': variables['WW_mass_GGF0']['range']=([0.0, 300.0, 310.0, 320.0, 330.0, 340.0, 350.0, 360.0, 370.0, 380.0, 390.0, 400.0, 410.0, 420.0, 430.0, 440.0, 450.0, 460.0, 470.0, 480.0, 490.0, 500.0, 510.0, 520.0, 530.0, 540.0, 550.0, 560.0, 570.0, 580.0, 590.0, 600.0, 610.0, 620.0, 630.0, 640.0, 650.0, 660.0, 670.0, 680.0, 690.0, 700.0, 710.0, 720.0, 730.0, 740.0, 750.0, 760.0, 770.0, 780.0, 790.0, 800.0, 810.0, 820.0, 830.0, 840.0, 850.0, 860.0, 870.0, 890.0, 910.0, 920.0, 940.0, 950.0, 970.0, 990.0, 1010.0, 1030.0, 1070.0, 1110.0, 1150.0, 1250.0, 1570.0, 3000.0],)


    variables['WW_mass_VBF']={
        'name': 'WW_mass',
        'range':([0.0, 170.0, 180.0, 190.0, 200.0, 210.0, 220.0, 230.0, 240.0, 250.0, 260.0, 270.0, 280.0, 290.0, 300.0, 310.0, 330.0, 340.0, 350.0, 360.0, 370.0, 380.0, 390.0, 400.0, 410.0, 420.0, 430.0, 440.0, 450.0, 460.0, 470.0, 480.0, 490.0, 500.0, 510.0, 520.0, 530.0, 540.0, 550.0, 560.0, 570.0, 580.0, 590.0, 600.0, 610.0, 630.0, 650.0, 660.0, 680.0, 740.0, 750.0, 780.0, 800.0, 890.0, 1020.0, 3000.0]
                 ,),
        'divideByBinWidth':1,
        'xaxis': 'M(WW) [GeV]',
        'fold':3,
        'cuts':cut_VBF,
    }
    if Year=='2017': variables['WW_mass_VBF']['range']=([0.0, 170.0, 180.0, 190.0, 200.0, 210.0, 220.0, 230.0, 240.0, 250.0, 260.0, 270.0, 280.0, 290.0, 300.0, 310.0, 320.0, 330.0, 340.0, 350.0, 360.0, 370.0, 380.0, 390.0, 400.0, 410.0, 420.0, 430.0, 440.0, 450.0, 460.0, 470.0, 480.0, 490.0, 500.0, 510.0, 520.0, 530.0, 540.0, 550.0, 560.0, 570.0, 580.0, 590.0, 600.0, 610.0, 620.0, 640.0, 650.0, 670.0, 690.0, 710.0, 740.0, 760.0, 800.0, 910.0, 1020.0, 3000.0],)
    if Year=='2018': variables['WW_mass_VBF']['range']=([0.0, 160.0, 170.0, 180.0, 200.0, 210.0, 220.0, 230.0, 240.0, 250.0, 260.0, 270.0, 280.0, 290.0, 310.0, 320.0, 330.0, 340.0, 350.0, 360.0, 370.0, 380.0, 390.0, 400.0, 410.0, 420.0, 430.0, 440.0, 450.0, 460.0, 470.0, 480.0, 490.0, 500.0, 510.0, 520.0, 530.0, 540.0, 550.0, 560.0, 570.0, 580.0, 590.0, 600.0, 620.0, 630.0, 650.0, 660.0, 670.0, 680.0, 700.0, 730.0, 770.0, 790.0, 810.0, 850.0, 950.0, 1080.0, 3000.0],)



    variables['WW_mass_GGF1']={
        'name': 'WW_mass',
        'range':([0.0, 160.0, 170.0, 180.0, 190.0, 200.0, 210.0, 220.0, 230.0, 240.0, 250.0, 260.0, 270.0, 280.0, 290.0, 300.0, 310.0, 320.0, 330.0, 340.0, 350.0, 360.0, 370.0, 380.0, 390.0, 400.0, 410.0, 420.0, 430.0, 440.0, 450.0, 460.0, 470.0, 480.0, 490.0, 500.0, 510.0, 520.0, 530.0, 540.0, 550.0, 560.0, 570.0, 580.0, 590.0, 600.0, 610.0, 620.0, 630.0, 640.0, 650.0, 660.0, 670.0, 680.0, 690.0, 700.0, 710.0, 720.0, 730.0, 740.0, 750.0, 760.0, 770.0, 780.0, 790.0, 800.0, 810.0, 820.0, 830.0, 840.0, 850.0, 860.0, 870.0, 890.0, 920.0, 930.0, 940.0, 960.0, 980.0, 990.0, 1010.0, 1050.0, 1130.0, 1430.0, 3000.0]
                 ,),
        'divideByBinWidth':1,
        'xaxis': 'M(WW) [GeV]',
        'fold':3,
        'cuts':cut_GGF1,
    }
    if Year=='2017': variables['WW_mass_GGF1']['range']=([0.0, 160.0, 170.0, 180.0, 190.0, 200.0, 210.0, 220.0, 230.0, 240.0, 250.0, 260.0, 270.0, 280.0, 290.0, 300.0, 310.0, 320.0, 330.0, 340.0, 350.0, 360.0, 370.0, 380.0, 390.0, 400.0, 410.0, 420.0, 430.0, 440.0, 450.0, 460.0, 470.0, 480.0, 490.0, 500.0, 510.0, 520.0, 530.0, 540.0, 550.0, 560.0, 570.0, 580.0, 590.0, 600.0, 610.0, 620.0, 630.0, 640.0, 650.0, 660.0, 670.0, 680.0, 690.0, 700.0, 710.0, 720.0, 730.0, 740.0, 750.0, 760.0, 770.0, 780.0, 790.0, 800.0, 810.0, 820.0, 830.0, 840.0, 850.0, 860.0, 870.0, 880.0, 890.0, 900.0, 910.0, 920.0, 940.0, 950.0, 960.0, 970.0, 990.0, 1010.0, 1020.0, 1050.0, 1070.0, 1090.0, 1120.0, 1150.0, 1190.0, 1250.0, 1340.0, 1800.0, 3000.0],)
    if Year=='2018': variables['WW_mass_GGF1']['range']=([0.0, 160.0, 170.0, 180.0, 190.0, 200.0, 210.0, 220.0, 230.0, 240.0, 250.0, 260.0, 270.0, 280.0, 290.0, 300.0, 310.0, 320.0, 330.0, 340.0, 350.0, 360.0, 370.0, 380.0, 390.0, 400.0, 410.0, 420.0, 430.0, 440.0, 450.0, 460.0, 470.0, 480.0, 490.0, 500.0, 510.0, 520.0, 530.0, 540.0, 550.0, 560.0, 570.0, 580.0, 590.0, 600.0, 610.0, 620.0, 630.0, 640.0, 650.0, 660.0, 670.0, 680.0, 690.0, 700.0, 710.0, 720.0, 730.0, 740.0, 750.0, 760.0, 770.0, 780.0, 790.0, 800.0, 810.0, 820.0, 830.0, 840.0, 850.0, 860.0, 870.0, 880.0, 890.0, 900.0, 910.0, 920.0, 930.0, 940.0, 950.0, 960.0, 970.0, 980.0, 990.0, 1000.0, 1020.0, 1040.0, 1050.0, 1070.0, 1080.0, 1110.0, 1140.0, 1160.0, 1210.0, 1260.0, 1320.0, 1420.0, 3000.0],)


    ##--dnn
    variables['WW_mass_GGFDNN0']={
        'name': 'WW_mass',
        'range':([0.0, 310.0, 320.0, 340.0, 350.0, 360.0, 370.0, 380.0, 390.0, 400.0, 410.0, 420.0, 430.0, 440.0, 450.0, 460.0, 470.0, 480.0, 490.0, 500.0, 510.0, 520.0, 530.0, 540.0, 550.0, 560.0, 570.0, 580.0, 590.0, 600.0, 610.0, 620.0, 630.0, 640.0, 650.0, 660.0, 670.0, 680.0, 690.0, 700.0, 710.0, 720.0, 730.0, 740.0, 750.0, 760.0, 770.0, 800.0, 810.0, 830.0, 850.0, 860.0, 870.0, 880.0, 920.0, 940.0, 970.0, 990.0, 1020.0, 1050.0, 1100.0, 3000.0]
                 ,),
        'divideByBinWidth':1,
        'xaxis': 'M(WW) [GeV]',
        'fold':3,
        'cuts':cut_GGFDNN0,
    }
    if Year=='2017': variables['WW_mass_GGFDNN0']['range']=([0.0, 310.0, 320.0, 330.0, 340.0, 350.0, 360.0, 370.0, 380.0, 390.0, 400.0, 410.0, 420.0, 430.0, 440.0, 450.0, 460.0, 470.0, 480.0, 490.0, 500.0, 510.0, 520.0, 530.0, 540.0, 550.0, 560.0, 570.0, 580.0, 590.0, 600.0, 610.0, 620.0, 630.0, 640.0, 650.0, 660.0, 670.0, 680.0, 690.0, 700.0, 710.0, 720.0, 730.0, 740.0, 750.0, 760.0, 770.0, 780.0, 790.0, 800.0, 810.0, 820.0, 830.0, 840.0, 850.0, 860.0, 870.0, 880.0, 890.0, 910.0, 930.0, 950.0, 970.0, 1000.0, 1050.0, 1100.0, 1340.0, 3000.0],)
    if Year=='2018': variables['WW_mass_GGFDNN0']['range']=([0.0, 300.0, 310.0, 320.0, 330.0, 340.0, 350.0, 360.0, 370.0, 380.0, 390.0, 400.0, 410.0, 420.0, 430.0, 440.0, 450.0, 460.0, 470.0, 480.0, 490.0, 500.0, 510.0, 520.0, 530.0, 540.0, 550.0, 560.0, 570.0, 580.0, 590.0, 600.0, 610.0, 620.0, 630.0, 640.0, 650.0, 660.0, 670.0, 680.0, 690.0, 700.0, 710.0, 720.0, 730.0, 740.0, 750.0, 760.0, 770.0, 780.0, 790.0, 800.0, 810.0, 820.0, 830.0, 840.0, 850.0, 860.0, 870.0, 890.0, 910.0, 920.0, 940.0, 950.0, 970.0, 990.0, 1020.0, 1040.0, 1080.0, 1130.0, 1180.0, 1330.0, 3000.0],)


    variables['WW_mass_VBFDNN']={
        'name': 'WW_mass',
        'range':([0.0, 180.0, 190.0, 200.0, 220.0, 230.0, 240.0, 250.0, 260.0, 270.0, 280.0, 290.0, 300.0, 310.0, 320.0, 330.0, 340.0, 350.0, 360.0, 370.0, 380.0, 390.0, 400.0, 410.0, 420.0, 430.0, 440.0, 450.0, 460.0, 470.0, 480.0, 490.0, 500.0, 510.0, 520.0, 530.0, 540.0, 550.0, 570.0, 590.0, 600.0, 630.0, 670.0, 690.0, 730.0, 800.0, 1000.0, 3000.0]
                 ,),
        'divideByBinWidth':1,
        'xaxis': 'M(WW) [GeV]',
        'fold':3,
        'cuts':cut_VBFDNN,
    }
    if Year=='2017': variables['WW_mass_VBFDNN']['range']=([0.0, 160.0, 170.0, 180.0, 190.0, 200.0, 210.0, 220.0, 230.0, 240.0, 250.0, 260.0, 270.0, 280.0, 290.0, 300.0, 310.0, 320.0, 330.0, 340.0, 350.0, 360.0, 370.0, 380.0, 390.0, 400.0, 410.0, 420.0, 430.0, 440.0, 450.0, 460.0, 470.0, 480.0, 490.0, 500.0, 510.0, 520.0, 530.0, 540.0, 550.0, 560.0, 580.0, 600.0, 620.0, 640.0, 660.0, 680.0, 700.0, 760.0, 820.0, 900.0, 3000.0],)
    if Year=='2018': variables['WW_mass_VBFDNN']['range']=([0.0, 170.0, 180.0, 190.0, 200.0, 210.0, 220.0, 230.0, 240.0, 250.0, 260.0, 270.0, 280.0, 290.0, 310.0, 320.0, 330.0, 340.0, 350.0, 360.0, 370.0, 380.0, 390.0, 420.0, 430.0, 440.0, 450.0, 460.0, 470.0, 480.0, 490.0, 500.0, 510.0, 520.0, 530.0, 540.0, 550.0, 560.0, 580.0, 600.0, 620.0, 640.0, 660.0, 680.0, 730.0, 770.0, 820.0, 920.0, 1050.0, 3000.0],)


    variables['WW_mass_GGFDNN1']={
        'name': 'WW_mass',
        'range':([0.0, 160.0, 170.0, 180.0, 190.0, 200.0, 210.0, 220.0, 230.0, 240.0, 250.0, 260.0, 270.0, 280.0, 290.0, 300.0, 310.0, 320.0, 330.0, 340.0, 350.0, 360.0, 370.0, 380.0, 390.0, 400.0, 410.0, 420.0, 430.0, 440.0, 450.0, 460.0, 470.0, 480.0, 490.0, 500.0, 510.0, 520.0, 530.0, 540.0, 550.0, 560.0, 570.0, 580.0, 590.0, 600.0, 610.0, 620.0, 630.0, 640.0, 650.0, 660.0, 670.0, 680.0, 690.0, 700.0, 710.0, 720.0, 730.0, 740.0, 750.0, 760.0, 770.0, 780.0, 790.0, 800.0, 810.0, 820.0, 830.0, 840.0, 850.0, 860.0, 870.0, 890.0, 920.0, 930.0, 940.0, 960.0, 980.0, 990.0, 1010.0, 1050.0, 1130.0, 1420.0, 3000.0]
                 ,),
        'divideByBinWidth':1,
        'xaxis': 'M(WW) [GeV]',
        'fold':3,
        'cuts':cut_GGFDNN1,
    }
    if Year=='2017': variables['WW_mass_GGFDNN1']['range']=([0.0, 160.0, 170.0, 180.0, 190.0, 200.0, 210.0, 220.0, 230.0, 240.0, 250.0, 260.0, 270.0, 280.0, 290.0, 300.0, 310.0, 320.0, 330.0, 340.0, 350.0, 360.0, 370.0, 380.0, 390.0, 400.0, 410.0, 420.0, 430.0, 440.0, 450.0, 460.0, 470.0, 480.0, 490.0, 500.0, 510.0, 520.0, 530.0, 540.0, 550.0, 560.0, 570.0, 580.0, 590.0, 600.0, 610.0, 620.0, 630.0, 640.0, 650.0, 660.0, 670.0, 680.0, 690.0, 700.0, 710.0, 720.0, 730.0, 740.0, 750.0, 760.0, 770.0, 780.0, 790.0, 800.0, 810.0, 820.0, 830.0, 840.0, 850.0, 860.0, 870.0, 880.0, 890.0, 900.0, 910.0, 920.0, 940.0, 950.0, 960.0, 970.0, 990.0, 1000.0, 1010.0, 1020.0, 1050.0, 1070.0, 1090.0, 1120.0, 1150.0, 1190.0, 1250.0, 1340.0, 1660.0, 3000.0],)
    if Year=='2018': variables['WW_mass_GGFDNN1']['range']=([0.0, 160.0, 170.0, 180.0, 190.0, 200.0, 210.0, 220.0, 230.0, 240.0, 250.0, 260.0, 270.0, 280.0, 290.0, 300.0, 310.0, 320.0, 330.0, 340.0, 350.0, 360.0, 370.0, 380.0, 390.0, 400.0, 410.0, 420.0, 430.0, 440.0, 450.0, 460.0, 470.0, 480.0, 490.0, 500.0, 510.0, 520.0, 530.0, 540.0, 550.0, 560.0, 570.0, 580.0, 590.0, 600.0, 610.0, 620.0, 630.0, 640.0, 650.0, 660.0, 670.0, 680.0, 690.0, 700.0, 710.0, 720.0, 730.0, 740.0, 750.0, 760.0, 770.0, 780.0, 790.0, 800.0, 810.0, 820.0, 830.0, 840.0, 850.0, 860.0, 870.0, 880.0, 890.0, 900.0, 910.0, 920.0, 930.0, 940.0, 950.0, 960.0, 970.0, 980.0, 990.0, 1000.0, 1020.0, 1040.0, 1050.0, 1070.0, 1080.0, 1110.0, 1140.0, 1160.0, 1210.0, 1260.0, 1320.0, 1420.0, 3000.0],)
    

'''
variables['WW_MET_over_mass']={
    'name':'WW_MET_over_mass',
    'range':(20,0,1),
    'xaxis':'MET/M(WW))',
    'fold':0
}

variables['WW_Whadpt_over_mass']={
    'name':'WW_Whadpt_over_mass',
    'range':(20,0,1),
    'xaxis':'P_{T}(HadronicW)/M(WW))',
    'fold':0
}


variables['WW_Wleppt_over_mass']={
    'name':'WW_Wleppt_over_mass',
    'range':(20,0,1),
    'xaxis':'P_{T}(LeptonicW)/M(WW))',
    'fold':0
}


variables['WW_dPhi']={
        'name':'WW_dPhi',
        'range':(100,0,3.5),
        'xaxis':'#Delta#phi(W, W)',
        'fold':0
}
'''



#variables['WW_dPhi_VBF']={
#        'name':'WW_dPhi_VBF',
#        'range':(100,0,3.5),
#        'xaxis':'#Delta#phi(W, W) corr',
#        'fold':0
#}

if Resolved:
    variables['WW_mass']['range']=        ([0,200,
         250,
         300,
         350,
         400,
         450,
         500,
         550,
         600,
         650,
         700,
         750,
         800,
         850,
         900,
         950,
         1000,
         1100,
         1200,
                                            1300,1400,1600,1800,
                                            2000,
                                        ],)
    variables['WW_pt']['range']=(40,0,400)

#if (not 'SR' in configration_py):
#    variables['WW_mass']['range']=(50,0,1000)

if Resolved:
    variables['WW_Mt']={
        'name': 'WW_Mt',
        'range':(50,0,500),
        #'divideByBinWidth':1,
        'xaxis': 'M_{T}(WW) [GeV]',
        'fold':3
    } 
   




variables['DNN_isVBF']={
    'name':'DNN_isVBF',
    'range':(20,0,1),
    'xaxis':'DNN_isVBF',
    'fold':0,
}

variables['dphi_lep_met']={
        'name':'dphi_lep_met',
        'range':(100,0,3.15),
        'xaxis':'#Delta#phi(l, MissingE_{T})',
        'fold':0
}

if Boosted:
    variables['max_mjj_Boost_'+WTAG+'_nom']={
        'name':'max_mjj_Boost_'+WTAG+'_nom',
        'range':(30,0,4500),
        'xaxis':'max_mjj_Boost_'+WTAG+'_nom',
        'fold':0
    }
    
    variables['mjj_of_max_dEta_Boost_'+WTAG+'_nom']={
        'name':'mjj_of_max_dEta_Boost_'+WTAG+'_nom',
        'range':(30,0,4500),
        'xaxis':'mjj_of_max_dEta_Boost_'+WTAG+'_nom',
        'fold':0
    }
    variables['max_dEta_Boost_'+WTAG+'_nom']={
        'name':'max_dEta_Boost_'+WTAG+'_nom',
        'range':(30,0,10),
        'xaxis':'max_dEta_Boost_'+WTAG+'_nom',
        'fold':0
    }
    
    variables['dEta_of_max_mjj_Boost_'+WTAG+'_nom']={
        'name':'dEta_of_max_mjj_Boost_'+WTAG+'_nom',
        'range':(30,0,10),
        'xaxis':'dEta_of_max_mjj_Boost_'+WTAG+'_nom',
        'fold':0
    }
if Resolved:

    variables['max_mjj_Resol_'+ALGO+'_nom']={
        'name':'max_mjj_Resol_'+ALGO+'_nom',
        'range':(30,0,4500),
        'xaxis':'max_mjj_Resol_'+ALGO+'_nom',
        'fold':0
    }
    
    variables['mjj_of_max_dEta_Resol_'+ALGO+'_nom']={
        'name':'mjj_of_max_dEta_Resol_'+ALGO+'_nom',
        'range':(30,0,4500),
        'xaxis':'mjj_of_max_dEta_Resol_'+ALGO+'_nom',
        'fold':0
    }
    variables['max_dEta_Resol_'+ALGO+'_nom']={
        'name':'max_dEta_Resol_'+ALGO+'_nom',
        'range':(30,0,10),
        'xaxis':'max_dEta_Resol_'+ALGO+'_nom',
        'fold':0
    }

    variables['dEta_of_max_mjj_Resol_'+ALGO+'_nom']={
        'name':'dEta_of_max_mjj_Resol_'+ALGO+'_nom',
        'range':(30,0,10),
        'xaxis':'dEta_of_max_mjj_Resol_'+ALGO+'_nom',
        'fold':0
    }


if Boosted:
    idx=0
    for M_MELA in MELA_MASS_BOOST:
        for C in MELA_C_BOOST:
        
            #'MEKD_'+str(M)    
            M=str(M_MELA)
            C=str(C)
            variables['MEKD'+str(idx)]={
                'name':'MEKD_Bst_C_'+C+'_M'+str(M),
                'range':(20,0,1),
                'xaxis':'MELA KD',
                'fold':0
            }
            idx+=1
    

if Resolved:
    idx=0
    for M_MELA in MELA_MASS_RESOL:
        for C in MELA_C_RESOL:
        
            #'MEKD_'+str(M)    
            M=str(M_MELA)
            C=str(C)
            variables['MEKD'+str(idx)]={
                'name':'MEKD_Res_C_'+C+'_M'+str(M),
                'range':(20,0,1),
                'xaxis':'MELA KD',
                'fold':0
            }
            idx+=1

#if FORFINAL:
#    VtoDraw=['WW_mass_GGF0','WW_mass_VBF','WW_mass_GGF1','WW_mass_GGFDNN0','WW_mass_VBFDNN','WW_mass_GGFDNN1','WW_mass','Event']
#    for v in sorted(variables):
#        if v in VtoDraw: continue
#        del variables[v]


if not StatOnly:

    if LepMetOnly:
        VtoDraw=['Lepton_eta[0]','PV_npvs','Lepton_pt[0]','Wlep_nom_mass','PuppiMET','Wlep_nom_pt','Wlep_Mt']
        for v in sorted(variables):
            if v in VtoDraw: continue
            del variables[v]

    if JetMetOnly:
        VtoDraw=['LeadingJet_eta','nBJet','SubLeadingJet_pt','nAK4Jet_eta4p7','maxmjj_dEta_jj_VBF','HadronicW_mass','HadronicW_pt','VBFJet2_eta','LeadingJet_BtagScore','SubLeadingAddJet_BtagScore','PV_npvs','AddJet_eta','nAK4Jet','mass_jj_VBF','maxmjj_mass_jj_VBF','AddJet_pt','LeadingAddJet_BtagScore','MEKD_Bst_C_0.001_M1500','LeadingAddJet_eta','HadronicW_Score','PuppiMET','AddJet_BtagScore','SubLeadingJet_BtagScore','LeadingJet_pt','dEta_jj_VBF','VBFJet1_eta','SubLeadingJet_eta','WW_pt_over_mass','SubLeadingAddJet_pt','SubLeadingAddJet_eta','WW_mass','LeadingAddJet_pt']
        for v in sorted(variables):
            if v in ListNotDraw:
                del variables[v]

if ForDatacard:
    for v in sorted(variables):
        if v!='<VARIABLE>':
            del variables[v]

print "len(variables)=",len(variables)
for v in variables:
    print variables[v]['name'] 

