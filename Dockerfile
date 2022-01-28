# Select the base image to use.
FROM python:3.8 as base

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH="/root/.poetry/bin:${PATH}"
RUN poetry config virtualenvs.create false

# Define function directory
ARG FUNCTION_DIR="/function"

# Set working directory to function root directory
WORKDIR ${FUNCTION_DIR}

COPY pyproject.toml poetry.lock ./

RUN poetry install

COPY entrypoint.sh /usr/local/bin/pd_entrypoint
RUN chmod +x /usr/local/bin/pd_entrypoint

ENTRYPOINT [ "pd_entrypoint" ]

# Copy function code
COPY . .

# Select the base image to use.
FROM base as fargate

CMD [ "gunicorn", "--capture-output", "pd_django_demo.wsgi", "-b", "0.0.0.0:80" ]


# Select the base image to use.
FROM base as lambda

# Important!
# This CMD is required for your image to be compatible with
# AWS Lambda and Python Deploy.
CMD [ "python", "-m", "awslambdaric", "pd_aws_lambda.dispatcher.dispatcher" ]
