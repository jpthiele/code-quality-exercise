import numpy as np
import os

# Return solution of the linar equation system A*x =b
# using the conjugate gradient metod
def conjugate_gradient(A,b):
  residual=b-np.dot(A,x)
  searchdirection=residual
  oldresidnorm= np.linalg.norm(residual)
  tol=1.0e-8
  while oldresidnorm> tol:
    A_searchdirection=np.dot(A,searchdirection)
    alpha=oldresidnorm*oldresidnorm/np.dot(searchdirection.T,A_searchdirection)
    x=x+alpha*searchdirection
    residual=residual-alpha* A_searchdirection
    newresidnorm=np.linalg.norm(residual)
    beta = newresidnorm*newresidnorm/(oldresidnorm*oldresidnorm)
    searchdirection=residual+beta*searchdirection
    oldresidnorm=newresidnorm
  return x


if __name__ == "__main__":
  #Example taken from Wikipedia page on the algorihm
  A=np.array([[4,1],[1,3]])
  b=np.array([[1],[2]])
  x=np.array([[2],[1]])
  x=conjugate_gradient(A,b,x)
