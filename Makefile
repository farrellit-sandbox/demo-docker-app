test:
	docker build -t test-demo-app .
	docker run --rm -p 80 test-demo-app
