'''

Author: Peter Chip (furamail001@gmail.com)

Date: 2015 03 24

Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

Theory: It looks for the probability of all the events that can cause a recessive offspring (first pick: Aa -> second pick: Aa or Aa -> aa or aa->aa or aa -> Aa And divides them with the appropriate number based on the punet table.
        The product of Aa -> aa and Aa -> aa gets the the probability of of getting a recessive offspring with the Aa as the first pick.
        The sum of aa_probability and Aa_probability is the total number of recessive outcumes.
        1 - the total number of recessive outcome is the probability of a dominant offspring.

'''

# Number of each genotype AA Aa aa and the total number of subjects.
number_of_dominant = 24
number_of_heterozygote = 18
number_of_recessive = 26
number_of_all = number_of_dominant + number_of_heterozygote + number_of_recessive

aa_probability = ((number_of_heterozygote / number_of_all)*(number_of_recessive/(number_of_all-1)))/2 + ((number_of_recessive/number_of_all)*((number_of_recessive-1)/(number_of_all-1)))

Aa_probability = ((number_of_heterozygote/number_of_all)*((number_of_heterozygote-1)/(number_of_all-1))/4)+ ((number_of_recessive/number_of_all)*(number_of_heterozygote/(number_of_all-1))/2)

dominant_probability = 1 - (aa_probability + Aa_probability)

print(dominant_probability)