"""Lab 2 starter: parameter accounting for mBERT and CAMeLBERT."""


from transformers import AutoModel

def audit(checkpoint: str) -> dict:
    model = AutoModel.from_pretrained(checkpoint)

    buckets = {
        "embeddings": 0,
        "attention": 0,
        "ffn": 0,
        "norms": 0,
        "pooler": 0,
        "other": 0,
    }

    for name, param in model.named_parameters():
        n = param.numel()

        if "embedding" in name.lower():
            buckets["embeddings"] += n
        elif "attention" in name.lower():
            buckets["attention"] += n
        elif "intermediate" in name.lower() or "output.dense" in name.lower():
            buckets["ffn"] += n
        elif "layernorm" in name.lower():
            buckets["norms"] += n
        elif "pooler" in name.lower():
            buckets["pooler"] += n
        else:
            buckets["other"] += n

    return buckets

if __name__ == "__main__":
    for ckpt in [
        "bert-base-multilingual-cased",
        "CAMeL-Lab/bert-base-arabic-camelbert-mix",
    ]:
        print(ckpt, audit(ckpt))
