from fastapi import FastAPI

# Create a fastapi object
app = FastAPI()

# Create an endpoint (route)
@app.get("/")
async def root():
    return {"message": "Hello World, I work"}

# Another endpoint with parameter
@app.get("/{name}")
async def hello(name: str):
    return {"message": f"Hello, {name}!"}
    # It is equivalent to:
    # "Hello," +name + "!"
    #"Hello, {}!".format(name)
    #("Hello, ",name, "!")
