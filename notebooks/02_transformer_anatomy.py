"""Lab 2 starter notebook-as-script.
Complete the marked sections, verify numerical equivalence, inspect parameter
accounting, causal masking, attention heads and pad-attention leakage.
"""


import torch

from bayan.attention import attention


def main():
  

  
    torch.manual_seed(42)
    mask = torch.tril(torch.ones(4, 4))

    q = torch.randn(1, 1, 4, 8)
    k = torch.randn(1, 1, 4, 8)
    v = torch.randn(1, 1, 4, 8)

    output = attention(q, k, v, mask=mask)

    print("Attention output:")
    print(output)
    print("Shape:", output.shape)
    print(mask)



if __name__ == "__main__":
    main()