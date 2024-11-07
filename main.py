import logging

from fastapi import FastAPI
from pydantic import BaseModel, Field


class RestAPIRequestBody(BaseModel):
    input_schema: str = "basic"  # for future use
    summary: str = ""  # for future use: let the LLM condense the message
    message: str = Field(..., description="User input message")


class SourceDocument(BaseModel):
    title: str | None = Field(None, description="Optional, title of the document")
    external_link: str | None = Field(None, description="Optional, external https link")
    content: str


class RestAPIResponseBody(BaseModel):
    documents: list[SourceDocument]


app = FastAPI()


@app.post("/query", response_model=RestAPIResponseBody)
async def query(request: RestAPIRequestBody) -> RestAPIResponseBody:
    # TODO: remove logging user data in production
    logging.debug(request.message)  # raw user input

    return RestAPIResponseBody(
        documents=[
            SourceDocument(
                title="Elizabeth",
                content="Elizabeth says 'Hello World'",
                external_link="https://www.example.com",
            ),
            SourceDocument(
                title="Angela",
                content="Angela says 'Hallo Welt'",
                external_link=None,
            ),
            SourceDocument(
                title="Carl",
                content="Carl says 'Hej världen'",
                external_link=None,
            ),
        ]
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=9001, log_level="info")
