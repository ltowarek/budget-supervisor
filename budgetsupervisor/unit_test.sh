#!/bin/bash
pytest -m "not webtest" --cov=. --no-cov-on-fail --cov-report html -vv
