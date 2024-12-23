### Before Starting...

For gathering the necessary data needed for the answers, I made use of the following script:

```bash

```

I am not sure if the idea was to obtain the result in some other way and if so, I would appreciate clarification on how i should have done it. Unless specified otherwise, the script was run with an array of 32768 elements and a sample of 1000, with the number of cores being the only non-constant variable.

### Question 1

For algorithm 1, does increasing the number of threads improve performance or hurt performance? Use data to back up your answer.

### Answer 1

| #threads    | avg time (ms) |
| ----------- | ------------- |
| 1           | .2405329      |
| 2           | .5290084      |
| 4           | .6647673      |

It would seem that, as the number of threads increases, the performance decreases, I would assume this is mainly due to the multiple optimizations used in the following implementations and aren't yet taken advantage of.

### Question 2

(a) For algorithm 6, does increasing the number of threads improve performance or hurt performance? Use data to back up your answer.

(b) What is the speedup when you use 2, 4, 8, and 16 threads (only answer with up to the number of cores on your system).

### Answer 2

(a)

| #threads    | avg time (ms) |
| ----------- | ------------- |
| 1           | .2382078      |
| 2           | .1843114      |
| 4           | .1730445      |

With all the optimizations now in use, it seems that the threads are able to spread the workload properly, leading to an increase in performance.

(b)

Calculating the speedup with the formula $S = \frac{T_1}{T_N}$, where $T_1$ is the time for a single thread and $T_N$ is the time for $N$ threads, we observe that:

- For 2 threads, there is a speedup of around 1.2928
- For 4 threads, it is around 1.3768

### Question 3

(a) Using the data for all 6 algorithms, what is the most important optimization, chunking the array, using different result addresses, or putting padding between the result addresses?

(b) Speculate how the hardware implementation is causing this result. What is it about the hardware that causes this optimization to be most important?

## Question 3

(a) To answer this, I'll first gather the necessary data:

- Algorithm 1

    | #threads    | avg time (ms) |
    | ----------- | ------------- |
    | 1           | .2405329      |
    | 2           | .5290084      |
    | 4           | .6647673      |

- Algorithm 2

    | #threads    | avg time (ms) |
    | ----------- | ------------- |
    | 1           | .2872724      |
    | 2           | .5242676      |
    | 4           | .6797561      |

- Algorithm 3

    | #threads    | avg time (ms) |
    | ----------- | ------------- |
    | 1           | .2405329      |
    | 2           | .5290084      |
    | 4           | .6647673      |

- Algorithm 4

    | #threads    | avg time (ms) |
    | ----------- | ------------- |
    | 1           | .2877619      |
    | 2           | .5262861      |
    | 4           | .6122215      |

- Algorithm 5

    | #threads    | avg time (ms) |
    | ----------- | ------------- |
    | 1           | .2896591      |
    | 2           | .1806251      |
    | 4           | .1700417      |

- Algorithm 6

    | #threads    | avg time (ms) |
    | ----------- | ------------- |
    | 1           | .2382078      |
    | 2           | .1843114      |
    | 4           | .1730445      |

With this data, we can observe that it is algorithm 5 (i.e padding between result adresses) the optimization that is the most impactful

(b) My guess as to why this may be the case is that it's likely related to needing to maintain cache coherency, if this implementation was not present, each thread would have to continually be invalidating the line corresponding to the address each time another thread attempts to access it to modify it.

