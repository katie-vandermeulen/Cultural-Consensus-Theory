## Structure and Choices

The model defines three functions: loading the data, running the model, and outputting the results. These functions are used in the main model block to run the CCT analysis.

Within the **run_model** function, I defined the priors for D and Z as uniform and bernoulli respectively. For D, a uniform prior is most accurate for reflecting informants' knowledge. It makes it so that it is equally likely for the informant to have no prior knowledge, for the informant to have full prior knowledge, and for the informant to have any level of prior knowledge in between. For Z, a bernoulli prior is most accurate because the correctness of an answer is a binary value. The informant can respond correctly (1) or incorrectly (0).

## Results and Checks
The informants are split directly in half with 5 of them having higher competence and 5 of them having lower competence. Informant 6 had the highest competence (0.870) while informant 3 had the lowest competence (0.561). With greater prior knowledge comes greater competence or correctness. This means that informant 6 is most likely to give a correct answer, and informant 3 is less likely to give a correct answer. This does not mean informant 3 will certainly answer incorrectly, but it means they have a lower chance. The CCT model puts more weight on informants with greater competence, because within the "plant knowledge" culture, the informants who are more competent are more likely to agree and understand the shared cultural consensus.

For the consensus answers, a mean closer to 0 indicates that the culture agrees that the answer is false. A mean closer to 1 indicates that the culture agrees the answer is true. Consensus answers that are closer to the middle (~0.5) indicate that even among competent informants the agreed upon answer is divided. This can be seen in item 5 (0.579).

When looking at the Diagnostics Summary, every **r_hat** value is 1.00, or close enough. This suggests that the model did in fact converge. Convergence means that the samples drawn in the **run_model** block are reliable for estimating competence and consensus.

## Discussion
The simple majority vote is taken from the raw data. This just calulates the majority answer without factoring in competence level. This simple majority vote therefore differs from the consensus. For example, in questions 2, 6, 8, and 10 the consensus gave the correct answer, however the majority vote gave the incorrect answer. This shows how in the CCT model, competence influences the consensus.