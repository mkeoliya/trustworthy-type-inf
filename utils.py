import json
import glob

# === OPENAI === 
def get_response(client, message, **kwargs):
    # create a completion using the chat endpoint
    completion = client.chat.completions.create(
        model="gpt-4-turbo",
        n = 1,
        response_format={ "type": "json_object" },
        messages=[{"role": "user", "content": message}],
        **kwargs
    )

    return completion


# === FILE UTILS === 
def insert_code(item, py_file):
    line_no = item['line_number']

    with open(py_file, "r") as f:
        lines = f.readlines()[:line_no]
        code = "\n".join(lines)
        item['code'] = code

    return item

def annotate_gt(py_file):
    basename = py_file.split(".")[0]
    gt_file = f"{basename}_gt.json"
    print(f"Annotating ground truth: {gt_file}")

    with open(gt_file, "r") as f:
        gt = json.load(f)
    
    new_gt = [ insert_code(item, py_file) for item in gt]
    
    with open(gt_file, "w") as f:
        json.dump(new_gt, f)

def annotate_gts(folders):
    for folder in folders:
        # find all python files in this folder at any depth
        py_files = glob.glob(f"{folder}/**/*.py", recursive=True)
        for py_file in py_files:
            print(f"Annotating ground truth for: {py_file}")
            # annotate_gt(py_file)



