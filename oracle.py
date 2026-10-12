import json, math

def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def plural(n, word, form=None): return str(jsnum(n)) + " " + (word if n == 1 else (form or word + "s"))
def fmt(x): return str(jsnum(x))
def round1(x): return jsnum(math.floor(x * 10 + 0.5) / 10)

def spot_plan(widthCm, depthCm, spotCm):
    if not (widthCm > 0) or not (depthCm > 0) or not (spotCm > 0):
        return {"error": "the blanket and the labeled spot must be positive"}
    if widthCm < spotCm or depthCm < spotCm:
        return {"error": "the blanket is smaller than one labeled spot"}
    across = math.floor(widthCm / spotCm)
    along = math.floor(depthCm / spotCm)
    spots = across * along
    leftover = round1(widthCm - across * spotCm)
    if spots <= 2: verdict = "a date blanket"
    elif spots <= 6: verdict = "a family blanket"
    else: verdict = "a full reunion"
    return {"spots": spots, "across": across, "along": along, "leftover": leftover, "verdict": verdict}

def basket_plan(heads, gramsPerHead, boxGrams):
    if not (heads > 0) or not (gramsPerHead > 0) or not (boxGrams > 0):
        return {"error": "the heads, the labeled portion and the labeled box must be positive"}
    total = round1(heads * gramsPerHead)
    boxes = math.ceil(total / boxGrams)
    spare = round1(boxes * boxGrams - total)
    if heads <= 2: verdict = "a quiet picnic"
    elif heads <= 6: verdict = "a family spread"
    else: verdict = "a crowd feast"
    return {"total": total, "boxes": boxes, "spare": spare, "verdict": verdict}

def ice_plan(coolerL, packL):
    if not (coolerL > 0) or not (packL > 0):
        return {"error": "the cooler and the labeled pack coverage must be positive"}
    packs = math.ceil(coolerL / packL)
    spare = round1(packs * packL - coolerL)
    if packs == 1: verdict = "a light chill"
    elif packs <= 3: verdict = "a working cooler"
    else: verdict = "a deep freeze"
    return {"packs": packs, "spare": spare, "verdict": verdict}

def render_spot(r, widthCm, depthCm, spotCm):
    return ("A blanket " + fmt(widthCm) + " cm x " + fmt(depthCm) + " cm at a labeled " + fmt(spotCm) + " cm spot marks "
            + plural(r["spots"], "spot") + " (" + fmt(r["across"]) + " x " + fmt(r["along"]) + ") with " + fmt(r["leftover"]) + " cm of fringe to spare - " + r["verdict"] + ".")

def render_basket(r, heads, gramsPerHead, boxGrams):
    return ("A party of " + plural(heads, "head") + " at a labeled " + fmt(gramsPerHead) + " g a head makes " + fmt(r["total"])
            + " g of picnic - " + plural(r["boxes"], "box", "boxes") + " at a labeled " + fmt(boxGrams) + " g" + ("" if r["boxes"] == 1 else " each")
            + ", with " + fmt(r["spare"]) + " g of room to spare - " + r["verdict"] + ".")

def render_ice(r, coolerL, packL):
    return ("A cooler " + fmt(coolerL) + " L at a labeled " + fmt(packL) + " L a pack takes " + plural(r["packs"], "ice pack")
            + ", covering " + fmt(round1(r["packs"] * packL)) + " L with " + fmt(r["spare"]) + " L of overlap - " + r["verdict"] + ".")

cases = []
def add(fn, f, rf, args):
    r = f(*args)
    c = {"fn": fn, "args": args, "result": r}
    if "error" not in r: c["render"] = rf(r, *args)
    cases.append(c)

for a in [[200,200,60],[120,120,60],[300,200,60],[60,60,60],[0,200,60],[200,200,0],[50,200,60],[150.5,200,60],[240,180,50],[100,100,45]]:
    add("spotPlan", spot_plan, render_spot, a)
for a in [[4,500,1200],[1,500,1200],[9,450,1000],[12,600,1200],[0,500,1200],[4,0,1200],[4,500,0],[2,500,1000],[6,375.5,1000],[3,800,800]]:
    add("basketPlan", basket_plan, render_basket, a)
for a in [[24,10],[8,10],[50,10],[10,10],[0,10],[24,0],[45,10],[12.5,10],[30,15],[60,8]]:
    add("icePlan", ice_plan, render_ice, a)
json.dump(cases, open("expected.json", "w"), separators=(",", ":"))
print(len(cases), "cases")
