---
title: "One Tiny Step Further in Model Learning"
summary: "Notes on how to learn modeling by reading broadly and thinking about process."
date: "2021-02-05"
authors:
  - admin
tags:
  - Modeling
  - Learning
  - Advice
---

In the past several months, I have been trying to develop a model with my advisor Cristina Moya to capture both the identity-driven polarization and the biased social learning process of public discussion dynamics. The model-developing process is challenging but it has been surprisingly helpful for me to understand the aesthetics of a good model and the meaning of true emergence. I summarized a few tips for model learners who are stuck.

## Read a lot of models

We all know the importance of reading other models but when you’re new in the modeling world, it is hard to know what to read. My suggestion is to start with one book in your field that summarizes the classical models you need to know (in my case, it’s Culture and the Evolutionary Processes, the only book I brought with me during the summer vacation). Question-driven reading is more effective. For example, I’m interested in both identity signaling and information transmission and thus I read about recent signaling models, coordination models, social learning models, and their empirical applications. Further on, I realized that I don’t have to be bounded to the topic but focus on the process, so I started to read models that can generate runaway processes. A large amount of literature is fundamental to cultivating a “sense of modeling”.

## Understand the real mechanisms

Sometimes we need to focus on specific aspects when reading other people’s papers. The most important thing is not to see how realistic their assumptions are (other modelers may disagree) but to understand which mechanisms produce their results. Sometimes, modeling papers might make bigger claims than they actually can because the mechanisms are not explicated clearly. I often think this is a great advantage of modeling compared to verbal theories. Because once the model is written, you will be able to understand the weirdest result produced through it.

Annotated literature reviews are great, but have you tried annotated model reviews? 😉

## Make analogies

Once you understand the mechanisms and you’re eager to adapt and extend, it’s time to make analogies from one abstract domain to another abstract domain. You need to resist the temptations of just writing down inspirations and philosophies from the models you just learned and started to think about the meanings of specific variables and processes. Sometimes it gets really weird when the contexts are very far from each other. In my case, it’s when I want to map sexual selection into sender-receiver interaction, or when I think of the actual cost to fitness when people chase misinformation. How can they work? Isn’t that too arbitrary? But actually, this is the space you can use your creativity to write more context-related process or connect it with field-specific theories.

## Do both the analytical solution and computational simulation (the drift can do much)

The next step is to write up the model! There are plenty of materials out there to help you write down a mathematical model (check out Mathematical Models of Social Evolution and a friend’s recommendation Matrix Population Models) or code up a computational model (Introduction to ABM course). In my opinion, computational models are necessary for understanding social and evolutionary processes. In my project, I didn’t realize that any tiny drift can lead to the instability of one group of the population before I did agent-based modeling, and now it has become a core question in understanding identity-driven processes. The computational models not only add stochasticity but also test whether the system is resilient to stochasticity. Results possible in numerical simulation might not be possible in computational simulation.

## Explain to people who don’t model

Pretty much the Feynman method. Or better, present to an academic audience who don’t model. The field of communication I interact with is mostly empirical. The advantage of presenting your model to an empirical audience is that you can learn what you don’t know about your model and get a lot of specific questions with specific examples. I believe these empirical questions are necessary, especially for you to think further about the applicability of your model and how likely your model is telling some obvious fact that does not require a modeling mind. To do this type of presentation, you need to at least prepare a concise answer to the question “Why do you need to build a model”? Because you will get that question for sure.
