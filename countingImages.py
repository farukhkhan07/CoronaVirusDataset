import os 

path = "D:/pythonScrapy/CoronaVirusDataset/Covid19-Cases"

N = 0
for root, _ , files in os.walk(path):
    cdp = os.path.abspath(root)
    for f in files:
        name, ext = os.path.splitext(f)
        if ext == ".png":
            cip = os.path.join(cdp,f)
            N += 1
print(N)
