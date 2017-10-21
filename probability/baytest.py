from __future__ import division
#Bayes Theorum
#simple example in python

healthy_population = 0.99 #p(no cancer)
cancer_population = 0.01 #p(cancer)
cancer_test_false_positive = 0.05 #p(no cancer|+)
cancer_test_false_negative = 0.05 #p(cancer|-)
cancer_test_positive_rate = 0.95 #p(+|cancer)

#probability that someone has cancer if they tested positve
#P(cancer|+) =

numerator = cancer_test_positive_rate * cancer_population
denominator = (cancer_test_positive_rate * cancer_population) \
            + (cancer_test_false_positive * healthy_population) 
print numerator / denominator


