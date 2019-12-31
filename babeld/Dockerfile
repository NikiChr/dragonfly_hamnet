FROM ubuntu:disco
RUN apt-get update \
    && apt-get install -y git build-essential \
    && git clone https://github.com/jech/babeld \
    && cd babeld \
    && make

FROM ubuntu:disco
COPY --from=0 /babeld/babeld .
#All Interfaces which are called hostname-* will be used for routing
CMD ./babeld $(cd /sys/class/net/&& ls -d $(hostname)-*)
