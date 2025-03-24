FROM python:3.11

ENV FLAG="JK, you've still got one more: https://youtu.be/PfPta1QKfqQ"

RUN apt-get update && apt-get install -y socat

COPY game.py /app/game.py

EXPOSE 42011

CMD while true; do echo "Starting service..."; socat TCP-LISTEN:42011,reuseaddr,fork EXEC:"python3 /app/game.py"; done
