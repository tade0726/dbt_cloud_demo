from setuptools import find_packages, setup

setup(
    name="dbt_cloud_demo",
    version="0.0.1",
    packages=find_packages(),
    package_data={
        "dbt_cloud_demo": [
            "dbt-project/**/*",
        ],
    },
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster-dbt",
        "dbt-core>=1.4.0",
        "dbt-databricks",
    ],
    extras_require={
        "dev": [
            "dagster-webserver",
        ]
    },
)

