FROM python

WORKDIR /home/server

COPY app app
COPY migrations migrations
COPY manage.py docker-entrypoint.sh env.sh ./
RUN chmod +x docker-entrypoint.sh env.sh

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn

ENV SECRET_KEY=fooo
ENV HOST=localhost
ENV PORT=5000
ENV FLASK_DEBUG=1

EXPOSE 5000

ENTRYPOINT ["sh", "./docker-entrypoint.sh"]
