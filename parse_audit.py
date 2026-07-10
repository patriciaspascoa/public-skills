import sys, json

d = json.load(sys.stdin)
r = d["result"].strip()

# Strip markdown code fences if present
if r.startswith("```"):
    lines = r.split("\n")
    lines = [l for l in lines if not l.strip().startswith("```")]
    r = "\n".join(lines).strip()

parsed = json.loads(r)
print("COST:", d["total_cost_usd"])
print("TURNS:", d["num_turns"])
print(json.dumps(parsed, ensure_ascii=False, indent=2))
