

from datasets import Dataset
from transformers import AutoTokenizer

def prepare_crop_dataset(input_file, output_file, tokenizer_name="meta-llama/Llama-2-7b-hf"):
    """Prepare crop price dataset for fine-tuning."""
    # Load data
    import pandas as pd
    data = pd.read_csv(input_file)

    # Convert to Hugging Face Dataset
    dataset = Dataset.from_pandas(data)

    # Tokenize the data
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
    def tokenize_function(example):
        return tokenizer(example["Query"], text_pair=example["Response"], truncation=True)

    tokenized_dataset = dataset.map(tokenize_function, batched=True)

    # Save processed dataset
    tokenized_dataset.save_to_disk(output_file)
    print(f"Dataset saved at {output_file}")

# Example Usage
# prepare_crop_dataset("crop_prices.csv", "processed_crop_dataset")
