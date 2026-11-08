"""Exact sample verification derived from the user's Legendre surface test case.

This checks only the section's Weierstrass equation modulo the conic relation.
It does NOT certify a K3 model, Picard roots, quotient, cohomology or r=2 surface.
Requires SymPy.
"""
import sympy as sp


def main():
    t, s = sp.symbols("t s")
    q = (4*t**2 + 1)/sp.Integer(5)
    x = q
    y = (2*sp.I/5)*s*(t**2-1)
    equation_difference = sp.together(y**2-x*(x-1)*(x-t**2))
    # As polynomials in s with coefficients rational in t, eliminate s^2-q.
    numerator, denominator = sp.fraction(equation_difference)
    assert sp.simplify(denominator) != 0
    quotient, remainder = sp.div(sp.Poly(numerator, s), sp.Poly(s*s-q, s))
    assert sp.simplify(remainder.as_expr()) == 0
    print("PASS: the section lies on the Legendre curve modulo s^2=(4t^2+1)/5")


if __name__ == "__main__":
    main()
