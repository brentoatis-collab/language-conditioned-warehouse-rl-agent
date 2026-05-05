# text_encoder.py
def encode_command(command):
    command = command.lower().strip()

    mapping = {
        "a1": (0,0), "a2": (0,1), "a3": (0,2), "a4": (0,3), "a5": (0,4),
        "b1": (1,0), "b2": (1,1), "b3": (1,2), "b4": (1,3), "b5": (1,4),
        "c1": (2,0), "c2": (2,1), "c3": (2,2), "c4": (2,3), "c5": (2,4),
        "d1": (3,0), "d2": (3,1), "d3": (3,2), "d4": (3,3), "d5": (3,4),
        "e1": (4,0), "e2": (4,1), "e3": (4,2), "e4": (4,3), "e5": (4,4),
    }

    for key in mapping:
        if key in command:
            return mapping[key]

    return (4,4)  # default fallback