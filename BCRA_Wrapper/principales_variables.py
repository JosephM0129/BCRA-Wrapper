#%%
import BCRA_Wrapper

import pandas as pd
import requests

base_url = "https://api.bcra.gob.ar"


BCRA_Wrapper.principales_variables().to_excel('./lista_variables.xlsx')