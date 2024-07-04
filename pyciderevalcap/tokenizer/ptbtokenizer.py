#!/usr/bin/env python
# 
# File Name : ptbtokenizer.py
#
# Description : Do the PTB Tokenization and remove punctuations.
#
# Creation Date : 29-12-2014
# Last Modified : Thu Mar 19 09:53:35 2015
# Authors : Hao Fang <hfang@uw.edu> and Tsung-Yi Lin <tl483@cornell.edu>

import os
import pdb # python debugger
import sys
import subprocess
import re
import tempfile
import itertools

# path to the stanford corenlp jar
STANFORD_CORENLP_3_4_1_JAR = 'stanford-corenlp-3.4.1.jar'

# punctuations to be removed from the sentences
PUNCTUATIONS = ["''", "'", "``", "`", "-LRB-", "-RRB-", "-LCB-", "-RCB-", \
        ".", "?", "!", ",", ":", "-", "--", "...", ";"] 

class PTBTokenizer:

    def __init__(self, _source='gts'):
        self.source = _source

    def tokenize(self, captions_for_image):
        cmd = ['java', '-cp', STANFORD_CORENLP_3_4_1_JAR, \
                'edu.stanford.nlp.process.PTBTokenizer', \
                '-preserveLines', '-lowerCase']


        sentences = None 
        if self.source == 'gts':
            image_id = [k for k, v in captions_for_image.items() for _ in range(len(v))]
            sentences = '\n'.join([c['caption'].replace('\n', ' ') for k, v in captions_for_image.items() for c in v])
            final_tokenized_captions_for_image = {}


        elif self.source == 'res':
            index = [i for i, v in enumerate(captions_for_image)]
            image_id = [v["image_id"] for v in captions_for_image]
            sentences = '\n'.join(v["caption"].replace('\n', ' ') for v in captions_for_image )
            final_tokenized_captions_for_index = []

        path_to_jar_dirname=os.path.dirname(os.path.abspath(__file__))

        tmp_file = tempfile.NamedTemporaryFile(delete=False, dir=path_to_jar_dirname, mode='w', encoding='utf-8')

        tmp_file.write(sentences)
        tmp_file.close()


        cmd.append(os.path.basename(tmp_file.name))

        # print(cmd)
        # print(path_to_jar_dirname)

        p_tokenizer = subprocess.Popen(cmd, cwd=path_to_jar_dirname, \
                stdout=subprocess.PIPE)

        sentences_bytes = sentences.rstrip().encode('utf-8')

        token_lines = p_tokenizer.communicate(input=sentences_bytes.rstrip())[0]    
        lines = token_lines.split(b'\n')

        os.remove(tmp_file.name)

        if self.source == 'gts':
            for k, line in zip(image_id, lines):
                if not k in final_tokenized_captions_for_image:
                    final_tokenized_captions_for_image[k] = []
                tokenized_caption = ' '.join([w for w in line.rstrip().decode('utf-8').split(' ') \
                        if w not in PUNCTUATIONS])
                final_tokenized_captions_for_image[k].append(tokenized_caption)

            return final_tokenized_captions_for_image

        elif self.source == 'res':
            for k, img, line in zip(index, image_id, lines):
                tokenized_caption = ' '.join([w for w in line.rstrip().decode('utf-8').split(' ') \
                        if w not in PUNCTUATIONS])
                final_tokenized_captions_for_index.append({'image_id': img, 'caption': [tokenized_caption]})

            return final_tokenized_captions_for_index
