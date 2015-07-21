#!/usr/bin/python -OO

dcNS="http://purl.org/dc/elements/1.1/"
dctermsNS = "http://purl.org/dc/terms/"
dspaceNS = "http://www.dspace.org/xmlns/dspace/dim"
fitsNS = "http://hul.harvard.edu/ois/xml/ns/fits/fits_output"
metsNS = "http://www.loc.gov/METS/"
premisNS = "info:lc/xmlns/premis-v2"
xlinkNS = "http://www.w3.org/1999/xlink"
xsiNS = "http://www.w3.org/2001/XMLSchema-instance"
pbcoreNS = "http://www.pbcore.org/PBCore/PBCoreNamespace.html"

dcBNS = "{" + dcNS + "}"
dctermsBNS = "{" + dctermsNS + "}"
dspaceBNS = "{" + dspaceNS + "}"
fitsBNS = "{" + fitsNS + "}"
metsBNS = "{" + metsNS + "}"
premisBNS = "{" + premisNS + "}"
xlinkBNS = "{" + xlinkNS + "}"
xsiBNS = "{" + xsiNS + "}"
pbcoreBNS = "{" + pbcoreNS + "}"

NSMAP = {
    'dc': dcNS,
    'dcterms': dctermsNS,
    'dim': dspaceNS,
    'fits': fitsNS,
    'mets': metsNS,
    'premis': premisNS,
    'xlink': xlinkNS,
    'xsi': xsiNS,
    'pbcore': pbcoreNS,
}
