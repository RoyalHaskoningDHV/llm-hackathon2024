# Large Language Models Workshop and Challenge 2024

The primary focus of this workshop is to provide hands-on experience with large language models. We will be using a project about `CPV-code classification` as a test case. Participants will split up into groups and work together to improve the multiclass classification performance of a classical NLP machine learning model.

# Agenda

- 9:15 – 9:45h: Lecture on Large Language Models
- 9:45 – 9:55h: Challenge specification
- 9:55 – 10:00h: Split into groups of 2-3
- 10:00 – 15:00h: Work on challenge
- 15:00 – 16:00h: Result Presentations and Group Discussion
- 16:00h onwards: Borrel and Prompt Injection Game

# The Challenge

The European Union requires tendering parties to assign so called common procurement vocabulary (CPV) codes to their tenders (read more [here](https://cpvcodes.eu/en/)). Since there are thousands of CPV-codes, it would be great if the author could get some help in choosing the most fitting option. In 2022, together with the municipality of Zwolle, we built a prototype machine learning model to accomplish this. The model was trained on tens of thousands of existing tenders (actually, there are 5 models, one for each level of the CPV code hierarchy). But its performance is not yet good enough to be useful in practice.

Today's challenge is to use Large Language Models to improve the performance of the classical ML model. For instance, a simple approach could be to get the best 20 or so predictions from the classical model and then improve on those using the an LLM.

# Template code

This repository contains a colab notebook called `llm_challenge_template.ipynb`. It contains template code you can use and some further instructions. Copy it and use it as you like.

Good luck!
