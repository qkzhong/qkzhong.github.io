---
title: Five Thoughts on Modeling
subtitle: null
date: 2022-July 22-13T 00:00:00Z
summary: >-
  Recently I attended the grad workshop of computational social science at SFI
  and met some amazing friends and the wonderful John Miller and Scott Page. In
  the short two weeks of time, I’ve learned from those great thinkers and
  thought through my own approach to modeling. Here are some of the things I
  just came to understand or now understand better.




  1. **Start simple** 


  As the first principle of modeling, starting simple is the thing I’ve known since the beginning but never actually do well. On the first day of the SFI workshop, we were assigned a homework task to model a question with a homework partner within 15 hours. My teammate and I kept telling each other, “let’s just start simple,” and yet ended up with more than 10 parameters and two levels of modeling within the first hour of discussion. How did that happen? I reviewed our model-building process and found that it has something to do with the abstraction process. I usually begin by thinking about what kind of macro phenomenon we want to address in the model and what is actually happening in this process. Then I use lines and lines of equations to represent the utility of individuals and groups and how they update their behavioral choices or values. It always ends up with complex and messy models.


  The problem with this approach is that it does not try to simplify reality and makes abstraction very difficult. The easiest way to get to abstraction is by thinking first about the simple, elegant models everyone admires, Schelling’s segregation model, Epstein & Axtell’s Sugarscape model, etc. Or fundamental game theory models: prisoner’s dilemma, dove-hawk games, etc. Those models are classic because they capture some of the most fundamental behavioral principles. Then deconstruct the real-world problem into a set of classic modeling problems. For example, my working model of self-censorship that concerns the importance of uncertainty is actually a combination of coordination games, social learning, and complex contagion. I can then mix and match those models and connect them with context-specific mechanisms. In this way, I model the social system by maximum simplification and abstraction from the beginning and then build up from those simple processes. 


  The advantage of modeling in this approach is that we can be more clear about how each part of the model works and better control the parameters and processes. This is not the only way for beginners to approach modeling, but it can be one of the easiest ways. A few years ago, my professor recommended me to study through all the models in NetLogo libraries, and of course, I didn’t do it. Now I get why I wasn’t a better modeler.


  **2. Situate the model in a context** 


  Starting simple is great, but if your model is simple and elegant from beginning to end, it’s very likely your model looks very similar to someone else’s model, even on the very topic you study. I had a terrible experience in a conference where someone presented a very similar model right after my presentation. I then think a lot about why our models got similar to each other and how to avoid it as a beginner. One reason is that there are only this many combinations of models. I do not have a strong background in Math, so my experience and familiarity with math limit how I express the relationship between components of a system and the combination of basic models. Now I’m convinced that there would always be an existing model that is very similar to whatever I am modeling right now but very likely better. 


  Another reason models got similar is that when we model a social system to answer a question, at exploratory stages, we may need to sweep through a lot of environmental parameters to understand how the model work. If two research on the same subfield happens to be both at this stage, a disaster might happen when they present together. 


  To avoid situations like this, we can get more familiar with models that are usually used in our fields (too bad my field doesn’t really have a modeling tradition). In that way, when models get similar, we can at least be aware of where that’s coming from. But an easier way to deal with it is to situate our model in a specific context. The advantage is twofold. First, we can better articulate the mechanism and ask better research questions to make the most out of modeling. Second, it will help the audience to understand the model better and understand why this model needs to exist. Bonus point is that it will give the model a flavor. Sometimes my models can be quite boring but by adding a story or context on top, it seems way more meaningful. 


  **3. Many iterations** 


  The many iteration approaches sound straightforward in agent-based modeling because we often say that we need to try out different things and try to compare which approach captures the mechanism and produces the emergence. But the mistake I made back then was to think of it as a one-step run. In other words, I build one version of the model and see if it works; if not, I build another version of it. If it does work, I try to build it into a paper. What I learned at SFI this time is that iterations can be used as one of the many steps in a pipeline to build up models. To see if a complex system captures the mechanism of a real-life mechanism, I always build up the system first and then try to develop or use the measures from the model to see if my hypotheses stand. This approach often ends up with me not being able to find the right measure in the model and wondering forever if this is an appropriate model. Instead, a multi-step iteration pipeline requires us to build parts of the complex system first and see if this part produces the exact intermediate results as expected. For example, in evolutionary models, because of the convenience of the theoretical framework, we can actually build in variation, transmission, and selection step by step to see how fitness varies, how selective forces change the frequency of cultural traits, and how cumulative changes happen in different conditions. 


  **4. Many models and extensions**


  I was inspired a lot by Scott’s talk on the many models approach, which pointed out how much we might miss using a single-model approach. As someone who’s trained mostly in (linear) empirical research, I often fear complex system and the “many models” approach may lead me to fall into the trap of “everything is related to everything” and not be able to identify the most important linear relationship or miss the variable that accounts for most of the variance. Yet, in social science, it is true that everything is related to everything, and it is nearly impossible to use one line of the model to explain everything in a system. Practically it’s also a dilemma. You cannot write a hundred models in a paper to explain one thing, but one model is usually too thin as an explanation.


  So what do we do to consider both sides? 


  The standard way of doing it is to have one base model and build extensions on top of the model. I understood this process for a long time but never truly got the logic. Now inspired by the “many models” approach, I understand extensions as a possibility for the base model to connect with other models. By incorporating other mechanisms in the base model, we can show how much it takes for this model to work with other models to explain the current phenomenon and how much does out take for the base model to be truly generalizable. This approach also helped me solve a problem I have had for a long time: it’s very difficult for me to find empirical evidence to support the model because I cannot find a perfect mapping to the mechanism. However, when I open up possibilities for my base model by connecting it with other models and analyzing how it works together with other mechanisms, it’s easier to find an empirical mapping to the model.


  **5. Means, variances, and shapes**


  Everyone wants phase transitions, shifting equilibrium, or tipping points from their model because those are exciting things in complex systems, and they are one of the main reasons why agent-based models are so attractive. After many failed experiments, one thing became clear to me: even when we cannot shift the equilibrium or find a tipping point, the shape of parameter dynamics, the convergence speed, and the difference in variance is equally interesting, especially when we analyze social systems.  In my work, I have three reasons to care about things other than phase transition and shifting equilibrium.


  (1)Mean statistics are important, but other statistics, including min, max, and variance, are also important, especially when we are analyzing risks, vulnerability, and resilience and when using the current model result to build the next step in the pipeline (the many iterations!).


  (2)The trend is important. Even when mean and variance are the same, sometimes it still means very different things when the trend is different, or in other words, their position in the dynamical system is different.


  (3) Shape provides information for intervention. Understanding the shape of change and estimating the conversion speed can help us make policy decisions on when policy intervention should step in and how much time and space the change leave for policy to work. 


  Those five points are concluded from my thoughts in those two weeks as a beginner in modeling. I am still thinking through some confusions I have during this time and plan to write about in the following blog articles. The first is how we endogenize parameters. In social science, few things are completely exogenous, and that’s why natural experiment design is difficult. Sometimes I endogenize parameters to get oscillation without a true purpose. I’m now trying to think of endogenization more systematically. The second is how we should think of stochasticity. A lot of times, ABM is different from formal models in that it builds on stochasticity in individual agents. How we make sense of that stochasticity in solving social science problems still remains unclear to me. Hopefully, I will write them up soon in the next blog article.**\***


  \*Some resources that inspired me and help me build up my thoughts include: 


  Epstein, J. M. (2008). [Why model?](https://www.jasss.org/11/4/12.html) ; Smaldino, P. E. (2020).[ How to translate a verbal theory into a formal model. ](https://psycnet.apa.org/record/2020-64973-002); Page, S. E. (2018). [*The model thinker: What you need to know to make data work for you*.](https://books.google.com/books?hl=en&lr=&id=iWRPDwAAQBAJ&oi=fnd&pg=PT8&dq=the+model+thinker&ots=jELK0atSQt&sig=EiuQI_3XiwvG73cxflHmljHOqfc#v=onepage&q=the%20model%20thinker&f=false)


  [C﻿heck my blog *Self-made Modeler* for more content!](selfmademodeler.wordpress.com)
draft: false
featured: false
authors:
  - Qiankun
lastmod: 2022-July 22-13T 00:00:00Z
tags:
  - Academic
  - Modeling
categories:
  - Blog
projects: []
image:
  caption: "Image credit: [**Unsplash**](https://unsplash.com/photos/CpkOjOcXdUY)"
  focal_point: ""
  placement: 2
  preview_only: false
---
## Overview

Recently I attended the grad workshop of computational social science at SFI and met some amazing friends and the wonderful John Miller and Scott Page. In the short two weeks of time, I’ve learned from those great thinkers and thought through my own approach to modeling. Here are some of the things I just came to understand or now understand better.