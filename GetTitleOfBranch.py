import ROOT


def GetTitleOfBranch(filepath,treename,branchname):
    mytfile=ROOT.TFile.Open(filepath)
    mytree=mytfile.Get(treename)
    mybr=mytree.GetBranch(branchname)
    title=mybr.GetTitle()



    mytfile.Close()
    return title

if __name__ == '__main__':
    #filepath='root://cms-xrdr.private.lo:2094//xrd//store/user/jhchoi/Latino/HWWNano/Summer16_102X_nAODv5_Full2016v6/MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10__HMFull_V11_nom/nanoLatino_VBFHToWWToLNuQQ_M1500__part0.root'
    #filepath='root://cms-xrdr.private.lo:2094//xrd//store/user/jhchoi/Latino/HWWNano/Summer16_102X_nAODv5_Full2016v6/MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10__HMFull_V11_nom/nanoLatino_TTToSemiLeptonic__part0.root'
    filepath='root://cms-xrdr.private.lo:2094//xrd//store/user/jhchoi/Latino/HWWNano/Summer16_102X_nAODv5_Full2016v6/MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10__HMFull_V11_nom/nanoLatino_DYJetsToLL_M-50-LO_ext2__part0.root'
    treename='Events'
    #branchname='LHEScaleWeight'
    branchname='LHEPdfWeight'
    #LHE pdf variation weights (w_var / w_nominal) for LHA IDs 262000 - 262100
    ##--->if ID starts from ****0 -> divided by 00000
    ##---->if ID starts from ****1.....????
    
    title=GetTitleOfBranch(filepath,treename,branchname)
    print title
