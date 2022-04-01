from LatinoAnalysis.Tools.HiggsXSection  import *
HiggsXS = HiggsXSection()
MX=1000
#a=HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH',int(MX),'pdf','bsm')
a=HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH',int(MX),'scale','bsm')
b=a.split('/')
if len(b)==1:
    up=b[0]
    down=str(2-float(b[0]))
elif len(b)==2:
    up=b[1]
    down=b[0]
print up,down
