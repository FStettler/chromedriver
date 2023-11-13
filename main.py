from fastapi import FastAPI
import requests
import json

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World!"}

@app.get("/get-stable-link")
async def get_latest_chromedriver_version():

    url_links = "https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json"

    data = requests.get(url_links)
    content = json.loads(data.text)

    stable_version = content["channels"]["Stable"]["version"]
    links_stable_version = content["channels"]["Stable"]["downloads"]["chromedriver"]

    for link in links_stable_version:
        if link["platform"] == 'win64':
            stable_version_link = link["url"]

    response = {
        "stable_version": stable_version,
        "stable_version_link": stable_version_link
    }

    return response



if __name__ == "__main__":

    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)