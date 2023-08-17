from fastapi import HTTPException


# Example external script
def completions(data):
    try:
        prompt: str = data["prompt"]
        # Example response
        return {"message": f"openllm completing prompt [{prompt}] ..."}
    except KeyError:
        raise HTTPException(
            status_code=400, detail="Invalid JSON format: 'prompt' key not found"
        )
