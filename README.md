(CIDEr)Consensus-based Image Description Evaluation
===================

This repository supports python 3.

## Usage ##

### Folder ###

```
.
├── README.md
├── cidereval.py
├── data
│   ├── coco-val-df.p
│   ├── gt.json
│   └── rf.json
├── params.json
├── pyciderevalcap
│   ├── __init__.py
│   ├── cider
│   │   ├── __init__.py
│   │   ├── cider.py
│   │   └── cider_scorer.py
│   ├── eval.py
│   ├── eval.pyc
│   └── tokenizer
│       ├── __init__.py
│       ├── ptbtokenizer.py
│       └── stanford-corenlp-3.4.1.jar
├── pydataformat
│   ├── __init__.py
│   ├── jsonify_refs.py
│   └── loadData.py
└── results.json
```

### Calculate CIDEr score ###
```python3 cidereval.py```


## Citation ##

```
Copyright (c) 2015, Xinlei Chen, Hao Fang, Tsung-Yi Lin, and Ramakrishna Vedantam
All rights reserved.
```