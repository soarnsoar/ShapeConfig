def ParseLHEPdfWeightTitle(title):
    #LHE pdf variation weights (w_var / w_nominal) for LHA IDs 262000 - 262100
    #

    ##
    nominalidx=-1


    idparts=title.split('for LHA IDs ')[1]
    firstid=idparts.split('-')[0]
    lastid=idparts.split('-')[1]
    
    firstid=firstid.replace(' ','')
    lastid=lastid.replace(' ','')

    if firstid.endswith('0'):
        nominalidx=0

    firstid=int(firstid)
    lastid=int(lastid)

    length=lastid-firstid+1

    lhapdfid=firstid+nominalidx
    
    return lhapdfid, length, nominalidx




if __name__ == '__main__':
    title='LHE pdf variation weights (w_var / w_nominal) for LHA IDs 262000 - 262100'
    lhapdfid,length,nominalidx = firstid, ParseLHEPdfWeightTitle(title)


    print 'length=',length
    print 'nominalidx=',nominalidx
    
