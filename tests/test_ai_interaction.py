"""
Test_Ai_Interaction:
"""

sphinx_needs_test_spec = ''
"""
.. test_spec:: Test of Ai_Interaction
   :id: TS_Ai_Interaction
   :status: verified
   :verified_by: TEST_RES_Ai_Interaction

   This is a test specification for the module : need : `M_ai_interaction`.

   **Test execution**

   Run tests in test class with pytest. Command: `pytest -q test_ai_interaction.py`

   **Test steps**

   .. autoclass:: test_ai_interaction.Test_Ai_Interaction
      :members:
      :undoc-members:

"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from ai_interaction import Ai_Interaction
import pytest

class Test_Ai_Interaction:
    def test_merge_dictionaries(self):
        """1. It shall be possible to get feedback from AI of requests."""

        ai = Ai_Interaction()

        task = "Du bist eine Kinderbuch Autor."
        request = "Erstelle eine Liste von fünf Charaktern für eine Weltraum-Piraten Geschichte. "

        response = ai.request(task, request,)

        print(response)

        str_response = str(response)

        assert len(str_response) > 0
