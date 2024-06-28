FROM public.ecr.aws/lambda/python:3.8

COPY requirements.txt .

RUN pip install -r requirements.txt -t .

COPY lambda_function.py .

CMD ["lambda_function.lambda_handler"]
