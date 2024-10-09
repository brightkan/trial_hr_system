ReadMe
# HR Management System APIs

This project is a mini HR management system developed. It provides three core APIs that support the staff onboarding process, including staff registration, staff retrieval, and staff updates. Additionally, a client application is included that consumes these APIs, along with an admin interface to track API performance.

## Table of Contents

- [Project Overview](#project-overview)
- [APIs Overview](#apis-overview)
  - [1. Staff Registration API](#1-staff-registration-api)
  - [2. Staff Retrieval API](#2-staff-retrieval-api)
  - [3. Staff Update API](#3-staff-update-api)
- [Client Application](#client-application)
- [Admin Interface](#admin-interface)
- [Installation and Setup](#installation-and-setup)


## Project Overview

The project consists of three APIs designed to manage HR processes. The APIs handle staff registration, retrieval, and updates. A client web or mobile app consumes these APIs to provide a user-friendly interface for interacting with the HR system.

## APIs Overview

### 1. Staff Registration API

This API allows new staff members to register. Required parameters include:
- `Surname` (String)
- `Other Name(s)` (String)
- `Date of Birth` (ISO 8601 format)
- `ID Photo` (Base64-encoded string, optional)

The endpoint is at `/api/v1/staff/register/`.

The staff member must also provide a unique 10-digit code for validation. Upon successful registration, a new Employee Number is generated and returned in the response.

### 2. Staff Retrieval API

This API fetches staff details:
- When an `Employee Number` is provided, the API returns the corresponding staff details.
- If no parameters are provided, the API returns a list of all registered staff members.

The endpoint is at `/api/v1/staff/retrieve/`.
When fetching a single staff member, the `Employee Number` is passed.
The endpoint becomes `/api/v1/staff/retrieve/{}`.

### 3. Staff Update API

This API allows updating the following details for a selected staff member:
- `Date of Birth`
- `ID Photo`

The endpoint is at `/api/v1/staff/update/`.

### API Security
All APIs implement security measures following current best practices, ensuring data protection and secure access.

## Client Application

The client application is built using React. It allows the user to interact with the three APIs via a user-friendly interface. The client handles:
- Staff registration
- Staff retrieval
- Staff details updates

It is accessible at `/` on the root path.

## Admin Interface

The project includes a simple admin interface that shows the following API performance metrics:
- Number of requests
- Number of successful requests
- Number of failed requests

The admin panel is accessible at `/admin/`.
The performance summary is accessible at `/admin/api_performance/apirequestlog/summary_view/`.


## Installation and Setup

The link to the deployment docs is [here](docs/deployment.md).

