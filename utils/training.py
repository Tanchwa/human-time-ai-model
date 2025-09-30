from datasets import load_dataset 
from transformers import T5Tokenizer, T5ForConditionalGeneration, Trainer, TrainingArguments

model_name = "google/flan-t5-small"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

dataset = load_dataset("json", data_files={
    "train": "spoken_time_data.jsonl",
    "validation": "spoken_time_data_validation.jsonl"
})

def preprocess(examples):
    # Combine into T5-style text-to-text instruction
    inputs = [f"Convert time to decimal hours: {x}" for x in examples["input"]]
    targets = [str(y) for y in examples["output"]]  # always strings

    return {"input_text": inputs, "target_text": targets}

dataset = dataset.map(preprocess, batched=True)

def tokenize_function(examples):
    model_inputs = tokenizer(
        examples["input_text"], max_length=64, truncation=True, padding="max_length"
    )
    labels = tokenizer(
        examples["target_text"], max_length=16, truncation=True, padding="max_length"
    )
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

tokenized_dataset = dataset.map(tokenize_function, batched=True)



training_args = TrainingArguments(
    output_dir="../t5_small_human_time_model",
    eval_strategy ="epoch",
    learning_rate=2e-4,
    per_device_train_batch_size=16,
    save_steps=100,
    save_total_limit=1,
    logging_steps=10,
    num_train_epochs=25,
    weight_decay=0.01,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],
    eval_dataset=tokenized_dataset["validation"],
)

trainer.train()
trainer.save_model("../t5_small_human_time_model")
tokenizer.save_pretrained("../t5_small_human_time_model")
