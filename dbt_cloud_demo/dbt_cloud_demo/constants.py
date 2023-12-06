import os
from pathlib import Path

from dagster_dbt import DbtCliResource

# We expect the dbt project to be installed as package data.
# For details, see https://docs.python.org/3/distutils/setupscript.html#installing-package-data.

if os.getenv("DEPLOY_ENV") == "prod":
    dbt_project_dir = Path(__file__).joinpath("..", "..", "dbt-project").resolve()
else:
    dbt_project_dir = Path(__file__).joinpath("..", "..", "..").resolve()


dbt = DbtCliResource(project_dir=os.fspath(dbt_project_dir))

# If DAGSTER_DBT_PARSE_PROJECT_ON_LOAD is set, a manifest will be created at run time.
# Otherwise, we expect a manifest to be present in the project's target directory.
if os.getenv("DAGSTER_DBT_PARSE_PROJECT_ON_LOAD"):
    dbt_parse_invocation = dbt.cli(["parse"], target_path=Path("target")).wait()
    dbt_manifest_path = dbt_parse_invocation.target_path.joinpath("manifest.json")
else:
    dbt_manifest_path = dbt_project_dir.joinpath("target", "manifest.json")
