import gradio as gr
from PIL import Image
from predictor import DepthEstimationModel

model = DepthEstimationModel()

def predict_depth(image):
    input_path = "input_image.png"
    output_path = "output_image.png"

    image.save(input_path)
    model.calculate_depthmap(input_path, output_path)

    depth_map = Image.open(output_path)
    return depth_map, output_path

with gr.Blocks(css="footer {display: none !important;}") as demo:
    gr.Markdown("# Depth Estimation App")
    gr.Markdown("Upload an image and get the predicted depth map.")

    with gr.Row():
        with gr.Column():
            input_image = gr.Image(label="Upload Image", type="pil")
            submit_btn = gr.Button("Generate Depth Map")

        with gr.Column():
            output_image = gr.Image(label="Depth Map")
            download_file = gr.File(label="Download Depth Map")

    submit_btn.click(fn=predict_depth, inputs=input_image, outputs=[output_image, download_file])

if __name__ == "__main__":
    demo.launch()