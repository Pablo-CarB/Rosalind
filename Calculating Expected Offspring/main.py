
# each input corresponds to the number of couples in a population possessing a genotype 
# pairing for a given factor, every couple has exactly two offspring. 
# The output is the expected number of children with dominant phenotype
def rand_variable(AA_AA,AA_Aa,AA_aa,Aa_Aa,Aa_aa,aa_aa):
    #E(X+Y) = E(X)+E(Y)
    return 2*(AA_AA + AA_Aa + AA_aa + Aa_Aa*(3/4) + Aa_aa*(1/2) + aa_aa*0)

print(rand_variable(16080,18697,19690,17051,16485,19208))