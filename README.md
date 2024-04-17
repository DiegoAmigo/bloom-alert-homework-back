# HOMEWORK BLOOM ALERT

## Getting Started

### Running the backend
#### Requirements
Make sure you have installed python 3.10 or superior
Go to the back folder and run the following command
install fastapi and uvicorn:

```bash
pip install fastapi
pip install "uvicorn[standard]"
```
Then run the following command:

    ```bash
    # if you want hot changes
    uvicorn main:app --reload
    # or
    uvicorn main:app
    ```
Running this command will initialize the backend, the database and seed this database with the csv files provided in http://localhost:8000/
