# Installation and Usage:

1. Clone the repository and change directory to the project folder

```bash
git clone https://github.com/SamuelDevdas/Study-GPT.git

cd .\Study-GPT\
```

2. Create a virtual environment with Python 3.11

```bash
py -3.11 -m venv venv
```

3. Activate the virtual environment

```bash

Windows:
venv\Scripts\activate

Linux/MacOS:
source venv/bin/activate

```

4. Install the requirements

```bash
pip install -r requirements.txt
```


5. Set api key in the 'set_api_key.py' file

```python
# Replace this with your OpenAI key, needs to run only once
os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY_HERE"
```

6. Run the app script

```bash
streamlit run streamlit_app.py
```

The app is ready to use and will be available at http://localhost:8502

**You can use the provided "lecture.mdx" as a sample markdown file to test the app.**

7. For BEST RESULTS: Set the model parameters at this location in the code: (venv\Lib\site-packages\embedchain\config\llm\base.py)

```python
MODEL PARAMETERS:
model = "gpt-4-turbo-preview"
temperature: float = 0
max_tokens: int = 4096
top_p: float = 0.01

```
