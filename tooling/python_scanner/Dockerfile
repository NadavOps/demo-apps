FROM python:3.11.4-slim

WORKDIR /project
ENV venv_location="/project/venv"

RUN pip install --upgrade pip && pip install --no-cache-dir pip-audit virtualenv

# To activate venv for running session -> . "$venv_location/bin/activate"
RUN python -m virtualenv "$venv_location"

# Making venv python the default python
ENV PATH="$venv_location/bin:$PATH"

COPY requirements.txt packages_to_check.txt
RUN pip install --no-cache-dir -r packages_to_check.txt

# PIPAPI_PYTHON_LOCATION is required for pip to use venv python
CMD ["bash", "-c", "pip list && PIPAPI_PYTHON_LOCATION=$venv_location/bin/python pip-audit"]
