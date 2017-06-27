# Dwarfsquad
Dwarfsquad is both a python package for modeling Ascent assay configurations, and a cli used to perform common manipulations for Assay Configuration. 

Most of the cli calls for assay configuration have been largely replaced by an interactive web app used to translate the json assay configuration to an xlsx file, and then back to a json file for import into Ascent.

https://assay-interchange.herokuapp.com/

dwarfsquad can be used from the command line to change assay configuration formats:

`dwarfsquad build full_ac Benzo-SP.xlsx > Benzo-SP.json`

dwarfsquad can be used to upload batches to a particular site:

`dwarfsquad upload batch 170403-0068_SRI.zip --site https://millenniumhealthtest.poweredbyascent.net --username indigo --password $PASS`

It has a few other options, but those are largely deprecated at this point.

Dwarfsquad is useful as a general API for modeling Ascent assay configurations. 

`pip install -r requirements.txt`  
`python setup.py install`  
`python`  
`>>> import dwarfsquad`  
