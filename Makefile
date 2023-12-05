black_code:
	black ./models
	black ./dbt_cloud_demo

format:
	make black_code
	sqlfmt ./models
	sqlfmt ./macros
	sqlfmt ./tests
