# RAG Project

This project uses a Retrieval-Augmented Generation (RAG) model to answer questions based on a custom corpus created from PDF and DOCX files.

## Setup

1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run the extraction: `sh scripts/run_extraction.sh`.
4. Generate answers using the RAG model.

## Project Structure

- `data/`: Contains input files.
- `corpus/`: Stores processed corpus data.
- `src/`: Source code.
- `models/`: Trained models.
- `notebooks/`: Jupyter notebooks for experimentation.
- `tests/`: Unit tests.
- `scripts/`: Helper scripts.
- `requirements.txt`: Dependencies list.
