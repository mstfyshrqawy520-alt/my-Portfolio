import gradio as gr
from transformers import pipeline
from PIL import Image, ImageDraw

# Initialize pipelines
classifier = pipeline("image-classification", model="google/vit-base-patch16-224")
detector = pipeline("object-detection", model="facebook/detr-resnet-50")
segmenter = pipeline("image-segmentation", model="facebook/maskformer-swin-tiny-ade")

def process_image(image, task):
    if task == "Classification":
        results = classifier(image)
        return {res["label"]: res["score"] for res in results}, image
    
    elif task == "Object Detection":
        results = detector(image)
        draw = ImageDraw.Draw(image)
        for res in results:
            box = res["box"]
            draw.rectangle([box["xmin"], box["ymin"], box["xmax"], box["ymax"]], outline="red", width=3)
            draw.text((box["xmin"], box["ymin"]), f"{res['label']} ({round(res['score'], 2)})", fill="red")
        return {"Objects Found": len(results)}, image
    
    elif task == "Segmentation":
        results = segmenter(image)
        # For simplicity, we just return the first mask overlayed or the last one
        # In a real app, we'd blend them. Here we'll return the mask image of the first detection.
        if results:
            mask = results[0]["mask"]
            return {"Segmented Label": results[0]["label"]}, mask
        return {"No masks found": 0}, image

# UI
with gr.Blocks(title="CV Multitask Hub") as demo:
    gr.Markdown("# 🖼️ CV Multitask Hub")
    gr.Markdown("A unified pipeline for detection, classification, and segmentation using Hugging Face Transformers.")
    
    with gr.Row():
        with gr.Column():
            input_img = gr.Image(type="pil", label="Upload Image")
            task_dropdown = gr.Dropdown(
                choices=["Classification", "Object Detection", "Segmentation"], 
                value="Classification", 
                label="Select Task"
            )
            submit_btn = gr.Button("Process")
        
        with gr.Column():
            output_label = gr.Label(label="Results")
            output_img = gr.Image(label="Visualization")

    submit_btn.click(
        fn=process_image, 
        inputs=[input_img, task_dropdown], 
        outputs=[output_label, output_img]
    )

if __name__ == "__main__":
    demo.launch()
