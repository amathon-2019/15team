FROM nikolaik/python-nodejs:python3.6-nodejs8

RUN mkdir /app

WORKDIR /app

ADD requirements.txt /app/

RUN pip install -r requirements.txt

ADD package.json /app/

RUN npm install

COPY . .

RUN echo export PATH="$HOME/.local/bin:$PATH"

EXPOSE 8765

ENTRYPOINT ["sh","./entrypoint.sh"]

CMD ["start"]
