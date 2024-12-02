
from transformers import AutoModelForCausalLM, AutoTokenizer

def evaluate_crop_model(model_dir, queries):
    """Evaluate the fine-tuned model with sample crop price queries."""
    tokenizer = AutoTokenizer.from_pretrained(model_dir)
    model = AutoModelForCausalLM.from_pretrained(model_dir)

    for query in queries:
        inputs = tokenizer(query, return_tensors="pt")
        outputs = model.generate(inputs.input_ids, max_length=50)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        print(f"Query: {query}")
        print(f"Response: {response}")

# Example Usage
# evaluate_crop_model("llama2_crop_price_model", ["What is the price of rice?", "Will onion prices fall?"])

