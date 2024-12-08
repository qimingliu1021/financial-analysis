import sys
sys.path.append("..")

from fastapi import Depends, APIRouter, Form
from fastapi.requests import Request

from starlette import status
from starlette.responses import RedirectResponse

from langchain_pinecone import PineconeVectorStore
from openai import OpenAI
import dotenv
import json
import yfinance as yf
import concurrent.futures
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document
from sklearn.metrics.pairwise import cosine_similarity
# from sentence_transformers import SentenceTransformer
from pinecone import Pinecone
import numpy as np
import requests
import os

router = APIRouter(
    prefix="/auto_research", 
    tags=["auto_research"], 
    responses={404: {"description": "Not Found"}}
)


@router.get("/")
async def read_example(): 
  return {"message": "Hello from auto_research!"}


@router.get("/get-stock-info")
def get_stock_info(symbol: str) -> dict:

    data = yf.Ticker(symbol)
    stock_info = data.info

    properties = {
        "Ticker": stock_info.get('symbol', 'Information not available'),
        'Name': stock_info.get('longName', 'Information not available'),
        'Business Summary': stock_info.get('longBusinessSummary'),
        'City': stock_info.get('city', 'Information not available'),
        'State': stock_info.get('state', 'Information not available'),
        'Country': stock_info.get('country', 'Information not available'),
        'Industry': stock_info.get('industry', 'Information not available'),
        'Sector': stock_info.get('sector', 'Information not available')
    }

    return properties


