coverage:
	@pytest --cov-config=.coveragerc --cov=video_downloader --cov-fail-under=80 --no-cov-on-fail tests
	@coverage-badge -f -o coverage.svg

test:
	@pytest

requirements:
	@poetry export -o requirements.txt --without-hashes --dev
