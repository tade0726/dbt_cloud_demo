black_code:
	black ./models
	black ./dbt_cloud_demo

format:
	make black_code
	sqlfmt ./models
	sqlfmt ./macros
	sqlfmt ./tests


web-dev:
	cd dbt_cloud_demo && DAGSTER_DBT_PARSE_PROJECT_ON_LOAD=1 dagster dev