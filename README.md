# Machine Learning Model Server for my [Todoist to Reclaim Webhook](github.com/tanchwa/Todoist-Reclaim-Webhook)

## Purpose
This code will serve a fine tuned LLM based on Meta's Llama 3 Model, and translate human input time to a format that the Reclaim.ai API expects to receive. 

## Methodology
the /utils directory has a python script to auto generate the training data used to fine tune the model. 
I started with [Meta's Llama 3.1 8B Param Model](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B)

## Use
Download the Docker Image from ...
This is designed to be used in conjunction with the webhook application.
