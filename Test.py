import pypsa
import pandas as pd

# replace with your actual network file path
fn = "resources/test-own-config-Ethylene/networks/base_s_10__Co2L0.7_2030.nc"

n = pypsa.Network(fn)


# show how many components we have
print(f"Total buses: {len(n.buses)}")
print(f"Total links: {len(n.links)}")

# filter buses by carrier
print("\n=== Buses of interest ===")
for carrier in ["ethylene", "ammonia", "industry methanol"]:
    buses = n.buses.index[n.buses.carrier == carrier]
    print(f"{carrier} buses ({len(buses)}):")
    print(buses.tolist())

# filter links by carrier names containing our commodities
print("\n=== Links of interest ===")
for link in n.links.index:
    carrier = n.links.at[link, "carrier"]
    if any(substr in carrier.lower() for substr in ["ethylene", "ammonia", "methanol", "steam cracker", "electric cracker"]):
        print(f"{link}: {carrier}")

# Loads
print("\n=== Loads of interest ===")
for load in n.loads.index:
    carrier = n.loads.at[load, "carrier"]
    if any(substr in carrier.lower() for substr in ["ethylene", "ammonia", "methanol"]):
        # Get the corresponding load (p_set) for this load
        #load_demand = n.loads_t.p_set[load].sum()  # Sum the demand over all snapshots (hours)

        print(f"{load}: {carrier}")

        # Print all information from the 'n.loads' DataFrame for this load
        load_info = n.loads.loc[load]  # Get all attributes of this load
        print(f"  Load details: {load_info.to_dict()}")  # Convert to dictionary for easy viewing
