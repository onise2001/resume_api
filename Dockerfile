FROM python

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD [ "gunicorn", "--config", "gunicorn_config.py", "resumes.wsgi:application"]
