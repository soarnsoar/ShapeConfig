UsePseudoData=False
print "UsePseudoData=",UsePseudoData
print "CombineWjets=",CombineWjets
DrawCombineTOP=True
import sys
sys.path.append(os.getcwd())
sys.path.append(os.getcwd()+'/xsec/')
#-----Variable Deinition-----#
from WPandCut2016 import *

import sys
from collections import OrderedDict


model_name = '_'+model.replace(".","")

plot=OrderedDict()

TOPS = [skey for skey in samples if ('TT' in skey or 'SingleTop' in skey or 'tW' in skey or 'ST' in skey)]



dict_TColor={
'green':416,##darker greeen
'cyan':432,##bright blue
'magenta':616,##violet
'yellow':400,
'blue':600,
'orange':800+7,##darker orange
'pink':900,
'black':1,
'red':632,
'azure':860,##blue
'gray':920,
}

scriptname=opt.plotFile

###--DY
groupPlot['DY']  = {
    'nameHR' : 'DY',
    'isSignal' : 0,
    'color': dict_TColor['yellow'], 
    'isData'   : 0,

    #'samples' : ['DY']
}


plot['DY10to50']  = {
                  'nameHR' : 'DY10to50',
                  'isSignal' : 0,
                  'color': dict_TColor['yellow'], 
                  'isData'   : 0,

              }

plot['DY50']  = {
                  'nameHR' : 'DY50',
                  'isSignal' : 0,
                  'color': dict_TColor['yellow'], 
                  'isData'   : 0,
              }

groupPlot['DY']['samples']=['DY10to50','DY50']


###--h125
groupPlot['h125']  = {
    'nameHR' : 'h125',
    'isSignal' : 0,
    'color': dict_TColor['magenta'], 
    'isData'   : 0,
    #'samples' : ['DY']
}

plot['ggH_hww']  = {
                  'nameHR' : 'ggH_hww',
                  'isSignal' : 0,
                  'color': dict_TColor['magenta'], 
                  'isData'   : 0,
              }

plot['qqH_hww']  = {
                  'nameHR' : 'qqH_hww',
                  'isSignal' : 0,
                  'color': dict_TColor['magenta'], 
                  'isData'   : 0,
              }

groupPlot['h125']['samples']=['ggH_hww','qqH_hww']


##---VH
groupPlot['VH']  = {
    'nameHR' : 'VH',
    'isSignal' : 0,
    'color': dict_TColor['pink'], 
    'isData'   : 0,
    #'samples' : ['DY']
}

plot['WmHWWlnuqq_M125']  = {
                  'nameHR' : 'WmHWWlnuqq_M125',
                  'isSignal' : 0,
                  'color': dict_TColor['pink'], 
                  'isData'   : 0,
              }
plot['WpHWWlnuqq_M125']  = {
                  'nameHR' : 'W[HWWlnuqq_M125',
                  'isSignal' : 0,
                  'color': dict_TColor['pink'], 
                  'isData'   : 0,
              }
plot['ZHWWlnuqq_M125']  = {
                  'nameHR' : 'ZHWWlnuqq_M125',
                  'isSignal' : 0,
                  'color': dict_TColor['pink'], 
                  'isData'   : 0,
              }


groupPlot['VH']['samples']=['WmHWWlnuqq_M125','WpHWWlnuqq_M125','ZHWWlnuqq_M125']



###--QCD
groupPlot['QCD']  = {
    'nameHR' : 'QCD',
    'isSignal' : 0,
    'color': dict_TColor['gray'],
    'isData'   : 0,
    'samples'  : []
}



groupPlot['QCD']['samples']=QCD_EM+QCD_MU+QCD_bcToE
for s in QCD_EM+QCD_MU+QCD_bcToE:
    plot[s]  = {
        'nameHR' : s,
        'isSignal' : 0,
        'color': dict_TColor['gray'],
        'isData'   : 0,
    }

###--QCD
groupPlot['WW']  = {
    'nameHR' : 'WW',
    'isSignal' : 0,
    'color': dict_TColor['blue']+1,
    'isData'   : 0,
    'samples'  : ['WW']
}


plot['WW']  = {
    'nameHR' : 'WW',
    'isSignal' : 0,
    'color': dict_TColor['blue']+1,
    'isData'   : 0,
}



##--MultiBoson
groupPlot['MultiBoson']={
    'nameHR' : 'MultiBoson',
    'isSignal' : 0,
    'color': dict_TColor['azure'],
    'isData'   : 0,
    'samples'  : MultiBoson+ggWW+qqWWqq
    
}

total=len(MultiBoson)
idx=-1*int(total/2)
for s in MultiBoson:
    plot[s]={
        'nameHR' : s,
        'isSignal' : 0,
        'color': dict_TColor['cyan']+idx,
        'isData'   : 0,
        
    }
    idx+=1


