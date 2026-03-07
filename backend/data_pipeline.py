import pandas as pd

def load_data():
    warranty = pd.read_csv("data/warranty_claims.csv")
    service = pd.read_csv("data/service_tickets.csv")
    defects = pd.read_csv("data/manufacturing_defects.csv")

    return warranty, service, defects


if __name__ == "__main__":
    w, s, d = load_data()
    print("Warranty records:", len(w))
    print("Service tickets:", len(s))
    print("Manufacturing defects:", len(d))
