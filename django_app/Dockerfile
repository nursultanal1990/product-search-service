FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

RUN pip install poetry==1.8 && \
    poetry config virtualenvs.create false

WORKDIR /src

COPY pyproject.toml poetry.lock* .

RUN poetry install --only main


COPY ./src /src

COPY ./src/entrypoint.sh ./entrypoint.sh

RUN chmod +x ./entrypoint.sh

CMD ["./entrypoint.sh"]
