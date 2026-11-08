"""Exact C2 representation example; scope limited to group-presentation relations."""
import sympy as sp

def main():
    rho_a = sp.Matrix([[0,1],[1,0]])
    assert rho_a**2 == sp.eye(2)
    P=sp.Matrix([[1,1],[1,-1]])
    assert P.det()!=0
    assert P.inv()*rho_a*P == sp.diag(1,-1)
    print("PASS: C2 relations and explicit splitting basis verified over Q")

if __name__ == "__main__":
    main()
