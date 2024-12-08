# Financial Analysis & Automation with LLMs (Next.js + FastAPI)

## Introduction

<p>
*Research Automation:* Build a system that can find relevant stocks based on natural language queries from the user (e.g. "What are companies that build data centers?"). All stocks on the New York Stock Exchange must also be searchable by metrics such as Market Capitalization, Volume, Sector, and more.</p>
<p>
*Market Firehose:* Build a system that can handle 100 articles per minute. Your system should be able to process unstructured text articles and parse out the publisher, author, date, title, body, related sector. This should include an API and database schema. It must be a highly extensible system that can support articles from many different feeds, allows others to subscribe to the system to receive structured articles, and must operate as close to real time as possible while being able to handle processing hundreds of articles per minute.</p>
<p>
*Market Analysis:* Build a system that can process articles received from the market firehose.It should determine which companies are related to the article, a sentiment per company (positive or negative), and an event type classification for each article. Remember, this system must operate as close to real time as possible, and your system may receive hundreds of articles per minute.
</p>

## Run the bot

## Common Command

### Frontend

`npm run dev`

### Backend

`uvicorn main:app --reload --host 0.0.0.0 --port 8000
`
# financial-analysis
