.PHONY: test

test:
	@python3 -m unittest discover -s test -p "*_test.py"