FROM python:latest
WORKDIR /code_to_run
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY / data_pipeline
RUN ls data_pipeline/
CMD ["python", "-u", "data_pipeline/runner.py"]