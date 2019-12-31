FROM docker:dind

COPY content/ /

#coreutils for extra date options
RUN apk add --no-cache bash \
	git \
	musl-dev \
	make \
	go \
	nano \
	tshark \
	py-pip \
	python-dev \
	libffi-dev \
	openssl-dev \
	gcc \
	libc-dev \
	coreutils \
	iproute2 \
	&& apk update \
	&& pip install docker-compose

RUN	git clone https://github.com/dragonflyoss/Dragonfly.git \
	&& cd Dragonfly \
	&& make build-client \
	&& make install-client

RUN ulimit -u unlimited

ENTRYPOINT dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375
CMD dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375
