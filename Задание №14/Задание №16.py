for p in range(25, 37):
    sleva = int('BO', p) + int('OM', p) + int('BL4', p)
    sprava = int('CNG', p)

    if sleva == sprava:
        print(p)
