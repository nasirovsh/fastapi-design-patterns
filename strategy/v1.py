from fastapi import FastAPI


class ImageProcessorStrategy:
    def process(self, image):
        pass


class BlurImageProcessor(ImageProcessorStrategy):
    def process(self, image):
        # Apply blur effect to the image
        pass


class ResizeImageProcessor(ImageProcessorStrategy):
    def process(self, image):
        # Resize the image
        pass


class ImageProcessor:
    def __init__(self, strategy: ImageProcessorStrategy):
        self.strategy = strategy

    def process_image(self, image):
        return self.strategy.process(image)


app = FastAPI()


strategies = {
    "blur": BlurImageProcessor(),
    "resize": ResizeImageProcessor()
}


@app.post("/process_image")
def process_image(image, processor_type: str):
    if processor_type not in strategies:
        raise ValueError("Invalid processor type")

    processor = ImageProcessor(strategies[processor_type])
    return processor.process_image(image)
