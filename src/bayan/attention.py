"""Lab 2 starter: scaled dot-product attention and multi-head attention."""


import torch
import math


def attention(q, k, v, mask=None):
    d_k = q.size(-1)

    scores = torch.matmul(q, k.transpose(-2, -1))
    scores = scores / math.sqrt(d_k)

    if mask is not None:
        scores = scores.masked_fill(mask == 0, float("-inf"))

    weights = torch.softmax(scores, dim=-1)

    return torch.matmul(weights, v)