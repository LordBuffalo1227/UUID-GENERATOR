import secrets

def generate_valid_uuid(uppercase=False):
    # 16 bytes (128 bits)
    b = bytearray(secrets.token_bytes(16))

    # Forzar versión (bits 12–15 del 7° byte)
    b[6] = (b[6] & 0x0F) | 0x40

    # Forzar variante (bits 6–7 del 9° byte)
    b[8] = (b[8] & 0x3F) | 0x80

    # Convertir a string estándar UUID
    token = b.hex()
    uuid_str = f"{token[0:8]}-{token[8:12]}-{token[12:16]}-{token[16:20]}-{token[20:32]}"

    return uuid_str.upper() if uppercase else uuid_str


# Ejemplo
print(generate_valid_uuid(True))
