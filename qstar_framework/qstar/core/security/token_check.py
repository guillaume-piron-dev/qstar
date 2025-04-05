# qstar/core/security/token_check.py
from fastapi import Request, HTTPException
import os

API_TOKEN = os.environ.get("QSTAR_API_TOKEN", "")


async def verify_token(request: Request):
    token = request.headers.get("Authorization")
    if token != f"Bearer {API_TOKEN}":
        raise HTTPException(status_code=403, detail="Token invalide ou manquant")
    return True


# Exemple d'utilisation avec FastAPI
if __name__ == "__main__":
    from fastapi import FastAPI, Depends
    import uvicorn

    app = FastAPI()

    @app.get("/secure")
    async def secure_endpoint(auth: bool = Depends(verify_token)):
        return {"status": "Accès autorisé à Q-STAR API sécurisée."}

    uvicorn.run(app, host="127.0.0.1", port=8080)
