import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin


class Pulse(BaseEstimator, TransformerMixin):

    def __init__(self, threshold=0):
        self._threshold = threshold

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return (X > self._threshold).astype(int)

    def fit_transform(self, X, y=None):
        return self.fit(X).transform(X)