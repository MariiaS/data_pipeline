FROM python:latest
WORKDIR /code_to_run
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY / data_processor
RUN ls data_processor/
RUN ls data_processor/user_data/hb/2021/04/28/
CMD ["python", "-u", "data_processor/db_helper.py"]