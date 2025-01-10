## refseq_metadata

A python scrip to get metadata infomation from NCBI by refseq ID.

This scrip will help your download the "all information(it shuld?)" from NCBI Refesq database. 

## Required enviroments(solved by mamba strongly recommanded, or just find a env which have biopython)

```
mamba create -n refseq_metadata
source activate refseq_metadata
mamba install biopython=1.84
```

## Files perpared
Your Refseq ID information one by one in you files, such as:

```
GCF_003695465.1
GCF_016036915.1
GCF_003003695.1
GCF_011045685.1
GCF_014325982.1
```

## One step to sovle the problem

```
python refseq.py -i YOU_LIST_FILES_NAME -o YOU_OTUPUTFILES_NAME.csv -e YOU E-MAIL ADDRESS (such as:*******@*****.com)
#The E-mail address was requested by NCBI datbase, not me
```

## The output shuld like this

|RsUid|GbUid|AssemblyAccession|LastMajorReleaseAccession|LatestAccession|.....|
|-|-|-|-|-|-|
|15833318|15786928|GCF_009866865.1|GCF_009866865.1|.....|
|23960828|23909188|GCF_016065415.1|GCF_016065415.1|.....|
|6302018|6251988|GCF_003008635.1|GCF_003008635.1|.....|

In case of banning IP, the requesting time was set by 0.5s after each query.
## Command line parameters including(requested and essential)

|Argument|Useage|
|-|-|
|-i|your input files, you need to number them one by one |
|-o|your out put files, shuld name as ".csv"|
|-e|your E-mail address|

## Author
Cecli Fang @IUE.CAS
## If this scrip help you, please cite: 
