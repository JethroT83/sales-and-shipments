FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PATH="/usr/local/bin:${PATH}"

# System deps (add build tools only if you need to compile packages)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    nodejs \
    npm \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python deps first for better caching
#COPY requirements.txt .
#RUN python -m pip install --upgrade pip && pip install -r requirements.txt && pip install django

COPY requirements.txt requirements-dev.txt ./
# use 'python -m pip' to guarantee matching interpreter
RUN python -m pip install --upgrade pip \
 && python -m pip install -r requirements.txt \
 && python -m pip install -r requirements-dev.txt \
 && python -m pip install pip-tools \
 && python - <<'PY'
import sys, sysconfig, shutil
print("PYTHON:", sys.executable)
print("SCRIPTS_DIR:", sysconfig.get_path("scripts"))
print("django-admin resolved to:", shutil.which("django-admin"))
PY

# Copy the rest of the src
COPY . .


# Non-root user
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

COPY requirements.txt .
RUN python -m pip install --user -r requirements.txt \
 && python -m pip install --user -r requirements-dev.txt

# Make sure user-level scripts (pip-compile, wheel, etc.) are on PATH
ENV PATH="/home/appuser/.local/bin:${PATH}"

EXPOSE 8000

# Entrypoint handles wait/migrate/collectstatic (dev-friendly)
ENTRYPOINT ["./entrypoint.sh"]

# Default dev command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
