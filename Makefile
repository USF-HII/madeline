all: build run test

build:
	docker build -t madeline-cli .

run:
	-docker kill madeline-cli
	sleep 1
	cid=$$(docker run --rm --detach --publish=8000:8000 --name=madeline-cli madeline-cli:latest); sleep 1; docker ps --filter="id=$$cid"

test:
	bin/test-app
	docker logs madeline-cli


