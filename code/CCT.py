import numpy as np
import pandas as pd
import pymc as pm
import arviz as az
import os

def load_data(pk):
    df = pd.read_csv(pk)
    return df.drop(columns="Informant").to_numpy()

def run_model(data, draws=2000, tune=1000, chains=4):
    N, M = data.shape
    with pm.Model() as model:
        
        D = pm.Uniform("D", lower=0.5, upper=1, shape=N)
        Z = pm.Bernoulli("Z", p=0.5, shape=M)
        D_reshaped = D[:, None]
        p = Z * D_reshaped + (1 - Z) * (1 - D_reshaped)
        
        pm.Bernoulli("X_obs", p=p, observed=data)
        trace = pm.sample(draws=draws, tune=tune, chains=chains,
                          target_accept=0.90, return_inferencedata=True) #Used AI to figure out needed parameters
    return trace

def show_results(trace, data):

    D_mean = trace.posterior["D"].mean(dim=["chain", "draw"]).values
    print("Posterior Mean Competence (D):")
    for i, d in enumerate(D_mean, start=1): #Used AI
        print(f"  Informant {i}: {d:.3f}")
    az.plot_posterior(trace, var_names=["D"])
    
    Z_mean = trace.posterior["Z"].mean(dim=["chain", "draw"]).values
    print("\nPosterior Mean for Consensus Answers (Z):")
    for i, z in enumerate(Z_mean, start=1):
        print(f"  Item {i}: Mean = {z:.3f}, Estimated = {int(round(z))}")
    az.plot_posterior(trace, var_names=["Z"])

    majority = np.round(data.mean(axis=0))
    print("\nSimple Majority Vote:")
    for i, m in enumerate(majority, start=1):
        print(f"  Item {i}: {int(m)}")

    print("\nDiagnostics Summary:")
    print(az.summary(trace, var_names=["D", "Z"]))

if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.realpath(__file__)) #Used AI to figure out how to get plant knowledge
    data_path = os.path.join(script_dir, "..", "data", "plant_knowledge.csv") #Used AI
    data = load_data(data_path)
    trace = run_model(data)
    show_results(trace, data)
