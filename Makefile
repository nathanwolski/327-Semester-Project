network:
	docker network create mynetwork

volume: testText.txt
	docker volume create shared_data

server:
	docker run -d --name server --network mynetwork -v shared_data:/data server", shell = True, check = True

clean:
	docker network rm mynetwork

all:  clean network volume server