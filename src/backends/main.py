# import subprocess
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from inference import infer_text_api
import uvicorn

PORT_API = 8008

app = FastAPI(
    title="API server",
    version="1.0.0",
)

# Configure CORS settings
origins = [
    "http://localhost:3000",
    "https://hoppscotch.io",
    "https://your-web-app.com",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    # allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Tell client we are ready to accept requests
@app.get("/api/v1/connect")
def connect():
    return {
        "message": f"Connected to api server on port {PORT_API}. Refer to 'http://localhost:{PORT_API}/docs' for api docs.",
    }


# Load in the ai model to be used for inference. Example of calling code inline.
@app.post("/api/v1/text/inference/load")
async def load_inference(data: dict):
    try:
        model_id: str = data["modelId"]
        return {"message": f"AI model [{model_id}] loaded."}
    except KeyError:
        raise HTTPException(
            status_code=400, detail="Invalid JSON format: 'modelId' key not found"
        )


# Text inference endpoint for prompting.
# An example of calling external code. Anything imported in this file will be included in the binary output by PyInstaller.
@app.post("/api/v1/text/inference/completions")
def run_completion(data: dict):
    print("endpoint: /completions")
    return infer_text_api.completions(data)


def start_api_server():
    try:
        print("Starting API server...")
        # Start the ASGI server
        uvicorn.run(app, host="0.0.0.0", port=PORT_API, log_level="info")
        return True
    except:
        print("Failed to start API server")
        return False


if __name__ == "__main__":
    # You can spawn sub-processes here before the main process. start_api_server() will block further code from execution.
    # command = ["python", "-m", "some_script", "--arg", "argValue"]

    # Execute the command
    # subprocess.Popen(command)

    # Starts the universal API server
    start_api_server()
