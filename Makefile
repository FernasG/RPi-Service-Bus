up:
	@docker compose up

sh\:redis:
	@docker compose exec redis bash

sh\:kafka:
	@docker compose exec kafka bash

sh\:rabbitmq:
	@docker compose exec rabbitmq bash
