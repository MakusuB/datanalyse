import datanalyse.dataelement.dataelement as dta
from pathlib import Path

de = dta.Dataelement(pfad=Path("Ahlborn.xlsx"))
print(de.name)