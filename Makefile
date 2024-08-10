.PHONY: clean
clean:
	rm -rf ./.venv
	rm -rf ./.pytest_cache
	rm -rf ./__pycache__
	rm -rf ebanx_account_manager/__pycache__
	rm -rf models/__pycache__
	rm -rf services/__pycache__
	rm -rf data/__pycache__
