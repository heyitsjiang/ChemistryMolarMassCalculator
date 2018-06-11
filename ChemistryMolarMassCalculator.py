# Putting the values of each element inside an organized tuple
tData = (
("H", 1.01), ("Li", 6.94), ("Na", 22.99), ("K", 39.10), ("Rb", 85.47), ("Cs", 132.91), ("Fr", 223), ("Be", 9.01),
("Mg", 24.31), ("Ca", 40.08), ("Sr", 87.62), ("Ba", 137.33), ("Sc", 44.96), ("Y", 88.91), ("La", 138.91),
("Ti", 47.87), ("Zr", 91.22), ("Hf", 178.49), ("V", 50.94), ("Nb", 92.91), ("Ta", 180.95),
("Cr", 52.00), ("Mo", 95.96), ("W", 183.84), ("Mn", 54.86), ("Tc", 98), ("Re", 186.21),
("Fe", 55.85), ("Ru", 101.07), ("Os", 190.23), ("Co", 58.93), ("Rh", 102.91), ("Ir", 192.22),
("Ni", 58.69), ("Pd", 106.42), ("Pt", 195.08), ("Cu", 63.55), ("Ag", 107.87), ("Au", 196.97),
("Zn", 65.38), ("Cd", 112.41), ("Hg", 200.59), ("B", 10.81), ("Al", 26.98), ("Ga", 69.72),
("In", 114.82), ("Tl", 204.38), ("C", 12.01), ("Si", 28.09), ("Ge", 72.63), ("Sn", 118.71), ("Pb", 207.20),
("N", 14.01), ("P", 30.97), ("As", 74.92), ("Sb", 121.76), ("Bi", 208.98), ("O", 16.00), ("S", 32.07), ("Se", 78.96),
("Te", 127.60), ("F", 19.00), ("Cl", 35.45), ("Br", 79.90), ("I", 126.90), ("He", 4.00), ("Ne", 20.18), ("Ar", 39.95),
("Kr", 83.90), ("Xe", 131.29), ("Ce", 140.12), ("Pr", 140.91), ("Nd", 144.24), ("Sm", 150.36), ("Eu", 151.96),
("Gd", 157.25), ("Tb", 158.93), ("Dy", 162.50), ("Ho", 164.93), ("Er", 167.26), ("Tm", 168.93), ("Yb", 173.05),
("Lu", 174.97), ("Th", 232.04), ("Pa", 231.04), ("U", 238.03))

#Assigning variables to each element in the tuble respective to element name
h, li, na, k, rb, cs, fr, be, mg, ca, sr, ba, sc, y, la, ti, zr, hf, v, nb, ta, cr, mo, w, mn, tc, re, fe, ru, os, co, rh, ir, ni, pd, pt, cu, ag, au, zn, \
cd, hg, b, al, ga, In, tl, c, si, ge, sn, pb, n, p, As, sb, bi, o, s, se, te, f, cl, br, I, he, ne, ar, kr, xe, ce, pr, nd, sm, eu, gd, tb, dy, ho, er, tm, yb, \
lu, th, pa, u = tData

#Creating a string list that contains each element's symbol
stringList = [h[0], li[0], na[0], k[0], rb[0], cs[0], fr[0], be[0], mg[0], ca[0], sr[0], ba[0], sc[0], y[0], la[0],
              ti[0], zr[0], hf[0], v[0],
              nb[0], ta[0], cr[0], mo[0], w[0], mn[0], tc[0], re[0], fe[0], ru[0], os[0], co[0], rh[0], ir[0], ni[0],
              pd[0], pt[0], cu[0], ag[0],
              au[0], zn[0], cd[0], hg[0], b[0], al[0], ga[0], In[0], tl[0], c[0], si[0], ge[0], sn[0], pb[0], n[0],
              p[0], As[0], sb[0], bi[0], o[0],
              s[0], se[0], te[0], f[0], cl[0], br[0], I[0], he[0], ne[0], ar[0], kr[0], xe[0], ce[0], pr[0], nd[0],
              sm[0], eu[0], gd[0], tb[0], dy[0],
              ho[0], er[0], tm[0], yb[0], lu[0], th[0], pa[0], u[0]]

