# Select the base image to use.
FROM python:3.8

# Define function directory
ARG FUNCTION_DIR="/function"

# Set working directory to function root directory
WORKDIR ${FUNCTION_DIR}

COPY requirements.txt .

RUN pip install -r requirements.txt

# Copy function code
COPY . .

# Important!
# These instructions are required for your image to be compatible with
# AWS Lambda and Python Deploy.
ENTRYPOINT [ "/usr/local/bin/python", "-m", "awslambdaric" ]
CMD [ "pd_aws_lambda.dispatcher.dispatcher" ]
