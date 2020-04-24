FROM python:3
ADD name_extraction.py /
ADD input.txt /
RUN pip install spacy
RUN python -m spacy download en_core_web_sm
CMD [ "python", "./name_extraction.py"]