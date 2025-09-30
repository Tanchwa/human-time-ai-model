# Machine Learning Model Server for my [Todoist to Reclaim Webhook](github.com/tanchwa/Todoist-Reclaim-Webhook)

## Purpose
This code will serve a fine tuned inference model based on google/flan_t5_small, and translate human input time to a format that the Reclaim.ai API expects to receive. 

## Methodology
the /utils directory has a python script to auto generate the training data used to fine tune the model. 
I started with [Google's Flan t5 small](https://huggingface.co/google/flan-t5-small)

## Use
Download the Docker Image from ...
This is designed to be used in conjunction with the webhook application.
