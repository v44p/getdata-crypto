FROM python:3.8-slim as builder

WORKDIR /install
COPY requirements.txt .
#COPY setup.py .
RUN apt-get update && apt-get install -y --no-install-recommends gcc build-essential && pip install --user -r requirements.txt 

FROM python:3.8-slim as release 

COPY --from=builder /root/.local /root/.local
WORKDIR /getdata-crypto
COPY . /getdata-crypto
#RUN pip install --user .
ENV PATH=/root/.local/bin:$PATH

CMD ["python", "-u", "-B", "getdata-crypto/main.py"]