import json
import csv
import random
import argparse

# Allowed minute increments
allowed_minutes = sorted(set(
    [i for i in range(10, 301, 10)] + [i for i in range(15, 301, 15)]
))

# Add spoken-style exact phrases with known decimal hour values
spoken_variants = {
    "half an hour": 0.5,
    "an hour": 1,
    "an hour and a half": 1.5,
    "a quarter hour": 0.25,
    "three quarters of an hour": 0.75,
    "one and a quarter hours": 1.25,
    "two and a quarter hours": 2.25,
    "one and three quarters hours": 1.75,
    "two and a half hours": 2.5,
}

# Natural phrasing templates
time_phrases = [
    ("{} minutes", lambda m: m),
    ("{} mins", lambda m: m),
    ("{} hour", lambda h: h * 60),
    ("{} hours", lambda h: h * 60),
    ("{} hour and {} minutes", lambda h, m: h * 60 + m),
    ("{} hours and {} minutes", lambda h, m: h * 60 + m),
    ("about {} minutes", lambda m: m),
    ("around {} hours", lambda h: h * 60),
    ("just over {} minutes", lambda m: m),
    ("roughly {} hours and {} minutes", lambda h, m: h * 60 + m),
    ("a total of {} minutes", lambda m: m),
]

tasks = ["Read", "Write code before tomorrow", "Exercise by the end of the day", "Study", "Cook", "Clean the house by Wednesday", "Clean", "Shop", "Take a break", "Meditate", "Plan", "Walk the dog by Tuesday at 5pm","Walk the dog"]

def generate_dataset(num_samples=200):
    data = []

    # Add spoken variants
    for phrase, hours in spoken_variants.items():
        phrase = f"{random.choice(tasks)} for {phrase}"
        data.append({
            "input": phrase,
            "output": f"{hours:.2f}"  
        })

    # Generate randomly phrased durations
    for _ in range(num_samples):
        template = random.choice(time_phrases)
        text_template, minute_func = template

        total_minutes = random.choice(allowed_minutes)
        hours_part = total_minutes // 60
        minutes_part = total_minutes % 60

        if "and" in text_template:
            phrase = text_template.format(hours_part, minutes_part)
        elif "hours" in text_template or "hour" in text_template:
            combined_hours = round(hours_part + minutes_part / 60, 2)
            phrase = text_template.format(combined_hours)
        else:
            phrase = text_template.format(total_minutes)

        phrase = f"{random.choice(tasks)} for {phrase}"
        float_hours = total_minutes / 60
        data.append({
            "input": phrase,
            "output": f"{float_hours:.2f}"
        })

    # Add some irrelevant phrases with "empty" output
    data += [
        {"input": "Just Relax for a bit", "output": "empty"},
        {"input": "Go to the gym", "output": "empty"},
        {"input": "Take a nap", "output": "empty"},
        {"input": "Read a book before tomorrow", "output": "empty"},
        {"input": "What's the weather like?", "output": "empty"},
        {"input": "My favorite color is blue", "output": "empty"},
        {"input": "Watch a movie", "output": "empty"},
        {"input": "Listen to music", "output": "empty"},
        {"input": "Go to the park before 4pm", "output": "empty"},
        {"input": "Call a friend before 3", "output": "empty"},
        {"input": "Go for a walk", "output": "empty"},
        {"input": "Meditate", "output": "empty"},
        {"input": "Do some yoga", "output": "empty"},
        {"input": "Cook a meal", "output": "empty"},
    ]

    return data

def write_jsonl(data, path="spoken_time_data.jsonl"):
    with open(path, "w", encoding="utf-8") as f:
        for item in data:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")

def write_csv(data, path="spoken_time_data.csv"):
    with open(path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["input", "output"])
        for item in data:
            writer.writerow([item["input"], item["output"]])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate spoken time dataset")
    parser.add_argument("--samples", type=int, default=300, help="Number of random samples to generate (excluding fixed spoken phrases)")
    parser.add_argument("--output", type=str, default="spoken_time_data.jsonl", help="Output JSONL file path")
    args = parser.parse_args()

    dataset = generate_dataset(args.samples)
    write_jsonl(dataset, args.output)
    write_csv(dataset, args.output.replace(".jsonl", ".csv"))

    print(f"✅ Generated {len(dataset)} total examples in {args.output} and {args.output.replace('.jsonl', '.csv')}")

