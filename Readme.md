# Polish formality dataset

Dataset with polish texts labeled with categories describing the degree of formality.

## Dataset description
In dataset.csv file you can find 4 columns:
- id - unique identifier of the text,
- text - text of the document,
- formality_2_categories - 0 - informal text, 1 - formal text,
- formality_3_categories - 0 - informal text, 1 - moderately formal text, 2 - formal text.

## Usage example
Run main.py to read dataset and display numbers of texts in each category.
```
python main.py
```