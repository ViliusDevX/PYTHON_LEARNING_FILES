info = {
    "days": 365,
    "cig_averages": {
        "weekday": 4,
        "saturday": 20,
        "sunday": 1
    },
    "pack_price": 4.50,
    "cigs_in_pack": 20,
    "minuters_per_cig": 5
}
weekday_smoke = str(input("Kiek DARBO dienu rukysi?: "))
saturday_smoke = str(input("Kiek SESTADIENIU rukysi: "))
sunday_smoke = str(input("Kiek SEKMADIENIU rukysi: "))
total_smoke_days = weekday_smoke + saturday_smoke + sunday_smoke
cigs = info["cig_averages"]
cigs_smoked = (cigs["weekday"] * weekday_smoke) + (cigs["saturday"] * saturday_smoke) + (cigs["sunday"] * sunday_smoke)
cigs_sum = info["pack_price"] / info["cigs_in_pack"] * float(cigs_smoked)
total_smoke_hours = float(cigs_smoked) * info["minuters_per_cig"] / 60
print(f"Po {total_smoke_days} dienu, busi surukes: {cigs_smoked}")
print(f"Sumokesi : {cigs_sum} euru")
print(f"Prastovesi traukdamas dumus: {total_smoke_hours}")