FROM python:3.12-slim

# Working directory inside container
WORKDIR /fastapi3

# Install Python dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir --timeout=300 --retries=10 -r requirements.txt

# Copy application source
COPY . /fastapi3 

RUN chmod +x /fastapi3/entrypoint.sh

# Expose FastAPI port
EXPOSE 8001

# Start FastAPI in development mode
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]
CMD ["/fastapi3/entrypoint.sh"]

# INSERT INTO employees (ename, email, salary, department_id, age) SELECT 'Employee_' || gs, 'employee' || gs || '@example.com', ROUND((30000 + RANDOM() * 70000)::numeric, 2), ((gs - 1) % 3) + 1, FLOOR(22 + RANDOM() * 39)::int FROM generate_series(1, 500) AS gs;
