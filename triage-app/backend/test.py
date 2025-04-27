from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

REPO_ID  = "VolodymyrPugachov/BioClinicalBERT-Triage"
SUBFOLDER = "checkpoint-6378"          # where the files really live

tok   = AutoTokenizer.from_pretrained(REPO_ID, subfolder=SUBFOLDER)
model = AutoModelForSequenceClassification.from_pretrained(REPO_ID, subfolder=SUBFOLDER)

triage = pipeline("text-classification", model=model, tokenizer=tok)

print(triage("15-year old complaining of cold"))
