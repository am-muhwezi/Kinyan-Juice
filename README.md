# Kinyan-Juice's Shop Application

## Overview
This project is a simple CRUD (Create, Read, Update, Delete) application with email and password authentication. The application is built using Flask for the backend and Vue.js for the frontend.

## Tech Stack
- **Frontend**: Vue.js
- **Backend**: Flask (Python)
- **Database**: SQLite (or any preferred database)
- **Authentication**: Email and Password

## Features
- User Registration
- User Login
- Create, Read, Update, and Delete operations for items
- Authentication with email and password

## Installation

### Backend
1. Clone the repository:
    ```sh
    git clone https://github.com/am-muhwezi/kinyan-juice.git
    cd kinyan-juice/backend
    ```
2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```
4. Run the Flask application:
    ```sh
    flask run
    ```

### Frontend
1. Navigate to the frontend directory:
    ```sh
    cd ../frontend
    ```
2. Install the required packages:
    ```sh
    npm install
    ```
3. Run the Vue.js application:
    ```sh
    npm run serve
    ```

## Testing & Documentation

### Backend Tests
To run the backend tests, navigate to the backend directory and run:
```sh
pytest
```

### Documenting Tests
The backend tests are located in the `tests` directory. Each test file corresponds to a specific module of the application. For example:
- `test_auth.py`: Contains tests for authentication (registration and login).
- `test_crud.py`: Contains tests for CRUD operations.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License.

## Contact
For any inquiries, please contact [intricatesyllable@gmail.com].
