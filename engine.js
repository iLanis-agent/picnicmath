(function (root) {
  "use strict";
  function plural(n, word, form) { return n + " " + (n === 1 ? word : (form || word + "s")); }
  function round1(x) { return Math.round(x * 10) / 10; }

  function spotPlan(widthCm, depthCm, spotCm) {
    if (!(widthCm > 0) || !(depthCm > 0) || !(spotCm > 0)) return { error: "the blanket and the labeled spot must be positive" };
    if (widthCm < spotCm || depthCm < spotCm) return { error: "the blanket is smaller than one labeled spot" };
    var across = Math.floor(widthCm / spotCm);
    var along = Math.floor(depthCm / spotCm);
    var spots = across * along;
    var leftover = round1(widthCm - across * spotCm);
    var verdict;
    if (spots <= 2) verdict = "a date blanket";
    else if (spots <= 6) verdict = "a family blanket";
    else verdict = "a full reunion";
    return { spots: spots, across: across, along: along, leftover: leftover, verdict: verdict };
  }

  function basketPlan(heads, gramsPerHead, boxGrams) {
    if (!(heads > 0) || !(gramsPerHead > 0) || !(boxGrams > 0)) return { error: "the heads, the labeled portion and the labeled box must be positive" };
    var total = round1(heads * gramsPerHead);
    var boxes = Math.ceil(total / boxGrams);
    var spare = round1(boxes * boxGrams - total);
    var verdict;
    if (heads <= 2) verdict = "a quiet picnic";
    else if (heads <= 6) verdict = "a family spread";
    else verdict = "a crowd feast";
    return { total: total, boxes: boxes, spare: spare, verdict: verdict };
  }

  function icePlan(coolerL, packL) {
    if (!(coolerL > 0) || !(packL > 0)) return { error: "the cooler and the labeled pack coverage must be positive" };
    var packs = Math.ceil(coolerL / packL);
    var spare = round1(packs * packL - coolerL);
    var verdict;
    if (packs === 1) verdict = "a light chill";
    else if (packs <= 3) verdict = "a working cooler";
    else verdict = "a deep freeze";
    return { packs: packs, spare: spare, verdict: verdict };
  }

  function renderSpot(r, widthCm, depthCm, spotCm) {
    return "A blanket " + widthCm + " cm x " + depthCm + " cm at a labeled " + spotCm + " cm spot marks " + plural(r.spots, "spot") + " (" + r.across + " x " + r.along + ") with " + r.leftover + " cm of fringe to spare - " + r.verdict + ".";
  }

  function renderBasket(r, heads, gramsPerHead, boxGrams) {
    return "A party of " + plural(heads, "head") + " at a labeled " + gramsPerHead + " g a head makes " + r.total + " g of picnic - " + plural(r.boxes, "box", "boxes") + " at a labeled " + boxGrams + " g" + (r.boxes === 1 ? "" : " each") + ", with " + r.spare + " g of room to spare - " + r.verdict + ".";
  }

  function renderIce(r, coolerL, packL) {
    return "A cooler " + coolerL + " L at a labeled " + packL + " L a pack takes " + plural(r.packs, "ice pack") + ", covering " + round1(r.packs * packL) + " L with " + r.spare + " L of overlap - " + r.verdict + ".";
  }

  var api = { spotPlan: spotPlan, basketPlan: basketPlan, icePlan: icePlan, renderSpot: renderSpot, renderBasket: renderBasket, renderIce: renderIce };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.PicnicMath = api;
})(this);
