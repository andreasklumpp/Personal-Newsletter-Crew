#!/usr/bin/env python
import warnings
from datetime import datetime
from dotenv import load_dotenv

from startup_newsletter_crew.crew import StartupNewsletterCrew

load_dotenv(override=True)

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI LLMs',
        'current_year': str(datetime.now().year)
    }
    
    try:
        result = StartupNewsletterCrew().crew().kickoff(inputs=inputs)
        print(result.raw)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


