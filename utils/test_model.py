from transformers import T5Tokenizer, T5ForConditionalGeneration
import argparse

model_path = "../t5_small_human_time_model"
tokenizer = T5Tokenizer.from_pretrained(model_path)
model = T5ForConditionalGeneration.from_pretrained(model_path)


def predict_decimal_hours(text):
    input_ids = tokenizer(f"Convert time to decimal hours: {text}", return_tensors="pt").input_ids
    output_ids = model.generate(input_ids, max_new_tokens=16)
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test the trained model with custom input.")
    parser.add_argument("--input", type=str, required=True, help="Input text to be processed by the model.")
    args = parser.parse_args()

    test_phrase = args.input
    predicted_text = predict_decimal_hours(test_phrase)
    
    print(f"Input: {test_phrase}")
    print(f"Predicted Output: {predicted_text}")
