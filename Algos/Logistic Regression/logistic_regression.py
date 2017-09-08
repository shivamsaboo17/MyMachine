import matplotlib.pyplot as plt
import numpy as np
from scipy.special import expit
from scipy import optimize

datafile = "ex2data1"
cols = np.loadtxt(datafile,delimiter=",",usecols=(0,1,2),unpack=True)

x = np.transpose(np.array(cols[:-1]))
y = np.transpose(np.array(cols[-1:]))
m = y.size

x = np.insert(x, 0,1,axis=1)

pos = np.array([x[i] for i in range(x.shape[0])if y[i] == 1])
neg = np.array([x[i] for i in range(x.shape[0])if y[i] == 0])


def plotData(): #Function to plot data
    plt.figure(figsize=(10, 6))
    plt.plot(pos[:, 1], pos[:, 2], 'k+', label='Admitted')
    plt.plot(neg[:, 1], neg[:, 2], 'yo', label='Not admitted')
    plt.xlabel('Exam 1 score')
    plt.ylabel('Exam 2 score')
    plt.legend()
    plt.grid(True)


def h(mytheta, myx):  #Returns hypothesis i.e the sigmoid function
    return expit(np.dot(myx,mytheta))

def computeCost(mytheta,myx,myy):   #Cost function for logistic regression
    term1 = np.dot(-np.array(myy).T,np.log(h(mytheta,myx)))
    term2 = np.dot((1-np.array(myy)).T,np.log(1-h(mytheta,myx)))
    return float ((1./m)* np.sum(term1-term2))

initialtheta = np.zeros((x.shape[1],1))
print(computeCost(initialtheta,x,y))

def optimizeTheta(mytheta, myx, myy):   #Optimize costfunction to get optimum parameters
    result = optimize.fmin(computeCost,x0=mytheta,args=(myx,myy),maxiter=400, full_output=True)
    return result[0], result[1]

theta, mincost = optimizeTheta(initialtheta, x, y)

boundary_xs = np.array([np.min(x[:,1]), np.max(x[:,1])])
boundary_ys = (-1./theta[2])*(theta[0] + theta[1]*boundary_xs)
plotData()
plt.plot(boundary_xs,boundary_ys,'b-',label='Decision Boundary')
plt.legend()
plt.show()
