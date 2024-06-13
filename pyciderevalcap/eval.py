__author__ = 'rama'
from pyciderevalcap.tokenizer.ptbtokenizer import PTBTokenizer
from pyciderevalcap.cider.cider import Cider


class CIDErEvalCap:
    def __init__(self, gts, res, df):
  
        tokenizer = PTBTokenizer('gts')
        _gts = tokenizer.tokenize(gts)

        tokenizer = PTBTokenizer('res')
        _res = tokenizer.tokenize(res)

        self.gts = _gts
        self.res = _res
        self.df = df

    def evaluate(self):

        method = "CIDEr"
        scorer = Cider(df=self.df)

        metric_scores = {}

        print('computing %s score...' % (scorer.method()))

        score, scores = scorer.compute_score(self.gts, self.res)
        print("Mean %s score: %0.3f" % (method, score))
        metric_scores[method] = list(scores)
        return metric_scores
