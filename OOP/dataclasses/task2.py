from dataclasses import dataclass, field

@dataclass
class Detection:

    label: str
    confidence: float
    box: tuple = field(default_factory=tuple)
    is_reliable: bool = field(init=False)

    def __post_init__(self):
        self.is_reliable = self.confidence > 0.8
        

    def area(self):
        return self.box[2] * self.box[3]
    


class DetectionHandler:

    def __init__(self, label: str, confidence: float, box: tuple):
        self.image = Detection(label, confidence, box)

    
image1 = DetectionHandler('image1.png', 0.9 ,(1, 2, 3, 4))
print(image1.image.is_reliable)
print(image1.image.area())



