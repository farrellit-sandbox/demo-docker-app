test:
	docker build -t test-demo-app .
	docker kill test-demo-app || true
	docker run --rm -d -p 8467:80 --name test-demo-app test-demo-app 
	open http://localhost:8467
