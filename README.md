(CIDEr)Consensus-based Image Description Evaluation
===================

This repository contains CIDEr implementation supporting Python 3.

## Usage ##

First place the folder name of ground-truth captions as **refName** and that of generated captions as **candName** in ```params.json``` as shown below:

```json
{
	"pathToData": "data/",
	"refName": "result_gt_transformer.json",
	"candName": "result_ref_transformer.json",
	"resultFile": "results.json",
	"idf": "coco-val-df"
}
```

Both files have the same format as shown below:

```json
[{"image_id": "0", "caption": "<START> an open refrigerator door and some bottles and a bag <END>"}, {"image_id": "1", "caption": "<START> a large truck parked on the cement in front of a building <END>"}, {"image_id": "2", "caption": "<START> a group of people outdoors at a park <END>"}]
```

Note the **image_id**s must match within corresponding pairs across the ground-truth and generated captions.


Then run the following command to output average CIDEr score of your generated captions:

```bash
python3 cidereval.py
```

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



## CIDEr-D ##

Also CIDEr-D scores can be calculated using ```cider-ciderD``` branch.

## Citation ##

This work is done by converting the code files of [cider](https://github.com/vrama91/cider) repository from Python2 to Python3.

```
Copyright (c) 2015, Xinlei Chen, Hao Fang, Tsung-Yi Lin, and Ramakrishna Vedantam
All rights reserved.
```