import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PREPROCESSED_FOLDER = os.path.join(BASE_DIR, "data", "preprocessed")
CURATED_FOLDER = os.path.join(BASE_DIR, "data", "curated")
SEMANTIC_FOLDER = os.path.join(BASE_DIR, "data", "semantic")

os.makedirs(CURATED_FOLDER, exist_ok=True)
os.makedirs(SEMANTIC_FOLDER, exist_ok=True)

def load_data():

    customers = pd.read_parquet(
        os.path.join(PREPROCESSED_FOLDER, "customers.parquet")
    )

    claims = pd.read_parquet(
        os.path.join(PREPROCESSED_FOLDER, "claims.parquet")
    )

    policies = pd.read_parquet(
        os.path.join(PREPROCESSED_FOLDER, "policies.parquet")
    )

    payments = pd.read_parquet(
        os.path.join(PREPROCESSED_FOLDER, "payments.parquet")
    )

    agents = pd.read_parquet(
        os.path.join(PREPROCESSED_FOLDER, "agents.parquet")
    )

    # Remove audit columns from all except customers
    for df in [claims, policies, payments, agents]:
        df.drop(
            columns=["Load_Date", "Created_By"],
            errors="ignore",
            inplace=True
        )

    return customers, claims, policies, payments, agents

def merge_customer_policy(customers, policies):

    return customers.merge(
        policies,
        on="Customer_ID",
        how="left"
    )

def merge_claims(df, claims):

    return df.merge(
        claims,
        on="Policy_ID",
        how="left"
    )

def merge_payments(df, payments):

    return df.merge(
        payments,
        on="Policy_ID",
        how="left"
    )

def save_curated(df):

    output = os.path.join(
        CURATED_FOLDER,
        "insurance_curated.parquet"
    )

    df.to_parquet(output, index=False)

    return output

def generate_kpi(df):

    policy_kpi = (
        df.groupby("Policy_Type")
        .agg(
            TotalClaimAmount=("Claim_Amount", "sum"),
            TotalClaims=("Claim_ID", "count")
        )
        .reset_index()
    )

    output_path = os.path.join(
        SEMANTIC_FOLDER,
        "kpi_policy.csv"
    )

    policy_kpi.to_csv(output_path, index=False)

    print(policy_kpi)

    return policy_kpi

def transform():

    customers, claims, policies, payments, agents = load_data()

    df = merge_customer_policy(
        customers,
        policies
    )

    df = merge_claims(
        df,
        claims
    )

    df = merge_payments(
        df,
        payments
    )

    save_curated(df)

    report = generate_kpi(df)

    print(report)

if __name__ == "__main__":

    transform()