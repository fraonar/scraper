import pandas as pd

def export_to_excel(data, file_name):
    df = pd.DataFrame(data)
    df.to_excel(file_name, index=False)