##--Top
total=len(TOPS)
idx=-1*int(total/2)
groupPlot['Top']={
    'nameHR' : 'Top',
    'isSignal' : 0,
    'color': dict_TColor['orange'],
    'isData'   : 0,
    'samples'  : TOPS
}
for top in TOPS:
    
    plot[top]  = {
        'nameHR' : top,
        'isSignal' : 0,
        'color': dict_TColor['orange']+idx,
        'isData'   : 0,
    }
    idx+=1

##--Wjets
groupPlot['Wjets']={
                  'nameHR' : 'W+jets',
                  'isSignal' : 0,
                  'color': dict_TColor['green'],
                  'isData'   : 0,
    'samples':Wjets
}
total=len(Wjets)
idx=-1*int(total/2)
for wjet in Wjets:
    plot[wjet]={
        'nameHR' : wjet,
        'isSignal' : 0,
        'color': dict_TColor['green']+idx,
        'isData'   : 0,
        
    }
    idx+=1


    
if UsePseudoData:
    plot['PseudoData']  = {
        'nameHR' : 'PseudoData',
        'isSignal' : 0,
        'color': 1, 
        'isData'   : 1 ,
        'isBlind'  : 0,
        'samples'  : ['PseudoData']
    }
else:
    plot['DATA']  = {
        'nameHR' : 'DATA',
        'isSignal' : 0,
        'color': 1, 
        'isData'   : 1 ,
        'isBlind'  : 0,
        'samples'  : ['DATA']
    }

import sys
sys.path.insert(0, "MassPoints")
from List_MX import *
from List_MX_VBF import *


#for MX in List_MX:
if 'SR' in scriptname or 'blind' in scriptname:
    if not UsePseudoData : plot['DATA']['isBlind']=1
if "Boost" in scriptname:
    #MList=[3000]
    MList={

        400:30,
        1000:3
    }
    #MList=[]
    #if Year=='2016':MList=[2500]
    #scale=100
    #targetxsec=3

else:
    MList={
        250:500,
        400:200
       }
    #MList=[]
    #scale=100
    #targetxsec=200
for i,MX in enumerate(MList):
    #scale=targetxsec/HWW_XSEC['GGF'][MX]
    targetxsec=MList[MX]
    scale=targetxsec
    plot['ggH_hww'+str(MX)+model_name]={
        #'nameHR':'ggHWWlnuqq_M'+str(MX)+'x'+str(scale),
        #'nameHR':'ggHWWlnuqq_M'+str(MX),
        #'nameHR':'GGF'+str(MX)+' x'+str(scale),
        'nameHR':'ggf'+str(MX)+' in '+str(targetxsec)+' pb',
        'scale' : scale,
        'isData'   : 0,
        'isSignal' : 2,
        'color':dict_TColor['red']+i*2,
        'samples' : ['ggH_hww'+str(MX)+model_name],
        'line':i+1,
        
    }
    groupPlot['ggH_hww'+str(MX)+model_name]={
        #'nameHR':'ggHWWlnuqq_M'+str(MX)+'x'+str(scale),
        'nameHR':'ggf'+str(MX)+' in '+str(targetxsec)+' pb',
        #'nameHR':'ggHWWlnuqq_M'+str(MX),
        'scale' : scale,
        'isData'   : 0,
        'isSignal' : 2,
        'color':dict_TColor['red']+i*2,
        'samples' : ['ggH_hww'+str(MX)+model_name],
        'line':i+1,
    }

    #for MX in List_MX_VBF:
for i,MX in enumerate(MList):
    #continue
    #scale=targetxsec/HWW_XSEC['VBF'][MX]
    targetxsec=MList[MX]
    scale=targetxsec
    groupPlot['qqH_hww'+str(MX)+model_name]={
        #'nameHR':'VBF M'+str(MX)+' x'+str(scale),
        'nameHR':'vbf'+str(MX)+' in '+str(targetxsec)+' pb',
        #'nameHR':'vbfHWWlnuqq_M'+str(MX),
        'isData'   : 0,
        'isSignal' : 2,
        'scale' : scale,
        'color':dict_TColor['blue']+i*2,
        'samples' : ['qqH_hww'+str(MX)+model_name],
        'line':i+1,
    }
    
    plot['qqH_hww'+str(MX)+model_name]={
        'nameHR':'vbf'+str(MX)+' in '+str(targetxsec)+' pb',
        #'nameHR':'vbfHWWlnuqq_M'+str(MX)+'x'+str(scale),
        #'nameHR':'vbfHWWlnuqq_M'+str(MX),
        'isData'   : 0,
        'isSignal' : 2,
        'scale' : scale,
        'color':dict_TColor['blue']+i*2,
        'samples' : ['qqH_hww'+str(MX)+model_name],
        'line':i+1,
    }

    

if Year=='2016':
    lumi=35.9
if Year=='2017':
    lumi=41.5
if Year=='2018':
    lumi=59.7


legend['lumi'] = 'L = '+str(lumi)+'/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'

for gr in sorted(groupPlot):
    groupPlot[gr]['fill']=1001

