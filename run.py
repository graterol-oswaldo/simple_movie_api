import uvicorn
from dotenv import load_dotenv
import os


def main():

    load_dotenv()

    if __name__ == "__main__":
        _host = os.getenv("HOST", "127.0.0.1")
        _port = int(os.getenv("PORT", 8080))
        _log_level = os.getenv("LOG_LEVEL", "info")

        uvicorn.run("app.main:app", host=_host, port=_port,
                    log_level=_log_level, reload=True)

if __name__ == "__main__":
    main()