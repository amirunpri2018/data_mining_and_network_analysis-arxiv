# Description

Each file in [single.zip](https://drive.google.com/file/d/0B8yQRmV2S-ZLNGJObFJPWlItVmM/view?usp=sharing) 
represents coauthorship graph formed from single year publications.

# Community finding : cfinder

Communities were looked for with commandline version of cfinder. 

Minimum edge weights (common publications between authors) considered were following:
- 1 for graphs from 1991 to 1999
- 3 for graphs from 2000 to 2010
- 5 for graphs from 2011 onwards

Command used: 

```
CFinder_commandline64.exe -i path/to/graph.csv -o path/to/output_folder -w miminum_weight -W 1000 -U -t 2
```

[Generated data](https://drive.google.com/file/d/0B8yQRmV2S-ZLN3l2ZlNJX0Y4ck0/view?usp=sharing)

# Centrality

## Betweeness centrality



## Eigencentrality
