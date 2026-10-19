from fast import FastAPI
app = FastAPI()

@app.get("/")
def home();
   return {"message": "Hello World!"}


