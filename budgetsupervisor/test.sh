#!/bin/bash
pytest budget/tests/test_models.py saltedge/tests/ --cov=. --no-cov-on-fail --cov-report html
