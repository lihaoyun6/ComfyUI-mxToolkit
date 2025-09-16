# ComfyUI - mxToolkit - Max Smirnov 2024
import nodes
import random

class AnyType(str):
    def __ne__(self, __value: object) -> bool:
        return False

any = AnyType("*")

class mxSeed:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "X": ("INT", {"default": 0, "min": 0, "max": 4294967296}),
            },
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("X",)

    FUNCTION = "main"
    CATEGORY = 'utils/mxToolkit'

    def main(self, X,):
        return (X,)


class mxStop:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "In": (any,),
            },
        }

    @classmethod
    def VALIDATE_INPUTS(s, **kwargs):
        return True

    RETURN_TYPES = (any,)

    FUNCTION = "main"
    CATEGORY = 'utils/mxToolkit'

    def main(self, In):
        out = In;
        nodes.interrupt_processing();
        return (out,)

class mxSlider:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "Xi": ("INT", {"default": 20, "min": -4294967296, "max": 4294967296}),
                "Xf": ("FLOAT", {"default": 20, "min": -4294967296, "max": 4294967296}),
                "isfloatX": ("INT", {"default": 0, "min": 0, "max": 1}),
            },
        }

    RETURN_TYPES = (any,)
    RETURN_NAMES = ("X",)

    FUNCTION = "main"
    CATEGORY = 'utils/mxToolkit'

    def main(self, Xi, Xf, isfloatX):
        if isfloatX > 0:
            out = Xf
        else:
            out = Xi
        return (out,)

class mxSliderSmall:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "Xi": ("INT", {"default": 2, "min": -4294967296, "max": 4294967296}),
                "Xf": ("FLOAT", {"default": 2, "min": -4294967296, "max": 4294967296}),
                "isfloatX": ("INT", {"default": 0, "min": 0, "max": 1}),
            },
        }
    
    RETURN_TYPES = (any,)
    RETURN_NAMES = ("X",)
    
    FUNCTION = "main"
    CATEGORY = 'utils/mxToolkit'
    
    def main(self, Xi, Xf, isfloatX):
        if isfloatX > 0:
            out = Xf
        else:
            out = Xi
        return (out,)

class mxSliderFloat:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "Xi": ("INT", {"default": 2, "min": -4294967296, "max": 4294967296}),
                "Xf": ("FLOAT", {"default": 2, "min": -4294967296, "max": 4294967296}),
                "isfloatX": ("INT", {"default": 1, "min": 0, "max": 1}),
            },
        }
    
    RETURN_TYPES = (any,)
    RETURN_NAMES = ("X",)
    
    FUNCTION = "main"
    CATEGORY = 'utils/mxToolkit'
    
    def main(self, Xi, Xf, isfloatX):
        if isfloatX > 0:
            out = Xf
        else:
            out = Xi
        return (out,)

class mxSliderFloatSmall:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "Xi": ("INT", {"default": 0, "min": -4294967296, "max": 4294967296}),
                "Xf": ("FLOAT", {"default": 0.5, "min": -4294967296, "max": 4294967296}),
                "isfloatX": ("INT", {"default": 1, "min": 0, "max": 1}),
            },
        }
    
    RETURN_TYPES = (any,)
    RETURN_NAMES = ("X",)
    
    FUNCTION = "main"
    CATEGORY = 'utils/mxToolkit'
    
    def main(self, Xi, Xf, isfloatX):
        if isfloatX > 0:
            out = Xf
        else:
            out = Xi
        return (out,)

class mxSlider2D:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "Xi": ("INT", {"default": 512, "min": -4294967296, "max": 4294967296}),
                "Xf": ("FLOAT", {"default": 512, "min": -4294967296, "max": 4294967296}),
                "Yi": ("INT", {"default": 512, "min": -4294967296, "max": 4294967296}),
                "Yf": ("FLOAT", {"default": 512, "min": -4294967296, "max": 4294967296}),
                "isfloatX": ("INT", {"default": 0, "min": 0, "max": 1}),
                "isfloatY": ("INT", {"default": 0, "min": 0, "max": 1}),
            },
        }

    RETURN_TYPES = (any, any,)
    RETURN_NAMES = ("X","Y",)

    FUNCTION = "main"
    CATEGORY = 'utils/mxToolkit'

    def main(self, Xi, Xf, isfloatX, Yi, Yf, isfloatY):
        if isfloatX > 0:
            outX = Xf
        else:
            outX = Xi
        if isfloatY > 0:
            outY = Yf
        else:
            outY = Yi
        return (outX, outY,)

class mxSlider2DA:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "Xi": ("INT", {"default": 1024, "min": -4294967296, "max": 4294967296}),
                "Xf": ("FLOAT", {"default": 1024, "min": -4294967296, "max": 4294967296}),
                "Yi": ("INT", {"default": 1024, "min": -4294967296, "max": 4294967296}),
                "Yf": ("FLOAT", {"default": 1024, "min": -4294967296, "max": 4294967296}),
                "isfloatX": ("INT", {"default": 0, "min": 0, "max": 1}),
                "isfloatY": ("INT", {"default": 0, "min": 0, "max": 1}),
            },
        }

    RETURN_TYPES = (any, any,)
    RETURN_NAMES = ("X","Y",)

    FUNCTION = "main"
    CATEGORY = 'utils/mxToolkit'

    def main(self, Xi, Xf, isfloatX, Yi, Yf, isfloatY):
        if isfloatX > 0:
            outX = Xf
        else:
            outX = Xi
        if isfloatY > 0:
            outY = Yf
        else:
            outY = Yi
        return (outX, outY,)

