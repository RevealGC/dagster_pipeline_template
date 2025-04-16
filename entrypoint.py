import dagster as dg
import assets.sample_asset as sample_asset

defs = dg.Definitions(
    assets= dg.load_assets_from_modules([sample_asset])
    )