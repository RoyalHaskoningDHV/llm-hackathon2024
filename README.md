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

# Data

You can download the data used to train the classical ML model from this [link](https://stllmchallenge2024.blob.core.windows.net/data/data_clean_ted_plus_tenderned.csv?sp=r&st=2024-09-04T11:30:19Z&se=2024-09-11T19:30:19Z&spr=https&sv=2022-11-02&sr=b&sig=C8cSMMAO4f6KVUqE1sJmZU6lEu8Wx9xv6FGGxcwM6e4%3D). It is already "cleaned" and a combination of tenders from TenderNed and TED. The TED tenders were translated to Dutch and come from the following countries: Germany, Sweden and the UK. Also note this [list](https://stllmchallenge2024.blob.core.windows.net/data/20220623%20AB%20volledige%20lijst%20CPV-codes%20gemeente%20Zwolle.xlsx?sp=r&st=2024-09-04T11:35:42Z&se=2024-09-11T19:35:42Z&spr=https&sv=2022-11-02&sr=b&sig=RQ8jHrS%2Fz4GxL5Nsl7I1JKRcTpkuGh81kdFOhsgO%2FnQ%3D) of most relevant codes for the municipality of Zwolle. This list will be important also in the scoring of your solution (see below).

# Template code

This repository contains a colab notebook called `llm_challenge_template.ipynb`. It contains template code you can use and some further instructions. Copy it and use it as you like.

# Scoring

To decide who the winner is we will look at recent tenders published on TenderNed. To be clear, any team who retrieves and uses data from after January 2024 from TenderNed is automatically disqualified from the competition. CPV codes most valued by the municipality of Zwolle are given a higher weight, so getting those right is more important than other codes. Similarly, getting codes right at a higher CPV code level of detail will give more points.

# Presenting results

Each team will have a chance to present their experience and results between 15-16h. Teams are free to create powerpoint presentations of max. 1 slide to support their presentation.

Good luck!
