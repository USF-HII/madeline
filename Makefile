all: build run test

build:
	docker build -t madeline-cli .

run:
	-docker kill madeline-cli; sleep 1
	cid=$$(docker run --rm --detach --publish=8000:8000 --name=madeline-cli madeline-cli:latest); sleep 1; docker ps --filter="id=$$cid"

nodetach:
	-docker kill madeline-cli; sleep 1
	docker run --rm --publish=8000:8000 --name=madeline-cli-nodetach madeline-cli:latest

interactive:
	docker run --rm -it --name=madeline-cli-interactive madeline-cli:latest

test:
	bin/test-app
