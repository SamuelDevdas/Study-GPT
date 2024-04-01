# Installation and Usage:

1. Clone the repository

```bash
git clone https://github.com/SamuelDevdas/Study-GPT.git
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

5. Run the script

```bash
streamlit run streamlit_app.py
```


6. Set the model parameters at this location in the code: (venv\Lib\site-packages\embedchain\config\llm\base.py)

```python
MODEL PARAMETERS:
model = "gpt-4-turbo-preview"
temperature: float = 0
max_tokens: int = 4096
top_p: float = 0.01

```