## Project 4. Bayes' Nets (inference in BN)
- we have packman and 2 houses: food house (*mostly* blue) and 
ghost house (*mostly* red); houses are initially invisible; 
- packman can make observations: 'none', 'red' and 'blue' (???)
- we are given the structure of BN;
- the goal is to implement variable elimination step by step;

- questions: what exactly does pachman try to infer? does he recalculate 
after each observation?

### questions 1-2
* construct BN with given structure; fill in CPTs;

### questions 3-5
* here we implement basic operations for factors: `join`, `eliminate` and
`normalize`;
