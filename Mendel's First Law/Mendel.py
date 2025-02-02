
def Mendel(AA, Aa, aa):
    tp = AA+Aa+aa

    prob_aa = 0.0

    # Aa x Aa cross
    prob_aa += Aa/tp * ((Aa-1) / (tp-1)) * (1 / 4)

    # Aa x aa cross
    prob_aa += aa / tp * (Aa / (tp - 1)) * (1 / 2)
    prob_aa += Aa / tp * (aa / (tp - 1)) * (1 / 2)

    # aa x aa cross
    prob_aa += aa/tp * (aa - 1) / (tp - 1)

    return 1-prob_aa

print(Mendel(26,23,19))




