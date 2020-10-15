FROM python:3

WORKDIR /macToolkit

ADD MacToolkit.py .
ADD requiredLibraries.txt .

RUN pip install --no-cache-dir -r requiredLibraries.txt

ENTRYPOINT ["python", "MacToolkit.py"]
