start_containers:
	docker-compose build
	docker-compose up -d --scale worker=4
clean:
	docker-compose down

all:  clean start_containers