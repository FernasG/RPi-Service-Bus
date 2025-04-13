up:
	@docker compose up

up\:producer:
	@docker compose -f docker-compose.services.yml up producer

up\:consumer:
	@docker compose -f docker-compose.services.yml up consumer

sh\:producer:
	docker compose exec producer bash

sh\:consumer:
	docker compose exec consumer bash

sh\:redis:
	@docker compose exec redis bash

sh\:kafka:
	@docker compose exec kafka bash

sh\:rabbitmq:
	@docker compose exec rabbitmq bash
