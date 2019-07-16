FROM dockerproxy.bale.ai/python:3.7

WORKDIR /bot_root

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY ./ ./
CMD ["python", "main.py"]
ENV PYTHONPATH /bot_root