class StrFormat:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "format": ("STRING", {"default": "", "multiline": True}),
                "value1": ("STRING", {"default": ""}),
                "value2": ("STRING", {"default": ""}),
                "value3": ("STRING", {"default": ""}),
                "value4": ("STRING", {"default": ""}),
                "value5": ("STRING", {"default": ""}),
                "value6": ("STRING", {"default": ""}),
            },
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)
    FUNCTION = "main"
    CATEGORY = 'utils/mxToolkit'
    
    def main(self, format, value1, value2, value3, value4, value5, value6):
        return (format.format(value1, value2, value3, value4, value5, value6),)

class StrFormatAdv:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "format": ("STRING", {"default": "", "multiline": True}),
                "value1": ("STRING", {"default": ""}),
                "switch1": ("BOOLEAN", {"default": True}),
                "value2": ("STRING", {"default": ""}),
                "switch2": ("BOOLEAN", {"default": True}),
                "value3": ("STRING", {"default": ""}),
                "switch3": ("BOOLEAN", {"default": True}),
                "value4": ("STRING", {"default": ""}),
                "switch4": ("BOOLEAN", {"default": True}),
                "value5": ("STRING", {"default": ""}),
                "switch5": ("BOOLEAN", {"default": True}),
                "value6": ("STRING", {"default": ""}),
                "switch6": ("BOOLEAN", {"default": True}),
            },
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)
    FUNCTION = "main"
    CATEGORY = 'utils/mxToolkit'
    
    def main(self, format, value1, switch1, value2, switch2, value3, switch3, value4, switch4, value5, switch5, value6, switch6):
        v1 = value1 if switch1 else ""
        v2 = value2 if switch2 else ""
        v3 = value3 if switch3 else ""
        v4 = value4 if switch4 else ""
        v5 = value5 if switch5 else ""
        v6 = value6 if switch6 else ""
        return (format.format(v1, v2, v3, v4, v5, v6),)

class CSVRandomPicker:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "csv_string": ("STRING", {
                    "multiline": True,
                    "default": "apple,banana,cat,dog"
                }),
                "count": ("INT", {
                    "default": 1,
                    "min": 1,
                    "max": 1000
                }),
                "separator": ("STRING", {
                    "default": ","
                }),
                "seed": ("INT", {
                    "default": 0,
                    "min": 0,
                    "max": 1125899906842624
                }),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    FUNCTION = "pick_random_items"
    CATEGORY = "Custom/Utils"
    
    @classmethod
    def IS_CHANGED(cls, *args, **kwargs):
        return True
    
    def pick_random_items(self, csv_string, count, separator, seed):
        items = [item.strip() for item in csv_string.split(separator) if item.strip()]
        if not items:
            return ("",)
        
        actual_count = min(count, len(items))
        
        rng = random.Random()
        rng.seed(seed)
        
        selected_items = rng.sample(items, actual_count)
        result = separator.join(selected_items)
        return (result,)

class CSVRandomPickerAdv:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "csv_string": ("STRING", {
                    "multiline": True,
                    "default": "apple,banana,cat,dog"
                }),
                "min_count": ("INT", {
                    "default": 1,
                    "min": 1,
                    "max": 1000
                }),
                "max_count": ("INT", {
                    "default": 1,
                    "min": 1,
                    "max": 1000
                }),
                "input_separator": ("STRING", {
                    "default": ","
                }),
                "output_separator": ("STRING", {
                    "default": ","
                }),
                "seed": ("INT", {
                    "default": 0,
                    "min": 0,
                    "max": 1125899906842624
                }),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    FUNCTION = "pick_random_items"
    CATEGORY = "Custom/Utils"
    
    @classmethod
    def IS_CHANGED(cls, *args, **kwargs):
        return True
    
    def pick_random_items(self, csv_string, min_count, max_count, input_separator, output_separator, seed):
        items = [item.strip() for item in csv_string.split(input_separator) if item.strip()]
        if not items:
            return ("",)
        
        if min_count > max_count:
            raise RuntimeError('"max_count" must be greater than "min_count"!')
        
        _min_count = min(min_count, len(items))
        _max_count = min(max_count, len(items))
        actual_count =  random.randint(_min_count, _max_count)
        
        rng = random.Random()
        rng.seed(seed)
        
        selected_items = rng.sample(items, actual_count)
        result = output_separator.join(selected_items)
        return (result,)

NODE_CLASS_MAPPINGS = {
    "mxSeed": mxSeed,
    "mxStop": mxStop,
    "mxSlider": mxSlider,
    "mxSliderSmall": mxSliderSmall,
    "mxSliderFloat": mxSliderFloat,
    "mxSliderFloatSmall": mxSliderFloatSmall,
    "mxSlider2D": mxSlider2D,
    "mxSlider2DA": mxSlider2DA,
    "StrFormat": StrFormat,
    "StrFormatAdv": StrFormatAdv,
    "CSVRandomPicker": CSVRandomPicker,
    "CSVRandomPickerAdv": CSVRandomPickerAdv,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "mxSeed": "Seed",
    "mxStop": "Stop",
    "mxSlider": "Slider Int (0~100)",
    "mxSliderSmall": "Slider Int (0~10)",
    "mxSliderFloat": "Slider Float (0~10)",
    "mxSliderFloatSmall": "Slider Float (0~1)",
    "mxSlider2D": "Slider 2D (1024*1024)",
    "mxSlider2DA": "Slider 2D (3072*3072)",
    "StrFormat": "String Format",
    "StrFormatAdv": "String Format (Advanced)",
    "CSVRandomPicker": "CSV RandomPicker",
    "CSVRandomPickerAdv": "CSV RandomPicker (Advanced)",
}