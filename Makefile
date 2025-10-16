.PHONY: up apply down worker order

up: ## start stack
	 docker compose up -d
apply: ## terraform apply (local)
	docker compose run --rm terraform init -input=false
	docker compose run --rm terraform apply -auto-approve
down:
	 docker compose down -v
worker:
	 docker compose exec app python manage.py worker
order:
	 curl -s -X POST localhost:8000/orders -d '{"email":"jedlynch@gmail.com"}' -H 'Content-Type: application/json' | jq
