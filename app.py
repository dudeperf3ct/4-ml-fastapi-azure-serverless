from fastapi import FastAPI
import classifier_router


app = FastAPI()
app.include_router(classifier_router.router)


@app.get("/")
async def root():
    return "Wine quality rating (0 -> bad and 1 -> good)"


@app.get('/healthcheck', status_code=200)
async def healthcheck():
    return 'dummy check! Classifier is all ready to go!'
