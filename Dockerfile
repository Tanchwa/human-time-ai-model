FROM python:3.10.19-alpine3.21 AS build

WORKDIR /utils
COPY ./utils/* /utils
RUN python3 -m pip install -r requirements.txt

RUN python3 training.py

FROM build AS runtime
WORKDIR /app
COPY --from=build ./t5_small_human_time_model ./t5_small_human_time_model

COPY requirements.txt .
RUN python3 -m pip install -r requirements.text

COPY ./utils/test_model.py /app/test_model.py

RUN adduser -u 5678 --disabled-password appuser && chown -R appuser /app

ENTRYPOINT ["python3","/app/test_model.py"]
