
from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments
from datasets import load_from_disk

def fine_tune_crop_model(dataset_path, output_dir, model_name="meta-llama/Llama-2-7b-hf"):
    """Fine-tune Llama 2 for crop price prediction."""
    # Load dataset
    dataset = load_from_disk(dataset_path)

    # Load tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    # Training arguments
    training_args = TrainingArguments(
        output_dir=output_dir,
        evaluation_strategy="epoch",
        learning_rate=5e-5,
        num_train_epochs=3,
        per_device_train_batch_size=4,
        save_total_limit=1,
        save_steps=500,
        logging_steps=100,
        fp16=True
    )

    # Trainer setup
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
        eval_dataset=dataset,
        tokenizer=tokenizer
    )

    # Fine-tuning
    trainer.train()
    trainer.save_model(output_dir)
    print(f"Model fine-tuned and saved to {output_dir}")

# Example Usage
# fine_tune_crop_model("processed_crop_dataset", "llama2_crop_price_model")
