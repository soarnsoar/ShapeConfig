##


##----Which Region you are interested in--##
#LIST_BST=['Boosted','Resolved']
LIST_BST=['Resolved','Boosted']
#LIST_BST=['Boosted']
#LIST_REGION=['SB','TOP','SR']
LIST_REGION=['Combine']
###-----END---

import sys
import glob
##inputargument = yeartag
VariableBlocks=[]
Year=str(sys.argv[1])



    

import os
import subprocess
from shutil import copyfile

##---Take AreaName
cwd=os.getcwd()
AreaName="_".join(cwd.split('/')[-5:-1])
WORKNAME=AreaName
if len(sys.argv)>2:
    ALIAS=sys.argv[2]
else:
    ALIAS=''
WORKNAME+=ALIAS


##---change 
#WPandCut2016 -> WPandCut<Year>
#samples_2016 -> samples_<Year>
from ApplyYearTag import ApplyYearTag,ChangeString

##--create workspace area
workspace=os.getcwd()+'/../'+Year+'/'+ALIAS
scriptdir=workspace+'/script'
os.system('mkdir -p '+workspace)
os.system('mkdir -p '+scriptdir)
os.system('mkdir -p '+workspace+'/logs')




##--cp configuration and variable
LIST_TEMPLATE=['configuration_template.py','variables_template.py']

for template in LIST_TEMPLATE:
    for bst in LIST_BST:
        for reg in LIST_REGION:
            newtemplate=workspace+'/'+template.replace('_template','_'+bst+'_'+reg)
            os.system('cp '+template+' '+newtemplate)
            ApplyYearTag(newtemplate,Year)
            ChangeString(newtemplate,'__REG__',reg)
            ChangeString(newtemplate,'__BST__',bst)
            ChangeString(newtemplate,'__TEST__',WORKNAME)
            
##--cp cuts
LIST_TEMPLATE=['cuts_Boosted_template.py','cuts_Resolved_template.py']
###----Make config/cuts
#for prod in LIST_PROD:
for reg in LIST_REGION:
    for template in LIST_TEMPLATE:
        #print template
        newtemplate=workspace+'/'+template
        newtemplate=newtemplate.replace('template.py',reg+'.py')

        ##--cp
        command='cp '+template+' '+newtemplate
        os.system(command)

        ApplyYearTag(newtemplate,Year)
        ChangeString(newtemplate,'__REG__',reg)
        

##---cp directories
LIST_CPDIR=['CutAndNuisances']

for cpdir in LIST_CPDIR:
    newdir=workspace+'/'+cpdir
    os.system('mkdir -p '+newdir)

    cplist=glob.glob(cpdir+'/*')
    for cp in cplist:
        command='cp '+cp+' '+newdir+'/'
        os.system(command)

    #ApplyYearTag
    pylist=glob.glob(newdir+'/*.py')
    shlist=glob.glob(newdir+'/*.sh')
    for f in pylist+shlist:
        ApplyYearTag(f,Year) ## 2016 -> <Year>
        if 'script' in cpdir:
            ChangeString(f,'__AREA__',AreaName)
            ChangeString(f,'2016',Year)

##--cp files
LIST_CP=['nuisances.py','aliases.py','plot.py','samples_test.py',]
for cp in LIST_CP:
    os.system('cp '+cp+' '+workspace+'/')
    newcp=workspace+'/'+cp
    ApplyYearTag(newcp,Year)
##---simple cp
LIST_CP=['samples_'+Year+'.py','WPandCut'+Year+'.py','RunPlot_example.sh','Wtagger_cfg.py','Wjjtagger_cfg.py']
for cp in LIST_CP:
    os.system('cp '+cp+' '+workspace+'/')

##--cp workspace to workspace

os.system('cp '+workspace+'/nuisances.py '+workspace+'/nuisances_Boosted.py')
os.system('cp '+workspace+'/nuisances.py '+workspace+'/nuisances_Resolved.py')

os.system('cp '+workspace+'/aliases.py '+workspace+'/aliases_Boosted.py')
os.system('cp '+workspace+'/aliases.py '+workspace+'/aliases_Resolved.py')

##--cp MassPoints
#os.system('rm -rf '+workspace+'/MassPoints')
os.system('mkdir -p '+workspace+'/MassPoints')
os.system('cp MassPoints/* '+workspace+'/MassPoints/')
pylist=glob.glob(workspace+'/MassPoints/*.py')
for f in pylist:
    ApplyYearTag(f,Year) ## 2016 -> <Year>



os.system('mkdir -p logs/')


    




