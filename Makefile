default: freeze

freeze: clean
	./fix_ml_html_statics.sh
	./insert_raw_to_ml_lectures.sh
	uv run python freeze.py

debug:
	uv run python debug.py

clean:
	find . -path ./.venv -prune -o -type f -name "*.pyc" -exec rm {} +