#creating a molar mass list that contains the molar mass of each element
massList = [h[1], li[1], na[1], k[1], rb[1], cs[1], fr[1], be[1], mg[1], ca[1], sr[1], ba[1], sc[1], y[1], la[1], ti[1],
            zr[1], hf[1], v[1],
            nb[1], ta[1], cr[1], mo[1], w[1], mn[1], tc[1], re[1], fe[1], ru[1], os[1], co[1], rh[1], ir[1], ni[1],
            pd[1], pt[1], cu[1], ag[1],
            au[1], zn[1], cd[1], hg[1], b[1], al[1], ga[1], In[1], tl[1], c[1], si[1], ge[1], sn[1], pb[1], n[1], p[1],
            As[1], sb[1], bi[1], o[1],
            s[1], se[1], te[1], f[1], cl[1], br[1], I[1], he[1], ne[1], ar[1], kr[1], xe[1], ce[1], pr[1], nd[1], sm[1],
            eu[1], gd[1], tb[1], dy[1],
            ho[1], er[1], tm[1], yb[1], lu[1], th[1], pa[1], u[1]]

#creating a string that holds numbers to check if there are multipliers in the formula
numbers = "123456789"

#Function where User inputs a formula
def enter_formula():
    formula = ""
    formula += str(input("Enter a chemical formula to calculate its mass: "))
    userinput = formula
    formula += "  "
    mm_calc(formula, userinput)

#Function that calculates the molar mass of the user input
def mm_calc(formula, userinput):
    term = 0 #will use this to iterate through user input, starting at [0]
    molar_mass = 0.00 #set molar mass to 0 to begin with
    pmm = 0.00 #a separate variable to calculate molar mass within parenthesis
    while "(" and ")" in formula:   #This makes sure to calculate things within "()" first
        term = formula.index("(") + 1   #Finding where the parentheses starts
        while term < formula.index(")"):  #going through everything within the parentheses
            
            #finding 2 lettered elements first! Very important because if you do 1 letter first, it will potentially add twice
            if formula[term] + formula[term + 1] in stringList:
                if formula[term + 2] in numbers:
                    #creating the multiplier if there are numbers, creating the counter in place of "term" so we can iterate without changing the variable "term".
                    multiplier = ""
                    counter = term + 2

                    while formula[counter] in numbers:
                        multiplier += formula[counter] #finding the number after the element by adding consecutive integers to "multiplier" and returning an int from it
                        counter += 1
                    #after returning the int of multiplier, multiply it by the element found in massList and add to molar_mass
                    pmm += int(multiplier) * massList[stringList.index(formula[term] + formula[term + 1])]

                else:
                    pmm += massList[stringList.index(formula[term] + formula[term + 1])]
                    
            elif formula[term] in stringList:

                if formula[term + 1] in numbers:
                    multiplier = ""
                    counter = term + 1
                    while formula[counter] in numbers:
                        multiplier += formula[counter]
                        counter += 1
                    pmm += int(multiplier) * massList[stringList.index(formula[term])]

                else:
                    pmm += massList[stringList.index(formula[term])]
        
            term += 1

        if formula[formula.index(")") + 1] in numbers:
            counter = formula.index(")") + 1
            multiplier = ""
            while formula[counter] in numbers:
                multiplier += formula[counter]
                counter += 1
            pmm *= int(multiplier) 
            molar_mass += pmm
            pmm = 0.00
            cleaned_formula = formula[:formula.index("(")] + formula[formula.index(")") + len(multiplier) + 1:]
            formula = cleaned_formula
            term = 0

        else:
            molar_mass += pmm
            pmm = 0.00
            cleaned_formula = formula[:formula.index("(")] + formula[formula.index(")") + 1:]
            formula = cleaned_formula
            term = 0

    while term < len(formula) - 1:
        if formula[term] + formula[term + 1] in stringList:
            if formula[term + 2] in numbers:
                counter = formula.index(formula[term + 2])
                multiplier = ""
                while formula[counter] in numbers:
                    multiplier += formula[counter]
                    counter += 1
                molar_mass += int(multiplier) * massList[stringList.index(formula[term] + formula[term + 1])]

            else:
                molar_mass += massList[stringList.index(formula[term] + formula[term + 1])]

        elif formula[term] in stringList:
            if formula[term + 1] in numbers:
                multiplier = ""
                counter = formula.index(formula[term + 1])
                while formula[counter] in numbers:
                    multiplier += formula[counter]
                    counter += 1
                molar_mass += int(multiplier) * massList[stringList.index(formula[term])]
            else:
                molar_mass += massList[stringList.index(formula[term])]

        term += 1
    print("{0} has a molar mass of {1} g/mol.".format(userinput, molar_mass))
    print("="*75)
    enter_formula()

#Calling the User input function to begin
enter_formula()
