FROM python:3.10

ENV POETRY_NO_INTERACTION=1 \
        POETRY_VIRTUALENVS_IN_PROJECT=true \
        PIP_DISABLE_PIP_VERSION_CHECK=on

RUN pip install poetry

WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN poetry install --no-dev
COPY ./src /app/

EXPOSE 8000

ENTRYPOINT ["poetry", "run"]
CMD ["uvicorn", "demo_setup.interface.api.main:app" , "--host", "0.0.0.0"]
