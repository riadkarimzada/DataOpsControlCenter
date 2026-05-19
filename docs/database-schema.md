# Database Schema Plan

The first version of the database will contain these tables:

## pipelines

Stores metadata about data pipelines.

Fields:

id
name
description
source_type
source_name
target_table
owner
created_at
is_active

## pipeline_runs

Stores execution history for each pipeline

Fields:

id
pipeline_id
status
started_at
finished_at
duration_seconds
rows_processed
rows_failed
triggered_by
environment
git_commit_hash

## data_quality_checks

Stores quality check results for pipeline runs.

Fields:

id
run_id
check_name
status
severity
failed_rows
message
created_at

## incidents

Stores pipeline incidents and their resolution status.

Fields:

id
pipeline_id
run_id
title
severity
status
root_cause
created_at
resolved_at

## deployments

Stores deployment status information.

Fields:

id
service_name
environment
version
commit_hash
status
deployed_at