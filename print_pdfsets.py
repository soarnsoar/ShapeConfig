f=open('PDF/nuisanceinfo_pdf.py','r')
exec(f)
f.close()
#lhadpdf_infos
pdfs=[]
for s in lhadpdf_infos:
    pdfs.append(lhadpdf_infos[s])

pdfs=list(set(pdfs))

print pdfs
