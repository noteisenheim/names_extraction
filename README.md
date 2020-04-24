# Extracting names
A test task for the internship at O. Dev, [whywhy.io](whywhy.io)

---

## How to run
#### First way
1. Install the dependencies 
```
pip install spacy
python -m spacy download en_core_web_sm
```
2. Run the [code](../name_extraction.py) with the command `python name_extraction.py`.

#### Second way
1. Build the docker image `docker build -t name-extraction .`
2. Run the image `docker run -i -t name-extraction`

## Input examples
Input examples are provided in the file [input.txt](../input.txt).

There is also a file with the expected outputs for the example inputs, [expected_output.txt](../expected_output.txt).

However, the real output differs from the expected one: there are french names that are not so common in English language. This can be solved by loading the model not only for English language.
