#!/bin/bash
pytest budget/tests/test_models.py  --cov=. --no-cov-on-fail --cov-report html