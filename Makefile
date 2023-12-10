start_containers:
	docker-compose build
	docker-compose up --scale worker=4
clean:
	docker-compose down

all:  start_containers