import geopandas as gpd
import pandas as pd


def prepare_steam_crackers(regions):


    """
    Load steam cracker plants and map onto bus regions.
    """

    df = pd.read_csv(f"/Users/go57cut/Library/CloudStorage/OneDrive-TUM/PhD/Research_content/Programming/PyPsa-EUR/data/steam_crackers.csv", sep=";", index_col=0)

    geometry = gpd.points_from_xy(df.Longitude, df.Latitude)
    gdf = gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326")

    gdf = gpd.sjoin(gdf, regions, how="inner", predicate="within")

    gdf.rename(columns={"name": "bus"}, inplace=True)
    gdf["country"] = gdf.bus.str[:2]

    return gdf

regions = gpd.read_file(f"/Users/go57cut/Library/CloudStorage/OneDrive-TUM/PhD/Research_content/Programming/PyPsa-EUR/resources/test-own-config-Ethylene/regions_onshore_base_s_10.geojson").set_index("name")

steam_crackers = prepare_steam_crackers(regions)

for i in steam_crackers.index:
    print(steam_crackers.loc[i])
