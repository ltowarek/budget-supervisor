#!/bin/bash
pytest -m "webtest" --cov=. --no-cov-on-fail --cov-report html -vv
