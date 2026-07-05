import numpy as np; 

def lg_solve(mu, Sigma, r):
    """
    Solve:
        min     w.T @ Sigma @ w
        s.t.    w.T @ mu    = r
                1.T @ w     = 1
    """

    mu = np.asarray(mu).reshape(-1, 1); 
    Sigma = np.asarray(Sigma); 
    n = len(mu); 

    ones = np.ones((n, 1)); 

    Sigma_inv_ones = np.linalg.solve(Sigma, ones); 
    Sigma_inv_mu = np.linalg.solve(Sigma, mu); 

    A = ones.T @ Sigma_inv_ones; 
    B = ones.T @ Sigma_inv_mu; 
    C = mu.T @ Sigma_inv_mu; 

    A = A.item(); 
    B = B.item(); 
    C = C.item(); 

    LHS = np.array([
            [C, B],
            [B, A]
        ]); 

    RHS = np.array([
            [2 * r],
            [2]
        ]); 

    lambd, gamma = np.linalg.solve(LHS, RHS); 

    w = 0.5 * (lambd * Sigma_inv_mu + gamma * Sigma_inv_ones); 

    return w.flatten(); 

