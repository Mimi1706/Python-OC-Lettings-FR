# API Documentation

## Overview
This API provides endpoints for managing lettings and user profiles. It includes functionality to render pages for viewing all lettings, specific lettings, user profiles, and handling error pages.

## Endpoints

### 1. Index View
- **URL**: `/`
- **Method**: `GET`
- **Description**: Renders the homepage.
- **Response**:
  - **200 OK**: Renders the homepage (`index.html`).
  - **500 Internal Server Error**: Renders a custom error page (`errors/error_500.html`) if an exception occurs.

---

### 2. List All Lettings
- **URL**: `/lettings/`
- **Method**: `GET`
- **Description**: Renders a list of all lettings.
- **Response**:
  - **200 OK**: Renders a page with a list of all lettings (`lettings/index.html`).
  - **500 Internal Server Error**: Renders a custom error page if an exception occurs.

---

### 3. Letting Details
- **URL**: `/lettings/<letting_id>/`
- **Method**: `GET`
- **Path Parameters**:
  - `letting_id` (int): The ID of the letting to retrieve.
- **Description**: Renders details for a specific letting.
- **Response**:
  - **200 OK**: Renders the details of the specified letting (`lettings/letting.html`).
  - **404 Not Found**: Renders a custom 404 error page if the letting does not exist.
  - **500 Internal Server Error**: Renders a custom error page if an exception occurs.

---

### 4. List All Profiles
- **URL**: `/profiles/`
- **Method**: `GET`
- **Description**: Renders a list of all user profiles.
- **Response**:
  - **200 OK**: Renders a page with a list of all user profiles (`profiles/index.html`).
  - **500 Internal Server Error**: Renders a custom error page if an exception occurs.

---

### 5. User Profile Details
- **URL**: `/profiles/<username>/`
- **Method**: `GET`
- **Path Parameters**:
  - `username` (str): The username of the profile to retrieve.
- **Description**: Renders a specific user profile based on username.
- **Response**:
  - **200 OK**: Renders the specified user profile (`profiles/profile.html`).
  - **404 Not Found**: Renders a custom 404 error page if the profile does not exist.
  - **500 Internal Server Error**: Renders a custom error page if an exception occurs.

---

### 6. Simulate 500 Error
- **URL**: `/error_500/`
- **Method**: `GET`
- **Description**: Simulates a 500 server error by raising an exception.
- **Response**:
  - **500 Internal Server Error**: Always renders a custom error page (`errors/error_500.html`).

---

### Error Handling

- **404 Error**: Handled by `error_404(request, exception)` which returns a custom 404 error page.
- **500 Error**: Handled by `error_500(request)` which returns a custom 500 error page.

---

### Dependencies
- **Models**:
  - `Letting`: Represents a letting entity.
  - `Profile`: Represents a user profile entity.

### External Services
- **Sentry**: Used for error monitoring and capturing exceptions.

---

### Notes
- This API is intended for rendering HTML pages and is not a RESTful API.
- Ensure that the server is running, and the Django application is correctly set up with the necessary templates to avoid rendering issues.
