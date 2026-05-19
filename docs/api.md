# API Plan

Planned backend endpoints:

## Pipelines

GET /pipelines
GET /pipelines/{id}
GET /pipelines/{id}/runs
POST /pipelines/{id}/trigger

## Data quality

GET /runs/{id}/quality-checks

## Incidents

GET /incidents
POST /incidents
PATCH /incidents/{id}

## Deployments

GET /deployments

## Metrics

GET /metrics/overview