# Mean-Variance Portfolio Optimisation

This project implements the classical Markowitz **Mean-Variance Optimisation (MVO)** model from first principles.

The project derives the analytical solution using **Lagrange multipliers**, validates the implementation against a numerical quadratic programming solver, and evaluates the resulting portfolios using historical financial market data.

## Methodology

The optimisation problem considered is

$$ \min \_w \quad w^T \Sigma w $$
$$ s.t. \quad \mu^T w = r $$
$$ \quad \quad \bold 1^T w = 1 $$

The analytical solution is obtained using the method of Lagrange multipliers and solved numerically using a Cholesky decomposition. The implementation is validated against a quadratic programming solver before being evaluated on historical financial data

## Experiment Design

- Training period: 1 July 2020 to 30 June 2025
- Testing period: 1 July 2025 to 30 June 2026
- Assets: 15 assets including ETFs, equity, etc.
- Benchmark: equally-weighted portfolio

## Results

The analytical implementation produced solutions equivalent to the quadratic programming solver to machine precision.

The out-of-sample benchmark demonstrated that:

- conservative target-return portfolios achieved the strongest risk-adjusted performance,
- aggressive target-return portfolios generalised poorly,
- equally-weighted portfolios remained a surprisingly robust benchmark.

## Report

The complete report is available in `MVO.pdf`

## Future Work

- Long-only constraints
- Rolling-window parameter estimation
- Include transaction costs
- Black-Litterman portfolios

## Requirements

```bash
pip install -r requirements.txt
```
