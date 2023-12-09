network:
	docker network create mynetwork

volume:
	docker volume create shared_data
	docker run -v shared_data:/data busybox sh -c "cp testText.txt /data"
#change the name of the text file
server:
	python server.py

clean:
	docker network rm mynetwork

all: clean network volume server