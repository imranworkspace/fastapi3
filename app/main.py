from app.routers.dept import router as dept_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# jeager ui 
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
# prometheus
from prometheus_fastapi_instrumentator import Instrumentator
app = FastAPI()
app.include_router(dept_router)
resource = Resource.create({
    "service.name": "fastapi3"
})

provider = TracerProvider(resource=resource)

exporter = OTLPSpanExporter(
    endpoint="jaeger:4317",
    insecure=True
)

provider.add_span_processor(
    BatchSpanProcessor(exporter)
)

trace.set_tracer_provider(provider)

FastAPIInstrumentor.instrument_app(app)
Instrumentator().instrument(app).expose(app)
