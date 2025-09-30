# Machine Learning Model Server for my [Todoist to Reclaim Webhook](github.com/tanchwa/Todoist-Reclaim-Webhook)

## Purpose
This code will serve a fine tuned inference model based on google/flan_t5_small, and translate human input time to a format that the Reclaim.ai API expects to receive. 

## Methodology
the /utils directory has a python script to auto generate the training data used to fine tune the model. 
I started with [Google's Flan t5 small](https://huggingface.co/google/flan-t5-small)

## Use
### Training the Model
clone the repo and `cd ./human-time-ai-model/utils`
run `python3 dataset_generator.py --samples ###` to generate a dataset. By default, it will output this to a file called `spoken_time_data.jsonl` 
run the command again with `--output spoken_time_data_validation.jsonl` to generate a validation set. 

You can then use the `training.py` script to run the fine tuning.
### Running the Model Server
~~Download the Docker Image from ... not yet available~~

This is designed to be used in conjunction with the webhook application.
