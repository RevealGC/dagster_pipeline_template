import dagster as dg
import assets.sample_asset as sample_asset



defs = dg.Definitions(
    assets = dg.with_source_code_references(
        [
            *dg.load_assets_from_modules(sample_asset)
        ]
    ),
    resources={},
    sensors={},
    schedules={},
    jobs={},
    ops={},
    )