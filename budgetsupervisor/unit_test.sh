#!/bin/bash
pytest -m "not (saltedge or selenium)"
