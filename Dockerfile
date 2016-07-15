FROM alpine:3.4
MAINTAINER The Inner Circle <https://github.com/TheInnerCircleO>

# Hangoutsbot version
ENV HOB_VERSION 2.7.9

# Create Hangoutsbot directories
RUN mkdir -p /opt/hangoutsbot /etc/hangoutsbot

# Set Hangoutsbot archive URL
ENV TARBALL_URL https://api.github.com/repos/hangoutsbot/hangoutsbot/tarball/${HOB_VERSION}

# Download and extract Hangoutsbot archive and install dependencies
RUN apk add --update ca-certificates gcc git python3-dev tar wget \
    && wget -qO- ${TARBALL_URL} | tar -xz --strip-components=1 -C /opt/hangoutsbot \
    && wget -qO- https://bootstrap.pypa.io/get-pip.py | python3 \
    && pip3 install --no-cache-dir -r /opt/hangoutsbot/requirements.txt \
    && pip3 install --no-cache-dir soundcloud TwitterAPI \
    && apk del --purge gcc git tar wget && rm -rf /var/cache/apk/*

# Add our custom plugins
COPY plugins/* /opt/hangoutsbot/hangupsbot/plugins/

VOLUME /etc/hangoutsbot

CMD ["/opt/hangoutsbot/hangupsbot/hangupsbot.py", "--config", "/etc/hangoutsbot/config.json", \
     "--cookies", "/etc/hangoutsbot/cookies.json", "--memory", "/etc/hangoutsbot/memory.json"]
